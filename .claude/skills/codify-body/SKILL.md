---
name: codify-body
description: Runs the whole draft-and-review body over every file in candidates/ in one shot - implementer drafts a fix in an isolated worktree, an independent reviewer grades it, PASS gets merged to main, FAIL gets left alone with a reason. No step-by-step prompting needed, one command does the whole thing.
---

# codify-body

This is Project 4's process (draft in isolation, independent review, only
PASS ships) turned into one reusable command instead of something typed
out by hand each time.

## Steps, run once per file in candidates/

1. Find every `.py` file under `candidates/` that has a matching failing
   test under `tests/`.
2. For each one, create an isolated git worktree on its own branch
   (`codify/<candidate-name>`) so drafts never collide with each other or
   with the main checkout.
3. In that worktree, draft a fix for the failing test(s).
4. Run the project's test command (`.venv/Scripts/python -m pytest -q`)
   inside the worktree.
5. Hand the diff and test result to a fresh reviewer agent that has no
   memory of this run or any prior run. It replies PASS or FAIL with
   reasons.
6. On PASS: merge that branch into main, remove the worktree.
   On FAIL: leave the worktree/branch as-is, record the FAIL reason, move
   to the next candidate.
7. Report one summary line per candidate at the end.

## What this does NOT do

No file here tracks what ran last time. Nothing gets read at the start of
a run or written at the end that a future run depends on. Run this skill
twice in a row and the second run has no idea the first one happened - it
just looks at whatever `candidates/` and `tests/` contain *right now* and
starts from zero. That is the point of Project 5: this is a reusable
engine, not a loop with a memory.
