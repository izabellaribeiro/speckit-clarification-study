I’ll read the required instructions and use the speckit-clarify skill to assess the active story, then report up to five prioritized questions without changing files or proposing answers.

1. What criteria determine that a Snapshot Serengeti image contains no animals? [NEEDS CLARIFICATION: Without a defined classification rule, implementation and acceptance tests cannot establish which images qualify for isolation.]

2. What should happen to an image when it is “isolated”? [NEEDS CLARIFICATION: The required change to image status, storage, or workflow visibility is undefined, leaving the feature’s core behavior ambiguous.]

3. What event should trigger automatic evaluation of an image for isolation? [NEEDS CLARIFICATION: The story does not specify when processing begins, so developers cannot determine which images are evaluated or when.]

4. What is the maximum acceptable time between that trigger and completed isolation? [NEEDS CLARIFICATION: “Promptly” provides no measurable deadline for implementation or performance validation.]

5. How should the system handle images whose animal presence cannot be determined confidently? [NEEDS CLARIFICATION: Undefined handling of uncertain images could isolate images containing animals or leave qualifying images unprocessed.]