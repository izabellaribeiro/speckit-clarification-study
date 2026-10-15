I’ll read the required instructions and use the speckit-clarify skill to identify up to five prioritized questions, without modifying files or proposing answers.

1. What criteria determine whether a segmented video clip is valid? [NEEDS CLARIFICATION: “Correct criteria” is undefined, preventing implementation of validation rules and testable acceptance conditions.]

2. Does “validate” mean an admin manually reviews clips, the system automatically checks them, or both? [NEEDS CLARIFICATION: The story does not establish who performs the checks, leaving the required system behavior and admin workflow uncertain.]

3. What outcome must be recorded for each clip after validation? [NEEDS CLARIFICATION: Validation results and their effect on clip status are unspecified, leaving the data model and completion behavior undefined.]

4. Which segmented clips must an admin be able to validate? [NEEDS CLARIFICATION: The eligible clip set and admin access boundaries are unspecified, risking incorrect scope or unauthorized access.]

5. What should happen when a clip cannot be assessed because its video content is unavailable or unreadable? [NEEDS CLARIFICATION: No failure behavior is defined, risking an unassessable clip being treated as valid or invalid without a completed assessment.]