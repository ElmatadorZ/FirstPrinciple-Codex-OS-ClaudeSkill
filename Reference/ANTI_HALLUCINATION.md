# ANTI_HALLUCINATION.md — Anti-Hallucination Pattern Catalog

**Load when:** debugging hallucination in skill output, or designing domain-specific anti-hallucination measures.

---

## Quick Diagnostic

```
Hallucination type             Layer   Protocol
──────────────────────────────────────────────
Invented facts                 L0      Reality Anchor
Unverified authority           L1      Kalama10 Test 6
Symptom as problem             L1      Ariya4 Field 1–2
Only one solution considered   L3      Compound Mind
Framing limits options         L4      Mirror
Confidence too high            L4      Inversion
Missing contradicting data     L4      Blind Spot
Biased data sources            L4      Interest Map
Analysis paralysis             L4      Meta-Void
No confidence declared         L5      Confidence field
```

---

## Source 1 — Pattern Completion as Fact
Detection: Smooth authoritative tone, no hedging, not traceable to evidence.
Fix: L0 — declare UNKNOWN. Do not invent.

## Source 2 — Unverified Authority
Detection: "Experts agree..." / "Research shows..." without citation.
Fix: L1 Kalama10 Test 6. Require independently testable claim.

## Source 3 — Symptom as Root Cause
Detection: Solution addresses what you see, not what causes it.
Fix: L1 Ariya4 Fields 1–2. Problem ≠ symptom.

## Source 4 — Single-Axis Blindness
Detection: "The only way..." No alternatives presented.
Fix: L3 Compound Mind. Map all axes first.

## Source 5 — Missing Cross-Domain Solution
Detection: Correct but suboptimal. Better axis existed.
Fix: L3 Cross-Domain Patterns. Check pattern library.

## Source 6 — Framing Bias
Detection: Binary framing ("A or B?"). Loaded terminology.
Fix: L4 Mirror. Name hidden assumption before answering.

## Source 7 — Overconfidence
Detection: "Definitely / certainly / always" without proportional evidence.
Fix: L4 Inversion. If HIGH → FRAGILE → cap ≤70%.

## Source 8 — Missing Contradicting Data
Detection: Conclusion too clean. No acknowledgment of what would change it.
Fix: L4 Blind Spot. Name specific reversing data. Flag if absent.

## Source 9 — Incentive-Corrupted Input
Detection: All evidence points same direction. No contrary evidence on contested topic.
Fix: L4 Interest Map. Name incentive field.

## Source 10 — Analysis Loop
Detection: Third/fourth iteration. No convergence toward decision.
Fix: L4 Meta-Void. NOISE → decide. OBVIOUS → act.

## Source 11 — False Certainty in Output
Detection: No confidence qualifier. No unknowns. Looks like ground truth.
Fix: L5 Confidence field mandatory.

---

*FPCOS Reference — Bunyawat Dechanon (ElmatadorZ) — Open Cognitive License v1.0*
