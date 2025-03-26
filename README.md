1. Language Overview

# MarkFunk Language Overview

MarkFunk is a vibrant, expressive markup language that blends traditional Markdown syntax with a rich set of funky text effects and basic scripting capabilities. Designed for creating visually engaging HTML documents, MarkFunk allows users to format text, apply animations, and even incorporate programming constructs like loops and variables—all within a simple, readable syntax.

## Key Characteristics
- **Markdown Foundation**: Builds on familiar Markdown conventions like headers, bold, and lists.
- **Funky Flair**: Offers over 90 unique text effects and animations, from `@rainbow{}` to `@vortex{}`.
- **Scripting Power**: Supports variables, loops (`@foreach`, `@for`, `@while`, `@repeat`), and inline code blocks.
- **HTML Output**: Compiles directly to styled HTML with embedded CSS animations.
- **Ease of Use**: Intuitive syntax for both beginners and advanced users.

MarkFunk is perfect for creating dynamic web content, educational materials, or just having fun with text presentation!

2. Language Features

# MarkFunk Language Features

MarkFunk provides a robust set of features to enhance text formatting and add interactivity:

## Text Formatting
- Standard Markdown: Headers (`#`, `##`, `###`), bold (`**`), italic (`*`), strikethrough (`~~`).
- Color Effects: `@red{}`, `@blue{}`, `@green{}`, `@purple{}`.
- Visual Effects: `@rainbow{}`, `@blink{}`, `@glow{}`, `@neon{}`, and many more.

## Structural Elements
- Lists: Unordered (`-`) and ordered (`1.`).
- Links: `[text](url)` and images `![alt](url)`.
- Tables: `|cell1|cell2|`.
- Blocks: `@quote{}`, `@alert{}`, `@note{}`, `@code{}`.

## Scripting Capabilities
- **Variables**: Declare with `@var{name=value}` and use with `{name}`.
- **Loops**:
  - `@foreach{items}:content` - Iterate over a list.
  - `@for{start-end}:content` - Numeric range loop.
  - `@while{count}:content` - Counter-based while loop.
  - `@repeat{times}:content` - Simple repetition.

## Animation and Effects
- Over 90 funky keywords with CSS animations (e.g., `@spin{}`, `@bounce{}`, `@vortex{}`).
- Customizable via compiled HTML and CSS output.

## Extensibility
- Easily add new keywords and effects by extending the pattern list in the compiler.

3. Reserved Keywords

# MarkFunk Reserved Keywords

Below is the complete list of reserved keywords in MarkFunk:

## Standard Markdown
1. `#` - H1 header
2. `##` - H2 header
3. `###` - H3 header
4. `**` - Bold
5. `*` - Italic
6. `~~` - Strikethrough
7. `-` - Unordered list item
8. `1.` - Ordered list item
9. `[]()` - Link
10. `![]()` - Image
11. `|` - Table row

## Funky Effects (Partial List)
12. `@rainbow{}` - Rainbow text
13. `@blink{}` - Blinking text
14. `@shout{}` - Uppercase text
15. `@whisper{}` - Small text
16. `@glow{}` - Glowing text
17. `@spin{}` - Spinning text
18. `@dance{}` - Dancing text
19. `@bubble{}` - Bubble text
20. `@retro{}` - Retro style
[... and 77 more, see full list in the compiler source]

## Structural Keywords
47. `@quote{}` - Blockquote
48. `@alert{}` - Alert box
49. `@note{}` - Note box
50. `@code{}` - Code block
51. `@button{}` - Button
52. `@spoiler{}` - Spoiler text
53. `@center{}` - Centered text
54. `@right{}` - Right-aligned text

## Scripting Keywords
55. `@var{}` - Variable declaration
56. `@foreach{}` - Foreach loop
57. `@for{}` - For loop
58. `@while{}` - While loop
59. `@repeat{}` - Repeat loop

**Note**: See the full list of 97 keywords in the MarkFunk compiler source for all funky effects.

4. Examples

5. Advanced Operators

# MarkFunk Advanced Operators

MarkFunk includes basic operators within its scripting capabilities:

## Variable Substitution
- Syntax: `{variable_name}`
- Used within code blocks to insert variable values.
- Example: `@var{x=10} Number: {x}` → "Number: 10"

## Loop Operators
- **@foreach{items}:content**
  - Iterates over comma-separated items.
  - Uses `{item}` for the current item.
  - Example: `@foreach{a, b}:Letter {item}`

- **@for{start-end}:content**
  - Loops from start to end (inclusive).
  - Uses `{i}` for the counter.
  - Example: `@for{1-3}:Num {i}`

- **@while{count}:content**
  - Loops `count` times.
  - Uses `{i}` for the counter (starts at 0).
  - Example: `@while{2}:Step {i}`

- **@repeat{times}:content**
  - Repeats content `times` times.
  - No built-in counter.
  - Example: `@repeat{3}:Hi`

## Limitations
- No arithmetic or conditional operators yet.
- Variables are static strings, no manipulation.

6. Programming Concepts

# MarkFunk Programming Concepts

MarkFunk introduces basic programming concepts to a markup language:

## Variables
- Declare with `@var{name=value}`.
- Scope: Limited to the current code block.
- Usage: Reference with `{name}`.

## Iteration
- **Foreach Loops**: Iterate over lists with `@foreach`.
- **For Loops**: Numeric iteration with `@for`.
- **While Loops**: Counter-based with `@while`.
- **Repeat Loops**: Simple repetition with `@repeat`.

## Code Blocks
- Enclosed in ``` marks.
- Support multiple lines with variables and loops.
- Rendered as `<pre><code>` with additional styling for loops.

## Styling
- Effects are applied via CSS classes or inline styles.
- Animations use `@keyframes` for dynamic behavior.

## Extensibility
- Add new keywords by extending the compiler's pattern list.
- Customize output with additional CSS.

7. Introduction

# Introduction to MarkFunk

Welcome to MarkFunk, the markup language that turns text into a visual party! Whether you're a writer wanting to spice up your documents or a coder looking for a fun way to prototype web content, MarkFunk has something for you.

## What is MarkFunk?
MarkFunk is a hybrid language that takes the simplicity of Markdown and infuses it with funky text effects and scripting features. Imagine writing a document where text can spin, glow, or even loop through a list—all with a few simple commands.

## Getting Started
1. Write your MarkFunk code using the syntax described in these docs.
2. Use the provided Python compiler to convert it to HTML.
3. Open the resulting HTML file in a browser to see the magic!

## Why MarkFunk?
- **Fun**: Over 90 effects to play with.
- **Simple**: Easy-to-learn syntax.
- **Powerful**: Loops and variables for dynamic content.

Start exploring MarkFunk today and unleash your creativity!