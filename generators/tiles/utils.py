from generators.conf import TILE_WIDTH, CORNER, CURRENCY
from generators.utils import canvas, rect, text, position_element, image

def text1(txt=None):
	t = text(txt)
	t.x, t.y = "50%", "13%"
	return t

def text2(txt=None):
	t = text(txt)
	t.x, t.y = "50%", "38%"
	return t

def price(value: int = 100):
	p = text(f"{value} {CURRENCY}")
	p.x, p.y = "50%", "90%"
	return p

def tile_base(text=None, image_tag=None, cost=None):
	tile_base = canvas(TILE_WIDTH, CORNER)
	tile_base.elements.append(rect())
	if (text != None): tile_base.elements.append(text1(text))
	if (image_tag != None): tile_base.elements.append(position_element(image(image_tag)))
	if (cost != None): tile_base.elements.append(price(cost))
	return tile_base