# First Principle Codex OS (FPCOS) v1.0

**Anti-Hallucination Cognitive Base Layer for Claude Skills**

[![License: OCL v1.0](https://img.shields.io/badge/License-Open%20Cognitive%20License%20v1.0-00FFB2.svg)](./LICENSE.md)
[![Version](https://img.shields.io/badge/Version-1.0-7B6EFF.svg)](./CHANGELOG.md)
[![Author](https://img.shields.io/badge/Author-ElmatadorZ-FF6B35.svg)](https://github.com/ElmatadorZ)
[![Claude Skill](https://img.shields.io/badge/Claude-Skill%20Compatible-blue.svg)](https://claude.ai)

---

## What is FPCOS?

Hallucination in LLMs is not a bug. It is an **emergent property** of systems that lack an epistemological gate between pattern completion and verified truth output.

**FPCOS** solves this by embedding a verification-first cognitive architecture as a shared base layer that every Claude Skill can inherit — creating a universal OS where:

- Every claim must pass **First Principle + Kalama10** verification
- Every problem must be framed through **Ariya4** before solutions are proposed
- Every system analysis maps **feedback loops, leverage, and dead weight**
- **Compound Mind** synthesizes across domains without single-axis traps
- Every output must survive **Shadow Gate** self-critique (non-skippable)

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    FPCOS — BASE LAYER v1.0                      │
│                                                                 │
│  L0 REALITY ANCHOR ──→ L1 AXIOM GATE ──→ L2 SYSTEM LENS       │
│         ↓                    ↓                    ↓             │
│  L3 COMPOUND MIND ──→ L4 SHADOW GATE ──→ L5 SYNTHESIS         │
│                       (NON-SKIPPABLE)                           │
│                                                                 │
│  ↕↕↕↕↕  SKILL INTERFACE LAYER (connect any domain)  ↕↕↕↕↕    │
│  [Finance]  [Coffee]  [Strategy]  [Medical]  [Code]  [...]    │
└─────────────────────────────────────────────────────────────────┘
```

| Layer | Name | Function |
|---|---|---|
| L0 | Reality Anchor | Declare KNOWN / INFERRED / UNKNOWN before any claim |
| L1 | Axiom Gate | First Principle + Kalama10 (10-rejection test) + Ariya4 |
| L2 | System Lens | Map variables, feedback loops, leverage, dead weight |
| L3 | Compound Mind | All-path mapping + cross-domain synthesis |
| L4 | Shadow Gate | 5-protocol self-critique — **always runs, non-skippable** |
| L5 | Synthesis | Verified output with mandatory confidence field |

---

## Quick Start

### Install as a Claude Skill

1. Copy the entire `SKILL.md` file contents
2. In Claude.ai → Settings → Skills → Create New Skill
3. Paste the content
4. Name it: `first-principle-codex-os`
5. Save and activate

### Use as Base for Your Own Skill

```yaml
---
name: "your-skill-name"
base_os: "first-principle-codex-os"
base_os_version: "1.0"
description: |
  Your skill description here.
  Built on FPCOS v1.0 by Bunyawat Dechanon (ElmatadorZ).
---
```

---

## Skill Interface Contract

| # | Contract | Removable? |
|---|---|---|
| 01 | Inherit Reality Anchor (L0) | ❌ |
| 02 | Apply Kalama10 as proof standard (L1) | ❌ |
| 03 | Use Ariya4 for problem framing (L1) | ❌ |
| 04 | Run Shadow Gate before output (L4) | ❌ |
| 05 | State confidence % and unknowns (L5) | ❌ |

**Skills MAY:** Add layers between L2–L4, rename layers for domain.
**Skills MAY NOT:** Remove L0, L1, L4, L5. Violate Kalama10.

---

## Repo Structure

```
fpcos/
├── SKILL.md                          ← Main skill file. Copy this.
├── README.md
├── LICENSE.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── references/
│   ├── CODEX_KALAMA.md
│   ├── CODEX_ARIYA4.md
│   ├── SHADOW_GATE_DEEP.md
│   ├── COMPOUND_MIND_PATTERNS.md
│   ├── SKILL_INHERITANCE.md
│   └── ANTI_HALLUCINATION.md
├── examples/
│   ├── example-finance-skill.md
│   └── example-research-skill.md
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md
    │   └── skill_proposal.md
    └── PULL_REQUEST_TEMPLATE.md
```

---

## License

**Open Cognitive License v1.0**
- ✅ Free — non-commercial & commercial revenue < $10M USD/year
- 💰 2% gross revenue — systems generating > $10M USD/year
- 📌 Attribution required: *"Built on FPCOS v1.0 by Bunyawat Dechanon (ElmatadorZ)"*

---

## Author

**Bunyawat Dechanon (ElmatadorZ)**

> *"ระบบที่ดีที่สุดคือระบบที่ตั้งคำถามกับตัวเองได้ — และยังทำงานได้ต่อ"*
> *"The best system is one that questions itself — and still functions."*

(judgment007@gmail.com)
