from generators.cards.utils import card_with_padding, title, left_right_aligned_text, INNER_OFFSETS as OFFSETS
from generators.utils import canvas, position, position_image, price
from conf.texts import STATION_NAME, STATION_RENT, FOR_STATIONS
from conf.game import STATION_RENTS

def rent_line(index):
	l = f"{index} {FOR_STATIONS}"
	r = price(STATION_RENTS[index-1])
	if index == 1: l = STATION_RENT
	return left_right_aligned_text(l, r, y=f"{20*index}%")

def rents():
	rents = canvas(f"{100 - 2*OFFSETS[0]}%", "50%")
	for i in range(1, 5):
		rl = rent_line(i)
		rents.elements.append(rl)
	return position(rents, x=f"{OFFSETS[0]}%")

def station(index: int):
	return card_with_padding([
		title(STATION_NAME[index], y="45%"),
		position_image("S", scale=0.65, cy="24%"),
		rents()
	])