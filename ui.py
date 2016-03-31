from PySide import QtCore
from PySide import QtGui

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

class MainWindow(MayaQWidgetDockableMixin, QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)\

        # Main widget
        main_widget = QtGui.QWidget()
        main_layout = QtGui.QVBoxLayout()

        # Create UI widgets
        self.test_btn = QtGui.QPushButton('Test')

        # Attach widgets to the main layout
        main_layout.addWidget(self.test_btn)

        # Set main layout
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Connect buttons signals
        self.test_btn.clicked.connect(self.on_test_btn_click)

    def on_test_btn_click(self):
        print 'Test button was clicked'

def main():
    w = MainWindow()
    w.show(dockable=True, floating=False, area='left')
