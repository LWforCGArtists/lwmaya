# This is the main file to start the application

import ui

# Reload for testing
# Remove for release!
reload(ui)

from ui import MainWindow

def run():
    w = MainWindow()
    w.show(dockable=True, floating=False, area='left')
