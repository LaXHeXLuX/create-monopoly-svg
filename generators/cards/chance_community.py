from .utils import card_base, title, content, WIDTH, OFFSET
from ..utils import text, rect, canvas, position_element
from ..conf import GAME, CH_NAME, CC_NAME

CONTENT_WIDTH_PERCENT = 71
CONTENT_HEIGHT_PERCENT = 70
CONTENT_LINE_HEIGHT = 4.6
FO_SCALE = 10
LOGO_BG_WIDTH = 14.5
LOGO_FONT_SIZE = WIDTH * 0.0285

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

def chance(txt: str, CH=True):
	chance = base()
	chance.elements.append(title(CH_NAME if CH else CC_NAME, y_percent=18))
	chance.elements.append(content(txt, 71, 70, y_percent=54))
	return chance

def community(txt: str):
	return chance(txt, CH=False)