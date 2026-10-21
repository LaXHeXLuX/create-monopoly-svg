from generators.tiles.utils import tile_base
from generators.utils import position_element, image
from generators.conf import CH_NAME, CC_NAME, IMAGE_SCALE

def c(text, image_tag, scale):
	c = tile_base(text=text)
	c.elements.insert(1, position_element(image(image_tag), cy="55%", scale=scale))
	return c

def chance():
	return c(CH_NAME, "CH", IMAGE_SCALE["CH"])

def community():
	return c(CC_NAME, "CC", IMAGE_SCALE["CC"])