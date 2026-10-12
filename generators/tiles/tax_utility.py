from generators.conf import TILE_WIDTH, CORNER, CURRENCY
from generators.utils import canvas, text1, price, centered_image

def c():
	c = canvas(TILE_WIDTH, CORNER, stroke=True)
	c.elements.extend([
		text1(),
		price(150)
	])
	return c

def tax_text(price):
	return f"MAKSA {price} {CURRENCY}"

def tax1():
	tax = c()
	tax.elements[1].text = "TULUMAKS"
	tax.elements[2].text = tax_text(200)
	tax.elements.append(centered_image("decals/dot1.svg", scale=0.2))
	return tax

def tax2():
	tax = c()
	tax.elements[1].text = "LISAMAKS"
	tax.elements[2].text = tax_text(150)
	tax.elements.append(centered_image("decals/dot2.svg", scale=0.2))
	return tax

def util1():
	util = c()
	util.elements[1].text = "ELEKTRIVÕRK"
	util.elements.append(centered_image("decals/windmill.svg", scale=0.8))
	return util

def util2():
	util = c()
	util.elements[1].text = "VEEVÄRK"
	util.elements.append(centered_image("decals/water_pump.svg", scale=0.75))
	return util