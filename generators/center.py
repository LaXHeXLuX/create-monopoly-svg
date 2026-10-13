from generators.conf import CENTER_COLOR, CENTER, FONT, CC_NAME, CH_NAME
from generators.utils import text, rect, canvas, position_element, centered_image
from generators.cards.utils import WIDTH, HEIGHT

def c():
	dotted_box = rect()
	dotted_box.stroke_width = "1.5"
	dotted_box.stroke_dasharray = "2"

	t = text(size=8)
	t.x, t.y = "50%", "50%"

	c = canvas(WIDTH, HEIGHT, stroke=False)
	c.elements.extend([dotted_box, t])

	return c

def card_place(text: str):
	card_place = c()
	card_place.elements[1].text = text
	return card_place

def center():
	PADDING = 20

	center = canvas(CENTER, CENTER, stroke=False)
	center.elements.extend([
		rect(CENTER_COLOR),
		centered_image("decals/kaart.svg", rotation=-45, scale=1.2),
		position_element(card_place(CC_NAME), PADDING + HEIGHT, PADDING, 1, False),
		position_element(card_place(CH_NAME), CENTER - PADDING - HEIGHT, CENTER - PADDING, 3, False)
	])

	return center