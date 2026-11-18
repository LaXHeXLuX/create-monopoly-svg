from conf.ui import FONT, FONT_BOLD, FONT_LIGHT, IMAGE_SCALE
from conf.texts import CURRENCY
FONTS = [FONT_LIGHT, FONT, FONT_BOLD]

# SVG objects
import svg
def text(txt: str, size=5, weight=0, align=0, fill="#000000"):
	txt = str(txt)
	anchor = ["start", "middle", "end"]
	lines = txt.split("\n")
	text = svg.Text(
		text=txt,
		fill=fill,
		text_anchor=anchor[align+1],
		dominant_baseline="middle",
		font_family=FONTS[weight+1],
		font_size=size,
	)
	if len(lines) == 1:
		return text
	text.text = None
	text.elements = []
	step = 1.32
	j = 1
	for i in range(len(lines)):
		if (lines[i] == ""):
			j += 1
			continue
		dy = f"{j*step}em"
		if i == 0: 
			dy = f"{-step/2 * (len(lines) - 1)}em"
		text.elements.append(svg.TSpan(
			text=lines[i],
			x="50%",
			dy=dy
		))
		j = 1
	return text

def rect(fill: str = "none", stroke: float = 0.5):
	r = svg.Rect(
		width="100%", height="100%",
		fill=fill
	)
	if (stroke > 0):
		r.stroke = "black"
		r.stroke_width = stroke
	return r

def canvas(w, h, overflow=False, base=False):
	canvas = svg.SVG(
		width=w,
		height=h,
		elements=[]
	)
	if overflow:
		canvas.overflow = "visible"
	if not base:
		canvas.xmlns = None
	return canvas

# utility methods
def position(el: svg, x="50%", y="50%"):
	el.x, el.y = x, y
	return el

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