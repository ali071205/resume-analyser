---
name: Precision Technical Minimal
colors:
  surface: '#fdf8f8'
  surface-dim: '#ddd9d8'
  surface-bright: '#fdf8f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f7f3f2'
  surface-container: '#f1edec'
  surface-container-high: '#ebe7e6'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#444748'
  inverse-surface: '#313030'
  inverse-on-surface: '#f4f0ef'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#b7102a'
  on-secondary: '#ffffff'
  secondary-container: '#db313f'
  on-secondary-container: '#fffbff'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#181c20'
  on-tertiary-container: '#808489'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#ffdad8'
  secondary-fixed-dim: '#ffb3b1'
  on-secondary-fixed: '#410007'
  on-secondary-fixed-variant: '#92001c'
  tertiary-fixed: '#e0e3e8'
  tertiary-fixed-dim: '#c3c7cc'
  on-tertiary-fixed: '#181c20'
  on-tertiary-fixed-variant: '#43474c'
  background: '#fdf8f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  h1:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.08em
  mono-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  container-max: 1440px
  gutter: 24px
---

## Brand & Style

This design system is built for high-stakes professional environments where data accuracy and speed are paramount. The aesthetic merges **Corporate Modernism** with **High-Tech Minimalism**, emphasizing clarity, authority, and mechanical precision. 

The visual language communicates "Intelligent Analysis" through structured layouts and a restrained color palette. It avoids decorative elements in favor of functional utility. The target audience—recruiters and HR tech specialists—should experience a sense of rigorous efficiency. The interface relies on sharp geometry and high-contrast relationships to guide the eye through complex resume data without fatigue.

## Colors

The palette is anchored by a sophisticated monochromatic base to maintain a serious, high-tech atmosphere. 

- **Primary (#0F0F0F):** Used for structural elements, headers, and primary navigation to ground the interface.
- **Accent (#E63946):** This Deep Red is reserved exclusively for high-priority calls to action, critical status highlights, and interactive "hotspots." Use it sparingly to maintain its psychological impact.
- **Background (#F8F9FA):** Provides a clean, clinical canvas that allows text and data visualizations to stand out.
- **Neutral/Text (#212529):** Used for body copy to ensure readability while maintaining a softer contrast than pure black.
- **Border (#DEE2E6):** Used for defining the rigid structure of cards and sections without adding visual weight.

## Typography

This design system utilizes **Inter** for its systematic, utilitarian clarity in all primary reading tasks. It is paired with **Space Grotesk** for labels and data points to inject a technical, futuristic edge.

Headlines should use tight tracking and heavy weights to project confidence. Body text follows a generous line height for scanability during long resume review sessions. "Label-caps" should be used for category headers and metadata tags to provide a clear visual break from standard prose.

## Layout & Spacing

The system employs a **Fixed Grid** model within a maximum 1440px container, utilizing a 12-column structure. A strict 4px baseline grid ensures vertical rhythm across all components.

Spacing is aggressive and intentional. Large 'XL' gaps are used to separate major functional modules, while 'XS' and 'SM' units handle the internal logic of data sets. Content density should be kept moderate; while it is a high-tech tool, overcrowding is avoided to ensure the AI-driven insights remain the focal point.

## Elevation & Depth

To maintain a "High-Tech" and professional feel, this design system rejects traditional soft shadows in favor of **Tonal Layering** and **Bold Outlines**.

- **Depth through Borders:** Hierarchy is established by 1px solid borders (#DEE2E6). No shadows are used to lift cards; instead, active or hovered elements gain a 2px border or a slight background shift to #FFFFFF.
- **Structural Layering:** The main background is #F8F9FA. Floating panels or modals use a pure #FFFFFF background with a high-contrast #0F0F0F 2px border to create "Hard Elevation."
- **Data Overlays:** Tooltips and temporary information layers use the Primary #0F0F0F background with white text to "pop" against the light UI.

## Shapes

The design system utilizes **Sharp Edges (0px)** for all primary containers, buttons, and input fields. This architectural approach reinforces the "High-Tech" precision of the platform.

Small interactive elements like checkboxes or tags may use a maximum of **4px (ROUND_FOUR)** radius only if necessary to distinguish them from larger layout blocks, but the preference remains sharp corners. Progress bars and data visualization fills should be strictly rectangular.

## Components

- **Buttons:** Primary buttons are solid #E63946 with white text, sharp corners, and no gradient. Secondary buttons are #0F0F0F or ghost-style with a 1px border.
- **Cards:** Defined by #DEE2E6 1px borders. No box-shadow. Header areas within cards should be separated by a horizontal rule.
- **Input Fields:** Sharp-edged boxes with a #DEE2E6 border. On focus, the border transitions to 2px #0F0F0F.
- **Data Visualizations:** Use a combination of #0F0F0F and #E63946 for charts. Bar charts should be flat, rectangular blocks without rounded caps.
- **Status Chips:** Small, sharp-edged labels. Use #E63946 for "Critical Match" and #0F0F0F for "Standard."
- **Progress Bars:** High-contrast trackers. The "fill" should be the Deep Red, while the "track" is the Border color.
- **Resume Preview:** A dedicated frame with a subtle #DEE2E6 border, treated as a "Document" class element with fixed margins.