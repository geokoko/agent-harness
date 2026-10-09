# Interaction evidence

Use only the checks relevant to the changed controls; this is not a mandatory
full-site audit. Prefer existing accessible components and native semantics.

- Use buttons for actions and links for navigation. Associate inputs with labels,
  icon-only controls with accessible names, and field errors with their inputs.
  Preserve useful input after validation failures and expose feedback beyond color.
- Inspect keyboard order, visible focus, activation, opening/closing and the focus
  destination after an operation. Follow the actual component pattern: modal
  dialogs contain focus while open and restore it appropriately on close;
  menus have their own navigation and dismissal behavior. Do not apply a modal
  focus trap to every popup. Consult the relevant WAI patterns for
  [modal dialogs](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) and
  [menu buttons](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/) when needed.
- Check the control's real loading, empty, failed, disabled and completed states.
  A successful click or lack of a console error does not prove the intended
  state change occurred. Inspect the resulting UI and relevant data evidence.
- Try relevant narrow/wide layouts, zoom, long or translated content and touch
  operation. Intentional scrolling tables differ from accidental page overflow.
  Ensure essential actions do not depend on hover alone.
- Use meaningful image alternatives and reserve media space to limit layout
  shifts. Choose loading behavior for the image's role instead of lazily loading
  every image. Keep motion purposeful and honor reduced-motion settings.

Record which behavior was operated, which was inspected in markup and which was
unavailable. Screenshot checks, code inspection and automated scans provide
different evidence; none alone proves full accessibility conformance.
