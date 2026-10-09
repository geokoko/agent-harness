# Comparable browser measurements

For each named page, collect at least three fresh loads and report per-metric
medians and spread. Record revision, URL, browser, network/cache conditions, and
time. Compare equivalent loads; cached SPA transitions are a different workload.
Missing cross-origin transfer-size data is unknown, not zero bytes. Bound each
observation window and the total number of attempts before collecting; disconnect
observers on completion or timeout. Keep unavailable paint/timing values null,
including pages with no emitted paint entry. A median requires at least three
numeric samples for that metric; otherwise report insufficient observations.
Do not retry indefinitely to make incomplete measurements look complete.

Use the project's metric definitions, thresholds, and accepted baseline. Without
an equivalent baseline, report absolute measurements and uncertainty rather than
a regression verdict. Preserve raw measurements behind the conclusion.

A requested baseline capture may create a baseline. Replacing an accepted
baseline requires promotion intent and retention of the previous evidence.
