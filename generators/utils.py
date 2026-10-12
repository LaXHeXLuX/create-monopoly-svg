from generators.conf import FONT, CURRENCY

# SVG objects
import svg
def text():
	return svg.Text(
		text="TEXT",
		text_anchor="middle",
		dominant_baseline="middle",
		font_family=FONT,
		font_size="5"
	)
def text1():
	t = text()
	t.x, t.y = "50%", "13%"
	return t
def text2():
	t = text()
	t.x, t.y = "50%", "38%"
	return t
def price(value: int = 100):
	p = text()
	p.x, p.y = "50%", "90%"
	p.text = f"{value} {CURRENCY}"
	return p
def rect(fill: str = "none", stroke: bool = True):
	r = svg.Rect(
		width="100%", height="100%",
		fill="none",
		stroke="black",
		stroke_width=0.5
	)
	r.fill = fill
	if (not stroke):
		r.stroke = "none"
		r.stroke_width = 0
	return r
def canvas(w: int, h: int, stroke: bool = False):
	canvas = svg.SVG(
		width=w,
		height=h,
		elements=[]
	)
	if (stroke): canvas.elements.append(rect())
	return canvas

# utility methods
def wrap(element: svg, x, y):
	return svg.SVG(
		x=x, y=y, overflow="visible",
		elements=[element],
	)

def position_element(element: svg, x, y, rotate: int, samePlace: bool = True):
	element.x = x
	element.y = y
	if (rotate > 0): 
		newX, newY = x, y
		if (samePlace): 
			newX = x + element.width/2
			newY = y + element.height/2
		element.transform = f"rotate({90 * rotate} {newX} {newY})"
	return element

def centered_image(href, rotation=0, scale=1, cx="50%", cy="50%"):
	transforms = []
	if rotation != 0:
		transforms.append(f"rotate({rotation})")
	if scale != 1:
		transforms.append(f"scale({scale})")

	return svg.SVG(
		x=cx, y=cy, overflow="visible",
		elements=[svg.Image(
			href=href,
			x="-50%", y="-50%",
			width="100%", height="100%",
			transform=" ".join(transforms) or None,
		)],
	)
