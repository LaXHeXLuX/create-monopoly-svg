from generators.cards.utils import card_base, title, left_right_aligned_text, OFFSET as OUTER_OFFSET, WIDTH, HEIGHT
from generators.utils import rect, canvas, price
from conf.texts import PROPERTY_NAME, PROPERTY_RIGHT, RENT, RENT_FOR_ZONE, HOUSE_PRICE, HOTEL_PRICE, PIECE
from conf.ui import ZONE_COLORS
from conf.game import PROPERTY_RENTS
from generators.tiles.property import cost as property_cost

OFFSET = OUTER_OFFSET + WIDTH * 0.035

def header(color, name: str):
	c = canvas(WIDTH - 2*OFFSET, HEIGHT * 0.19, overflow=True)
	c.x, c.y = OFFSET, OFFSET

	r = rect(fill=color)
	r.stroke_width = 0.36
	right = title(PROPERTY_RIGHT, 23, weight=-1, size=0.9)
	name = title(name, 65, size=1.6)

	c.elements.extend([r, right, name])
	return c

def footer(zone):
	footer_height = HEIGHT * 0.18
	c = canvas(WIDTH - 2*OFFSET, footer_height, overflow=True)
	c.x, c.y = OFFSET, HEIGHT - OFFSET - footer_height

	stroke = rect()
	stroke.height = "0.001%"
	stroke.stroke_width = 0.35

	house_hotel_price = f"1 {PIECE} {price(50 * ((zone+1) // 2))}"
	t1 = left_right_aligned_text(HOUSE_PRICE, house_hotel_price)
	t1.y = "30%"
	t2 = left_right_aligned_text(HOTEL_PRICE, house_hotel_price)
	t2.y = "65%"

	c.elements.extend([stroke, t1, t2])
	return c


def property(zone: int, index: int):
	zone = int(zone) - 1
	index = int(index) - 1

	card = card_base()
	card.elements.extend([
		header(ZONE_COLORS[zone], PROPERTY_NAME[zone][index]),
		footer(zone)
	])

	cost_list = PROPERTY_NAME[zone, index]
	print(cost_list)

	return card