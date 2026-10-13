from generators.tiles.utils import tile_base
from generators.utils import position_element, image
from generators.conf import STATION_NAME, IMAGE_SCALE

def station(index: int):
	station = tile_base(text=STATION_NAME[index-1], cost=200)
	station.elements.append(position_element(image("decals/S.svg"), scale=IMAGE_SCALE["S"]))
	return station