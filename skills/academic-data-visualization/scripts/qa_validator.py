#!/usr/bin/env python3
"""Validate plotting sources or rendered bundles and return auditable QA evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from PIL import Image, ImageStat

from manifest_lib import load_manifest, sha256_file
from palette_lib import THEMES


QA_VERSION = "2.0.0"
PROFILE_PIXELS = {
    "journal_print": (3242, 2160),
    "report_web": (2000, 1200),
    "keynote_screen": (1920, 1080),
    "poster_large": (3600, 2400),
}


@dataclass(frozen=True)
class Finding:
    check_id: str
    pass_: bool
    severity: str
    detail: str


def check_cl3_dpi(source: str) -> Finding:
    """保留旧 API，同时把缺失 DPI 从假通过改为明确警告。"""
    values = [int(match.group(1)) for match in re.finditer(r"(?:dpi|res)\s*=\s*(\d+)", source)]
    if not values:
        return Finding("CL-3", False, "WARN", "No explicit raster DPI; validate the rendered file")
    too_low = [value for value in values if value < 300]
    return Finding(
        "CL-3",
        not too_low,
        "PASS" if not too_low else "FAIL",
        "Raster DPI declarations meet the print baseline" if not too_low else f"Raster DPI below 300: {too_low}",
    )


def audit_source(path: Path, production_interface: bool = False) -> list[Finding]:
    source = path.read_text(encoding="utf-8", errors="replace")
    findings: list[Finding] = []
    forbidden = {
        "SRC-1": (r"install\.packages\s*\(|(?:pip|conda)\s+install", "Runtime package installation is forbidden"),
        "SRC-2": (r"read_(?:csv|table)\s*\(\s*['\"]\./|read\.csv\s*\(\s*['\"]\./", "CWD-relative input path is forbidden"),
        "SRC-3": (r"plt\.show\s*\(", "Interactive plt.show() is forbidden in headless templates"),
    }
    for check_id, (pattern, detail) in forbidden.items():
        matched = bool(re.search(pattern, source, flags=re.IGNORECASE))
        findings.append(Finding(check_id, not matched, "FAIL" if matched else "PASS", detail if matched else f"{detail}: not found"))
    has_main = "if __name__ == \"__main__\"" in source or "if __name__ == '__main__'" in source
    findings.append(Finding("SRC-4", has_main, "PASS" if has_main else "FAIL", "Explicit main entrypoint" if has_main else "Missing explicit main entrypoint"))
    if production_interface:
        missing_flags = [flag for flag in ("--input", "--demo", "--output-dir", "--profile", "--theme", "--seed") if flag not in source]
        findings.append(Finding("SRC-5", not missing_flags, "PASS" if not missing_flags else "FAIL", "Unified CLI is present" if not missing_flags else f"Missing CLI flags: {missing_flags}"))
    return findings


def image_is_blank(image: Image.Image) -> bool:
    grayscale = image.convert("L")
    stats = ImageStat.Stat(grayscale)
    return stats.var[0] < 2.0


def audit_png(path: Path, profile: str) -> list[Finding]:
    findings: list[Finding] = []
    with Image.open(path) as image:
        image.verify()
    with Image.open(path) as image:
        expected = PROFILE_PIXELS[profile]
        tolerance = 3
        dimensions_ok = all(abs(actual - target) <= tolerance for actual, target in zip(image.size, expected, strict=True))
        findings.append(Finding("OUT-1", dimensions_ok, "PASS" if dimensions_ok else "FAIL", f"PNG dimensions {image.size}; expected {expected}"))
        blank = image_is_blank(image)
        findings.append(Finding("OUT-2", not blank, "PASS" if not blank else "FAIL", "PNG contains visible variation" if not blank else "PNG appears blank or nearly uniform"))
        findings.append(Finding("OUT-3", image.mode in {"RGB", "RGBA"}, "PASS" if image.mode in {"RGB", "RGBA"} else "FAIL", f"PNG colour mode is {image.mode}"))
    return findings


def audit_grayscale(path: Path, expected_size: tuple[int, int]) -> list[Finding]:
    with Image.open(path) as image:
        ok = image.mode in {"L", "LA"} and image.size == expected_size and not image_is_blank(image)
        return [Finding("OUT-4", ok, "PASS" if ok else "FAIL", f"Grayscale proof mode={image.mode}, size={image.size}")]


def audit_svg(path: Path) -> list[Finding]:
    root = ET.parse(path).getroot()
    text_nodes = [node for node in root.iter() if node.tag.rsplit("}", 1)[-1] == "text"]
    ok = bool(text_nodes)
    return [Finding("OUT-5", ok, "PASS" if ok else "FAIL", f"SVG contains {len(text_nodes)} editable text nodes")]


def audit_pdf(path: Path) -> list[Finding]:
    payload = path.read_bytes()
    valid = payload.startswith(b"%PDF") and len(payload) > 5000
    embedded = any(token in payload for token in (b"/FontFile2", b"/FontFile3"))
    return [
        Finding("OUT-6", valid, "PASS" if valid else "FAIL", f"PDF signature and size ({len(payload)} bytes)"),
        Finding("OUT-7", embedded, "PASS" if embedded else "FAIL", "Embedded TrueType/OpenType font program found" if embedded else "No embedded font program found"),
    ]


def relative_luminance(hex_color: str) -> float:
    rgb = [int(hex_color[index:index + 2], 16) / 255 for index in (1, 3, 5)]
    linear = [value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4 for value in rgb]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast_ratio(first: str, second: str = "#FFFFFF") -> float:
    a, b = relative_luminance(first), relative_luminance(second)
    lighter, darker = max(a, b), min(a, b)
    return (lighter + 0.05) / (darker + 0.05)


def audit_metadata(path: Path, source_path: Path, profile: str) -> list[Finding]:
    metadata = json.loads(path.read_text(encoding="utf-8"))
    findings = [
        Finding("DATA-1", metadata.get("profile") == profile, "PASS" if metadata.get("profile") == profile else "FAIL", f"Recorded profile: {metadata.get('profile')}"),
        Finding("DATA-2", metadata.get("source_rows", 0) > 0, "PASS" if metadata.get("source_rows", 0) > 0 else "FAIL", f"Recorded source rows: {metadata.get('source_rows')}"),
        Finding("DATA-3", metadata.get("source_sha256") == sha256_file(source_path), "PASS" if metadata.get("source_sha256") == sha256_file(source_path) else "FAIL", "Source-data hash matches metadata"),
        Finding("DATA-4", bool(metadata.get("metrics")), "PASS" if metadata.get("metrics") else "FAIL", "Computed metrics are recorded"),
    ]
    theme_id = metadata.get("theme")
    palette = metadata.get("palette")
    expected_theme = THEMES.get(theme_id)
    palette_matches = bool(
        expected_theme
        and isinstance(palette, dict)
        and palette.get("categorical") == expected_theme["categorical"]
        and palette.get("sequential") == expected_theme["sequential"]
        and palette.get("diverging") == expected_theme["diverging"]
        and palette.get("accent") == expected_theme["accent"]
    )
    findings.append(
        Finding(
            "COLOR-1",
            palette_matches,
            "PASS" if palette_matches else "FAIL",
            f"Theme {theme_id!r} matches references/palette-library.json" if palette_matches else "Rendered palette is not an exact registered theme",
        )
    )
    palette_values: list[str] = []
    if isinstance(palette, dict):
        for role in ("categorical", "sequential", "diverging"):
            values = palette.get(role, [])
            if isinstance(values, list):
                palette_values.extend(values)
        accent = palette.get("accent")
        if isinstance(accent, str):
            palette_values.append(accent)
    ratios = [contrast_ratio(color) for color in palette_values if re.fullmatch(r"#[0-9A-Fa-f]{6}", color)]
    # 颜色不是唯一编码时，低于 3:1 可作为警告；关键线和文字仍需达到目标对比度。
    low = [round(value, 2) for value in ratios if value < 3]
    findings.append(Finding("A11Y-1", not low, "PASS" if not low else "WARN", "Palette colours reach 3:1 against white" if not low else f"Palette colours below 3:1 against white require redundant encoding: {low}"))
    return findings


def audit_output_bundle(output_dir: Path, manifest_path: Path) -> dict[str, Any]:
    manifest = load_manifest(manifest_path)
    profile = json.loads((output_dir / "figure-metadata.json").read_text(encoding="utf-8"))["profile"]
    required = manifest["outputs"]["required"]
    findings: list[Finding] = []
    missing = [name for name in required if name not in {"qa-report.json", "run-record.json"} and not (output_dir / name).is_file()]
    findings.append(Finding("OUT-0", not missing, "PASS" if not missing else "FAIL", "All renderer outputs exist" if not missing else f"Missing outputs: {missing}"))
    if not missing:
        findings.extend(audit_png(output_dir / "figure.png", profile))
        with Image.open(output_dir / "figure.png") as image:
            expected_size = image.size
        findings.extend(audit_grayscale(output_dir / "figure-grayscale.png", expected_size))
        findings.extend(audit_svg(output_dir / "figure.svg"))
        findings.extend(audit_pdf(output_dir / "figure.pdf"))
        findings.extend(audit_metadata(output_dir / "figure-metadata.json", output_dir / "source-data.csv", profile))
        alt_text = (output_dir / "alt-text.txt").read_text(encoding="utf-8").strip()
        findings.append(Finding("A11Y-2", len(alt_text) >= 40, "PASS" if len(alt_text) >= 40 else "FAIL", f"Alt text length: {len(alt_text)}"))
    result = {
        "qa_version": QA_VERSION,
        "asset_id": manifest["asset_id"],
        "profile": profile,
        "findings": [asdict(item) for item in findings],
        "summary": {
            "passed": sum(item.pass_ for item in findings),
            "failed": sum(not item.pass_ and item.severity == "FAIL" for item in findings),
            "warnings": sum(item.severity == "WARN" for item in findings),
        },
    }
    result["passed"] = result["summary"]["failed"] == 0
    return result


def write_report(report: dict[str, Any], path: Path | None) -> None:
    payload = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if path:
        path.write_text(payload, encoding="utf-8")
    print(payload, end="")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", type=Path, help="Plotting source file")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--production-interface", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.output_dir or args.manifest:
        if not args.output_dir or not args.manifest:
            raise SystemExit("--output-dir and --manifest must be used together")
        report = audit_output_bundle(args.output_dir.resolve(), args.manifest.resolve())
    elif args.target:
        findings = audit_source(args.target.resolve(), args.production_interface)
        report = {
            "qa_version": QA_VERSION,
            "target": str(args.target.resolve()),
            "findings": [asdict(item) for item in findings],
            "passed": all(item.pass_ or item.severity == "WARN" for item in findings),
        }
    else:
        raise SystemExit("Provide a source target or --output-dir with --manifest")
    write_report(report, args.report.resolve() if args.report else None)
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
