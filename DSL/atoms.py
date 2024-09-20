# This file defines a domain-specific language (DSL) for ARC tasks, generally
# inspired by the approach given in this notebook:
# https://www.kaggle.com/code/zenol42/dsl-and-genetic-algorithm-applied-to-arc
#
# Each DSL function takes as input an image or list of images, which are stored
# in the following dictionary format:
# {'im': image, an np.array, a grid at most 30 x 30, entries from 0 to 9
#  'canv': (w,h) the dimensions of the ambient grid where image lives
#  'pos': (x,y), the position of the image relative to its canvas}
# 
# Each function in our DSL takes a (possibly empty) list of images, and 
# returns a list of images. Thus a 'program' in our DSL entails simply calling
# functions in sequence on the input image. Our final guesses are the first
# two images in the final output list.


import numpy as np
from copy import deepcopy

################################################################################
# Symmetry functions (rotate, reflect, tile, etc)
################################################################################

def identity(x):
	return x

def rotate_cw(x):
	rotated = []
	for grid in x:
		grid_rotated = deepcopy(grid)
		grid_rotated['im'] = np.rot90(grid_rotated['im'], axes = (1,0))
		rotated.append(grid_rotated)
	return rotated

def rotate_ccw(x):
	rotated = []
	for grid in x:
		grid_rotated = deepcopy(grid)
		grid_rotated['im'] = np.rot90(grid_rotated['im'], axes = (0,1))
		rotated.append(grid_rotated)
	return rotated

def rotate_180(x):
	rotated = []
	for grid in x:
		grid_rotated = deepcopy(grid)
		grid_rotated['im'] = np.rot90(grid_rotated['im'], k=2)
		rotated.append(grid_rotated)
	return rotated

# Flips over y-axis
def mirror_h(x):
	mirrored = []
	for grid in x:
		grid_mirrored = deepcopy(grid)
		grid_mirrored['im'] = np.flip(grid_mirrored['im'], axis=1)
		mirrored.append(grid_mirrored)
	return mirrored

# Flips over x-axis
def mirror_v(x):
	mirrored = []
	for grid in x:
		grid_mirrored = deepcopy(grid)
		grid_mirrored['im'] = np.flip(grid_mirrored['im'], axis=0)
		mirrored.append(grid_mirrored)
	return mirrored

# Flips over up-right diagonal
def mirror_ur(x):
	mirrored = []
	for grid in x:
		grid_mirrored = deepcopy(grid)
		grid_mirrored['im'] = np.flip(np.rot90(grid_mirrored['im']), axis=1)
		mirrored.append(grid_mirrored)
	return mirrored

# Flips over down-right diagonal
def mirror_dr(x):
	mirrored = []
	for grid in x:
		grid_mirrored = deepcopy(grid)
		grid_mirrored['im'] = np.flip(np.rot90(grid_mirrored['im']), axis=0)
		mirrored.append(grid_mirrored)
	return mirrored

# Tiles the input rectangularly over the canvas
def tile_rect(x):
	pass

# Mirrors over y-axis, attempts to align, and stacks results
def repair_h_symmetry(x):
	pass

# Mirrors over x-axis, attempts to align, and stacks results
def repair_v_symmetry(x):
	pass

# Rotates by 90, 180, and 270 degrees, and attempts to align, and stacks
# results
def repair_rotational_symmetry(x):
	pass

def center_all(x):
	pass

################################################################################
# Quantitative functions (biggest, smallest, unique, count, sort, etc)
################################################################################

def sort_largest_first(x):
	return sorted(x, key=lambda y:(y['im'] != 0).sum())

def sort_smallest_first(x):
	return sorted(x, key=lambda y:(y['im'] != 0).sum(), reverse=True)

def unique(x):
	result = []
	for grid in x:
		add = True
		for grid2 in result:
			if grid['im'] == grid2['im']:
				add = False
		if add:
			result.append(deepcopy(grid))
	return result

def unique_shape(x):
	result = []
	for grid in x:
		add = True
		for grid2 in result:
			if (grid['im'] != 0) == (grid2['im'] != 0):
				add = False
		if add:
			result.append(deepcopy(grid))
	return result

def non_singletons(x):
	result = []
	for grid in x:
		if (grid['im'] != 0).sum() > 1:
			result.append(deepcopy(grid))
	return result

def sort_most_numerous_first(x):
	pass

def sort_least_numerous_first(x):
	pass


################################################################################
# Logical functions (AND, OR, XOR, etc)
################################################################################

def stack_and(x):
	pass

def stack_or(x):
	pass

def stack_xor(x):
	pass

################################################################################
# Pasting functions (stack, glue along edge, alignment, etc)
################################################################################

def stack(x):
	pass

def stack_first_two(x):
	pass

def align_translate_and_stack(x):
	pass

def align_translate_rotate_and_stack(x):
	pass

def glue_horizontal(x):
	pass

def glue_vertical(x):
	pass

################################################################################
# Recoloring functions
################################################################################


################################################################################
# Physical functions (gravity, collision, etc)
################################################################################

def gravity(x):
	pass

def move_towards_and_collide(x):
	pass

def adjacent(x):
	pass

def extend_h(x):
	pass

def extend_v(x):
	pass

################################################################################
# Geometric functions (get objects, holes, split input into chunks, etc)
################################################################################

def split_by_colors(x):
	pass

def split_by_objects(x):
	pass

def split_by_objects_strict(x):
	pass

def holes(x):
	pass
