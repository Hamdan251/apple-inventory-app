# Branch Workflow: Spec-Driven Development (SDD)

This branch documents the implementation of the identical inventory export feature, but executes it using **Spec-Driven Development (SDD)**. Instead of letting the AI guess project constraints, a formal document was engineered first to constrain the LLM inside strict boundary limits.

## What Was Done
1. **Document-First Architecture:** Created an isolated directory called `open-spec` and authored a formal `spec.md` markdown blueprint outlining data schemas, hard requirements, and system checks.
2. **Specification Controls:** Explicitly outlined mandatory column titles (`"Apple Variety"`, `"Quantity"`), a designated naming convention (`apple_report.csv`), and an active data validation rule to catch items with an active stock count of zero.
3. **Contextual Anchoring:** Prompted the online AI Chat engine by passing the document directly as context: *"Read open-spec/spec.md and update app.py to implement the CSV export feature strictly using these requirements and guardrails."*
4. **Implementation:** The AI verified the code against the specifications, integrating defensive logic blocks into `app.py`.

## Results & Outcomes
* **Defensive Guardrails Added:** The application successfully flags out-of-stock items (such as zero-count Granny Smith apples) directly within the CSV row data as `[OUT OF STOCK]`, keeping errors from breaking the database layer.
* **Output Artifact:** Automatically generates a precisely formatted `apple_report.csv`.
* **Architectural Takeaways:** Anchoring the LLM to a specification source file completely eliminated hallucinations and assumptions. The resulting codebase is highly clinical, predictable, and structurally decoupled from the AI's internal tendencies—demonstrating production-grade AI engineering.
