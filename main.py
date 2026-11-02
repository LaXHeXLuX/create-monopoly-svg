def main(canvas):
	save_svg(canvas, "pytest.svg")

def save_svg(canvas, filename, clean=True):
	if (clean):
		from generators.clean_svg import embed_svg
		canvas = embed_svg(canvas)
	from pathlib import Path
	path = Path(filename)
	path.parent.mkdir(parents=True, exist_ok=True)
	file = open(filename, "w+", encoding="UTF8")
	file.write(str(canvas))
	file.close()

from generators.board import board
from generators.center import center
from generators.corner import go, jail, free_parking, go_to_jail

from generators.tiles.property import property
from generators.tiles.station import station
from generators.tiles.tax_utility import tax, util
from generators.tiles.chance_community import chance, community

from generators.cards.chance_community import chance as chance_card, community as community_card, chance_back, community_back
from generators.cards.utility import util as utility_card
from generators.cards.station import station as station_card
from generators.cards.property import property as property_card
from generators.cards.back import property_back, station_back, utility_back

arg_map = {
	"b": board,

	"ce": center,
	"go": go,
	"j": jail,
	"fp": free_parking,
	"gj": go_to_jail,

	"p": property,
	"s": station,
	"t": tax,
	"u": util,
	"ch": chance,
	"cc": community,

	"chc": chance_card,
	"chb": chance_back,
	"ccc": community_card,
	"ccb": community_back,
	"uc": utility_card,
	"ub": utility_back,
	"sc": station_card,
	"sb": station_back,
	"pc": property_card,
	"pb": property_back
}

def do_all():
	out = "output/"

	# board
	save_svg(board(), f"{out}board.svg")

	# cards
	# chance
	out = f"output/cards/chance/"
	from conf.long_texts import CC_TEXTS, CH_TEXTS
	save_svg(chance_back(), f"{out}CH_B.svg")
	for i in range(len(CH_TEXTS)):
		save_svg(chance_card(CH_TEXTS[i]), f"{out}CH{i}.svg")

	# community
	out = f"output/cards/community/"
	save_svg(community_back(), f"{out}CC_B.svg")
	for i in range(len(CC_TEXTS)):
		save_svg(community_card(CC_TEXTS[i]), f"{out}CC{i}.svg")

	# utilities
	out = f"output/cards/utility/"
	for i in range(2):
		save_svg(utility_card(i), f"{out}U{i}.svg")
		save_svg(utility_back(i), f"{out}U{i}B.svg")

	# stations
	out = f"output/cards/station/"
	for i in range(4):
		save_svg(station_card(i), f"{out}S{i}.svg")
		save_svg(station_back(i), f"{out}S{i}B.svg")

	# properties
	out = f"output/cards/property/"
	from conf.game import PROPERTY_COSTS
	for z in range(len(PROPERTY_COSTS)):
		for i in range(len(PROPERTY_COSTS[z])):
			save_svg(property_card(z, i), f"{out}P{z}{i}.svg")
			save_svg(property_back(z, i), f"{out}P{z}{i}B.svg")

import sys
def run():
	if len(sys.argv) < 2:
		main(board())
		return
	
	op = sys.argv[1]
	if (op in ["a", "all"]):
		do_all()
		return
	
	if sys.argv[1] not in arg_map:
		print("Need argument in " + f"{{{", ".join(arg_map.keys())}}}")
		return

	
	params = sys.argv[2:]
	print(f"op: {op}, params: {params}")
	main(arg_map[op](*params))

if __name__ == '__main__':
	run()