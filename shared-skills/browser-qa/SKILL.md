---
name: browser-qa
description: Exercise web-app user journeys in a real browser, reproduce failures, and create regression tests or fixes when requested.
---

# Browser journey verification

Use the request and existing context to distinguish exploratory QA, regression
test creation, and fixing a known failure. A QA-only request produces evidence
and findings; application edits and project test additions require matching
scope. Existing authorization persists. Ask only when an unresolved target,
account, or action boundary would change what can safely be tested.

## Use the client's Chrome MCP

Run interactive QA in Chrome through the active client's browser MCP:
- In GPT/Codex, use the GPT/Codex Chrome integration.
- In Claude Code, use Claude in Chrome.

Discover and follow that integration's current tools and instructions; tool names
and connection setup belong to the client. Select Chrome explicitly, preserving
unrelated tabs and sessions. If the required integration is unavailable, report
the blocker and leave browser verification pending. Do not silently substitute
the in-app browser, another browser, or a separate automation stack. A different
route needs the user's authorization. Existing regression tests and static
checks can supplement, but do not establish that this Chrome journey ran.

## Establish the journey and environment

Identify the affected journey, its expected result, starting state, relevant
roles, and environment. A smoke test checks the affected main path; a requested
journey sweep covers its relevant alternate and failure paths. State the depth
actually exercised. Use the actual application, the client's Chrome MCP,
test framework, fixtures, and startup instructions. Inspect enough code or docs
to understand the flow and available test data; do not replace the app with a
mock page or install a new browser stack merely to complete the check.

Prefer a disposable local environment or the designated test environment when
either can reproduce the behavior. Use approved accounts and isolated test data
where appropriate. Preserve the user's existing sessions and unrelated records.
Before a step sends a message, purchases, deletes real data, or otherwise changes
an external system, check that existing authority covers that action and target.
Continue within granted scope; ask only for a missing consequential authorization.
Clean up only records created for this test when their removal is authorized.

## Exercise observable behavior

Operate the relevant journey from its real entry point through the expected
outcome. Verify the resulting state or data, not just a successful click, a page
load, or the absence of console errors. When persistence is part of the expected
behavior, check after reload or from another affected view. Inspect failure paths and alternate
states that could affect this change, such as validation, empty results,
loading, permission differences, retries, or returning to a partially completed
flow. Scale coverage to the task instead of expanding into a full-site audit.

Check relevant viewport, keyboard, focus, and touch behavior. Treat screenshots,
markup inspection, executed interactions, and automated scans as different
evidence; no single one establishes complete accessibility. Use observed page
state and stable user-facing locators according to the available tool's rules.
Avoid fixed sleeps when the tool can wait for the actual state transition.

Keep failures reproducible: record the starting state, actions, expected and
actual outcome, environment, and useful screenshot, trace, or log evidence.
Distinguish application defects from unavailable dependencies, setup failures,
and incomplete checks. If a potentially consequential submission times out,
inspect whether it took effect before retrying; do not repeat uncertain writes
until something appears to work. Protect credentials, session state, and private
data in captured artifacts and anything shared with the user.

## Automate or repair within the requested scope

When regression tests are requested, use the project's existing conventions and
isolated fixtures. Assert user-observable outcomes, include the demonstrated
failure where useful, and check that the test detects that failure. A recorded
interaction script without outcome assertions is not a regression test.

When fixes are authorized, repair the cause and re-run the affected journey and
relevant existing checks. Capture fresh evidence after the change. Do not weaken
assertions or silently replace expected screenshots just to turn a failure green.
If a fix or automation is outside scope, report a concrete reproduction and the
smallest useful correction instead of modifying the project.

Report the tested environment and revision when known, journeys and states
actually exercised, confirmed failures, changes made, and remaining untested
scope. If the browser or app cannot run, state that limitation and distinguish
any static inspection from executed QA. Testing does not authorize publication,
deployment, or changes to personal client configuration.
