# coding: utf-8

import argparse
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


def create_matrix(filename, colnum, rank, sep=':', savecsv=False):

    df = pd.read_csv(filename, sep=sep, header=None, comment='#')
    matrix = df.iloc[:, [colnum]].values.reshape(rank, rank)

    if savecsv:
        mname = os.path.splitext(os.path.basename(filename))[0] + '_col-{0:d}'.format(colnum) + '.csv'
        np.savetxt(mname, matrix)

    return matrix

def heatmap(matrix, size, cmap='viridis', show_colorbar=True):
    '''
    Args:
        matrix : array_like
            Matrix to be colormapped
        size : int
            Size of the plot in inches
    '''

    plt.figure(figsize=(size, size))
    plt.pcolor(m, cmap=cmap)

    ax = plt.gca()
    ax.set_aspect('equal')

    if show_colorbar:
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.2)
        plt.colorbar(cax=cax)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='name of the data file')
    parser.add_argument('colnum', type=int, help='column number (starting from 0)')
    parser.add_argument('rank', type=int, help='rank of the matrix to be formed')
    parser.add_argument('--cmap', default='viridis', help='matplotlib colormap name, default is "viridis"')
    parser.add_argument('--sep', default=':', help='separator for columns in data file, default is ":"')
    parser.add_argument('--plotsize', type=int, default=10, help='size of the plot in inches')
    parser.add_argument('--savecsv', action='store_true', help='save the reshaped matrix as csv')
    parser.add_argument('--hide_cbar', action='store_false', help='do not show the colorbar on plots')

    args = parser.parse_args()

    m = create_matrix(args.filename, args.colnum, args.rank, sep=args.sep, savecsv=args.savecsv)
    heatmap(m, args.plotsize, cmap=args.cmap, show_colorbar=args.hide_cbar)

