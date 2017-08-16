#! /usr/bin/env python3
import argparse, os, sys

from PyQt5 import QtWidgets

from data    import Packet
from io      import Reader
from log     import Recorder
from modules import BaseModule
from ui      import DabbleViewer


if __name__ == '__main__':
    """Dabble with some things."""
    #cli = argparse.ArgumentParser()
    #cli.add_argument('--dir', type=str)

    #args = cli.parse_args()

    #if not args.dir:
    #    print('You must specify a directory where there is data.')
    #    print('usage: dabble --dir [directory]')
    #    exit(2)

    # Make a QApplication.
    qapp = QtWidgets.QApplication(sys.argv)

    # Open up a view on the chosen directory.
    ui = dabbleview(directory)

    sys.exit(qapp.exec_())

