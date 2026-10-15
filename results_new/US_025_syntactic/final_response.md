I’ll read the required instructions and use the speckit-clarify skill to identify up to five unanswered questions for the active story, without modifying files.

1. What does “user credentials” refer to in this story? [NEEDS CLARIFICATION: The term does not identify the data being managed, leaving its sensitivity and data model undefined.]

2. Which actions must the moderator be able to perform on user credentials? [NEEDS CLARIFICATION: “Manage” does not specify supported operations, so implementation scope and acceptance tests cannot be determined.]

3. Which users’ credentials may a moderator manage? [NEEDS CLARIFICATION: The authorization boundary is unspecified, risking unauthorized access to or changes to other users’ credentials.]

4. What information must a game transcript contain in the exported CSV? [NEEDS CLARIFICATION: Transcript contents and CSV fields are undefined, preventing validation of export completeness and correctness.]

5. How does the moderator identify the game whose transcript should be exported? [NEEDS CLARIFICATION: The story provides no game-selection rule, leaving the export target and user interaction undefined.]