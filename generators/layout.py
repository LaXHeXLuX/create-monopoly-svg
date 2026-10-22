ROW_COUNT = 4
ROW_SIZE = 9
def layout():
	layout = [None] * ROW_SIZE * ROW_COUNT

	layout[10] = "U1"
	layout[25] = "U2"
	layout[3] = "T1"
	layout[34] = "T2"
	
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
