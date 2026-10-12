from generators.tiles.tile import tile
from generators.conf import ZONES
from generators.utils import rect, text2, price

def property(name: str, zone: int, cost: int):
	zone = int(zone)
	cost = int(cost)
	property = tile(cost=cost)
	r = rect(fill=ZONES[zone])
	r.height = "25%"
	property.elements.extend([r, text2(name), price(cost)])
	return property