from generators.tiles.tile import tile
from generators.utils import centered_image

def tax1():
	tax = tile(text="TULUMAKS", cost="MAKSA 200")
	tax.elements.append(centered_image("decals/dot1.svg", scale=0.2))
	return tax

def tax2():
	tax = tile(text="LISAMAKS", cost="MAKSA 150")
	tax.elements.append(centered_image("decals/dot2.svg", scale=0.2))
	return tax

def util1():
	util = tile(text="ELEKTRIVÕRK", cost="150")
	util.elements.append(centered_image("decals/windmill.svg", scale=0.8))
	return util

def util2():
	util = tile(text="VEEVÄRK", cost="150")
	util.elements.append(centered_image("decals/water_pump.svg", scale=0.75))
	return util