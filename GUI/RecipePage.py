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
        self.createUI()
    
    def createUI(self):
        self.mainLayout = QVBoxLayout()

        self.createProgressBar()
        self.createRecipeTable()

        self.setLayout(self.mainLayout)
        

    def createRecipeTable(self) -> None:
        self.recipeTable = QTableWidget()
        self.recipeTable.setObjectName("recipeTable")
        self.recipeTable.setColumnCount(2)
        self.recipeTable.setRowCount(5)
        self.recipeTable.setHorizontalHeaderLabels(["Recipe Name","Link"])
        self.recipeTable.horizontalHeader().setSectionResizeMode(0,QtWidgets.QHeaderView.Stretch)

        self.mainLayout.addWidget(self.recipeTable)

    def createProgressBar(self) -> None:
        self.recipeProgressBar = QProgressBar()

        self.mainLayout.addWidget(self.recipeProgressBar)
        self.recipeProgressBar.hide()