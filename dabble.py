#! /usr/bin/env python3
import argparse, os, sys

from PyQt5 import QtWidgets

from io      import *
from data    import *
from log     import *
from modules import *
from ui      import *


if __name__ == '__main__':
    """Dabble with some things."""
    cli = argparse.ArgumentParser()
    cli.add_argument('--dir', type=str)

    args = cli.parse_args()

    if not args.dir:
        print('You must specify a directory where there is data.')
        print('usage: dabble --dir [directory]')
        exit(2)

    # Make a QApplication.
    qapp = QtWidgets.QApplication(sys.argv)

    # Open up a view on the chosen directory.
    directory = args.dir
    ui = DabbleView.DabbleView(directory)

    sys.exit(qapp.exec_())

