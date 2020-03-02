# Utilities for plotting and saving

import numpy as np
from matplotlib import pyplot as plt
from os.path import dirname, abspath

import mib # project-specific library

# These should define a standard look for plots, at least with default values that 
# are used frequently. That way we can easily change that look for all the graphs in the book

def set_axes(axes, xlabel, ylabel, legend, xlim, ylim, xscale, yscale, 
             xticks, yticks, yhide, yrot, yzero, grid, equal):
    """Set the axes for matplotlib."""
    axes.set_xscale(xscale)
    axes.set_yscale(yscale)
    if xlim:
        axes.set_xlim(xlim)
    else:
        axes.set_xlim(auto=True)
    if ylim:
        axes.set_ylim(ylim)
    else:
        axes.set_ylim(auto=True)
    if grid:
        axes.grid()
    if equal:
        axes.set_aspect(aspect='equal')
    if ylabel:
        if yrot:
            axes.set_ylabel(ylabel, fontsize=12, rotation=0, labelpad=15)
        else:
            axes.set_ylabel(ylabel, fontsize=12)
    if xlabel:
        axes.set_xlabel(xlabel, fontsize=12)
    axes.get_yaxis().set_visible(not yhide)
    if yzero:
        axes.axhline(color='black', linewidth=0.5)
    axes.tick_params(axis = 'both', which = 'major', labelsize = 10)
    axes.tick_params(axis = 'both', which = 'minor', labelsize = 9)
    if xticks:
        axes.set_xticks(xticks,[]); # no minor ticks
    if yticks:
        axes.set_yticks(yticks,[]); # no minor ticks
    if legend:
        axes.legend(legend)
    plt.draw()
    #     To change the font and control the fontsize, can use some of these commands:
    #     axes.set_xlabel(xlabel, fontname='Arial', fontsize = 12)
    #     axes.set_ylabel(ylabel, fontname='Arial', fontsize = 12)
    #     axes.tick_params(axis = 'both', which = 'major', labelsize = 10)
    #     axes.tick_params(axis = 'both', which = 'minor', labelsize = 9)
    #     plt.yticks(fontname = "Arial")
    #     plt.xticks(fontname = "Arial")
    #     if legend:
    #         axes.legend(legend, prop={"size":12, "family":'Arial'})
    #     For options on legend placement see https://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot
        
def plot(X, Y=None, xlabel=None, ylabel=None, legend=[], 
         xlim=None, ylim=None, xscale='linear', yscale='linear',
         xticks=None, yticks=None, yhide=False, yrot=False, yzero=False, 
         fmts=['g-', 'm--', 'b-.', 'r:'], linewidth=2, markersize=5, 
         grid=False, equal=False, figsize=(5,3), axes=None):
    """
    Plot data points.
    X: an array or list of arrays
    Y: an array or list of arrays
    If Y exists then those values are plotted vs the X values
    If Y doesn't exist the X values are plotted
    xlabel, ylabel: axis labels
    legend: list of labels for each Y series
    xlim, ylim: [low,high] list of limits for the 2 axes 
    xscale, yscale: 'linear' or 'log'
    xticks, yticks: list of locations for tick marks, or None for auto ticks
    yhide: hide the y axis?
    yrot: rotate the yaxis label to horizontal?
    yzero: zero line for the y-axis?
    fmts: a list of format strings to be applied to successive Y-series
    linewidth, markersize: obvious
    grid: draw a grid?
    equal: use equal aspect ratio, i.e. same scale per unit on x and y axis?
    figsize: (h,v) in inches
    axes: pre-existing axes where to draw the plot
    """
    
    if not axes: # start a new figure
        fig = plt.figure(figsize=figsize)
        axes = plt.gca()
    
    def has_one_axis(X): # Return True if X (ndarray or list) has 1 axis
        return (hasattr(X, "ndim") and X.ndim == 1 or isinstance(X, list)
                and not hasattr(X[0], "__len__"))

    if has_one_axis(X):
        X = [X]
    if Y is None:
        X, Y = [[]] * len(X), X
    elif has_one_axis(Y):
        Y = [Y]
    if len(X) != len(Y):
        X = X * len(Y)
    # axes.cla() # clears these axes
    for x, y, fmt in zip(X, Y, fmts):
        if len(x):
            axes.plot(x, y, fmt, linewidth=linewidth, markersize=markersize)
        else:
            axes.plot(y, fmt, linewidth=linewidth, markersize=markersize)
    set_axes(axes, xlabel, ylabel, legend, xlim, ylim, xscale, yscale, 
             xticks, yticks, yhide, yrot, yzero, grid, equal)
    plt.tight_layout()

    return axes # useful if we started a new figure

def save_img(imgname):
    """
    Saves the current plot to the img/ folder in the project directory
    """
    projectpath = dirname(dirname(abspath(mib.__file__)))
    plt.savefig(projectpath+'/img/'+imgname, bbox_inches = "tight") 

def test_plot():
    x = np.arange(-10,10,.01)
    t = [0.1,0.3,1,3,10]
    y = [np.exp(-x**2/(4*ti))/np.sqrt(4*np.pi*ti) for ti in t]
    plot (x,y,fmts=['g-','m--','b-.','r:','k-'],linewidth=1,
        xlabel='Distance',ylabel='Concentration',yzero=True,
        legend=['t=0.1','0.3','1','3','10'],xticks=[-10,-5,-1,0,1,5,10])
    
    
