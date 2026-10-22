from generators.cards.utils import card_base, title
from generators.utils import canvas, position_image, text, price
from conf.texts import STATION_NAME, STATION_RENT, FOR_STATIONS

FONT_SIZE = 3.2

def rent_line(index):
	rent = text(price(25 * 2**(index-1)), size=FONT_SIZE, weight=-1, align=1)
	rent.x = "100%"
	rent_text = f"{index} {FOR_STATIONS}"
	if index == 1: rent_text = STATION_RENT
	txt = text(rent_text, size=FONT_SIZE, weight=-1, align=-1)
	w_percent = 82
	c = canvas(f"{w_percent}%", "50%")
	c.overflow = "visible"
	c.elements.extend([rent, txt])
	c.x = f"{50 - w_percent/2}%"
	c.y = f"{50 + 9*index}%"
	return c

def station(index: int):
	index = int(index)
	station = card_base()
	station.elements.extend([
		title(STATION_NAME[index-1], 45),
		position_image("S", scale=0.65, cy="24%")
	])
	for i in range(1, 5):
		rl = rent_line(i)
		station.elements.append(rl)
	return station