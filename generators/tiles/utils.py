from generators.conf import TILE_WIDTH, CORNER
from generators.utils import canvas, price, text1, position_element, image

def tile_base(text=None, href=None, cost=None):
	tile_base = canvas(TILE_WIDTH, CORNER, stroke=True)
	if (text != None): tile_base.elements.append(text1(text))
	if (href != None): tile_base.elements.append(position_element(image(href)))
	if (cost != None): tile_base.elements.append(price(cost))
	return tile_base