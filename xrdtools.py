# coding: utf-8

import argparse
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


def parse_data(filename, colnum, sep=':', savecsv=False):
    '''
    Parse data from `filename` to pandas DataFrame

    Args:
        filename : str
            name of the data file
        colnum : int
            number of the column with the data to plot
        sep : str
            value separator in the file
        savecsv : bool
            a flag to mark if a csv file should be save with parsed data

    Returns:
        matrix : array_like

    '''

    # read the data from file
    df = pd.read_csv(filename, sep=sep, header=None, comment='#')

    # extract indices from the first column in the file
    ind = df.iloc[:, 0].str.split('_', expand=True)
    ind.rename(columns={2: 'ind_x', 3: 'ind_y'}, inplace=True)
    ind.loc[:, 'ind_x'] = ind['ind_x'].astype(int)
    ind.loc[:, 'ind_y'] = ind['ind_y'].astype(int)

    # merged the indices with the main df
    df = df.join(ind[['ind_x', 'ind_y']])

    # pivot the dataframe to
    matrix = df.pivot(index='ind_x', columns='ind_y', values=colnum)

    if savecsv:
        mname = os.path.splitext(os.path.basename(filename))[0] + '_col-{0:d}'.format(colnum) + '.csv'
        np.savetxt(mname, matrix)

    return matrix


def heatmap(matrix, size=10, cmap='viridis', show_colorbar=True):
    '''
    Create a heatmap form a matrix of data

    Args:
        matrix : array_like
            Matrix to be colormapped
        size : int
            Size of the plot in inches

    '''

    plt.figure(figsize=(size, size))
    plt.pcolor(matrix, cmap=cmap)

    ax = plt.gca()
    ax.set_aspect('equal')

    if show_colorbar:
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.2)
        plt.colorbar(cax=cax)

    plt.tight_layout()
    plt.show()


def disk_mask(array, x0, y0, radius):
    '''
    Create a circular mask for a rectangular array

    Args:
        array : array_like
            array with the data
        x0, y0 : int
            coordinates of the origin of the circle
        radius : int
            radius of the circle

    Returns:
        mask : array_like

    '''

    xdim, ydim = array.shape
    y, x = np.ogrid[-x0:xdim - x0, -y0:ydim - y0]
    mask = x * x + y * y < radius**2
    return mask


def cli():
    'CLI interface'

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='name of the data file')
    parser.add_argument('colnum', type=int, help='column number (starting from 0)')
    parser.add_argument('--cmap', default='viridis', help='matplotlib colormap name, default is "viridis"')
    parser.add_argument('--sep', default=':', help='separator for columns in data file, default is ":"')
    parser.add_argument('--plotsize', type=int, default=10, help='size of the plot in inches')
    parser.add_argument('--savecsv', action='store_true', help='save the reshaped matrix as csv')
    parser.add_argument('--hide_cbar', action='store_false', help='do not show the colorbar on plots')

    args = parser.parse_args()

    m = parse_data(args.filename, args.colnum, sep=args.sep, savecsv=args.savecsv)
    heatmap(m, args.plotsize, cmap=args.cmap, show_colorbar=args.hide_cbar)


if __name__ == '__main__':

    cli()
