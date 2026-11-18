from generators.tiles.utils import tile_base
from generators.utils import rect, text, position
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
	property.elements.extend([r, position(text(name), y="38%")])
	return property