import timeout_decorator

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
	actual_activated = set([(r,c) for r in range(len(actual)) for c in range(len(actual[0])) if actual[r][c] != 0])
	expected_activated = set([(r,c) for r in range(len(expected)) for c in range(len(expected[0])) if expected[r][c] != 0])
	return len(actual_activated.difference(expected_activated))


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


def is_valid_grid(G, enforce_30_x_30 = True):
	"""
	Verify that a grid is indeed a tuple of tuples of ints from 0 to 9,
	with all rows having same length and dimensions at most 30 x 30
	"""

	# Verify G is a nonempty tuple
	if not isinstance(G, tuple):
		return False
	if len(G) == 0:
		return False

	# Verify rows are tuples containing ints 0 to 9
	for row in G:
		if not isinstance(row, tuple):
			return False

	# Check rows have same lengths
	if len(set([len(row) for row in G])) > 1:
		return False

	# Check grid is at most 30 x 30
	if enforce_30_x_30:
		if not len(G) <= 30:
			return False
		if not len(G[0]) <= 30:
			return False

	# Check entries are 0 to 9
	entries = set([a for a in row for row in G])
	if not len(entries.difference(set([0,1,2,3,4,5,6,7,8,9]))) == 0:
		return False

	return True


def score_solvers_vs_tasks(solvers: dict, # {solver_name: solver_function}
						   in_out_pairs: list, # List of dicts {'input': in_grid, 'output': out_grid}
						   scoring_functions: dict, # {scoring_function_name, scoring_function}
						   reduction:str = 'sum', # After scoring a function on all pairs, how to combine scores
						   solver_timeout:float = None, # Maximum time to try each solver
						   ) -> dict:
	results = {solver_name: None for solver_name in solvers.keys()}

	@timeout_decorator.timeout(solver_timeout)
	def apply_solver(solver, G):
		return solver(G)

	for solver_name, solver in solvers.items():
		total_score = 0
		solver_failed = False
		for pair in in_out_pairs:
			in_grid = pair['input']
			out_expected = pair['output']
			out_actual = None
			try:
				# Note: We can get an exception for two reasons here.
				# Either the solver breaks on the input, or the solver times out.
				out_actual = apply_solver(solver, in_grid)
			except:
				solver_failed = True
			if is_valid_grid(out_actual):
				scores = [scoring_func(out_actual, out_expected) for scoring_func in scoring_functions.values()]
				if reduction == 'sum':
					total_score += sum(scores)
				else:
					raise Exception(f"Scoring reduction '{reduction}' not implemented.")
			else:
				solver_failed = True

		if not solver_failed:
			results[solver_name] = total_score

	return results
