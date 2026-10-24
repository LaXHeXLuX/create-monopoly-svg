from generators.cards.utils import card_base, title, left_right_aligned_text, OFFSET as OUTER_OFFSET, WIDTH, HEIGHT
from generators.utils import rect, canvas, price, text
from conf.texts import PROPERTY_NAME, PROPERTY_RIGHT, RENT, RENT_FOR_ZONE, HOUSE_PRICE, HOTEL_PRICE, PIECE, PLUS_4_HOUSES
from conf.ui import ZONE_COLORS
from conf.game import PROPERTY_RENTS, HOUSE_PRICES, HOTEL_PRICES

OFFSET = OUTER_OFFSET + WIDTH * 0.035
HEADER_HEIGHT = HEIGHT * 0.19
FOOTER_HEIGHT = HEIGHT * 0.18

def header(color, name: str):
	c = canvas(WIDTH - 2*OFFSET, HEADER_HEIGHT, overflow=True)
	c.x, c.y = OFFSET, OFFSET

	r = rect(fill=color)
	r.stroke_width = 0.36
	right = title(PROPERTY_RIGHT, 23, weight=-1, size=0.9)
	name = title(name, 65, size=1.6)

	c.elements.extend([r, right, name])
	return c

def house_hotel_price(zone):
	prices = [p[zone // 2] for p in [HOUSE_PRICES, HOTEL_PRICES]]
	return [f"1 {PIECE} {price(p)}" for p in prices]

def footer(zone):
	c = canvas(WIDTH - 2*OFFSET, FOOTER_HEIGHT, overflow=True)
	c.x, c.y = OFFSET, HEIGHT - OFFSET - FOOTER_HEIGHT

	stroke = rect()
	stroke.height = "0.001%"
	stroke.stroke_width = 0.35

	house_hotel_prices = house_hotel_price(zone)
	t1 = left_right_aligned_text(HOUSE_PRICE, house_hotel_prices[0])
	t1.y = "30%"
	t2 = left_right_aligned_text(HOTEL_PRICE, house_hotel_prices[1])
	t2.y = "65%"
	plus_4_houses = text(PLUS_4_HOUSES, size=2.15, weight=-1, align=1)
	plus_4_houses.x = "100%"
	plus_4_houses.y = "30%"
	t2.elements.append(plus_4_houses)

	c.elements.extend([stroke, t1, t2])
	return c

def rents(zone: int, index: int):
	c = canvas(WIDTH - 2*OFFSET, HEIGHT - 2*OFFSET - HEADER_HEIGHT - FOOTER_HEIGHT)
	c.x, c.y = OFFSET, OFFSET + HEADER_HEIGHT

	rents = PROPERTY_RENTS[zone][index]

	step = 13
	start = 10
	t1 = left_right_aligned_text(RENT, price(rents[0]))
	t1.y = f"{start}%"
	c.elements.append(t1)
	t2 = left_right_aligned_text(RENT_FOR_ZONE, price(rents[0]*2))
	t2.y = f"{start + step}%"
	c.elements.append(t2)
	for i in range(1, len(rents)):
		t = left_right_aligned_text(RENT, price(rents[i]))
		t.y = f"{start + (i+1)*step}%"
		c.elements.append(t)

	return c

def property(zone: int, index: int):
	zone = int(zone)
	index = int(index)

	card = card_base()
	card.elements.extend([
		header(ZONE_COLORS[zone], PROPERTY_NAME[zone][index]),
		rents(zone, index),
		footer(zone)
	])

	return card