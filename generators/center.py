from conf.ui import CENTER_COLOR, CENTER
from conf.texts import CC_NAME, CH_NAME
from generators.utils import text, rect, canvas, position, position_element, position_image
from generators.cards.utils import WIDTH, HEIGHT

def card_place(txt: str):
	dotted_box = rect()
	dotted_box.stroke_width = "1.5"
	dotted_box.stroke_dasharray = "2"

	card_place = canvas(HEIGHT, WIDTH)
	card_place.elements.extend([
		dotted_box, 
		position(text(txt, size=8))
	])
	return card_place

def center():
	PADDING = 20

	center = canvas(CENTER, CENTER)
	center.elements.extend([
		rect(CENTER_COLOR),
		position_image("center", rotation=-45),
		position_element(card_place(CC_NAME), cx=PADDING + WIDTH, cy=PADDING, rotation=90),
		position_element(card_place(CH_NAME), cx=CENTER - PADDING - WIDTH, cy=CENTER - PADDING, rotation=270)
	])

	return center