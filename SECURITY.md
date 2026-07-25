# Security Policy

FPCOS is a **cognitive base layer** — a reasoning contract that other skills inherit. Its security
surface is unusual, so it is worth stating precisely.

## What counts as a vulnerability here

### 1. Integrity bypass (most serious)
A way to satisfy the FPCOS contract on paper while defeating its purpose — for example:

- a phrasing that causes **L4 Shadow Gate** to be skipped, summarised away, or answered
  perfunctorily, when it is defined as non-skippable
- an input pattern that makes **L0 Reality Anchor** accept an unfounded premise as anchored
- a way to get a confident answer where **L1 Axiom Gate** should have forced a refusal
- inheritance that appears to preserve L0/L1/L4/L5 but neutralises them in practice

These are the reports that matter most: FPCOS is inherited by downstream skills, so a bypass
propagates to every one of them.

### 2. Prompt-injection resistance
Content that causes a skill running FPCOS to abandon the pipeline when processing untrusted input
(a pasted document, a web page, a tool result).

### 3. Tooling defects
Bugs in `tools/validate_skill.py` or CI — for example, a validator that reports PASS on a SKILL.md
with L4 removed.

## Out of scope

- Weaknesses of the underlying model itself (report to the model vendor).
- Downstream skills that inherit FPCOS incorrectly — report to that project.
- The fact that a sufficiently determined user can instruct a model to ignore any system prompt;
  FPCOS raises the cost of unfounded output, it does not make a model tamper-proof.

## Reporting

Report privately first via
[GitHub Security Advisories](https://github.com/ElmatadorZ/FirstPrincipleCodex-OS-Skill/security/advisories/new).
Please include the layer affected (L0–L5), a reproducible prompt or input, the observed output, and
what the pipeline should have produced instead.

**Response targets:** acknowledgement within 7 days · initial assessment within 30 days.

## Disclosure

Confirmed integrity bypasses are published in [CHANGELOG.md](CHANGELOG.md) with the layer affected
and the correction. Credit is given unless the reporter requests otherwise.

## Supported versions

| Version | Supported |
|---|---|
| 1.x | ✅ |
