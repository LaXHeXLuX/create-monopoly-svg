from conf.ui import CORNER, JAIL_COLOR
from conf.game import GO_MONEY
from conf.texts import price, IF_PASS_GET_MONEY, GO, JUST, VISITING, JAIL_TEXTS, FREE, PARKING, GO_TO, JAIL
from generators.utils import text, rect, wrap, canvas, position_image

def c():
	c = canvas(CORNER, CORNER)
	c.elements.append(rect())
	return c

def rotated_text(x, y, txt: str, rotation: int = -45, size: int = 7):
	t = text(txt, size)
	t.transform = f"rotate({rotation})"
	return wrap(t, x, y)

def go():
	go = c()
	go.elements.extend([
		rotated_text(-5.5, 40.5, f"{IF_PASS_GET_MONEY} {price(GO_MONEY)}", size=5),
		rotated_text(32, 32, GO, size=12),
		position_image("GO", rotation=180, cx="70%", cy="70%")
	])
	return go

def jail():
	JAIL_SQUARE_WIDTH_PERCENT = 75
	JAIL_SQUARE_WIDTH = f"{JAIL_SQUARE_WIDTH_PERCENT}%"
	HALF1 = JAIL_SQUARE_WIDTH_PERCENT / 2
	HALF2 = (100 - JAIL_SQUARE_WIDTH_PERCENT) / 2
	jail = c()
	r = rect(JAIL_COLOR)
	r.width, r.height = JAIL_SQUARE_WIDTH, JAIL_SQUARE_WIDTH
	jail.elements.append(r)
	for i in range(len(JAIL_TEXTS)):
		xy = 27 - 3*len(JAIL_TEXTS) + 6*i
		txt = rotated_text(xy, xy, JAIL_TEXTS[i])
		jail.elements.append(txt)
	jail.elements.extend([
		rotated_text(f"{HALF1}%", f"{100 - HALF2}%", JUST, rotation=0),
		rotated_text(f"{100 - HALF2}%", f"{HALF1}%", VISITING, rotation=-90),

	])
	return jail

def free_parking():
	free_parking = c()
	free_parking.elements.extend([
		rotated_text(15, 15, FREE),
		rotated_text(45, 45, PARKING),
		position_image("FP", rotation=-45, cy="45%", cx="45%")
	])
	return free_parking

def go_to_jail():
	go_to_jail = c()
	go_to_jail.elements.extend([
		rotated_text(17, 17, GO_TO),
		rotated_text(45, 45, JAIL),
		position_image("GTJ", rotation=-45, cy="48%", cx="48%")
	])
	return go_to_jail