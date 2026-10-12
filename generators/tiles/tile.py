from generators.conf import TILE_WIDTH, CORNER
from generators.utils import canvas, price, text1, centered_image

def tile(text=None, href=None, cost=None):
	tile = canvas(TILE_WIDTH, CORNER, stroke=True)
	if (text != None): tile.elements.append(text1(text))
	if (href != None): tile.elements.append(centered_image(href))
	if (cost != None): tile.elements.append(price(cost))
	return tile