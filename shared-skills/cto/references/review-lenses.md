# Engineering decision lenses

Select the lenses that could materially change the requested decision.
Gather the smallest evidence set that can support or refute the
important claims.

## Architecture and technical direction

Trace one representative critical flow through boundaries, data
ownership, dependencies and failure paths. Check whether the design
supports the actual product and delivery constraints. Identify coupling
that makes a specific change unsafe or slow; file count and
architectural style alone prove little.

Compare a targeted improvement with a larger change only when both are
viable. For a proposed service split, rewrite, framework change or new
abstraction, state the concrete constraint it solves, the transition
cost, the new operating burden, and the evidence that the existing
approach cannot reasonably meet the need. Keep deliberate, useful
simplicity when it fits the team and the workload.

## Reliability, data integrity and operational readiness

Inspect the critical failure modes and their consequences: timeouts,
retries, duplicate work, partial writes, dependency failure, degraded
operation and recovery. Follow the ownership of alerts, incidents,
releases and rollback. Distinguish configured controls from evidence
that they were exercised.

Use the product's agreed reliability and recovery requirements. If none
exist, propose targets as decisions, not as existing service guarantees.
Check what a restore exercise, rollback rehearsal or incident record
actually covers. Missing telemetry or rehearsals can leave readiness
unknown without proving failure. Recommend the smallest safe
verification; do not test production or trigger failover as an
incidental part of a review.

## Scalability, performance and cost

Establish the actual workload shape, concurrency, growth assumptions,
measured latency and error rates, limiting resource and dependency
constraints. Cite the measurement window and environment. Distinguish a
local result from production capacity and a forecast from observed
demand. Missing traffic or cost data calls for a measurement plan, not
an invented capacity ceiling or savings figure.

Tie infrastructure cost to workload and useful output. Include storage,
network, external services, model usage where applicable, and
operational labor when evidence supports it. Compare alternatives using
explicit assumptions and dated vendor sources; label estimates and their
sensitivity to workload. Suggest resource changes without provisioning
or purchasing them during a review.

## Technical debt and delivery capacity

Identify debt through concrete costs: repeated incidents, recurring
rework, slow changes, brittle tests, difficult onboarding or unclear
ownership. Use the available change history and delivery evidence rather
than code aesthetics. Separate maintenance required for a near-term
commitment from discretionary cleanup. Account for available skills,
capacity, dependencies and support work.

For an engineering priority list, connect each item to a product
commitment or an operating risk. Propose the smallest complete increment
and its validation. Preserve existing priorities unless evidence
justifies a visible tradeoff. Avoid arbitrary capacity allocations,
made-up headcount, or a rewrite presented as debt reduction.

## Build versus buy and dependency choices

Compare the current approach, a bounded internal solution and relevant
existing services where appropriate. Include capability fit, integration
and migration, data handling, contractual constraints, failure modes,
exit costs and long-term maintenance. Check current primary sources for
facts that can change.

Separate technical feasibility from procurement, security and business
approval. Do not infer vendor suitability from marketing, or treat
signing up for a trial as harmless when it creates an account,
obligation or charge. A recommendation identifies the decisive unknowns
and the smallest evaluation that resolves them.

## Security and product boundaries

Consider trust boundaries, data sensitivity, access ownership and
dependency risk when they affect technical direction or readiness. A
concrete concern or an explicitly requested audit warrants an in-depth
security review; a technical-direction overview is not a security
certification. Integrate current specialist evidence instead of
duplicating reviews by default.

Product strategy establishes customer outcomes and priorities.
Engineering assesses feasibility, cost, sequencing and operational
consequences. Surface a conflict with evidence and options; do not
quietly replace the user's product direction, privacy requirements or
accepted release criteria.
