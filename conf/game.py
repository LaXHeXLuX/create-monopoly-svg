# Here are constants that define the functional elements of the game, such as house prices, board layout, etc. 
# Everything is initially set to the standard Monopoly rules

ROW_COUNT = 4
ROW_SIZE = 9
def layout():
	layout = [None] * ROW_SIZE * ROW_COUNT

	layout[10] = "U0"
	layout[25] = "U1"
	layout[3] = "T0"
	layout[34] = "T1"
	
	for i in range(ROW_COUNT):
		layout[ROW_SIZE*i + ROW_SIZE//2] = f"S{i}"

	for i in [1, 15, 29]:
		layout[i] = "CC"

	for i in [6, 19, 32]:
		layout[i] = "CH"

	layout[0] = "P11"
	layout[2] = "P12"

	pi = 2
	ii = 1
	for i in range(len(layout)):
		if (layout[i] != None): continue

		layout[i] = f"P{pi}{ii}"

		ii += 1
		if (ii > 3):
			ii = 1
			pi += 1

	return layout
LAYOUT = layout()

def property_costs():
	property_costs = [[60, 60]]

	for zone in range(1, 7):
		property_costs.append([])
		for i in range(3):
			price = 60 + zone*40 + (i // 2)*20
			property_costs[zone].append(price)

	property_costs.append([350, 400])

	return property_costs
PROPERTY_COSTS = property_costs()

STATION_COST = 200
STATION_RENTS = [25 * 2**i for i in range(ROW_COUNT)]
UTILITY_COSTS = [150, 150]
TAX_COSTS = [200, 100]

PROPERTY_RENTS = [
	[
		[2, 10, 30, 90, 160, 250],
		[4, 20, 60, 180, 320, 450]
	],
	[
		[6, 30, 90, 270, 400, 550],
		[6, 30, 90, 270, 400, 550],
		[8, 40, 100, 300, 450, 600]
	],
	[
		[10, 50, 150, 450, 625, 750],
		[10, 50, 150, 450, 625, 750],
		[12, 60, 180, 500, 700, 900]
	],
	[
		[14, 70, 200, 550, 750, 950],
		[14, 70, 200, 550, 750, 950],
		[16, 80, 220, 600, 800, 1000]
	],
	[
		[18, 90, 250, 700, 875, 1050],
		[18, 90, 250, 700, 875, 1050],
		[20, 100, 300, 750, 925, 1100]
	],
	[
		[22, 110, 330, 800, 975, 1150],
		[22, 110, 330, 800, 975, 1150],
		[24, 120, 360, 850, 1025, 1200]
	],
	[
		[26, 130, 390, 900, 1100, 1275],
		[26, 130, 390, 900, 1100, 1275],
		[28, 150, 450, 1000, 1200, 1400]
	],
	[
		[35, 175, 500, 1100, 1300, 1500],
		[50, 200, 600, 1400, 1700, 2000]
	]
]
FULL_COLOR_SET_MULTIPLIER = 2
HOUSE_PRICES = [50, 100, 150, 200]
HOTEL_PRICES = [50, 100, 150, 200]

GO_MONEY = 200

PAWN_VALUE = 0.5
PAWN_COEFFICIENT = 0.05