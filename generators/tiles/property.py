import svg
from generators.conf import ZONES, TILE_WIDTH, CORNER, CURRENCY
from generators.utils import text2, price, canvas

def c():
	c = canvas(TILE_WIDTH, CORNER, stroke=True)
	c.elements.extend([
		svg.Rect(
			width=TILE_WIDTH, height=15,
			fill="#fac",
			stroke="black",
			stroke_width=0.5
		),
		text2(),
		price()
	])
	return c

def card(name: str, zone: int, price: int):
	zone = int(zone)
	price = int(price)
	card = c()
	card.elements[1].fill = ZONES[zone]
	card.elements[2].text = name
	card.elements[3].text = f"{price} {CURRENCY}"
	return card