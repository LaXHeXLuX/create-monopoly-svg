from conf.ui import TILE_WIDTH, CORNER
from generators.utils import canvas, rect, text, position_image, price as price_str

def text1(txt=None):
	t = text(txt)
	t.x, t.y = "50%", "13%"
	return t

def text2(txt=None):
	t = text(txt)
	t.x, t.y = "50%", "38%"
	return t

def price(value: int = 100):
	p = text(price_str(value))
	p.x, p.y = "50%", "90%"
	return p

def tile_base(txt=None, image_tag=None, cost=None):
	tile_base = canvas(TILE_WIDTH, CORNER)
	tile_base.elements.append(rect())
	if (txt != None): tile_base.elements.append(text1(txt))
	if (image_tag != None): tile_base.elements.append(position_image(image_tag))
	if (cost != None): tile_base.elements.append(price(cost))
	return tile_base