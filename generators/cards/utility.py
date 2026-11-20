from generators.cards.utils import card_with_padding, title, card_text
from generators.utils import position, position_image
from conf.texts import U_NAME
from conf.long_texts import UTILITY_CARD_TEXT

def utility(index: int):
	return card_with_padding([
		title(U_NAME[index], y="45%"),
		position_image(f"U{index}", scale=0.65, cy="24%"),
		position(card_text(UTILITY_CARD_TEXT), y="72%")
	])