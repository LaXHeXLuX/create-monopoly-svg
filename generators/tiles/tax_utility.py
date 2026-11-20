from generators.tiles.utils import tile_base
from conf.texts import T_NAME, T_PAY, U_NAME
from conf.game import UTILITY_COSTS, TAX_COSTS

def tax(index: int):
	return tile_base(txt=T_NAME[index], image_tag=f"T{index}", cost=f"{T_PAY} {TAX_COSTS[index]}")

def utility(index: int):
	return tile_base(txt=U_NAME[index], image_tag=f"U{index}", cost=UTILITY_COSTS[index])