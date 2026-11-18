from generators.tiles.utils import tile_base
from generators.utils import position_image
from conf.texts import STATION_NAME
from conf.game import STATION_COST

def station(index: int):
	return tile_base(txt=STATION_NAME[index], image_tag="S", cost=STATION_COST)