from generators.tiles.utils import tile_base, text2
from generators.utils import rect
from conf.ui import ZONE_COLORS
from conf.texts import PROPERTY_NAME

def cost(zone: int, index: int):
	if zone == 1: return 60
	if zone == 8: return 300 + 50*index
	return 20 + zone*40 + (index // 3)*20

def property(zone: int, index: int):
	zone = int(zone)
	index = int(index)
	c = cost(zone, index)
	name = PROPERTY_NAME[zone-1][index-1]
	property = tile_base(cost=c)
	r = rect(fill=ZONE_COLORS[zone])
	r.height = "25%"
	property.elements.extend([r, text2(name)])
	return property