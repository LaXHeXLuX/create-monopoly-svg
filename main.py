from pathlib import Path
from generators.clean_svg import embed_svg

def main(canvas):
	save_svg(canvas, "output.svg")

def save_svg(canvas, filename, clean=True):
	if (clean): canvas = embed_svg(canvas)
	path = Path(filename)
	path.parent.mkdir(parents=True, exist_ok=True)
	path.write_text(str(canvas), encoding="UTF8")

from generators.board import board_with_padding as board
from generators.center import center
from generators.corner import go, jail, free_parking, go_to_jail

from generators.tiles.property import property
from generators.tiles.station import station
from generators.tiles.tax_utility import tax, utility
from generators.tiles.chance_community import chance, community

from generators.cards.chance_community import chance as chance_card, community as community_card, chance_back, community_back
from generators.cards.utility import utility as utility_card
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
	"u": utility,
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

from conf.long_texts import CC_TEXTS, CH_TEXTS
from conf.game import PROPERTY_COSTS
from conf.texts import U_NAME, STATION_NAME

def do_all():
	out = "output/"

	# board
	save_svg(board(), f"{out}board.svg")

	# cards
	cards_out = f"{out}/cards/"
	# chance
	out = f"{cards_out}chance/"
	save_svg(chance_back(), f"{out}CH_B.svg")
	for i in range(len(CH_TEXTS)):
		save_svg(chance_card(CH_TEXTS[i]), f"{out}CH{i}.svg")

	# community
	out = f"{cards_out}community/"
	save_svg(community_back(), f"{out}CC_B.svg")
	for i in range(len(CC_TEXTS)):
		save_svg(community_card(CC_TEXTS[i]), f"{out}CC{i}.svg")

	# utilities
	out = f"{cards_out}utility/"
	for i in range(len(U_NAME)):
		save_svg(utility_card(i), f"{out}U{i}.svg")
		save_svg(utility_back(i), f"{out}U{i}B.svg")

	# stations
	out = f"{cards_out}station/"
	for i in range(len(STATION_NAME)):
		save_svg(station_card(i), f"{out}S{i}.svg")
		save_svg(station_back(i), f"{out}S{i}B.svg")

	# properties
	out = f"{cards_out}property/"
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
	
	if op not in arg_map:
		print(f"Need argument in {", ".join(arg_map.keys())}")
		return

	
	params = sys.argv[2:]
	for i in range(len(params)):
		try: params[i] = int(params[i])
		except ValueError: pass
	print(f"op: {op}, params: {params}")
	main(arg_map[op](*params))

if __name__ == '__main__':
	run()