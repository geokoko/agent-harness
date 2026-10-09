# Bounded deployment comparison

Record the baseline revision, environment, time, checked pages/endpoints, and
available response, console, screenshot, and timing evidence. Compare equivalent
environments. A new snapshot without an earlier baseline cannot establish the
absence of a deployment regression.

Use the requested observation interval and duration, or state a bounded default.
Repeat suspicious observations to distinguish transient failures. Preserve the
old baseline; replace it only when promotion is requested. Read selected legacy
baselines in place instead of silently migrating or deleting them.

Report observed changes and unavailable signals. Monitoring does not create a
background daemon or authorize rollback.
