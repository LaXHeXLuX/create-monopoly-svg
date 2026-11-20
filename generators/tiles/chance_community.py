from generators.tiles.utils import tile_base
from conf.texts import CH_NAME, CC_NAME

def c(txt, image_tag):
	return tile_base(txt=txt, image_tag=image_tag, image_y="55%")

def chance():
	return c(CH_NAME, "CH")

def community():
	return c(CC_NAME, "CC")