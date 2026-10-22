from .utils import card_base, title, content
from ..utils import position_image
from ..conf import STATION_NAME, UTILITY_CARD_TEXT

def station(index: int):
	index = int(index)
	utility = card_base()
	utility.elements.extend([
		title(STATION_NAME[index-1], 45),
		position_image("S", scale=0.65, cy="24%"),
		content(UTILITY_CARD_TEXT, 70, 40, y_percent=71)
	])
	return utility