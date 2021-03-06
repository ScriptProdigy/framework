import sys

from PyQt4 import QtGui
from includes import PluginFramework

class Main:
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        self.plugins = PluginFramework.PluginFramework()
        while(True):
            pass
    
    def run(self):
        self.app.exec_()


if(__name__ == "__main__"):
    print("Starting up..")
    Main = Main()
    Main.run()
    print("Exiting..")
