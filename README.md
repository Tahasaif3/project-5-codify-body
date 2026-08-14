# Project 5 - Codify the Body

Idea: Project 4's process (implementer drafts in isolation, an independent
reviewer grades it, only PASS ships) written down once as a skill
(`.claude/skills/codify-body/SKILL.md`) instead of typed out step by step
every time. Then prove it has no memory of its own runs - it's an engine
you can call, not a loop with a journal.

## Run 1 - three candidates at once
Three buggy files sat in `candidates/`, each with a failing test:
- `temp_convert.py` - used 30 instead of 32 in the F-to-C formula.
- `word_count.py` - split on a literal space, so extra spaces broke the count.
- `discount_cap.py` - no cap, so >100% discount went negative.

One pass through the skill's steps: a worktree per candidate, a fix
drafted in each, an independent reviewer agent grading each on its own
(no shared context between the three reviews) - all three came back
`PASS` and got merged to main.

## Run 2 - proving there's no memory
A fourth candidate, `dedupe.py`, was added afterward (order-losing bug
from using `set()`). Running the exact same skill steps again did not
"remember" the first three candidates in any way - there is no file this
skill reads at the start or writes at the end. It just looked at whatever
`candidates/` + `tests/` contained *at that moment*, found the one new
failing test, worktree'd it, fixed it, sent it to a fresh reviewer, got
`PASS`, merged it. Nothing recorded that Run 1 ever happened.

Compare this with Project 3's `progress.md`: that file is exactly the
piece this project deliberately does not have.

## Done when
- One skill invocation runs the whole draft-and-review body across
  several candidates, each in its own isolated worktree, each with its
  own independent reviewer verdict. Done - Run 1.
- A second invocation shows no memory of the first. Done - Run 2 handled
  a brand-new candidate with zero reference to what Run 1 did.
