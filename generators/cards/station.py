from generators.cards.utils import card_base, title, left_right_aligned_text, WIDTH, INNER_OFFSET as OFFSET
from generators.utils import canvas, position_image, text, price
from conf.texts import STATION_NAME, STATION_RENT, FOR_STATIONS

FONT_SIZE = 3.2

def rent_line(index):
	l = f"{index} {FOR_STATIONS}"
	r = price(25 * 2**(index-1))
	if index == 1: l = STATION_RENT
	aligned_text = left_right_aligned_text(l, r, size=FONT_SIZE)
	aligned_text.y = f"{18*index}%"
	return aligned_text

def rents():
	rents = canvas(WIDTH - 2*OFFSET, "50%")
	rents.x = OFFSET
	rents.y = "50%"
	for i in range(1, 5):
		rl = rent_line(i)
		rents.elements.append(rl)
	return rents

def station(index: int):
	index = int(index)
	station = card_base()
	station.elements.extend([
		title(STATION_NAME[index], 45),
		position_image("S", scale=0.65, cy="24%"),
		rents()
	])
	return station