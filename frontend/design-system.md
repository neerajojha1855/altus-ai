# Neo-Brutalism Design System

## Core Philosophy
Neo-Brutalism is characterized by a raw, unpolished, yet highly structured aesthetic. It rejects soft shadows and rounded corners in favor of aggressive contrast, stark borders, and vibrant colors.

## Color Palette
- **Primary Background:** `#ffffff` (Pure White)
- **Primary Text:** `#000000` (Pure Black)
- **Accent 1 (Neon Yellow):** `#FFE800` - Use for primary calls to action.
- **Accent 2 (Hot Pink):** `#FF007F` - Use for destructive actions or important alerts.
- **Accent 3 (Cyan):** `#00E5FF` - Use for secondary highlights or active states.
- **Accent 4 (Lime Green):** `#00FF00` - Use for success states.
- **Borders & Shadows:** `#000000` (Pure Black)

## Typography
- **Primary Font:** `Inter`, `Space Grotesk`, or system sans-serif.
- **Headings:** Bold (800 or 900 weight), large tracking.
- **Body:** Medium (500 weight), high legibility.

## UI Elements (Tailwind CSS Guide)

### Borders
Everything should have a thick, solid black border. No border-radius.
- **Classes:** `border-4 border-black rounded-none`

### Shadows
Shadows must be solid black, offset, with zero blur.
- **Classes:** `shadow-[6px_6px_0px_0px_rgba(0,0,0,1)]`

### Buttons
Buttons should pop with bright colors and distinct shadows that compress when clicked.
- **Default State:** `bg-[#FFE800] text-black font-bold border-4 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] transition-all`
- **Hover/Active State:** `hover:translate-x-[2px] hover:translate-y-[2px] hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] active:translate-x-[4px] active:translate-y-[4px] active:shadow-none`

### Cards
Containers for content should stand out aggressively from the background.
- **Classes:** `bg-white border-4 border-black shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] p-6`

### Inputs
Form fields should look like rigid boxes.
- **Classes:** `border-4 border-black p-3 focus:outline-none focus:ring-4 focus:ring-[#00E5FF] bg-white`
