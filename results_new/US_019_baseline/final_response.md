I’ll use the installed speckit-clarify skill, first reading the required instructions, then identifying and reviewing the active story without modifying files.

1. What should happen when the moderator selects an item for estimation or re-estimation? [NEEDS CLARIFICATION: The story does not define whether selection merely marks the item or starts an estimation process, leaving the required behavior and acceptance tests undefined.]

2. Which items are eligible for selection for estimation and for re-estimation? [NEEDS CLARIFICATION: No eligibility rules or item states are specified, so developers cannot determine which selections to allow or reject.]

3. What should happen to an item’s previous estimate when it is selected for re-estimation? [NEEDS CLARIFICATION: The treatment of existing estimates is undefined, risking unintended loss of results or inconsistent estimate history.]

4. Over which items does a moderator have permission to make selections? [NEEDS CLARIFICATION: The moderator’s authority is not scoped, leaving authorization checks undefined and potentially allowing unauthorized selections.]

5. What should happen if another item is selected while an estimation is already in progress? [NEEDS CLARIFICATION: The story does not define how overlapping selections affect ongoing work, risking interrupted estimation or results associated with the wrong item.]