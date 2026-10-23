from generators.cards.utils import card_base, title, left_right_aligned_text
from generators.utils import canvas, position_image, text, price
from conf.texts import STATION_NAME, STATION_RENT, FOR_STATIONS

FONT_SIZE = 3.2

def rent_line(index):
	l = f"{index} {FOR_STATIONS}"
	r = price(25 * 2**(index-1))
	if index == 1: l = STATION_RENT
	aligned_text = left_right_aligned_text(l, r, size=FONT_SIZE, w_percent=82)
	aligned_text.y = f"{50 + 9*index}%"
	return aligned_text

def station(index: int):
	index = int(index)
	station = card_base()
	station.elements.extend([
		title(STATION_NAME[index-1], 45, size=1.5),
		position_image("S", scale=0.65, cy="24%")
	])
	for i in range(1, 5):
		rl = rent_line(i)
		station.elements.append(rl)
	return station