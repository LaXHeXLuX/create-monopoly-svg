import base64
import re
from pathlib import Path
from conf.ui import FONTS, FONT_FILES, FONT_DIR, ROOT

base64_fonts = {}

def font_face(weight):
	if weight not in base64_fonts: 
		base64_fonts[weight] = base64.b64encode((FONT_DIR / FONT_FILES[weight]).read_bytes()).decode()
	return f'@font-face {{ font-family: "{FONTS[weight]}"; src: url("data:font/ttf;base64,{base64_fonts[weight]}"); }}'

def font_style(svg: str):
	faces = [font_face(w) for w, name in FONTS.items() if f'font-family="{name}"' in svg]
	return f"<style>{''.join(faces)}</style>" if faces else ""

def embed_svg(svg, base_dir: Path = ROOT, embed_font: bool = False):
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

	if embed_font:
		style = font_style(svg)
		if style:
			svg = re.sub(r"<svg\b[^>]*>", lambda m: m[0] + style, svg, count=1)
		
	return svg

def embed(path: Path):
	return embed_svg(path.read_text(encoding="utf-8"), base_dir=path.parent)
