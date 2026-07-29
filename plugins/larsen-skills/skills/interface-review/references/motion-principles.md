# Motion principles

Use motion to explain change, preserve continuity, provide feedback, or express a
deliberate product character.

## Pass the purpose and frequency gate

For every animation, state:

- what the user should understand or feel;
- whether motion improves comprehension, feedback, continuity, spatial
  orientation, or brand expression;
- how often it occurs;
- whether it blocks input or delays completion;
- what happens in reduced-motion mode.

Frequent transitions should be quieter and shorter. Rare, expressive moments can
carry more character and duration. If the purpose is only "make it feel modern",
keep exploring or remove the motion.

## Describe motion precisely

Specify:

- trigger and end condition;
- affected elements and hierarchy;
- property changes;
- duration or spring parameters;
- easing per property;
- delay, overlap, and stagger;
- transform origin;
- interruption and reversal behavior;
- responsive and reduced-motion alternatives;
- completion state and focus behavior.

Separate choreography from implementation syntax so the intent survives a
library change.

## Choose timing from distance and context

- Small local feedback is usually faster than a large spatial transition.
- Exit can be faster than entrance when the departing element is no longer
  important.
- Coordinated properties do not always need identical easing.
- Use dwell in ambient cycles so the interface is readable between transitions.
- Avoid long sequential chains that make the user wait.

Duration values are starting hypotheses. Verify them in the actual interface.

## Use easing to communicate physical or attentional behavior

- Ease-out emphasizes arrival and is useful for many entrances and direct
  responses.
- Ease-in can make an exit feel decisive.
- Ease-in-out suits travel with a visible departure and arrival.
- A spring is useful when preserving velocity, reacting to gestures, or creating
  a material settle.
- Linear timing is appropriate for continuous progress, constant rotation, or
  time-based scrubbing.

Do not use a spring merely to add bounce. Choose damping and response from the
desired character, and avoid overshoot when it harms precision.

## Preserve continuity and velocity

- Prefer transforms and shared geometry when an object should feel continuous.
- Keep transform origin consistent with the perceived hinge, pivot, or force.
- When an animation is interrupted, begin the next response from the current
  visual state rather than snapping to a stored endpoint.
- Avoid overlapping controllers that fight over the same property.
- Treat layout measurement, scroll, drag, and resize as changing inputs.

## Design gestures as systems

Define:

- the direct manipulation region;
- drag axis and constraints;
- visual resistance beyond a boundary;
- distance and velocity thresholds;
- cancel and escape behavior;
- keyboard and non-pointer alternatives;
- focus behavior after completion;
- how the gesture responds to interruption.

The interface must remain operable without performing the gesture.

## Protect performance

- Prefer `transform` and `opacity` for frequent animation.
- Measure before applying `will-change`, and scope it to the active transition.
- Avoid repeated layout reads mixed with writes.
- Treat blur, filters, masks, large translucent layers, SVG path updates, and
  canvas contours as performance-sensitive.
- Test representative low-power hardware and busy pages, not only an isolated
  demo.
- Pause ambient work when the page is hidden and when the element is irrelevant.

## Reduced motion

Reduced motion is a designed variant:

- remove unnecessary travel, rotation, parallax, zoom, and looping;
- preserve state feedback through immediate changes or restrained fades;
- react if the preference changes while the interface is open;
- do not make essential information depend on animation completion.

## Verification

Test:

- rapid repeated input;
- mid-flight reversal;
- hover and focus during a scheduled cycle;
- hidden-tab and visibility restoration;
- resize and content changes;
- reduced motion at load and at runtime;
- unmount or navigation cleanup;
- keyboard and touch;
- dropped frames, layout shifts, and CPU/GPU cost;
- exact rest states so ambient cycles do not drift.
