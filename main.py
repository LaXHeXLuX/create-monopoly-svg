def main(canvas):
	file = open("pytest.svg", "w+", encoding="UTF8")
	file.write(str(canvas))
	file.close()
	import generators.clean_svg as clean_svg
	clean_svg.main()

def print_list(arr):
	return f"{{{", ".join(arr)}}}"

from generators.board import board
from generators.tiles.property import property
from generators.center import center
from generators.tiles.chance_community import chance, community
from generators.corner import go, jail, free_parking, go_to_jail
from generators.tiles.station import station
from generators.tiles.tax_utility import tax, util

arg_map = {
	"p": property,
	"ce": center,
	"ch": chance,
	"cc": community,
	"go": go,
	"j": jail,
	"fp": free_parking,
	"gj": go_to_jail,
	"s": station,
	"t1": tax(1),
	"t2": tax(2),
	"u1": util(1),
	"u2": util(2)
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