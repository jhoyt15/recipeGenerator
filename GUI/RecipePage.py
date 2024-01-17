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

        self.recipePageTitle = QLabel("Recipes")
        self.recipePageTitle.setObjectName("recipePageTitle")
        self.recipePageTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.recipePageTitle)

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
        self.recipeTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.mainLayout.addWidget(self.recipeTable)

    def createProgressBar(self) -> None:
        self.recipeProgressBar = QProgressBar()
        self.recipeProgressBar.setStyleSheet("QProgressBar::chunk {"
                                             "background-color: qlineargradient(x1:0,x1:0,x2:1,y2:0 stop: 0 #323aad, stop: 1 #288bb5);}")

        self.mainLayout.addWidget(self.recipeProgressBar)
        self.recipeProgressBar.hide()