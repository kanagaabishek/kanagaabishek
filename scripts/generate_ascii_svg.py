#!/usr/bin/env python3
"""
Generate ASCII art SVG from source PNG/JPEG using ascii-magic
"""
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_ascii_svg.py <input_image> <output_svg>")
        sys.exit(1)

    input_image = Path(sys.argv[1])
    output_svg = Path(sys.argv[2])

    if not input_image.exists():
        print(f"Error: Input image {input_image} not found")
        sys.exit(1)

    try:
        import ascii_magic

        # Convert image to ASCII art
        art = ascii_magic.from_image(str(input_image))
        # Get ASCII art as string with 80 columns (adjust as needed)
        ascii_str = art.to_ascii(columns=80)

        # Split into lines
        lines = ascii_str.split('\n')
        # Remove empty lines at the end and beginning if needed, but keep all for now
        if lines and lines[-1] == '':
            lines.pop()  # remove trailing empty line
        if lines and lines[0] == '':
            lines.pop(0)  # remove leading empty line

        if not lines:
            raise ValueError("No lines in ASCII art")

        # Calculate dimensions
        max_line_length = max(len(line) for line in lines)
        font_size = 12
        line_height = 14  # font_size + 2 for spacing
        char_width = font_size  # approximate width of a character in monospace font
        padding = 10
        width = max_line_length * char_width + padding * 2
        height = len(lines) * line_height + padding * 2

        # Build SVG content
        svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <rect width="{width}" height="{height}" fill="#0d1117"/>
  <text x="{padding}" y="{padding + font_size}" fill="#c9d1d9" font-size="{font_size}">'''

        # Add each line as a tspan
        for i, line in enumerate(lines):
            # Escape XML entities
            escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&apos;')
            y_pos = padding + font_size + i * line_height
            svg_content += f'<tspan x="{padding}" y="{y_pos}">{escaped_line}</tspan>'

        svg_content += '</text></svg>'

        output_svg.parent.mkdir(parents=True, exist_ok=True)
        output_svg.write_text(svg_content, encoding='utf-8')
        print(f"Generated ASCII SVG: {output_svg} ({len(lines)} lines, max line length {max_line_length})")

    except ImportError:
        print("Error: ascii-magic not installed. Please install it with: pip install ascii-magic")
        sys.exit(1)
    except Exception as e:
        print(f"Error generating ASCII art: {e}")
        # Fallback to a simple message
        svg_content = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="200" viewBox="0 0 400 200" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <rect width="400" height="200" fill="#0d1117"/>
  <text x="20" y="50" fill="#c9d1d9" font-size="16">ASCII Art Generation Failed</text>
  <text x="20" y="80" fill="#8b949e" font-size="14">Please check that ascii-magic is installed</text>
  <text x="20" y="110" fill="#8b949e" font-size="14">and the input image is valid.</text>
</svg>'''
        output_svg.parent.mkdir(parents=True, exist_ok=True)
        output_svg.write_text(svg_content, encoding='utf-8')
        print(f"Generated fallback SVG: {output_svg}")

if __name__ == "__main__":
    main()