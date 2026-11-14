from generators.cards.utils import rect, title, left_right_aligned_text, card_with_padding, INNER_OFFSETS as OFFSETS, INNER_HEIGHT as HEIGHT, INNER_WIDTH as WIDTH
from generators.utils import canvas, price, text
from conf.texts import PROPERTY_NAME, PROPERTY_RIGHT, RENT, RENT_FOR_ZONE, HOUSE_PRICE, HOTEL_PRICE, PIECE, PLUS_4_HOUSES
from conf.ui import ZONE_COLORS
from conf.game import PROPERTY_RENTS, HOUSE_PRICES, HOTEL_PRICES

HEADER_HEIGHT = 22
FOOTER_HEIGHT = 20

def house(fill=None, number=None):
	scale = 4
	c = canvas(scale, scale)
	from svg import Path
	house = Path(d="M 50 0 65 15 65 10 80 10 80 30 100 50 85 50 85 100 15 100 15 50 0 50")
	house.transform = f"scale({0.01 * scale})"
	if fill != None: house.fill = fill
	c.elements.append(house)
	if number != None: 
		t = text(number, size=3, weight=1)
		t.fill = "white"
		t.x, t.y = "50%", "65%"
		c.elements.append(t)
	return c

def header(color, name: str):
	c = canvas("100%", f"{HEADER_HEIGHT}%", overflow=True)

	r = rect(fill=color)
	right = title(PROPERTY_RIGHT, 23, size=0.6, weight=-1)
	name = title(name, 65, size=1.07)

	c.elements.extend([r, right, name])
	return c

def house_hotel_price(zone):
	prices = [p[zone // 2] for p in [HOUSE_PRICES, HOTEL_PRICES]]
	return [f"1 {PIECE} {price(p)}" for p in prices]

def footer(zone):
	c = canvas("100%", f"{FOOTER_HEIGHT}%", overflow=True)
	c.y = HEIGHT - FOOTER_HEIGHT

	stroke = rect()
	stroke.height = "0.0001%"

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
	c = canvas("100%", f"{100 - HEADER_HEIGHT - FOOTER_HEIGHT}%")
	c.y = f"{HEADER_HEIGHT}%"

	rents = PROPERTY_RENTS[zone][index]

	start = 10
	step = (100 - 2*start) / len(rents)
	t1 = left_right_aligned_text(RENT, price(rents[0]))
	t1.y = f"{start}%"
	c.elements.append(t1)
	t2 = left_right_aligned_text(RENT_FOR_ZONE, price(rents[0]*2))
	t2.y = f"{start + step}%"
	c.elements.append(t2)
	for i in range(1, len(rents)):
		color = "#1FB25A"
		number = i
		if i == len(rents)-1:
			color = "#ff5353"
			number = None
		t = left_right_aligned_text(RENT, price(rents[i]))
		t.y = f"{start + (i+1)*step}%"

		h = house(fill=color, number=number)
		h.x = "18%"
		h.y = "-12%"
		t.elements.append(h)

		c.elements.append(t)

	return c

def property(zone: int, index: int):
	zone = int(zone)
	index = int(index)

	inner_card = canvas(
		f"{100 - 2*OFFSETS[0]}%",
		f"{100 - 2*OFFSETS[1]}%",
		overflow=True
	)
	inner_card.x = f"{OFFSETS[0]}%"
	inner_card.y = f"{OFFSETS[1]}%"
	inner_card.elements.extend([
		header(ZONE_COLORS[zone], PROPERTY_NAME[zone][index]),
		rents(zone, index),
		footer(zone)
	])
	print(f"checking card header stroke size 1: {inner_card.elements[0].elements[0].stroke_width}")
	
	card = canvas(WIDTH, HEIGHT, overflow=True)
	card.elements.append(inner_card)
	print(f"checking card header stroke size 2: {card.elements[0].elements[0].elements[0].stroke_width}")
	return card_with_padding(card)