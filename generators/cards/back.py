from generators.cards.utils import title, card_text, card_base, WIDTH, HEIGHT
from generators.utils import rect, position, price
from conf.texts import PAWN_VALUE as PAWN_VALUE_TXT, TO_UNPAWN_PAY, IF_PAWNED, PROPERTY_NAME, STATION_NAME, U_NAME
from conf.game import PAWN_VALUE, PAWN_COEFFICIENT, PROPERTY_COSTS, STATION_COST, UTILITY_COSTS

from svg import LinearGradient, Stop, Defs

def linear_gradient(s, e, id):
	return LinearGradient(
		id=id,
		gradientTransform="rotate(90)",
		elements=[
			Stop(offset="0%", stop_color=s),
			Stop(offset="100%", stop_color=e)
		]
	)

PADDING1 = 4.8
PADDING2 = 6.1

def bg(padding, grad_id):
	bg = rect(fill=f"url(#{grad_id})", stroke=0)
	bg.x, bg.y = padding, padding
	bg.width = WIDTH - 2*padding
	bg.height = HEIGHT - 2*padding
	return bg

def back_base():
	light_red = "#ff8888"
	dark_red = "#ff2222"
	up = linear_gradient(light_red, dark_red, "up")
	down = linear_gradient(dark_red, light_red, "down")
	base = card_base()
	base.elements.extend([
		Defs(elements=[up, down]),
		bg(PADDING1, "up"),
		bg(PADDING2, "down")
	])
	return base

def pawn_value_text(value: int):
	return f"{PAWN_VALUE_TXT} {price(int(PAWN_VALUE * value))}"

def unpawn_cost_text(value: int):
	return f"{TO_UNPAWN_PAY} {price(int((PAWN_VALUE + PAWN_COEFFICIENT) * value))}"

def white_text(txt, y_percent, scale=1):
	return position(card_text(txt, size=4*scale, fill="#ffffff"), y=f"{y_percent}%")

def back(name: str, value: int):
	base = back_base()
	base.elements.extend([
		title(name, y="16%", fill="#ffffff"),
		white_text(pawn_value_text(value), 36),
		white_text(unpawn_cost_text(value), 56),
		white_text(IF_PAWNED, 85, scale=0.6)
	])
	return base

def property_back(zone: int, index: int):
	return back(PROPERTY_NAME[zone][index], PROPERTY_COSTS[zone][index])

def station_back(index: int):
	return back(STATION_NAME[index], STATION_COST)

def utility_back(index: int):
	return back(U_NAME[index], UTILITY_COSTS[index])