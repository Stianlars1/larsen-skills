# Visual systems

Use this reference to turn visual decisions into a coherent system.

## Typography

- Choose type for the product's voice, language coverage, legibility, and
  technical constraints.
- Define a small role-based scale before tuning individual screens.
- Pair font size with line height, measure, weight, and letter spacing.
- Use weight and contrast before adding more sizes.
- Balance headings deliberately; do not force line breaks that collapse with real
  content or localization.
- Use tabular figures for changing numeric data that should not visually jump.
- Test diacritics, long Norwegian and English words, numbers, and mixed-case UI
  labels.

## Color

- Prefer perceptual color tooling such as OKLCH for palette construction.
- Define colors by role: surface, text, border, accent, success, warning, danger,
  focus, and selection.
- Verify contrast after gamut mapping and in every interactive state.
- Keep hue and chroma changes purposeful across light and dark themes.
- Do not encode state through color alone.
- Test translucent colors against the actual backgrounds they will overlay.

## Gradients

- Define the job first: lighting, depth, emphasis, material, atmosphere, or
  transition.
- Control interpolation space and hue path instead of accepting accidental muddy
  midpoints.
- Place stops to shape perceived velocity and light, not merely at equal
  percentages.
- Avoid gradients that reduce text contrast or create false affordances.
- Use noise or texture only when it solves banding or supports the material.

## Radius and shape

- Use a small radius system tied to component scale and nesting.
- For nested rounded rectangles, preserve the apparent inset:
  `outer radius ≈ inner radius + gap`.
- Adjust mathematically correct shapes optically when icons, glyphs, or asymmetric
  content appear off-center.
- Keep hit areas generous even when the visible shape is compact.

## Borders, shadows, and depth

- Use borders for separation and definition; use shadows for depth and elevation.
- Prefer layered, low-contrast shadows over one heavy blur.
- Make light direction consistent.
- Reduce or remove shadows when a surface already has sufficient contrast.
- Check translucent and blurred surfaces over both calm and busy content.

## Icons and images

- Keep icon family, stroke, fill, size, and optical weight consistent.
- Align icons optically with text, not only by bounding boxes.
- Use the correct asset resolution and aspect behavior.
- Provide meaningful alternatives for informative imagery.
- Avoid decorative images that compete with the primary task.

## Polish order

Apply polish in this order:

1. content and structure;
2. layout and responsive behavior;
3. type and color roles;
4. states and accessibility;
5. shape, borders, and depth;
6. motion and micro-interaction;
7. decorative atmosphere.

Later layers must not compensate for an unresolved earlier layer.
