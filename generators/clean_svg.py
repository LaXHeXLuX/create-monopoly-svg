import base64
import re
from pathlib import Path
from conf.ui import FONTS, FONT_FILES, FONT_DIR
from conf.io import ROOT, EMBED_FONTS

base64_fonts = {}

def font_face(weight):
	if weight not in base64_fonts: 
		base64_fonts[weight] = base64.b64encode((FONT_DIR / FONT_FILES[weight]).read_bytes()).decode()
	return f'@font-face {{ font-family: "{FONTS[weight]}"; src: url("data:font/ttf;base64,{base64_fonts[weight]}"); }}'

def font_style(svg: str):
	faces = [font_face(w) for w, name in FONTS.items() if f'font-family="{name}"' in svg]
	return f"<style>{''.join(faces)}</style>" if faces else ""


MIME = {
	".jpg": "image/jpeg",
	".jpeg": "image/jpeg",
	".png": "image/png",
	".gif": "image/gif",
	".webp": "image/webp",
}

def embed_svg(svg, base_dir: Path = ROOT):
	svg = str(svg)

	def to_data_uri(m):
		path = base_dir / m[2]
		if path.suffix.lower() == ".svg":
			data = embed(path).encode()
			mime = "image/svg+xml"
		else:
			data = path.read_bytes()
			if path.suffix.lower() not in MIME:
				raise ValueError(f"Unsupported image type: {path}")
			mime = MIME[path.suffix.lower()]
		return f'{m[1]}="data:{mime};base64,{base64.b64encode(data).decode()}"'

	svg = re.sub(
		r'((?:xlink:)?href)="(?!#|[a-z][a-z0-9+.-]+:)([^"]+)"',
		to_data_uri,
		svg,
		flags=re.IGNORECASE,
	)

	if EMBED_FONTS:
		style = font_style(svg)
		if style:
			svg = re.sub(r"<svg\b[^>]*>", lambda m: m[0] + style, svg, count=1)

	return svg

def embed(path: Path):
	return embed_svg(path.read_text(encoding="utf-8"), base_dir=path.parent)
