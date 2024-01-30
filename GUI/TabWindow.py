from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class TabWindow(QTabWidget):
    def __init__(self, parent=None):
        super(TabWindow, self).__init__(parent)

    def resizeEvent(self, event):
        self.tabBar().setFixedWidth(self.width())
        super(TabWindow, self).resizeEvent(event)