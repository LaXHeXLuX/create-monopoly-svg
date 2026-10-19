from .utils import card_base, WIDTH, OFFSET, LOGO_BG_WIDTH
from ..utils import text, rect, canvas, position_element
from ..conf import GAME, CH_NAME, CC_NAME, FONT_LIGHT

from svg import ForeignObject, G

TITLE_FONT_SIZE = WIDTH * 0.05
CONTENT_FONT_SIZE = WIDTH * 0.036
CONTENT_WIDTH_PERCENT = 71
CONTENT_HEIGHT_PERCENT = 70
CONTENT_LINE_HEIGHT = 4.6
FO_SCALE = 10
LOGO_FONT_SIZE = WIDTH * 0.0285

text_style_items = [
	"display: flex",
	"align-items: center",
	"height: 100%",
	"text-align: center",
	f"font-family: '{FONT_LIGHT}'",
	f"font-size: {FO_SCALE*CONTENT_FONT_SIZE}px",
	f"line-height: {FO_SCALE*CONTENT_LINE_HEIGHT}px"
]

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

def title(CH: bool):
	txt = text(CH_NAME if CH else CC_NAME, size=TITLE_FONT_SIZE, weight=1)

	return position_element(txt, cy="18%")

def content(txt: str):
	txt = "TEKST MURRAB ISE RIDU VASTAVALT PIKKUSELE. VÕIMALUS KA ISE MANUAALSELT SÄTTIDA. TEINE VÕIMALUS ON LASTA TEISTEL KÕIK ENDA EEST ÄRA TEHA."
	fo = ForeignObject(
		x=f"{FO_SCALE * (50 - CONTENT_WIDTH_PERCENT/2)}%", 
		y=f"{FO_SCALE * (54 - CONTENT_HEIGHT_PERCENT/2)}%", 
		width = f"{FO_SCALE * CONTENT_WIDTH_PERCENT}%", 
		height = f"{FO_SCALE * CONTENT_HEIGHT_PERCENT}%"
	)
	style = "; ".join(text_style_items)
	xmlns = "http://www.w3.org/1999/xhtml"
	div = f"<div xmlns=\"{xmlns}\" style=\"{style}\">{txt}</div>"
	fo.elements = [div]

	g = G(transform=f"scale({1/FO_SCALE})")
	g.elements = [fo]
	return g

def chance(txt: str):
	chance = base()
	chance.elements.append(title(CH=True))
	chance.elements.append(content(txt))
	return chance

def community(txt: str):
	community = base()
	community.elements.append(title(CH=False))
	community.elements.append(content(txt))
	return community