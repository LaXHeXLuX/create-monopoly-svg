from generators.utils import canvas, rect, text, position_element
from conf.ui import FONT_LIGHT

HEIGHT = 88
WIDTH = 56
OFFSET = HEIGHT * 0.039

def card_base(portrait=True, stroke=True, bg="white"):
	w, h = WIDTH, HEIGHT
	if (not portrait): w, h = HEIGHT, WIDTH
	cb = canvas(w, h)
	if bg != None:
		r = rect(fill=bg, stroke=False) 
		cb.elements.append(r)
	if (stroke):
		r = rect() 
		r.stroke_width=0.36
		r.width = cb.width - 2*OFFSET
		r.height = cb.height - 2*OFFSET
		r.x, r.y = OFFSET, OFFSET
		cb.elements.append(r)
		
	return cb

def title(txt: str, y_percent, size=1, weight=1, fill="#000000"):
	txt = text(txt, size=WIDTH * 0.075 * size, weight=weight, fill=fill)
	return position_element(txt, cy=f"{y_percent}%")

from svg import ForeignObject, G

CONTENT_LINE_HEIGHT = 4.6
text_style_items = [
	"display: flex",
	"align-items: center",
	"justify-content: center",
	"height: 100%",
	"text-align: center",
	"white-space: pre-line",
	f"font-family: '{FONT_LIGHT}'"
]

def content(txt: str, w_percent, h_percent, x_percent=50, y_percent=50, font_size=1, scale=10, fill="#000000", line_height=CONTENT_LINE_HEIGHT):
	fo = ForeignObject(
		x=f"{scale * (x_percent - w_percent/2)}%", 
		y=f"{scale * (y_percent - h_percent/2)}%", 
		width = f"{scale * w_percent}%", 
		height = f"{scale * h_percent}%"
	)
	style = "; ".join(text_style_items)
	style += f"; font-size: {scale*font_size*WIDTH*0.06}px"
	style += f"; line-height: {scale*line_height}px"
	style += f"; color: {fill}"

	xmlns = "http://www.w3.org/1999/xhtml"
	div = f"<div xmlns=\"{xmlns}\" style=\"{style}\">{txt}</div>"
	fo.elements = [div]

	g = G(transform=f"scale({1/scale})")
	g.elements = [fo]
	return g

def left_right_aligned_text(l_txt: str, r_txt: str, size=3.2, w_percent=100):
	l = text(l_txt, size=size, weight=-1, align=-1)
	r = text(r_txt, size=size, weight=-1, align=1)
	r.x = "100%"
	c = canvas(f"{w_percent}%", "50%")
	c.overflow = "visible"
	c.elements.extend([l, r])
	c.x = f"{50 - w_percent/2}%"
	return c