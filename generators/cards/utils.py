from generators.utils import canvas, rect as base_rect, text, position

RATIO = 88/56
HEIGHT = 88
WIDTH = 56
OFFSET = WIDTH * 0.058
INNER_HEIGHT = HEIGHT - 2*OFFSET
INNER_WIDTH = WIDTH - 2*OFFSET
inner_offset_width_percent = 4
INNER_OFFSETS = [inner_offset_width_percent, inner_offset_width_percent / RATIO]

def rect(fill="none", stroke = 0.36):
	return base_rect(fill, stroke)

def card_base(portrait=True):
	w, h = WIDTH, HEIGHT
	if not portrait: w, h = h, w
	cb = canvas(w, h, base=True)
	cb.elements.append(rect("#ffffff", stroke=0))
	return cb

def card_with_padding(elements, portrait=True):
	iw, ih = INNER_WIDTH, INNER_HEIGHT
	if not portrait: iw, ih = ih, iw
	card = canvas(iw, ih, overflow=True)
	card.elements.append(rect())
	card.elements.extend(elements)
	card.x, card.y = OFFSET, OFFSET
	cwp = card_base(portrait=portrait)
	cwp.elements.append(card)
	return cwp

def title(txt: str, y, size=1, weight=1, fill="#000000"):
	txt = text(txt, size=WIDTH * 0.075 * size, weight=weight, fill=fill)
	return position(txt, y=y)

def card_text(txt: str, size=3.2, align=0, fill="#000000"):
	return text(txt, size=size, weight=-1, align=align, fill=fill)

def left_right_aligned_text(l_txt: str, r_txt: str, w_percent=100, y="50%"):
	l = card_text(l_txt, align=-1)
	r = card_text(r_txt, align=1)
	r.x = "100%"
	c = canvas(f"{w_percent}%", "50%", overflow=True)
	c.elements.extend([l, r])
	return position(c, x=f"{50 - w_percent/2}%", y=y)