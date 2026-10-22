from generators.tiles.utils import tile_base
from generators.utils import position_image
from conf.texts import T_NAME, T_PAY, U_NAME

def tax(index: int):
	index = int(index)
	tax = tile_base(txt=T_NAME[index-1], cost=f"{T_PAY} {100 + 50*index}")
	tax.elements.append(position_image(f"T{index}"))
	return tax

def util(index: int):
	index = int(index)
	util = tile_base(txt=U_NAME[index-1], cost="150")
	util.elements.append(position_image(f"U{index}"))
	return util