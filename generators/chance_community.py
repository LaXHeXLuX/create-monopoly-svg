import svg
from conf import CARD_WIDTH, CORNER
from utils import canvas, centered_image, text1

def c():
	c = canvas(CARD_WIDTH, CORNER, stroke=True)
	c.elements.append(text1())
	return c

def chance():
	chance = c()
	chance.elements[1].text = "LOOS"
	chance.elements.insert(1, centered_image("decals/question.svg", cy="55%"))
	return chance

def community():
	community = c()
	community.elements[1].text = "ÜHISFOND"
	community.elements.insert(1, centered_image("decals/piggy_bank.svg", cy="55%", scale=0.8))

	return community