I’ll use the installed speckit-clarify skill, first reading the required instructions, then reviewing the active story for up to five material ambiguities without modifying files.

1. Are both classification reliability weighting and credential management required in this feature? [NEEDS CLARIFICATION: The story explicitly couples unrelated goals, leaving the implementation scope and acceptance boundaries unclear.]

2. How is a volunteer’s experience level determined? [NEEDS CLARIFICATION: No experience measure or level definition is provided, so the input to the reliability calculation cannot be established consistently.]

3. What rule maps a volunteer’s experience level to a classification reliability weight? [NEEDS CLARIFICATION: The calculation and output scale are undefined, preventing implementation and verification of correct weights.]

4. Which user credentials must admins manage, and what management operations are required? [NEEDS CLARIFICATION: Neither the credential types nor the permitted operations are specified, leaving the credential management behavior undefined.]

5. Which users’ credentials may a Zooniverse admin manage? [NEEDS CLARIFICATION: The authorization boundary is unspecified, risking unauthorized changes to other users’ access.]