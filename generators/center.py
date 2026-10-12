import svg
from generators.conf import CENTER_COLOR, CENTER, FONT
from generators.utils import rect, canvas, position_element, centered_image

WIDTH = 88
HEIGHT = 56

def c():
	dotted_box = rect()
	dotted_box.stroke_width = "1.5"
	dotted_box.stroke_dasharray = "2"

	c = canvas(WIDTH, HEIGHT, stroke=False)
	c.elements.extend([
		dotted_box,
		svg.Text(
			x=44, y=28,
			text="TEXT",
			text_anchor="middle",
			dominant_baseline="middle",
			font_family=FONT,
			font_size="8"
		)
	])

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
		position_element(card_place("ÜHISFOND"), PADDING + HEIGHT, PADDING, 1, False),
		position_element(card_place("LOOS"), CENTER - PADDING - HEIGHT, CENTER - PADDING, 3, False)
	])

	return center