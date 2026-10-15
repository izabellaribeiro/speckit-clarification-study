I’ll use the installed speckit-clarify skill, first reading the required instructions and constitution, then reviewing only the active story for substantive ambiguities.

1. Which prerequisite story must be completed before image upload is allowed? [NEEDS CLARIFICATION: The prerequisite is unidentified, so developers cannot determine which dependency controls upload availability.]

2. What observable condition establishes that the prerequisite story has been completed? [NEEDS CLARIFICATION: “Completed” lacks a testable definition, leaving the upload eligibility rule undefined.]

3. Whose completion of the prerequisite determines whether a user may upload an image? [NEEDS CLARIFICATION: The story does not establish whether completion applies to the uploading user or a broader scope, risking incorrect access decisions.]

4. What should happen when a user attempts to upload an image before the prerequisite is completed? [NEEDS CLARIFICATION: The blocked interaction and failure response are unspecified, preventing consistent enforcement and acceptance testing.]

5. What image formats and maximum file size are permitted? [NEEDS CLARIFICATION: Upload validation boundaries are missing, leaving acceptance of unsupported or oversized files undefined.]