from conf.ui import FONT, FONT_BOLD, FONT_LIGHT, IMAGE_SCALE
from conf.texts import CURRENCY
FONTS = [FONT_LIGHT, FONT, FONT_BOLD]

# SVG objects
import svg
def text(txt, size=5, weight=0, align=0):
	anchor = ["start", "middle", "end"]
	return svg.Text(
		text = txt,
		text_anchor = anchor[align+1],
		dominant_baseline = "middle",
		font_family = FONTS[weight+1],
		font_size = size
	)

def text_with_bg(txt, bg, padding=1, size=5, bold=False):
	t = text(txt, size=size, bold=bold)
	r = rect()

def rect(fill: str = "none", stroke: bool = True):
	r = svg.Rect(
		width="100%", height="100%",
		fill=fill
	)
	if (stroke):
		r.stroke = "black"
		r.stroke_width = 0.5
	return r

def canvas(w, h, overflow=False):
	canvas = svg.SVG(
		width=w,
		height=h,
		elements=[]
	)
	if overflow:
		canvas.overflow = "visible"
	return canvas

# utility methods
def wrap(element: svg, x, y):
	return svg.SVG(
		x=x, y=y, overflow="visible",
		elements=[element],
	)

def image(tag: str):
	return svg.Image(
		href=f"decals/{tag}.svg",
		x="-50%", y="-50%",
		width="100%", height="100%"
	)

def position_element(el: svg, rotation=0, scale=1, cx="50%", cy="50%"):
	transforms = []
	if rotation != 0:
		transforms.append(f"rotate({rotation})")
	if scale != 1:
		transforms.append(f"scale({scale})")

	el.transform = " ".join(transforms)

	return wrap(el, cx, cy)

def position_image(tag: str, rotation=0, scale=1, cx="50%", cy="50%"):
	return position_element(
		image(tag), 
		rotation=rotation, 
		scale=IMAGE_SCALE[tag]*scale, 
		cx=cx, cy=cy
	)

def price(value: int):
	return f"{value} {CURRENCY}"