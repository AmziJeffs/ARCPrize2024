# This file defines a domain-specific language (DSL) for ARC tasks, generally
# inspired by the approach given in this notebook:
# https://www.kaggle.com/code/zenol42/dsl-and-genetic-algorithm-applied-to-arc
#
# Each DSL function takes as input an image or list of images, which are stored
# in the following dictionary format:
# {'image': image, an np.array, a grid at most 30 x 30, entries from 0 to 9
#  'canvas': (w,h) the dimensions of the ambient grid where image lives
#  'pos': (x,y), the position of the image relative to its canvas}
# 
# Each function in our DSL takes a (possibly empty) list of images, and 
# returns a list of images. Thus a 'program' in our DSL entails simply calling
# functions in sequence on the input image. Our final guesses are the first
# two images in the final output list.


import numpy as np

################################################################################
# Symmetry functions (rotate, reflect, tile, etc)
################################################################################

def identity(x):
	return x

def rotate_cw(x):
	pass

def rotate_ccw(x):
	pass

def rotate_180(x):
	pass

def mirror_h(x):
	pass

def mirror_v(x):
	pass

def mirror_ur(x):
	pass

def mirror_dr(x):
	pass

def tile_rect(x):
	pass

def repair_h_symmetry(x):
	pass

def repair_v_symmetry(x):
	pass

def repair_rotational_symmetry(x):
	pass

def center_all(x):
	pass

################################################################################
# Quantitative functions (biggest, smallest, unique, count, sort, etc)
################################################################################

def sort_largest_first(x):
	pass

def sort_smallest_first(x):
	pass

def sort_most_numerous_first(x):
	pass

def sort_least_numerous_first(x):
	pass

def sort_by_colors(x):
	pass

def unique(x):
	pass

def non_singletons(x):
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
