from generators.tiles.utils import tile_base, text2
from generators.utils import rect
from conf.ui import ZONE_COLORS
from conf.texts import PROPERTY_NAME
from conf.game import PROPERTY_COSTS

def property(zone: int, index: int):
	zone -= 1
	index -= 1
	name = PROPERTY_NAME[zone][index]
	property = tile_base(cost=PROPERTY_COSTS[zone][index])
	r = rect(fill=ZONE_COLORS[zone])
	r.height = "25%"
	property.elements.extend([r, text2(name)])
	return property