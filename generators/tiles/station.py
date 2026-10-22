from generators.tiles.utils import tile_base
from generators.utils import position_image
from generators.conf import STATION_NAME

def station(index: int):
	station = tile_base(text=STATION_NAME[index-1], cost=200)
	station.elements.append(position_image("S"))
	return station