from ..utils import canvas, rect, position_element

WIDTH = 88
HEIGHT = 56
OFFSET = WIDTH * 0.037

def card_base(portrait=True, stroke=True, bg="white"):
	w, h = WIDTH, HEIGHT
	if (portrait): w, h = HEIGHT, WIDTH
	cb = canvas(w, h)
	if bg != None:
		r = rect(fill=bg) 
		cb.elements.append(r)
	if (stroke):
		r = rect() 
		r.stroke_width=0.36
		r.width = cb.width - 2*OFFSET
		r.height = cb.height - 2*OFFSET
		r.x, r.y = OFFSET, OFFSET
		cb.elements.append(r)
		
	return cb

