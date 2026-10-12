from generators.tiles.chance_community import chance, community
from generators.tiles.property import property
from generators.tiles.station import station
from generators.tiles.tax_utility import tax, util

def tile(id: str):
	if (id == "CH"):
		return chance()
	if (id == "CC"):
		return community()
	i = int(id[1])
	if (id[0] == "P"):
		return property(i, int(id[2]))
	if (id[0] == "S"):
		return station(i)
	if (id[0] == "T"):
		return tax(i)
	if (id[0] == "U"):
		return util(i)

	raise Exception(f"invalid id {id}")