from conf.ui import TILE_WIDTH, CORNER
from conf.texts import price as price_str
from generators.utils import canvas, rect, text, position, position_image

def price(value):
	return position(text(price_str(value)), y="90%")

def tile_base(txt=None, image_tag=None, image_y="50%", cost=None):
	tile_base = canvas(TILE_WIDTH, CORNER, base=True)
	tile_base.elements.append(rect())
	if (txt != None): tile_base.elements.append(position(text(txt), y="13%"))
	if (image_tag != None): tile_base.elements.append(position_image(image_tag, cy=image_y))
	if (cost != None): tile_base.elements.append(price(cost))
	return tile_base