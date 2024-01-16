from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class IngredientForm(QFrame):
    def __init__(self):
        super(IngredientForm,self).__init__()
        self.setObjectName("HomePage")
        with open("GUI/Styles/HomePage.css","r") as file:
            self.setStyleSheet(file.read())
        self.createUI()

    def createUI(self)->None:
        self.mainLayout = QVBoxLayout()


        self.setLayout(self.mainLayout)