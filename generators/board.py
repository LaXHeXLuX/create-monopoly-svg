from generators.conf import BG_COLOR, CENTER, CORNER, TILE_WIDTH, BOARD
from generators.utils import rect, canvas, position_element
from generators.corner import corners
from generators.center import center
from generators.layout import layout
from generators.tiles.tile import tile

rowElements = layout()

def row(index: int):
	row = canvas(CENTER, CORNER)
	for i in range(9):
		el = tile(rowElements[9*index + i])
		el.x = CENTER - (i+1)*TILE_WIDTH
		row.elements.append(el)
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