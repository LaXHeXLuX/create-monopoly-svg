def main(canvas):
	file = open("pytest.svg", "w+", encoding="UTF8")
	file.write(str(canvas))
	file.close()
	import generators.clean_svg as clean_svg
	clean_svg.main()

def print_list(arr):
	return f"{{{", ".join(arr)}}}"

from generators.board import board
from generators.center import center
from generators.corner import go, jail, free_parking, go_to_jail

from generators.tiles.property import property
from generators.tiles.station import station
from generators.tiles.tax_utility import tax, util
from generators.tiles.chance_community import chance, community

from generators.cards.chance_community import chance as chance_card, community as community_card
from generators.cards.utility import util as util_card
from generators.cards.station import station as station_card

arg_map = {
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
	"ccc": community_card,
	"uc": util_card,
	"sc": station_card
}

import sys
def run():
	if len(sys.argv) < 2:
		main(board())
		return
	
	if len(sys.argv) < 2 or sys.argv[1] not in arg_map:
		print("Need argument in " + print_list(arg_map.keys()))
		return
	
	op = sys.argv[1]
	params = sys.argv[2:]
	print(f"op: {op}, params: {params}")
	main(arg_map[op](*params))

if __name__ == '__main__':
	run()