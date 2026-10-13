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
	position_element(corners[0], cx=BOARD-CORNER, cy=BOARD-CORNER, rotation=0),
	position_element(row(0), cx=CORNER, cy=BOARD-CORNER, rotation=0),
	position_element(corners[1], cx=CORNER, cy=BOARD-CORNER, rotation=90),
	position_element(row(1), cx=CORNER, cy=CORNER, rotation=90),
	position_element(corners[2], cx=CORNER, cy=CORNER, rotation=180),
	position_element(row(2), cx=BOARD-CORNER, cy=CORNER, rotation=180),
	position_element(corners[3], cx=BOARD-CORNER, cy=CORNER, rotation=270),
	position_element(row(3), cx=BOARD-CORNER, cy=BOARD-CORNER, rotation=270)
])

def board():
	board = canvas(BOARD, BOARD)
	board.viewBox = f"0 0 {BOARD} {BOARD}"
	board.elements.extend([
		boardBase, 
		position_element(center(), cx=CORNER, cy=CORNER),
		boardRows
	])
	return board