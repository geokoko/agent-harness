# GitHub pull request reviews

Read this when the user asks to post review findings to a GitHub pull request.
Posting is an external write: do it only on that request, after the findings
are verified, and never mention the tools, agents or models involved.

Verify each claim against the code at the pull request head before posting;
drop or downgrade what you cannot confirm. Submit one review per request through
the pull request reviews API, pinned to the reviewed head commit. Use `COMMENT`
unless the user asks to approve or request changes; GitHub rejects both on the
author's own pull request.

Give each finding its own inline comment on the line that shows the defect. Open
with a severity label (High, Medium or Low, adding "regression" or "partly
inherited" when it applies), then state the defect, a concrete failure scenario,
the code evidence and the smallest correct fix. Say "reproduced" only for
behavior observed at runtime.

GitHub accepts inline comments only on lines inside the diff hunks. Check every
anchor against the diff from the merge base to the head before posting. Move a
finding on an unchanged line to the change that causes or exposes it and cite
the original line; put findings with no fitting line in the review body.

The review body states what was exercised, such as test-plan results, which
findings should block the merge, findings without a line, non-blocking cleanup,
and issues noticed that the pull request did not introduce.

After posting, confirm that every comment is attached to its intended line and
not outdated, then report the review URL.
