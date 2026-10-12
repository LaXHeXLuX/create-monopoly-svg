def main(canvas):
	file = open("pytest.svg", "w+", encoding="UTF8")
	file.write(str(canvas))
	file.close()
	import clean_svg as clean_svg
	clean_svg.main()

def print_list(arr):
	return f"{{{", ".join(arr)}}}"

from board import board
from property import card
from center import center
from chance_community import chance, community
from corner import go, jail, free_parking, go_to_jail
from port import port
from tax_utility import tax1, tax2, util1, util2

arg_map = {
	"c": card,
	"ce": center,
	"ch": chance,
	"co": community,
	"go": go,
	"j": jail,
	"fp": free_parking,
	"gj": go_to_jail,
	"p": port,
	"t1": tax1,
	"t2": tax2,
	"u1": util1,
	"u2": util2
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