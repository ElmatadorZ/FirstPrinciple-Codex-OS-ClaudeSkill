"""The FPCOS contract.

FPCOS is a single-file base layer that every domain skill inherits, so the
promise that matters is that the non-removable layers are actually present and
marked non-removable. These tests hold SKILL.md to that — they are the pytest
companion to tools/validate_skill.py, so a contributor sees the contract without
reading the validator.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"


def _split():
    text = SKILL.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, "frontmatter must be present and delimited"
    return yaml.safe_load(m.group(1)), text[m.end():]


def test_canonical_filename_lowercase_extension():
    # Claude's skill loader is case-sensitive and expects exactly SKILL.md.
    # The file was SKILL.MD, which a case-sensitive loader would not find.
    assert SKILL.exists()
    assert SKILL.name == "SKILL.md"


def test_frontmatter_and_license():
    fm, _ = _split()
    for f in ("name", "description", "license", "version"):
        assert f in fm
    assert str(fm["license"]).lower().replace(" ", "-") == "apache-2.0"


def test_license_matches_license_file():
    fm, _ = _split()
    lic = (ROOT / "LICENSE").read_text(encoding="utf-8")
    assert "Apache License" in lic
    assert str(fm["license"]).lower().replace(" ", "-") == "apache-2.0"


def test_metadata_declares_base_layer_role():
    fm, _ = _split()
    meta = fm.get("metadata", {})
    assert meta.get("compatibility")
    assert meta.get("not_for")
    # FPCOS's whole identity is that it is a base layer, not an optional add-on.
    assert "base" in str(meta.get("role", "")).lower()


def test_non_removable_layers_present():
    _, body = _split()
    # L0 (Reality Anchor), L1 (Axiom Gate), L4 (Shadow Gate), L5 (Synthesis) are
    # the layers the OS declares can never be removed by an inheriting skill.
    for layer in ("L0", "L1", "L4", "L5"):
        assert layer in body, f"non-removable layer {layer} must be present"


def test_shadow_gate_is_non_skippable():
    _, body = _split()
    assert re.search(r"shadow gate", body, re.I)
    assert re.search(r"non.?skippable|always runs|❌ No", body, re.I)


def test_known_inferred_unknown_separation():
    _, body = _split()
    for word in ("Known", "Inferred", "Unknown"):
        assert word in body


def test_output_states_confidence_and_unknowns():
    _, body = _split()
    assert re.search(r"confidence", body, re.I)
    assert re.search(r"unknown", body, re.I)


def test_inheritance_contract_marks_layers_non_removable():
    _, body = _split()
    # The SKILL INTERFACE CONTRACT table marks the inherited rules "❌ No"
    # (may not be removed). At least the core ones must be there.
    assert "SKILL INTERFACE CONTRACT" in body
    assert body.count("❌ No") >= 4
