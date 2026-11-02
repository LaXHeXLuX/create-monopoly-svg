from generators.cards.utils import card_base, title, content
from generators.utils import position_image
from conf.texts import U_NAME
from conf.long_texts import UTILITY_CARD_TEXT

def util(index: int):
	index = int(index)
	utility = card_base()
	utility.elements.extend([
		title(U_NAME[index], 45),
		position_image(f"U{index+1}", scale=0.65, cy="24%"),
		content(UTILITY_CARD_TEXT, 70, 50, y_percent=71)
	])
	return utility