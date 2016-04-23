from PySide import QtCore
from PySide import QtGui

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

from vray import VRayConfig

class VRayPanelWidget(QtGui.QWidget):

    def __init__(self):
        # Initialize parent constructor
        QtGui.QWidget.__init__(self)

        self.vrc = VRayConfig()

        # Set panel name to be able to reference it later
        self.setObjectName('VRayPanel')

        # Configure panel layout
        self.setLayout(QtGui.QVBoxLayout())
        self.layout().setAlignment(QtCore.Qt.AlignTop)

        # Labels
        vray_panel_lbl = QtGui.QLabel('VRay Configuration')

        self.layout().addWidget(vray_panel_lbl)

        # Buttons
        set_render_settings_btn = QtGui.QPushButton("Set Render Settings")
        linearize_textures_btn = QtGui.QPushButton("Linearize Textures")
        linearize_solid_colors_btn = QtGui.QPushButton("Linearize Colors")

        self.layout().addWidget(set_render_settings_btn)
        self.layout().addWidget(linearize_textures_btn)
        self.layout().addWidget(linearize_solid_colors_btn)

        # Connect buttons actions
        set_render_settings_btn.clicked.connect(self.set_render_settings)
        linearize_textures_btn.clicked.connect(self.linearize_textures)
        linearize_solid_colors_btn.clicked.connect(self.linearize_colors)

    def set_render_settings(self):
        self.vrc.set_linear_settings()

    def linearize_textures(self):
        self.vrc.linearize_all_textures()

    def linearize_colors(self):
        self.vrc.linearize_solid_materils()

class MainWindow(MayaQWidgetDockableMixin, QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)\

        # Main widget
        main_widget = QtGui.QWidget()
        main_layout = QtGui.QVBoxLayout()

        # Create UI widgets
        self.vray_panel = VRayPanelWidget()
        self.test_btn = QtGui.QPushButton('Test')

        # Attach widgets to the main layout
        main_layout.addWidget(self.vray_panel)
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
