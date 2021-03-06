from PyQt5 import QtGui, QtWidgets


class ModuleList(QtWidgets.QListView):
    """This is a widget to hold lists of modules duh."""
    def __init__(self, parent):
        super(ModuleList, self).__init__(parent)
        self.layout = QtWidgets.QGridLayout(self)
        self.setWindowTitle('module list')
        self.model = QtGui.QStandardItemModel(self)
        self.setMinimumSize(200, 300)

    def makeAddButton(self):
        button = QtWidgets.QPushButton('+', self)
        return button

    def addModule(self):
        pass

