# Here are constants that define the visual appearance of the SVG objects. 
# Everything is initially set to the standard Monopoly values
# The exception is IMAGE_SCALE, as the images aren't the same as in a standard Monopoly game

from conf.game import ROW_SIZE
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent

# dimensions
BOARD = 490
PADDING = 5
CORNER = 65
CENTER = BOARD - 2*CORNER
TILE_WIDTH = CENTER / ROW_SIZE

# fonts
FONTS = {
	-1: "ITCKabelStd-Book",
	0: "ITCKabelStd",
	1: "ITCKabelStd-Bold"
}
FONT_FILES = {
	-1: "ITCKabelStdBook.TTF",
	0: "ITCKabelStdMedium.TTF",
	1: "ITCKabelStdBold.TTF"
}
FONT_DIR = ROOT / "fonts"


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
CH_BG = "#ffa4a4"
CC_BG = "#f9e48e"
HOUSE_COLOR = "#1fb25a"
HOTEL_COLOR = "#ff5353"
JAIL_COLOR = "#ffa500"

# image scales
IMAGE_SCALE = {
	"S": 0.7,
	"CH": 1,
	"CC": 0.8,
	"T0": 0.2,
	"T1": 0.2,
	"U0": 0.7,
	"U1": 0.6,
	"GO": 0.6,
	"FP": 0.45,
	"GTJ": 0.45,
	"center": 1.2
}
