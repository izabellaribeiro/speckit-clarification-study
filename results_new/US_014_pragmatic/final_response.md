I’ll use the installed speckit-clarify skill, read the required instructions first, then review only the active story and report up to five clarification questions without changing files.

1. What terminology and conventions from the previous sprint must this feature follow? [NEEDS CLARIFICATION: The referenced terminology and conventions are absent from the story, leaving required behavior and acceptance criteria undefined.]

2. What conditions determine when Zoonibot should comment on a subject? [NEEDS CLARIFICATION: No decision rules are specified, so developers cannot implement or test whether a comment is warranted.]

3. What should the admin receive to “know when”: an explanation of the rules, a decision for a particular subject, or a notification when conditions are met? [NEEDS CLARIFICATION: The intended user interaction and observable outcome are ambiguous, leading to materially different feature implementations.]

4. Which subjects are eligible for Zoonibot comments? [NEEDS CLARIFICATION: The eligible subject scope is unspecified, so the feature could apply commenting rules to unintended subjects.]

5. How should an existing Zoonibot comment on a subject affect whether another comment is warranted? [NEEDS CLARIFICATION: Repeat-comment behavior is undefined, risking duplicate comments or suppression of required follow-up comments.]