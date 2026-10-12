from generators.tiles.utils import tile_base
from generators.utils import centered_image
from generators.conf import CH_NAME, CC_NAME, IMAGE_SCALE

def c(text, href, scale):
	c = tile_base(text=text)
	c.elements.insert(1, centered_image(href, cy="55%", scale=scale))
	return c

def chance():
	return c(CH_NAME, "decals/CH.svg", IMAGE_SCALE["CH"])

def community():
	return c(CC_NAME, "decals/CC.svg", IMAGE_SCALE["CC"])