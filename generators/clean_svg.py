import base64
import re
from pathlib import Path
from conf.ui import FONT

FONT_FILE = Path.home() / "Library/Fonts/ITCKabelStdMedium.TTF"

FONT_STYLE = (
	f'<style>@font-face {{ font-family: "{FONT}"; '
	f'src: url("data:font/otf;base64,{base64.b64encode(FONT_FILE.read_bytes()).decode()}"); }}'
	f"</style>"
)

def embed_svg(svg, base_dir: Path = "."):
	base_dir = Path(base_dir)
	svg = str(svg)

	# Replace href="something.svg" with the embedded (and itself embedded) file
	svg = re.sub(
		r'href="([^"#:]+\.svg)"',
		lambda m: 'href="data:image/svg+xml;base64,'
		+ base64.b64encode(embed(base_dir / m[1]).encode()).decode()
		+ '"',
		svg,
	)

	# Add the font right after the opening <svg> tag if this file uses it
	if FONT in svg:
		svg = re.sub(r"<svg\b[^>]*>", lambda m: m[0] + FONT_STYLE, svg, count=1)

	return svg

def embed(path: Path):
	return embed_svg(path.read_text(encoding="utf-8"), base_dir=path.parent)
