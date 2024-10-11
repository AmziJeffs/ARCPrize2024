import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import colors

import os
import json
from pathlib import Path

ARC_CMAP = colors.ListedColormap(
    ['#000000', '#0074D9','#FF4136','#2ECC40','#FFDC00',
     '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25'])
ARC_NORM = colors.Normalize(vmin=0, vmax=9)

def plot_one(ax, task, i, train_or_test, input_or_output):
    """
    Plot a single grid onto an axis
    """
    input_matrix = task[train_or_test][i][input_or_output]
    ax.imshow(input_matrix, cmap=ARC_CMAP, norm=ARC_NORM)
    ax.grid(True, which='both', color='lightgrey', linewidth=0.5)    
    ax.set_yticks([x-0.5 for x in range(1+len(input_matrix))])
    ax.set_xticks([x-0.5 for x in range(1+len(input_matrix[0]))])     
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_title(train_or_test + ' ' + input_or_output)
    

def plot_task(task):
    """
    Plot the input / output pairs for a given task
    """    
    num_train = len(task['train'])
    fig, axs = plt.subplots(2, num_train, figsize = (3 * num_train, 3 * 2))
    for i in range(num_train):
        plot_one(axs[0,i], task, i, 'train', 'input')
        plot_one(axs[1,i], task, i, 'train', 'output')
        
    num_test = len(task['test'])
    fig, axs = plt.subplots(2, num_test, figsize = (3 * num_test, 3 * 2))
    if num_test == 1: 
        plot_one(axs[0], task, 0, 'test', 'input')
        plot_one(axs[1], task, 0, 'test', 'output')     
    else:
        for i in range(num_test):      
            plot_one(axs[0, i], task, i, 'test', 'input')
            plot_one(axs[1, i], task, i, 'test', 'output')  
    plt.tight_layout()
    plt.show()


def show_grid(grid):
    """
    Visualize a single grid
    """    
    fig, ax = plt.subplots(figsize = (4, 4))
    ax.imshow(grid, cmap=ARC_CMAP, norm=ARC_NORM)
    ax.grid(True, which='both', color='lightgrey', linewidth=0.5)    
    ax.set_yticks([x-0.5 for x in range(1+len(grid))])
    ax.set_xticks([x-0.5 for x in range(1+len(grid[0]))])     
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.show()