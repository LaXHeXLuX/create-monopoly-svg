from conf import TILE_WIDTH, CORNER
from utils import canvas, centered_image, text1, price

def c():
	c = canvas(TILE_WIDTH, CORNER, stroke=True)
	c.elements.extend([
		text1(),
		price(200),
		centered_image("decals/port.svg", scale=0.7)
	])
	return c

def port(name: str):
	port = c()
	port.elements[1].text = name
	return port