from conf.ui import BG_COLOR, CENTER, CORNER, TILE_WIDTH, BOARD, PADDING
from generators.utils import rect, canvas, position_element
from generators.corner import corners
from generators.center import center
from conf.game import LAYOUT, ROW_SIZE
from generators.tiles.tile import tile

def row(index: int):
	row = canvas(CENTER, CORNER)
	for i in range(ROW_SIZE):
		el = tile(LAYOUT[ROW_SIZE*index + i])
		el.x = CENTER - (i+1)*TILE_WIDTH
		row.elements.append(el)
	return row

boardBase = canvas(BOARD, BOARD)
boardBase.elements.append(rect(BG_COLOR, stroke=0))

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

def board_with_padding():
	size = BOARD + 2*PADDING
	c = canvas(size, size, base=True)
	c.elements.append(rect(fill=BG_COLOR))
	b = board()
	b.x, b.y = PADDING, PADDING
	c.elements.append(b)
	return c