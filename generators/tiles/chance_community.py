from generators.tiles.utils import tile_base
from generators.utils import position_image
from conf.texts import CH_NAME, CC_NAME

def c(txt, image_tag):
	c = tile_base(txt=txt)
	c.elements.insert(1, position_image(image_tag, cy="55%"))
	return c

def chance():
	return c(CH_NAME, "CH")

def community():
	return c(CC_NAME, "CC")