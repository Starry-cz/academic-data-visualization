#!/usr/bin/env python3
"""Shared helpers for the dependency-free chart registry toolchain."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "references" / "chart-registry.yaml"
SCHEMA_PATH = ROOT / "references" / "chart-registry.schema.json"
SOURCE_PATH = ROOT / "references" / "chart-taxonomy-source.md"
CHART_TYPES_DIR = ROOT / "references" / "chart-types"
ALIAS_INDEX_PATH = ROOT / "references" / "chart-alias-index.md"
FIGURES_DIR = ROOT / "assets" / "figures"


def load_json(path: Path) -> dict[str, Any]:
    """Load a JSON-compatible YAML/JSON document."""
    return json.loads(path.read_text(encoding="utf-8"))


def load_registry() -> dict[str, Any]:
    return load_json(REGISTRY_PATH)


def load_schema() -> dict[str, Any]:
    return load_json(SCHEMA_PATH)


def resolve_ref(schema: dict[str, Any], ref: str) -> dict[str, Any]:
    if not ref.startswith("#/"):
        raise ValueError(f"Only local schema refs are supported: {ref}")
    node: Any = schema
    for part in ref[2:].split("/"):
        node = node[part.replace("~1", "/").replace("~0", "~")]
    return node


def validate_schema(instance: Any, node: dict[str, Any], root: dict[str, Any], path: str = "$") -> list[str]:
    """执行本仓库 Schema 使用到的确定性子集，避免 CI 引入外部 JSON Schema 依赖。"""
    if "$ref" in node:
        return validate_schema(instance, resolve_ref(root, node["$ref"]), root, path)

    errors: list[str] = []
    expected = node.get("type")
    if expected is not None:
        accepted = expected if isinstance(expected, list) else [expected]
        type_map = {
            "object": dict,
            "array": list,
            "string": str,
            "integer": int,
            "boolean": bool,
            "null": type(None),
        }
        if not any(isinstance(instance, type_map[name]) and not (name == "integer" and isinstance(instance, bool))
                   for name in accepted):
            return [f"{path}: expected type {accepted}, got {type(instance).__name__}"]

    if "const" in node and instance != node["const"]:
        errors.append(f"{path}: expected constant {node['const']!r}")
    if "enum" in node and instance not in node["enum"]:
        errors.append(f"{path}: value {instance!r} is not in {node['enum']}")
    if isinstance(instance, str):
        if len(instance) < node.get("minLength", 0):
            errors.append(f"{path}: string is shorter than minLength")
        if "pattern" in node and not re.fullmatch(node["pattern"], instance):
            errors.append(f"{path}: value {instance!r} does not match {node['pattern']!r}")
    if isinstance(instance, list):
        if len(instance) < node.get("minItems", 0):
            errors.append(f"{path}: array is shorter than minItems")
        if "maxItems" in node and len(instance) > node["maxItems"]:
            errors.append(f"{path}: array is longer than maxItems")
        item_schema = node.get("items")
        if item_schema:
            for index, value in enumerate(instance):
                errors.extend(validate_schema(value, item_schema, root, f"{path}[{index}]"))
    if isinstance(instance, dict):
        properties = node.get("properties", {})
        for required in node.get("required", []):
            if required not in instance:
                errors.append(f"{path}: missing required property {required!r}")
        if node.get("additionalProperties") is False:
            for key in instance.keys() - properties.keys():
                errors.append(f"{path}: unexpected property {key!r}")
        for key, value in instance.items():
            if key in properties:
                errors.extend(validate_schema(value, properties[key], root, f"{path}.{key}"))
    return errors


def normalize_alias(value: str) -> str:
    return re.sub(r"[\s_–—-]+", "", value).casefold()


def alias_lookup(registry: dict[str, Any]) -> dict[str, list[str]]:
    lookup: dict[str, list[str]] = {}
    for chart in registry["charts"]:
        for value in [chart["id"], chart["name_zh"], chart["name_en"],
                      *chart["aliases_zh"], *chart["aliases_en"]]:
            key = normalize_alias(value)
            lookup.setdefault(key, [])
            if chart["id"] not in lookup[key]:
                lookup[key].append(chart["id"])
    for term in registry["ambiguous_terms"]:
        lookup[normalize_alias(term["term"])] = list(term["candidate_ids"])
    return lookup


def resolve_chart_name(registry: dict[str, Any], value: str) -> list[str]:
    """Resolve an exact user-facing name; multiple IDs indicate declared ambiguity."""
    return alias_lookup(registry).get(normalize_alias(value), [])


def parse_source_taxonomy() -> list[dict[str, Any]]:
    """Parse every category bullet, including entries that still lack a canonical ID."""
    entries: list[dict[str, Any]] = []
    category_id: str | None = None
    for line_number, line in enumerate(SOURCE_PATH.read_text(encoding="utf-8").splitlines(), start=1):
        heading = re.match(r"^##\s+(\d{2})\.", line)
        if heading:
            category_id = heading.group(1)
            continue
        if category_id and line.startswith("- "):
            item = re.match(r"^-\s+`([a-z0-9-]+)`\s+—\s*(.+)$", line)
            entries.append(
                {
                    "category_id": category_id,
                    "canonical_id": item.group(1) if item else None,
                    "source_label": item.group(2) if item else line[2:].strip(),
                    "line": line_number,
                }
            )
    return entries


def source_memberships() -> list[tuple[str, str]]:
    """Return mapped ``(category_id, canonical_id)`` pairs from the source taxonomy."""
    return [
        (entry["category_id"], entry["canonical_id"])
        for entry in parse_source_taxonomy()
        if entry["canonical_id"] is not None
    ]


def production_records(registry: dict[str, Any]) -> list[dict[str, Any]]:
    return [chart for chart in registry["charts"] if chart["implementation_status"] == "production_template"]


def status_counts(registry: dict[str, Any]) -> dict[str, int]:
    counts = {"production_template": 0, "reusable_pattern": 0, "on_demand": 0}
    for chart in registry["charts"]:
        counts[chart["implementation_status"]] += 1
    return counts


def category_filename(category: dict[str, str]) -> str:
    return f"{category['id']}-{category['slug']}.md"


def replace_generated_block(text: str, name: str, replacement: str) -> str:
    start = f"<!-- {name}:start -->"
    end = f"<!-- {name}:end -->"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    if not pattern.search(text):
        raise ValueError(f"Missing generated block markers: {name}")
    return pattern.sub(f"{start}\n{replacement.rstrip()}\n{end}", text)
