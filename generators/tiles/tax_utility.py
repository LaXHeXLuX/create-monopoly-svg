from generators.tiles.utils import tile_base
from generators.utils import position_element, image
from generators.conf import T_NAME, T_PAY, U_NAME, IMAGE_SCALE

def tax(index: int):
	index = int(index)
	tax = tile_base(text=T_NAME[index-1], cost=f"{T_PAY} {100 + 50*index}")
	tax.elements.append(position_element(image(f"T{index}"), scale=IMAGE_SCALE[f"T{index}"]))
	return tax

def util(index: int):
	index = int(index)
	util = tile_base(text=U_NAME[index-1], cost="150")
	util.elements.append(position_element(image(f"U{index}"), scale=IMAGE_SCALE[f"U{index}"]))
	return util