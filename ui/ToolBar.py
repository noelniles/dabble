from PyQt5 import QtCore, QtWidgets


class ToolBar(QtWidgets.QToolBar):
    addModuleSignal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(ToolBar, self).__init__(parent)
        addModuleTool = parent.addToolBar('+')

        addModuleAction = QtWidgets.QAction('Add Module', self)
        self.addModuleSignal.connect(self.addModuleAction)
        addModuleTool.addAction(addModuleAction)


    def addModuleAction(self):
        self.addModuleSignal.emit()
        print('adding module')
