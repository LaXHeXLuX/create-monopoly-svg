from conf import BG_COLOR, CENTER, CORNER, TILE_WIDTH, BOARD
from utils import rect, canvas, position_element
from property import card
from chance_community import chance, community
from port import port
from tax_utility import tax1, tax2, util1, util2
from corner import corners
from center import center

rowElements = [
	[
		card("EMMASTE", 1, 60),
		community(),
		card("TOHVRI", 1, 60),
		tax1(),
		port("SÕRU"),
		card("NURSTE", 2, 100),
		chance(),
		card("MÄNSPE", 2, 100),
		card("ÕNGU", 2, 120)
	],
	[
		card("KÕPU", 3, 140),
		util1(),
		card("LUIDJA", 3, 140),
		card("KÕRGESSAARE", 3, 160),
		port("KALANA"),
		card("LAUKA", 4, 180),
		community(),
		card("MALVASTE", 4, 180),
		card("TAHKUNA", 4, 200)
	],
	[
		card("KÄRDLA", 5, 220),
		chance(),
		card("TUBALA", 5, 220),
		card("PALADE", 5, 240),
		port("HELTERMAA"),
		card("HELLAMAA", 6, 260),
		card("SUUREMÕISA", 6, 260),
		util2(),
		card("KASSARI", 6, 280)
	],
	[
		card("KÄINA", 7, 300),
		card("MÄELTSE", 7, 300),
		community(),
		card("JAUSA", 7, 320),
		port("ORJAKU"),
		chance(),
		card("MÄNNAMAA", 8, 350),
		tax2(),
		card("LELU", 8, 400)
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