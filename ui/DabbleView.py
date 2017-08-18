from PyQt5 import QtCore, QtGui, QtWidgets

from ui import ModuleList
from ui import ToolBar

class DabbleView(QtWidgets.QMainWindow):
    """Dabble user interface."""
    def __init__(self, directory, parent=None):
        super(DabbleView, self).__init__(parent)
        # Set up the layout.
        self.layout = QtWidgets.QGridLayout()

        # Keep a copy of the user's chosen directory.
        self.directory = directory

        # Center the main window and resize it to 90% of the available screen size.
        self.centerAndResize()

        # Make the menu on the top of the window.
        self.makeTopMenu()

        # Keep a list of the OpenCV modules.
        self.modules = None # intially we have no modules
        self.modules_list = ModuleList.ModuleList(self)

        # And add them to the GUI window.
        self.layout.addWidget(self.modules_list, 0, 1)

        # Add it to the scene.
        self.graphics = self.makeGraphicsDisplay()
        self.scene.addItem(self.graphics)

        # Make a view.
        self.view  = QtWidgets.QGraphicsView(self.scene, self)

        # Make a grid to hold all the stuff.
        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.modules_list, 0, 0, -1, 1)
        self.grid.addWidget(self.view, 0, 1)

        central = QtWidgets.QWidget()
        central.setLayout(self.grid)
        # Set the central widget to the grid.
        self.setCentralWidget(central)

        # Add the tool bar.
        self.tb = ToolBar.ToolBar(self)
        self.tb.addModuleSignal.connect(self.addModule)
        # Finally show the GUI.
        self.show()

    def addModule(self):
        print('got the signal')

    def centerAndResize(self):
        """Center the window and use 90% of the screen."""
        availableSize = QtWidgets.QDesktopWidget().availableGeometry(self)
        width         = availableSize.width()
        height        = availableSize.height()

        width  = width * 0.9
        height = height * 0.9

        newSize = QtCore.QSize(width, height)

        self.setGeometry(QtWidgets.QStyle.alignedRect(
            QtCore.Qt.LeftToRight,
            QtCore.Qt.AlignCenter,
            newSize,
            availableSize))
        print('set geomatry')


    def makeTopMenu(self):
        """Add a menu bar to this main window."""
        menu_bar = self.menuBar()

        input_menu    = QtWidgets.QMenu("Input", self)
        module_menu   = QtWidgets.QMenu("Preprocessing", self)
        learning_menu = QtWidgets.QMenu("Learning", self)

        menu_bar.addMenu(input_menu)
        menu_bar.addMenu(module_menu)
        menu_bar.addMenu(learning_menu)

        print('made menu')

    def makeModuleList(self):
        """Make the initial list of modules.

        Return
        a QListWidget containing all of the modules.
        """
        module_list = QtWidgets.QListWidget()

        if self.modules:
            for module in self.modules:
                module_list.addItem(module)

        for i in range(10):
            item = QtWidgets.QListWidgetItem('&Item {}'.format(i))
            module_list.addItem(str(i))

        print("Made a list")
        return module_list

    def makeGraphicsDisplay(self):
        """This is where the images are diaplayed."""
        self.scene = QtWidgets.QGraphicsScene(self)

        # Load the images in their place.
        pixmap = QtGui.QPixmap('/home/me/Pictures/utah_teapot.jpg')

        # Return a graphics item.
        return QtWidgets.QGraphicsPixmapItem(pixmap)

    def addModule(self, module):
        """Add a module to the list fo modules."""
        self.module.append(module)

    def browse(self):
        print('browse clicked')

    def find(self):
        pass

    def aninmateFindClick(self):
        pass

    def openFileOfItem(row, column):
        pass

    def contextMenu(position):
        pass
