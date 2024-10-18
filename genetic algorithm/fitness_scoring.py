def width_score(actual, expected):
	return abs(len(actual[0]) - len(expected[0]))


def height_score(actual, expected):
	return abs(len(actual) - len(expected))


def palette_score(actual, expected):
	actual_vals = set([a for row in actual for a in row])
	expected_vals = set([a for row in expected for a in row])
	return len(actual_vals.symmetric_difference(expected_vals))


def activated_score(actual, expected):
	"""
	Number of pixels that are incorrectly activated
	"""
	h = min(len(actual), len(expected))
	w = min(len(actual[0]), len(expected[0]))
	score = 0
	for r in range(h):
		for c in range(w):
			if actual[r][c] == 0 and expected[r][c] != 0:
				score += 1
			if actual[r][c] != 0 and expected[r][c] == 0:
				score += 1
	return score


def exact_match_score(actual, expected):
	"""
	Number of cells that do not exactly match between grids
	"""
	actual_entries = set([(actual[r][c], (r,c)) for r in range(len(actual)) for c in range(len(actual[0]))])
	expected_entries = set([(expected[r][c], (r,c)) for r in range(len(expected)) for c in range(len(expected[0]))])
	return len(actual_entries.symmetric_difference(expected_entries))



scoring_functions = {
	'width': width_score,
	'height': height_score,
	'palette': palette_score,
	'activated': activated_score,
	'exact_match_correct': exact_match_score, 
}
