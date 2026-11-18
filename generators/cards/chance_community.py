from generators.cards.utils import card_base, card_with_padding, card_text, title, INNER_WIDTH as IH, INNER_HEIGHT as IW, OFFSET
from generators.utils import text, rect, position, canvas, position_image
from conf.texts import GAME, CH_NAME, CC_NAME
from conf.ui import CH_BG, CC_BG

CONTENT_WIDTH_PERCENT = 71
CONTENT_HEIGHT_PERCENT = 70
CONTENT_LINE_HEIGHT = 4.6
FO_SCALE = 10
logo_font_size_percent = 16
logo_bg_width_percent = logo_font_size_percent+2

def logo():
	r = rect(fill="#ffffff", stroke=0)
	r.x, r.y = "-50%", "-50%"
	txt = text(GAME, size=f"{logo_font_size_percent}%", weight=-1)
	txt.font_weight = "100"
	c = canvas(f"{logo_bg_width_percent}%", 5, overflow=True)
	c.elements.append(r)
	c.elements.append(txt)
	c.x = "50%"
	c.y = f"100%"
	return c

def base():
	return card_with_padding([logo()], portrait=False)

def card(txt: str, CH=True):
	card = base()
	card.elements.extend([
		title(CH_NAME if CH else CC_NAME, y="19%"),
		position(card_text(txt), y="55%")
	])
	return card

def chance(txt: str):
	return card(txt, CH=True)

def community(txt: str):
	return card(txt, CH=False)

def back(CH=True):
	cb = card_base(portrait=False)
	bg = rect(CH_BG if CH else CC_BG)
	bg.width, bg.height = IW, IH
	bg.x, bg.y = OFFSET, OFFSET
	cb.elements.extend([
		bg,
		position_image("CH" if CH else "CC", scale=0.75)
	])
	return cb

def chance_back():
	return back(CH=True)

def community_back():
	return back(CH=False)