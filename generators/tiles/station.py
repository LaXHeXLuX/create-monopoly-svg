from generators.tiles.utils import tile_base
from generators.utils import position_image
from conf.texts import STATION_NAME
from conf.game import STATION_COST

def station(index: int):
	station = tile_base(txt=STATION_NAME[index-1], cost=STATION_COST)
	station.elements.append(position_image("S"))
	return station