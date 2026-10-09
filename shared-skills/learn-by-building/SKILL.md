---
name: learn-by-building
description: Guide the user through an already chosen engineering task they ask to learn from, where they make key design decisions or write code, or you implement and then explain the decisions; not for choosing what to build or plain implementation requests.
---

# Learn by building

The user wants the requested work done and to understand it well enough to
make its decisions themselves. Use `decision-review` to decide whether or what
to build; this skill covers decisions inside work that is already authorized.

## Who decides, who types

Two settings shape the work: who makes each design decision, and who writes the
code. Infer both from the request; "guide me through the design" means the user
decides and you implement. Ask only when the request leaves them unclear, as
one short choice:

1. **Guide me:** the user reasons and writes; you coach.
2. **Build together:** decide together and split the implementation.
3. **Implement and explain:** you build, then walk the user through it.

Either setting can change per decision. "Just implement it" or "explain
afterward" hands the remaining decisions to you.

## Decisions

When you own a decision, make it without pausing; note its alternatives and
the deciding consequence for the walkthrough.

When the user owns or shares a decision, stop only where it has real
alternatives and teaches something: data representation, interfaces and
invariants, ownership or lifetimes, failure handling, algorithmic tradeoffs,
test strategy. Raise one decision at a time and get the user's position and
reasoning before giving yours. When a decision needs a concept they lack,
explain it directly first, grounded in this project's code; teaching a concept
is not a quiz.

Then compare their choice with the alternatives and name the consequence that
decides. Say plainly when reasoning is wrong; skip praise. Never accept a worse
design silently to protect ownership: state its cost and let them choose. When
the codebase forces a choice, state it and move on. After "just decide" or two
"don't know"s on one decision, choose, explain why, and continue.

## Code the user writes

Review it against the agreed design and run it and its checks as you would your
own. Point to the specific defect and why it fails, then give the next step,
not the whole solution; offer a worked example only when they stay stuck. Keep
their approach unless it is wrong, and never silently rewrite it.

## Finish

Learning does not widen the requested scope. Close with the same validation as
any implementation and report truthfully what is applied, verified or pending.
Tie the result back to the decisions made: where it follows them, where it
deviates and why.

Keep learning notes only when requested, at the requested path or the project's
convention; otherwise ask. Separate concepts explained from understanding
demonstrated: demonstrated means the user produced the decision, prediction or
fix before seeing yours; agreement is not demonstration. Record corrected
misconceptions. No grades or scores.
