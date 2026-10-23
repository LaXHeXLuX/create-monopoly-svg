# Here are constants that define the visual appearance of the SVG objects. 
# Everything is initially set to the standard Monopoly values
# The exception is IMAGE_SCALE, as the images aren't the same as in a standard Monopoly game

# dimensions
BOARD = 490
CORNER = 65
CENTER = BOARD - 2*CORNER
TILE_WIDTH = CENTER / 9

# fonts
FONT = "ITCKabelStd"
FONT_BOLD = "ITCKabelStd-Bold"
FONT_LIGHT = "ITCKabelStd-Book"

# colors
BG_COLOR = "#e8f4ea"
CENTER_COLOR = "#d9f6ff"
ZONE_COLORS = [
	"#955436",
	"#aae0fa",
	"#d93a96",
	"#f7941d",
	"#ed1b24",
	"#fef200",
	"#1fb25a",
	"#0072bb"
]
MAP = "#ceecd3"

# image scales
IMAGE_SCALE = {
	"S": 0.7,
	"CH": 1,
	"CC": 0.8,
	"T1": 0.2,
	"T2": 0.2,
	"U1": 0.8,
	"U2": 0.8,
	"kaart": 1.2
}
