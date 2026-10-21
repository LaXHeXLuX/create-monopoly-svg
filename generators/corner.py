from generators.conf import CORNER
from generators.utils import text, rect, wrap, canvas, position_element, image

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
		rotated_text(15, 15, "MÖÖDUDES", size=5),
		rotated_text(19, 19, "SAAD 200 €", size=5),
		rotated_text(32, 32, "START", size=12),
		position_element(image("GO"), rotation=180, scale=0.6, cx="70%", cy="70%")
	])
	return go

def jail():
	JAIL_SQUARE_WIDTH_PERCENT = 75
	JAIL_SQUARE_WIDTH = f"{JAIL_SQUARE_WIDTH_PERCENT}%"
	HALF1 = JAIL_SQUARE_WIDTH_PERCENT / 2
	HALF2 = (100 - JAIL_SQUARE_WIDTH_PERCENT) / 2
	jail = c()
	r = rect("orange")
	r.width, r.height = JAIL_SQUARE_WIDTH, JAIL_SQUARE_WIDTH
	jail.elements.extend([
		r,
		rotated_text(18, 18, "PIHLA"),
		rotated_text(24, 24, "RABAS"),
		rotated_text(30, 30, "EKSINUD"),
		rotated_text(f"{HALF1}%", f"{100 - HALF2}%", "LIHTSALT", rotation=0),
		rotated_text(f"{100 - HALF2}%", f"{HALF1}%", "KÜLASTAD", rotation=-90),

	])
	return jail

def free_parking():
	free_parking = c()
	free_parking.elements.extend([
		rotated_text(15, 15, "VABA"),
		rotated_text(45, 45, "LÕKKEPLATS"),
		position_element(image("FP"), rotation=-45, scale=0.45, cy="45%", cx="45%")
	])
	return free_parking

def go_to_jail():
	go_to_jail = c()
	go_to_jail.elements.extend([
		rotated_text(17, 17, "EKSID ÄRA"),
		rotated_text(45, 45, "PIHLA RAPPA"),
		position_element(image("GTJ"), rotation=-45, scale=0.45, cy="48%", cx="48%")
	])
	return go_to_jail

corners = [
	go(),
	jail(),
	free_parking(),
	go_to_jail()
]