import svg
from generators.conf import CORNER, FONT
from generators.utils import wrap, canvas, centered_image

def c():
	return canvas(CORNER, CORNER, stroke=True)

def rotated_text(x, y, text: str, rotation: int = -45, size: int = 7):
	return wrap(
		svg.Text(
			x=0, y=0,
			text=text,
			text_anchor="middle",
			dominant_baseline="middle",
			font_family=FONT,
			font_size=size,
			transform=f"rotate({rotation})",
		), 
		x, y
	)

def go():
	go = c()
	go.elements.extend([
		rotated_text(15, 15, "MÖÖDUDES", size=5),
		rotated_text(19, 19, "SAAD 200 €", size=5),
		rotated_text(32, 32, "START", size=12),
		centered_image("decals/arrow.svg", rotation=180, scale=0.6, cx="70%", cy="70%")
	])
	return go

def jail():
	JAIL_SQUARE_WIDTH_PERCENT = 75
	JAIL_SQUARE_WIDTH = f"{JAIL_SQUARE_WIDTH_PERCENT}%"
	HALF1 = JAIL_SQUARE_WIDTH_PERCENT / 2
	HALF2 = (100 - JAIL_SQUARE_WIDTH_PERCENT) / 2
	jail = c()
	jail.elements.extend([
		svg.Rect(
			x=0, y=0,
			width=JAIL_SQUARE_WIDTH, height=JAIL_SQUARE_WIDTH,
			fill="orange",
			stroke="black",
			stroke_width=0.5
		),
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
		centered_image("decals/fire.svg", rotation=-45, scale=0.45, cy="45%", cx="45%")
	])
	return free_parking

def go_to_jail():
	go_to_jail = c()
	go_to_jail.elements.extend([
		rotated_text(17, 17, "EKSID ÄRA"),
		rotated_text(45, 45, "PIHLA RAPPA"),
		centered_image("decals/compass.svg", rotation=-45, scale=0.45, cy="48%", cx="48%")
	])
	return go_to_jail

corners = [
	go(),
	jail(),
	free_parking(),
	go_to_jail()
]