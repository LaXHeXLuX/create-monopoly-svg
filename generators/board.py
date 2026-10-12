from generators.conf import BG_COLOR, CENTER, CORNER, TILE_WIDTH, BOARD
from generators.utils import rect, canvas, position_element
from generators.tiles.property import property
from generators.tiles.chance_community import chance, community
from generators.tiles.port import port
from generators.tiles.tax_utility import tax1, tax2, util1, util2
from generators.corner import corners
from generators.center import center

rowElements = [
	[
		property("EMMASTE", 1, 60),
		community(),
		property("TOHVRI", 1, 60),
		tax1(),
		port("SÕRU"),
		property("NURSTE", 2, 100),
		chance(),
		property("MÄNSPE", 2, 100),
		property("ÕNGU", 2, 120)
	],
	[
		property("KÕPU", 3, 140),
		util1(),
		property("LUIDJA", 3, 140),
		property("KÕRGESSAARE", 3, 160),
		port("KALANA"),
		property("LAUKA", 4, 180),
		community(),
		property("MALVASTE", 4, 180),
		property("TAHKUNA", 4, 200)
	],
	[
		property("KÄRDLA", 5, 220),
		chance(),
		property("TUBALA", 5, 220),
		property("PALADE", 5, 240),
		port("HELTERMAA"),
		property("HELLAMAA", 6, 260),
		property("SUUREMÕISA", 6, 260),
		util2(),
		property("KASSARI", 6, 280)
	],
	[
		property("KÄINA", 7, 300),
		property("MÄELTSE", 7, 300),
		community(),
		property("JAUSA", 7, 320),
		port("ORJAKU"),
		chance(),
		property("MÄNNAMAA", 8, 350),
		tax2(),
		property("LELU", 8, 400)
	]
]

def row(index: int):
	row = canvas(CENTER, CORNER)
	x = CENTER - TILE_WIDTH
	for el in rowElements[index]:
		el.x = x
		row.elements.append(el)
		x -= TILE_WIDTH
	return row

boardBase = canvas(BOARD, BOARD)
boardBase.elements.append(rect(BG_COLOR, stroke=False))

boardRows = canvas(BOARD, BOARD)
boardRows.elements.extend([
	position_element(corners[0], BOARD-CORNER, BOARD-CORNER, 0),
	position_element(row(0), CORNER, BOARD-CORNER, 0),
	position_element(corners[1], 0, BOARD-CORNER, 1),
	position_element(row(1), CORNER, CORNER, 1, False),
	position_element(corners[2], 0, 0, 2),
	position_element(row(2), BOARD-CORNER, CORNER, 2, False),
	position_element(corners[3], BOARD-CORNER, 0, 3),
	position_element(row(3), BOARD-CORNER, BOARD-CORNER, 3, False)
])

def board():
	board = canvas(BOARD, BOARD)
	board.viewBox = f"0 0 {BOARD} {BOARD}"
	board.elements.extend([
		boardBase, 
		position_element(center(), CORNER, CORNER, 0), 
		boardRows
	])
	return board