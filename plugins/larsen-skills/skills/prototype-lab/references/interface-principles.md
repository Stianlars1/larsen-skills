# Interface principles

Use this reference when planning, building, or reviewing an interface. It is a
decision framework, not a visual recipe.

## Start with the product job

Before discussing polish, establish:

- who is using the surface;
- what they are trying to complete;
- what information or action is primary;
- what can fail or create irreversible consequences;
- which states must exist: loading, empty, partial, error, success, disabled,
  offline, and permission-limited;
- how often the user encounters the surface.

If the product job is unclear, visual polish cannot make the interface correct.

## Establish reading and action order

The visual hierarchy should match the user's likely sequence:

1. orient;
2. understand the current state;
3. identify the next action;
4. inspect supporting detail;
5. recover from uncertainty or error.

Use grouping, alignment, spacing, contrast, type scale, and progressive
disclosure to make that order legible. Avoid equally loud sections, arbitrary
cards, and decorative separation without semantic grouping.

## Make relationships visible

- Keep labels close to the values or controls they describe.
- Align related content to shared edges or baselines.
- Use spacing as a hierarchy system, not a collection of isolated numbers.
- Prefer fewer containers. Add a surface only when it communicates grouping,
  state, depth, or interaction.
- Keep the DOM reading order meaningful before changing visual order.
- Test narrow and wide layouts as recomposed interfaces, not scaled screenshots.

## Make interaction legible

Every interactive element needs:

- an understandable label;
- a visible affordance;
- hover, focus, active, disabled, loading, and error behavior where applicable;
- a sufficiently large target;
- keyboard operation;
- state that does not rely on color alone;
- feedback proportional to the action.

Do not make a visual layer carry semantic responsibility. Use real links,
buttons, inputs, and controls underneath or alongside decorative effects.

## Preserve user control

- Confirm destructive or costly actions when the consequence is not obvious.
- Keep escape routes and undo close to the affected action.
- Do not steal focus or unexpectedly move content.
- Make optimistic feedback distinguishable from confirmed completion.
- Preserve input and context across recoverable errors.
- Ensure animation can be interrupted without producing an invalid state.

## Write for decisions

Interface copy should answer what happened, why it matters, and what the user can
do next.

- Use specific verbs for actions.
- Put the differentiating words early.
- Avoid vague labels such as "Submit", "Continue", or "Learn more" when a more
  precise label fits.
- Use sentence case unless the product language specifies otherwise.
- Keep errors close to their cause and retain the user's work.
- Use empty states to explain both meaning and next action.

## Treat accessibility as behavior

Check:

- semantic structure and landmarks;
- accessible names, descriptions, and relationships;
- focus order, focus visibility, and focus restoration;
- full keyboard operation;
- screen-reader announcements for important asynchronous state;
- contrast in every state;
- zoom, text resize, content reflow, and touch target size;
- reduced-motion behavior;
- input methods beyond a precision pointer.

Accessibility is not a final checklist. It changes the component and interaction
model from the beginning.

## Verify the actual experience

Review at least:

- initial, loading, empty, success, partial, and error states;
- keyboard-only operation;
- screen-reader structure where material;
- reduced-motion mode;
- representative narrow and wide viewports;
- slow network or delayed data where material;
- interruption and repeated interaction;
- real copy and realistic content lengths.

Separate source inspection, local runtime observation, and live-environment proof
in the final report.
