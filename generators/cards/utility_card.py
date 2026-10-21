from .utils import card_base, WIDTH
from ..utils import text, rect, canvas, position_element

TITLE_FONT_SIZE = WIDTH * 0.05
LOGO_FONT_SIZE = WIDTH * 0.0285

def utility_base():
	utility = card_base()
	return utility

def util(index: int):
	return utility_base()