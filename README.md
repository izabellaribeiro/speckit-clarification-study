# Spec Kit Clarification Study

Replication materials for an exploratory study of user story perturbations in a noninteractive Spec Kit-based LLM clarification workflow.

The workload contains 45 parent stories, four conditions, and 180 executions. Human content review covers 100 selected questions (25 per condition); it is distinct from the complete execution counts.

## Contents

- `inputs/`: baseline, syntactic, semantic, and pragmatic inputs.
- `results_new/`: sanitized logs, final responses, and metadata for 180 executions.
- `speckit_codex/`: workflow template, clarification skill, and constitution.
- `run_replication.py` and `extract_markers.py`: execution and extraction scripts.
- `reference/`: documented human coding, final classification CSV, datasets, themes, and provenance records.
- `release_manifest.json`: SHA-256 hashes of released artifacts.
- `REPLICATION_STATUS.md`: preparation history, review scope, and methodological limitations.

## Inspecting and reproducing

Existing outputs can be inspected without rerunning the model. Running new executions requires a compatible Codex CLI and access to the configured model. From the repository root, inspect the runner options with `python run_replication.py --help`; preview the workload with `python run_replication.py --all --dry-run`. Model execution may incur costs and need not reproduce identical responses.

The original experimental hashes identify original files; sanitized release copies have separate hashes in the release manifest. Private original logs and Git history are not included. Historical preparation notes describe the state when recorded and should be read with subsequent confirmation entries.
