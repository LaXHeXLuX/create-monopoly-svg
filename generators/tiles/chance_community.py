from generators.tiles.tile import tile
from generators.utils import centered_image

def c(text, href):
	c = tile(text=text)
	c.elements.insert(1, centered_image(href, cy="55%", scale=0.8))
	return c

def chance():
	return c("LOOS", "decals/question.svg")

def community():
	return c("ÜHISFOND", "decals/piggy_bank.svg")