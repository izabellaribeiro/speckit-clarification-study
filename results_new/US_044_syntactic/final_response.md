I’ll read the required instructions and use the speckit-clarify skill to assess the active story, then report up to five prioritized questions without changing files.

1. What should happen to an image when it is automatically “isolated”? [NEEDS CLARIFICATION: “Isolate” does not define the required action or the image’s resulting availability, leaving the core behavior untestable.]

2. What qualifies an image as containing “no animals,” including cases with partially visible or indistinct animals? [NEEDS CLARIFICATION: The classification boundary is undefined, so images containing animals could be incorrectly isolated.]

3. Which Snapshot Serengeti images should be processed, and what should trigger processing? [NEEDS CLARIFICATION: The eligible image set and processing trigger are unspecified, leaving coverage and execution timing undefined.]

4. How should processing handle images whose animal presence cannot be determined? [NEEDS CLARIFICATION: No behavior is defined for uncertain results, creating a risk of incorrect isolation or silently unprocessed images.]

5. What maximum rate of incorrectly isolating images that contain animals is acceptable? [NEEDS CLARIFICATION: No measurable accuracy requirement is provided, preventing validation of whether automatic isolation is sufficiently reliable.]