from generators.cards.utils import card_base, title, content, WIDTH, OFFSET
from generators.utils import text, rect, canvas, position_element, position_image
from conf.texts import GAME, CH_NAME, CC_NAME
from conf.ui import CH_BG, CC_BG

CONTENT_WIDTH_PERCENT = 71
CONTENT_HEIGHT_PERCENT = 70
CONTENT_LINE_HEIGHT = 4.6
FO_SCALE = 10
LOGO_BG_WIDTH = 14.5
LOGO_FONT_SIZE = WIDTH * 0.044

def logo():
	r = rect(fill="white", stroke=False)
	r.x, r.y = "-50%", "-50%"
	txt = text(GAME, size=LOGO_FONT_SIZE, weight=-1)
	txt.font_weight = "100"
	c = canvas(LOGO_BG_WIDTH, 5)
	c.overflow = "visible"
	c.elements.append(r)
	c.elements.append(txt)
	return c

def base():
	cb = card_base(portrait=False)
	l = position_element(logo(), cy=f"{cb.height - OFFSET}")
	cb.elements.append(l)
	return cb

def card(txt: str, CH=True):
	card = base()
	card.elements.append(title(CH_NAME if CH else CC_NAME, y_percent=19))
	card.elements.append(content(txt, 75, 70, y_percent=57))
	return card

def chance(txt: str):
	return card(txt, CH=True)

def community(txt: str):
	return card(txt, CH=False)

def back(CH=True):
	cb = card_base(portrait=False, bg=CH_BG if CH else CC_BG)
	cb.elements.append(position_image("CH" if CH else "CC", scale=0.75))
	return cb

def chance_back():
	return back(CH=True)

def community_back():
	return back(CH=False)