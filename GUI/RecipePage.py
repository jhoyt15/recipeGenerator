from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class RecipePage(QFrame):
    def __init__(self):
        super(RecipePage,self).__init__()
        self.setObjectName("RecipePage")
        with open("GUI/Styles/RecipePage.css","r") as file:
            self.setStyleSheet(file.read())