# NLP Emotional Drift & Ethical Framing Evaluation

This repository contains a manually annotated set of model-generated responses to open-ended prompts. The goal is to evaluate subtle issues in AI-generated answers such as emotional misalignment, ethical distortion, responsibility evasion, and justification drift.

## Contents

- `prompts_and_responses.csv`: 10 original prompts and ChatGPT baseline answers
- `annotations.csv`: Manual evaluations with binary flags and rationale
- `schema.md`: Description of annotation criteria

## Annotation Flags

Each response is evaluated on four criteria:
1. Emotion Drift
2. Ethical Distortion
3. Responsibility Shifted
4. Rewrite Needed

All annotations are binary (Yes/No), with justification embedded in comments or analysis.

## License

MIT License
