# SKILL_INHERITANCE.md — How to Inherit FPCOS in Your Skill

**Load when:** building a new Claude Skill that uses FPCOS as base OS.

---

## Step 1 — Declare Inheritance in Frontmatter

```yaml
---
name: "your-skill-name"
version: "1.0"
author: "Your Name"
base_os: "first-principle-codex-os"
base_os_version: "1.0"
description: |
  Your skill description.
  Built on FPCOS v1.0 by Bunyawat Dechanon (ElmatadorZ).
---
```

---

## Step 2 — Map Your Pipeline

```markdown
## PIPELINE
INPUT → [L0 Reality Anchor] → [L1 Axiom Gate]
      → [L2 System Lens] → [YOUR DOMAIN LAYERS] → [L3 Compound Mind]
      → [L4 Shadow Gate + extensions] → [L5 Synthesis]
```

---

## Step 3 — Declare Contract Compliance

```markdown
## FPCOS CONTRACT COMPLIANCE

| Contract | Implementation in [Your Skill] |
|---|---|
| L0 Reality Anchor | [how Known/Inferred/Unknown works in your domain] |
| L1 Kalama10 | [proof standard for domain claims] |
| L1 Ariya4 | [problem frame adapted to domain] |
| L4 Shadow Gate | [5 core protocols + domain extensions] |
| L5 Confidence | [confidence field format] |
```

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails |
|---|---|
| Skip L0 "for obvious questions" | Obvious = highest Mirror failure risk |
| Remove Blind Spot "for expert topics" | Expert ≠ complete. Most needed here. |
| Domain expertise exempts Kalama10 | Expertise narrows prior, doesn't eliminate verification |
| Domain extensions replace core 5 | Extensions are additive. Core always runs first. |
| Remove confidence field "for simple output" | Simple + false certainty = hallucination |

---

## Attribution Template

```
Built on First Principle Codex OS v1.0
by Bunyawat Dechanon (ElmatadorZ)
https://github.com/ElmatadorZ/first-principle-codex-os
License: Open Cognitive License v1.0
```

---

*FPCOS Reference — Bunyawat Dechanon (ElmatadorZ) — Open Cognitive License v1.0*
