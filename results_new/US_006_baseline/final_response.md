I’ll use the installed speckit-clarify skill, read the required instructions first, and review only the active story without modifying files.

1. Which audio and visual quality metrics must admins be able to filter by? [NEEDS CLARIFICATION: The story names no metrics, leaving the required video attributes and filter coverage undefined.]

2. How are quality metric values obtained for each video? [NEEDS CLARIFICATION: The source of metric values is unspecified, leaving unclear whether this feature must produce those values or consume existing data.]

3. How should an admin specify the matching condition for each metric? [NEEDS CLARIFICATION: Undefined comparison rules prevent determining which videos qualify and writing verifiable acceptance tests.]

4. How should multiple metric conditions combine to determine whether a video matches? [NEEDS CLARIFICATION: Different combination rules produce different result sets for the same selected filters.]

5. How should filtering treat videos with missing quality metric values? [NEEDS CLARIFICATION: Undefined handling of incomplete data can silently include or exclude videos and produce inconsistent results.]