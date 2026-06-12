---
name: Skill Intelligence System
colors:
  surface: '#f8f9ff'
  surface-dim: '#ccdbf3'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e6eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d5e3fc'
  on-surface: '#0d1c2e'
  on-surface-variant: '#454652'
  inverse-surface: '#233144'
  inverse-on-surface: '#eaf1ff'
  outline: '#767683'
  outline-variant: '#c6c5d4'
  surface-tint: '#4c56af'
  primary: '#000666'
  on-primary: '#ffffff'
  primary-container: '#1a237e'
  on-primary-container: '#8690ee'
  inverse-primary: '#bdc2ff'
  secondary: '#006b5c'
  on-secondary: '#ffffff'
  secondary-container: '#68fadd'
  on-secondary-container: '#007261'
  tertiary: '#00105a'
  on-tertiary: '#ffffff'
  tertiary-container: '#14267a'
  on-tertiary-container: '#8392ea'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e0e0ff'
  primary-fixed-dim: '#bdc2ff'
  on-primary-fixed: '#000767'
  on-primary-fixed-variant: '#343d96'
  secondary-fixed: '#68fadd'
  secondary-fixed-dim: '#44ddc1'
  on-secondary-fixed: '#00201a'
  on-secondary-fixed-variant: '#005145'
  tertiary-fixed: '#dee0ff'
  tertiary-fixed-dim: '#bac3ff'
  on-tertiary-fixed: '#00105b'
  on-tertiary-fixed-variant: '#2f3f92'
  background: '#f8f9ff'
  on-background: '#0d1c2e'
  surface-variant: '#d5e3fc'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  title-sm:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 32px
  xl: 48px
  margin-mobile: 20px
  gutter-mobile: 12px
---

## Brand & Style

This design system is engineered to feel like a high-performance diagnostic tool for career development. It communicates authority and precision through a "Corporate / Modern" aesthetic, punctuated by high-tech data visualizations. The interface prioritizes clarity and cognitive ease, ensuring that complex skill density maps and growth trajectories remain accessible. 

The visual language balances the weight of professional expertise with the kinetic energy of personal growth. It utilizes vast whitespace to separate data clusters, ensuring the user feels in control of their information. The emotional response should be one of calm confidence—moving the user from "uncertainty" to "insight" through structured, intelligent layouts.

## Colors

The palette is anchored by Deep Indigo, providing a foundation of trust and institutional knowledge. Electric Teal serves as the primary action and "growth" color, used strategically for progress indicators, success states, and primary calls to action. 

Slate Gray is utilized for body text and secondary information to maintain high readability without the harshness of pure black. Data visualizations should utilize subtle gradients that transition from Deep Indigo to Electric Teal, symbolizing the journey from foundational knowledge to specialized mastery.

## Typography

The typography system relies exclusively on **Inter** to maintain a systematic, utilitarian feel that thrives in data-heavy environments. The hierarchy is strictly enforced through weight variations and the use of uppercase labels for technical metadata.

Headlines use tighter letter-spacing and heavier weights to anchor sections, while body text maintains a generous line height to prevent user fatigue during long reading sessions. Small labels use increased letter-spacing to ensure legibility on mobile screens, particularly within data cards and skill badges.

## Layout & Spacing

The design system utilizes a fluid 4-column grid for mobile devices, anchored by 20px side margins. All spatial relationships are governed by a 4px base unit, ensuring mathematical consistency across the UI.

Padding within cards and containers should scale based on the content's complexity; high-density data visualizations use 16px (sm) internal padding, while hero sections and empty states use 32px (lg) to emphasize focus. Group related skill clusters with 8px (xs) spacing to create visual associations, while separating major functional blocks with 48px (xl) of vertical whitespace.

## Elevation & Depth

Depth is established through a combination of tonal layering and soft ambient shadows. Backgrounds are kept slightly off-white (#F8FAFC) to allow pure white cards to "float" prominently.

Shadows are never pure black; they are tinted with the Deep Indigo primary color at very low opacities (4-8%) to maintain a sophisticated, clean look. Use two primary elevation levels:
1. **Surface:** Flat, used for the main background.
2. **Raised:** Used for interactive cards and skill nodes, featuring a 12px blur with a 4px Y-offset.
3. **Overlay:** Reserved for modals and dropdowns, utilizing a 20px blur and a subtle 1px Slate Gray outline for crisp definition.

## Shapes

The shape language reflects the "Professional" personality by using refined, medium-radius curves. A standard 0.5rem (8px) corner radius is applied to primary cards and input fields to soften the "high-tech" edge, making the app feel approachable rather than clinical.

Buttons and skill chips utilize a more aggressive "Pill" shape (fully rounded) to differentiate interactive elements from informational containers. Data visualization markers (nodes in a skill tree) should remain perfectly circular to signify points of data precision.

## Components

### Buttons & Inputs
Primary buttons are solid Electric Teal with white text, using a pill shape for maximum tap-target recognition. Input fields use a subtle Slate Gray border (1px) that transitions to Deep Indigo on focus, accompanied by a soft glow effect.

### Skill Cards
Cards are the primary vehicle for information. They feature 16px internal padding, white backgrounds, and a subtle indigo-tinted shadow. Headers within cards should use `label-caps` for categorical context.

### Progress & Growth Indicators
Skill proficiency is represented by "Pulse Bars"—linear progress indicators that use a gradient from Deep Indigo to Electric Teal. These should include micro-animations where the teal "lead" of the bar glows slightly to indicate active growth.

### Chips & Badges
Use small, pill-shaped chips for skill tags. Verified skills receive an Electric Teal background with 10% opacity and a solid teal text color, while "in-progress" skills use a Slate Gray treatment.

### Data Visualizations
Charts should avoid sharp corners. Bar charts use rounded caps, and line graphs use a 2px stroke width with smoothed Bezier curves. Use subtle background blurs behind data tooltips to maintain a high-tech, layered feel.