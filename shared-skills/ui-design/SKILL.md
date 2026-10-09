---
name: ui-design
description: Design, build, redesign or polish web interfaces, from visual direction and design systems to responsive pages and components.
---

# Frontend design and implementation

Turn the requested interface work into a coherent, usable result. Infer whether
the user wants design exploration, a concrete direction, implementation or
polish. A review alone reports findings; building or polishing authorizes the
corresponding local changes. Existing authorization persists, and a settled
direction does not need another design-approval gate. No mode authorizes commits,
publication, installation or deployment by itself.
Scale preparation to the change: a spacing fix needs the affected component,
tokens and rendered result, not a full design brief or a site-wide redesign.

## Establish the direction

Inspect the relevant running interface, components, tokens, styles and existing
design/brand documents. Preserve approved patterns and reference fidelity unless
the user requests a redesign. Use the actual stack and supplied assets; do not
introduce a framework, UI kit, font service or other dependency by habit.
When reproducing a supplied reference, report meaningful deviations and their
reasons instead of silently replacing the requested direction with your taste.

Resolve the audience, the screen's main job, usage context and desired impression
from the brief. Ask only for missing answers that would change the direction.
When the user wants exploration, develop useful alternatives together. Otherwise
offer one coherent recommendation and connect concrete choices to the product's
needs: content hierarchy, layout/density, type scale, spacing, color roles,
imagery and motion. "Clean and modern" is not a usable design specification.

Use the [design preferences](references/design-preferences.md) when shaping a
new direction or judging visual polish. For a reusable design system, update
the existing source of truth when authorized; a concise `DESIGN.md` can be a
fallback when none exists. A small component change needs no new design document.

## Build or polish the requested interface

Implement the actual page or components when that is the request. Reuse the
project's component and token conventions; keep consistent variants and states
without introducing an abstraction for every small difference. Base the layout
on realistic content lengths and the user's task, not placeholder card counts.

Cover the states the feature needs: loading, empty, error, success, disabled,
selection, hover and visible focus. Use semantic elements, clear labels, keyboard
operation, sensible focus order and accessible feedback. Do not substitute a
screenshot or automated scan for an accessibility assessment. Respect reduced
motion and avoid animation that hides state or obstructs input.
For interactive controls, read the relevant [interaction checks](references/interaction-checks.md).

Check responsive behavior at useful widths, with long content, overflow, touch
interaction and zoom where relevant. Give images appropriate sizing and loading
behavior; avoid unnecessary dependencies or decorative effects that make the
interface slow or distracting. Judge performance against observed behavior.

Wire requested actions to real behavior when in scope. Identify prototype-only
or unavailable actions honestly; do not present dead controls, fake success,
invented testimonials, metrics or customer logos as a finished working product.
Use supplied or appropriately authorized assets and mark placeholder content.

## Verify the result

Use available browser/preview tools to inspect the affected rendered pages and
states. Check meaningful interactions and relevant keyboard/focus behavior, not
only whether the page loads. For polish, compare before and after in the same
conditions. Read the [rendered UI evidence guidance](references/visual.md)
when reviewing the result, and run the project's relevant existing checks.

Report the implemented scope, inspected views/states, actual check results and
remaining limitations. If the browser or application cannot run, complete safe
authorized work and disclose what remains visually unverified. Tool availability
does not authorize an installation or bypass. Preserve unrelated changes and
leave publication pending until explicitly requested.
