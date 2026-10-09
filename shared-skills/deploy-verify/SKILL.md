---
name: deploy-verify
description: Apply read-only verification to an explicitly requested existing deployment or monitoring window.
---

# Deployment verification contract

Identify the requested revision, environment, and provider run. The newest
unrelated successful run cannot establish this deployment's status. This skill
does not authorize deploying, retrying a release, rolling back, or changing
production data or configuration.

A successful pipeline does not establish which revision the environment serves.
Link the requested revision to the running release using a version endpoint,
build identifier, release record or equivalent evidence. Without that link,
report `UNVERIFIED` even if the site responds. Use the project's actual deployment
facts; do not guess a production URL or create configuration while verifying.

Verify the affected behavior with safe existing health/API/browser checks.
Record actual assertions and unavailable signals; inspect rendered evidence
before making visual claims. Missing access or an unavailable environment is
`UNVERIFIED`, never a healthy result.

Bound polling by a deadline appropriate to the request. For comparison over a
monitoring window, read [baseline handling](references/monitor.md). A suspicious
observation warrants verification and reporting, not an automatic rollback.

Report revision/run, environment, checks and evidence, skipped paths, and the
observed outcome: `LIVE AND HEALTHY`, `DEGRADED`, `FAILED`, or `UNVERIFIED`.
Healthy requires both the deployed revision and affected checks to be confirmed.
Degraded means a verified live failure; failed means a confirmed failed release
or service. An access or identity gap is unverified, not a failure diagnosis.
