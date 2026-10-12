from generators.tiles.tile import tile
from generators.utils import centered_image

def port(name: str):
	port = tile(text=name, cost=200)
	port.elements.append(centered_image("decals/port.svg", scale=0.7))
	return port