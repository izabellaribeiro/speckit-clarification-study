I’ll read the required instructions, then use the speckit-clarify skill to identify up to five prioritized questions for the active story, without modifying files or proposing answers.

1. Which spreadsheet formats and sheet layouts must the import accept? [NEEDS CLARIFICATION: Undefined input formats and layouts prevent determining which files are supported and how story rows are identified.]

2. Which spreadsheet columns define a story, and which values are required or restricted? [NEEDS CLARIFICATION: Missing field mappings and validation rules prevent reliably creating valid stories from spreadsheet data.]

3. What should happen when a spreadsheet contains both valid and invalid story rows? [NEEDS CLARIFICATION: Undefined failure handling leaves whether to import any stories, reject the file, or report individual failures unresolved.]

4. How should the import identify and handle stories that duplicate existing stories or other spreadsheet rows? [NEEDS CLARIFICATION: Missing identity and duplicate-handling rules could cause repeated stories or unintended changes to existing data.]

5. What maximum import completion time and spreadsheet size define “promptly”? [NEEDS CLARIFICATION: The performance goal lacks a measurable time limit and workload, so acceptance tests cannot establish whether it is met.]