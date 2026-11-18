from generators.tiles.utils import tile_base
from generators.utils import position_image
from conf.texts import T_NAME, T_PAY, U_NAME
from conf.game import UTILITY_COSTS, TAX_COSTS

def tax(index: int):
	tax = tile_base(txt=T_NAME[index], cost=f"{T_PAY} {TAX_COSTS[index-1]}")
	tax.elements.append(position_image(f"T{index}"))
	return tax

def utility(index: int):
	utility = tile_base(txt=U_NAME[index], cost=UTILITY_COSTS[index-1])
	utility.elements.append(position_image(f"U{index}"))
	return utility