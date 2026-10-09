# Behavioral verification

Keep coverage and execution separate: a named test may exist without running in
this review. Report covered/partial/missing evidence separately from executed
pass/fail or not executed, with the reason.

Trace the claimed user behavior through its relevant entry point and consumers.
Exercise meaningful success and failure paths using existing disposable tests
or a safe local reproduction. Include boundary, repeated/concurrent action,
partial failure and authorization cases when they bear on the change.

State the assertions actually checked, the code revision/diff and any skipped
environment-dependent paths. A green command with skipped tests does not prove
those paths; static reading is not an executed test. Name the covering test for
a coverage claim and verify it can detect the relevant failure.

Do not manufacture one finding per missing test or test every possible input.
Separate confirmed failures, worthwhile unanswered questions, and established
coverage. Testing a live external system still requires matching authority.
