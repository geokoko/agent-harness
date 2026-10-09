# Optional task templates and design preferences

Read only the relevant section. These are reusable output shapes, not stages,
mandatory files, or additional approvals. Reuse the project’s existing formats
and vocabulary. A request to draft a plan or review an idea does not authorize
implementation; existing implementation authority does not expire because a
plan is useful. Keep advice in the conversation unless a saved artifact helps
or is requested.

## Plan or specification

Use observable outcomes and the smallest coherent scope. Read the relevant
code and existing decisions before inventing work. Resolve questions that
materially change the result; batch related questions and continue independent
work. A ready implementation request does not need a compulsory interview.

```text
Objective and intended user behavior:
Current behavior and relevant evidence:
Scope and material exclusions:
Acceptance criteria (observable pass/fail):
Proposed approach and important alternatives:
Dependencies, constraints and consequential unknowns:
Smallest complete increment(s), in dependency order:
Validation and rollout/recovery needs when relevant:
Existing authority; any remaining decision:
```

Keep the format proportionate. An acceptance criterion states what must be
true, not merely which files should be edited. An existing accepted plan can
be reused when its assumptions and source revision still apply. Distinguish
an unresolved product decision from an implementation detail the agent can
reasonably choose within scope.

## Tickets and vertical slices

Prefer narrow increments that deliver an observable end-to-end behavior.
Include only the layers each behavior actually needs. Each ticket should be
verifiable in its own right and state its blocking dependencies.

```text
Title:
What this makes possible:
Acceptance criteria:
Blocked by (or none):
Relevant constraints/decisions:
Validation:
```

For a wide mechanical migration, use expand → migrate → contract: introduce a
compatible form, move consumers in coherent batches, then remove the old form
when no consumer remains. If intermediate batches cannot be independently
green, say so and identify the integration verification that establishes the
result. Do not promise independent safety without evidence.

Draft in the requested destination; an ordinary drafting request can finish
in chat. Creating external issues or changing an existing board requires the
corresponding authorization. Reuse an already-authorized publication scope;
do not require a second ceremony just because a template describes publication.
Avoid incidental paths that will become stale, but preserve a precise schema,
state transition or named interface when it records the actual decision.

## Domain language and decisions

Read the project’s existing glossary and ADRs. Separate customer/domain terms
from general programming vocabulary. Where a term has two meanings, show a
concrete scenario that exposes the ambiguity and compare the stated model
with the implementation. Do not quietly overwrite an established definition.

When an authorized glossary update is useful, keep it short:

```text
Term: one or two sentences defining the concept in this project.
Avoid: ambiguous synonyms, with a reason when needed.
```

Follow existing `CONTEXT.md`/`CONTEXT-MAP.md` conventions if present; do not
impose them on every repository. Keep the glossary about domain meaning;
put implementation choices in their owning technical records.

Record an ADR when a real tradeoff is consequential to reverse or would be
surprising without context. A short paragraph is enough:

```text
Decision title
Context, chosen option, and the reason for choosing it.
Rejected alternative or consequence only when useful to future readers.
Status or superseding decision when needed.
```

Use the existing location/numbering. Create new records only when artifact
edits are authorized; a discussion can deliver the proposed wording in chat.

## Modules, interfaces and testable boundaries

Preserve useful project vocabulary instead of imposing synonyms. When deciding
an interface, consider everything its caller must know: inputs, invariants,
ordering, errors, configuration and relevant performance behavior. Prefer an
interface that hides real complexity and keeps a related change local.

Ask whether removing a proposed abstraction would simplify the code or merely
redistribute the same complexity among callers. Avoid pass-through layers that
earn no simplification. Introduce adapters where real variation or an external
dependency warrants them. Accept external dependencies explicitly when that
makes behavior easier to test; do not introduce a framework to enforce this.
When multiple designs are plausible, compare a few materially different options
by caller burden, locality, migration cost and testability. Routine edits do
not require a design competition.

## Requested test-first work

When the user asks for TDD, work through one useful behavior at a time:
write a failing test, implement enough to satisfy it, then improve the code
while that behavior remains green. Use the project’s established public
interfaces and domain language. Resolve a material uncertainty about the
interface; do not demand approval for every test boundary already in scope.

Prefer tests that survive internal refactoring. Use independently derived
expected values from a specification, worked example or known result; copying
the implementation’s calculation into an assertion cannot challenge it.
Exercise realistic interfaces, using controlled external services, time,
randomness or a test database when needed. Mocking an internal call graph is
usually weaker evidence than checking its observable outcome.

Run the checks relevant to the change and report what actually executed.
Separate required coverage from passed, failed, skipped or unavailable checks.
Passing fixtures do not prove deployment, customer outcomes or live integration.
Do not add implementation-mirroring tests for reversible prose/layout changes.

## Provenance

Selected from the `main` snapshots of
[domain modeling](https://github.com/geokoko/agent-harness/tree/e65d080f2a69457942abaee69d613e1851e9314d/shared-skills/domain-modeling),
[module design](https://github.com/geokoko/agent-harness/tree/e65d080f2a69457942abaee69d613e1851e9314d/shared-skills/codebase-design),
[TDD](https://github.com/geokoko/agent-harness/tree/e65d080f2a69457942abaee69d613e1851e9314d/shared-skills/test-first-development),
[tickets](https://github.com/geokoko/agent-harness/blob/e65d080f2a69457942abaee69d613e1851e9314d/claude-skills/to-tickets/SKILL.md),
and September’s
[scope and evidence corrections](https://github.com/geokoko/agent-harness/blob/128efe0edf1418958e473f384694ea9358b6c435/docs/skill-tuning.md).
These selections deliberately remove compulsory interviews, universal seam
approval, fixed file destinations and repeated permission prompts.
