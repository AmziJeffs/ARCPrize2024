import timeout_decorator
import sys

# Catches syntax warnings in solver defs as errors, so that the solvers don't bother
# trying to execute.
import warnings
warnings.filterwarnings("error")

sys.path.insert(0, '../DSL')
from solver_class import Solver


def width_score(actual, expected):
	"""
	Difference in width, normalized by denominator that is max difference with
	expected among all widths in range [1, 30]
	"""
	return abs(len(actual[0]) - len(expected[0])) / max(len(expected[0]) - 1, 30 - len(expected[0]))


def height_score(actual, expected):
	"""
	Difference in height, normalized by denominator that is max difference with
	expected among all heights in range [1, 30]
	"""
	return abs(len(actual) - len(expected)) / max(len(expected) - 1, 30 - len(expected))


def palette_score(actual, expected):
	"""
	Symmetric difference in palettes, normalized by union of palettes
	"""
	actual_vals = set([a for row in actual for a in row])
	expected_vals = set([a for row in expected for a in row])
	return len(actual_vals.symmetric_difference(expected_vals)) / len(actual_vals.union(expected_vals))


def activated_score(actual, expected):
	"""
	Number of pixels in actual that are incorrectly activated, normalized by
	total pixels in actual 
	"""
	actual_activated = set([(r,c) for r in range(len(actual)) for c in range(len(actual[0])) if actual[r][c] != 0])
	expected_activated = set([(r,c) for r in range(len(expected)) for c in range(len(expected[0])) if expected[r][c] != 0])
	if len(actual_activated) == 0:
		return 1.0
	else:
		return len(actual_activated.difference(expected_activated)) / len(actual_activated)


def exact_match_score(actual, expected):
	"""
	Number of cells that do not exactly match between grids, normalized by
	union of all entries over both grids
	"""
	actual_entries = set([(actual[r][c], (r,c)) for r in range(len(actual)) for c in range(len(actual[0]))])
	expected_entries = set([(expected[r][c], (r,c)) for r in range(len(expected)) for c in range(len(expected[0]))])
	return len(actual_entries.symmetric_difference(expected_entries)) / len(actual_entries.union(expected_entries))


scoring_functions = {
	'width': width_score,
	'height': height_score,
	'palette': palette_score,
	'activated': activated_score,
	'exact_match_correct': exact_match_score, 
}


def is_valid_grid(G, enforce_30_x_30 = True, enforce_palette = False):
	"""
	Verify that a grid is indeed a tuple of tuples of ints from 0 to 9,
	with all rows having same length and dimensions at most 30 x 30.

	By default, enforce_palette is False to speed up runtime.
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
	if enforce_palette:
		entries = set([a for a in row for row in G])
		if not len(entries.difference(set([0,1,2,3,4,5,6,7,8,9]))) == 0:
			return False

	return True


def score_solvers_vs_tasks(solvers: list[Solver],
						   in_out_pairs: list, # List of dicts {'input': in_grid, 'output': out_grid}
						   scoring_functions: dict, # {scoring_function_name, scoring_function}
						   solver_timeout:float = None, # Maximum time to try each solver
						   ) -> dict:
	results = []

	# Create a function for applying solvers to grids, possibly using timeout
	def apply_solver(solver, G):
		return solver(G)
	if solver_timeout:
		@timeout_decorator.timeout(solver_timeout)
		def apply_solver(solver, G):
			return solver(G)

	# Run solvers
	# TODO: Parallelize this
	for solver in solvers:
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
				total_score += sum(scores) / len(scores)
			else:
				solver_failed = True

		total_score = total_score / len(in_out_pairs)

		if solver_failed:
			total_score = 1.0
		
		results.append((total_score, solver))

	return results
