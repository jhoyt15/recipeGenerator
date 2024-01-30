from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class RecipePage(QFrame):
    currentRecipes = []
    def __init__(self):
        super(RecipePage,self).__init__()
        self.setObjectName("RecipePage")
        with open("GUI/Styles/RecipePage.css","r") as file:
            self.setStyleSheet(file.read())
        self.createUI()
    
    def createUI(self):
        ''' Create the UI components for the Recipe Tab
        '''
        self.mainLayout = QVBoxLayout()

        self.recipePageTitle = QLabel("Recipes")
        self.recipePageTitle.setObjectName("recipePageTitle")
        self.recipePageTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.recipePageTitle)

        self.createProgressBar()
        self.createRecipeTable()
        self.createLoadFavoriteRecipesButton()

        self.setLayout(self.mainLayout)
        

    def createRecipeTable(self) -> None:
        ''' Create the table which displays the recipes.
        '''
        self.recipeTable = QTableWidget()
        self.recipeTable.setObjectName("recipeTable")
        self.recipeTable.setColumnCount(3)
        self.recipeTable.setRowCount(20)
        self.recipeTable.setHorizontalHeaderLabels(["Recipe Name","Link","Favorite"])
        self.recipeTable.horizontalHeader().setSectionResizeMode(0,QtWidgets.QHeaderView.Stretch)
        self.recipeTable.horizontalHeader().setSectionResizeMode(1,QtWidgets.QHeaderView.ResizeToContents)
        self.recipeTable.horizontalHeader().setSectionResizeMode(2,QtWidgets.QHeaderView.ResizeToContents)
        self.recipeTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.mainLayout.addWidget(self.recipeTable)

    def createProgressBar(self) -> None:
        ''' Create the progress bar which will display the progress during recipe generation.
        '''
        self.recipeProgressBar = QProgressBar()
        self.recipeProgressBar.setStyleSheet("QProgressBar::chunk {"
                                             "background-color: qlineargradient(x1:0,x1:0,x2:1,y2:0 stop: 0 #323aad, stop: 1 #288bb5);}")

        self.mainLayout.addWidget(self.recipeProgressBar)
        self.recipeProgressBar.hide()

    def createLoadFavoriteRecipesButton(self)->None:
        ''' Create the button to allow the user to load their favorite recipes
        '''
        self.loadFavoriteRecipesButton = QPushButton("Load Favorite Recipes")
        self.loadFavoriteRecipesButton.setObjectName("loadFavRecipesButton")
        self.loadFavoriteRecipesButton.setStyleSheet("background-color: qlineargradient(x1:0,x1:0,x2:1,y2:0 stop: 0 #323aad, stop: 1 #288bb5);")

        self.mainLayout.addWidget(self.loadFavoriteRecipesButton)