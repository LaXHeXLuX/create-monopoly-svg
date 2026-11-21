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

	def to_data_uri(m):
		MIME = {
			".svg": "image/svg+xml",
			".jpg": "image/jpeg",
			".jpeg": "image/jpeg",
			".png": "image/png",
			".gif": "image/gif",
			".webp": "image/webp",
		}

		path = base_dir / m[2]
		if path.suffix.lower() == ".svg":
			data = embed(path).encode()  # recursive embed, as before
			mime = "image/svg+xml"
		else:
			data = path.read_bytes()
			mime = MIME[path.suffix.lower()]
		return f'{m[1]}="data:{mime};base64,{base64.b64encode(data).decode()}"'

	# Matches href="..." and xlink:href="..." pointing at local files
	# (no '#' fragments, no ':' so URLs and existing data: URIs are skipped)
	svg = re.sub(
		r'((?:xlink:)?href)="([^"#:]+\.(?:svg|jpe?g|png|gif|webp))"',
		to_data_uri,
		svg,
		flags=re.IGNORECASE,
	)

	if embed_font:
		style = font_style(svg)
		if style:
			svg = re.sub(r"<svg\b[^>]*>", lambda m: m[0] + style, svg, count=1)

	return svg

def embed(path: Path):
	return embed_svg(path.read_text(encoding="utf-8"), base_dir=path.parent)
