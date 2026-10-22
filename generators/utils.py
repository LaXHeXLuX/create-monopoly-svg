from generators.conf import FONT, FONT_BOLD, FONT_LIGHT, IMAGE_SCALE
FONTS = [FONT_LIGHT, FONT, FONT_BOLD]

# SVG objects
import svg
def text(txt, size=5, weight=0):
	return svg.Text(
		text = txt,
		text_anchor = "middle",
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
		fill=fill,
		stroke="black",
		stroke_width=0.5
	)
	if (not stroke):
		r.stroke = "none"
		r.stroke_width = 0
	return r

def canvas(w: int, h: int):
	return svg.SVG(
		width=w,
		height=h,
		elements=[]
	)

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