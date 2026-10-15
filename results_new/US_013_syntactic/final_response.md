I’ll read the required instructions, identify the active spec, and use the speckit-clarify skill to produce a single batch of clarification questions without changing files.

1. What operations does “manage unrelated user credentials” include? [NEEDS CLARIFICATION: The permitted credential operations are undefined, preventing implementation and acceptance testing of this capability.]

2. Whose credentials may a Zooniverse admin manage? [NEEDS CLARIFICATION: The affected users and administrative authority are unspecified, leaving access boundaries undefined and risking unauthorized credential changes.]

3. What conditions indicate that a volunteer should receive education? [NEEDS CLARIFICATION: No decision criteria define when education is needed, so developers cannot implement or validate the identification logic.]

4. How should the admin be informed that a volunteer needs education? [NEEDS CLARIFICATION: The story does not define how this information reaches the admin, leaving the core interaction and its acceptance criteria uncertain.]

5. Does the education capability include educating the volunteer, or only identifying when education is needed? [NEEDS CLARIFICATION: The boundary between identifying a need and delivering education is unclear, creating materially different implementation scopes.]