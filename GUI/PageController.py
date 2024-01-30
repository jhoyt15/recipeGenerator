from GUI.HomePage import HomePage
from GUI.RecipePage import RecipePage
from GUI.MainPage import MainPage
from dataHandling.recipeDataHandler import RecipeDataHandler
from dataHandling.generateRecipe import generateRecipe
from dataHandling.areFavoriteRecipes import areFavoriteRecipes
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from googlesearch import search
import operator
import webbrowser
class PageController: 
    def __init__(self,homePage: HomePage,recipePage :RecipePage,mainPage: MainPage):
        self.homePage = homePage
        self.recipePage = recipePage
        self.mainPage = mainPage
        self.connectToDB()

        self.searchThread = SearchThread(self)

        self.homePage.generateRecipeButton.clicked.connect(self.generateAndShowRecipes)
        self.homePage.addIngredientButton.clicked.connect(self.addIngredient)
        self.recipePage.loadFavoriteRecipesButton.clicked.connect(self.loadFavoriteRecipes)

        ingredientCompleter = QCompleter(self.getAllIngredientNames())
        ingredientCompleter.setCaseSensitivity(Qt.CaseInsensitive)
        self.homePage.ingredientField.setCompleter(ingredientCompleter)

    def generateAndShowRecipes(self) -> None:
        ''' Generates recipes based on the current ingredients and adds them to the recipe table.
        '''
        if(len(self.homePage.ingredientList) == 0):
            self.noRecipeWarning = QMessageBox.warning(self.mainPage,"No Ingredients!","Please Add Ingredients.")
        else:
            self.recipeList = generateRecipe(self.homePage.ingredientList,self.databaseConnection)
            self.recipePage.recipeTable.clearContents()
            if(len(self.recipeList) > 0):
                self.recipePage.recipeProgressBar.show()
                self.searchThread.start()
                self.searchThread.recipes.connect(self.addRecipeToTable)
                self.searchThread.progress.connect(self.updateProgressBar)
            else:
                self.noRecipeWarning = QMessageBox.warning(self.mainPage,"No Recipes!","No Recipes Found!")

    def connectToDB(self) -> None:
        ''' Open a connection to the DB
        '''
        self.databaseConnection = RecipeDataHandler()

    def openLink(self) -> None:
        ''' Opens a link when a button is clicked
        '''
        link = self.recipePage.sender().link
        webbrowser.open(link)

    def addRecipeToTable(self,data:dict) -> None:
        self.recipePage.currentRecipes.clear()
        topSearchResults = data["searchButtonLinks"]
        recipeIsFavorite = areFavoriteRecipes(self.databaseConnection,self.recipeList)
        for i in range(0,len(self.recipeList)):
            recipe = self.recipeList[i]
            self.recipePage.currentRecipes.append(recipe)

            favoriteButton = QPushButton()
            favoriteButton.setObjectName("favoriteRecipeButton")
            favoriteButton.recipeName = recipe
            favoriteButton.isFavorite = recipeIsFavorite[i]
            if(favoriteButton.isFavorite == 1):
                favoriteButton.setStyleSheet("background-color: red;")
            favoriteButton.clicked.connect(self.updateFavoriteRecipes)

            recipe = ' '.join(recipe.split())
            recipeLabel = QLabel(recipe.title())
            self.recipePage.recipeTable.setCellWidget(i,0,recipeLabel)

            searchButton = QPushButton("Top Recipe")
            searchButton.setObjectName("linkButton")
            searchButton.link = topSearchResults[i]
            searchButton.clicked.connect(self.openLink)
            self.recipePage.recipeTable.setCellWidget(i,1,searchButton)

            self.recipePage.recipeTable.setCellWidget(i,2,favoriteButton)

        self.recipePage.recipeTable.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.recipePage.recipeTable.horizontalHeader().setSectionResizeMode(1,QHeaderView.ResizeToContents)
        self.recipePage.recipeTable.horizontalHeader().setSectionResizeMode(2,QHeaderView.ResizeToContents)
        self.recipePage.recipeProgressBar.hide()
        self.recipePage.recipeProgressBar.setValue(0)
    
    def updateProgressBar(self,val:int)->None:
        self.recipePage.recipeProgressBar.setValue(int((val/len(self.recipeList))*100))

    def getAllIngredientNames(self)->list:
        ingredients = self.databaseConnection.executeQuery("SELECT ingredient_name FROM Ingredients")
        ingredients = list(map(operator.itemgetter(0),ingredients))
        return [ingredient.capitalize() for ingredient in ingredients]

    def addIngredient(self)->None:
        text = self.homePage.ingredientField.text()
        if text != "" and self.homePage.ingredientList.__contains__(text.lower()) == False:
            self.homePage.ingredientList.append(text.lower())
            ingredientName = QLabel(text.capitalize())
            deleteButton = QPushButton()
            deleteButton.setIcon(QIcon("GUI/Images/deleteIcon.png"))
            deleteButton.clicked.connect(self.homePage.deleteIngredient)
            self.homePage.ingredientListWidgets.append(deleteButton)
            self.homePage.ingredientsTable.insertRow(self.homePage.ingredientsTable.rowCount())
            self.homePage.ingredientsTable.setCellWidget(self.homePage.ingredientsTable.rowCount()-1,0,ingredientName)
            self.homePage.ingredientsTable.setCellWidget(self.homePage.ingredientsTable.rowCount()-1,1,deleteButton)

    def loadFavoriteRecipes(self)->None:
        self.recipeList = self.databaseConnection.executeQuery("SELECT name FROM Recipe WHERE favorite = 1")
        self.recipeList = list(map(operator.itemgetter(0),self.recipeList))
        self.recipePage.recipeTable.clearContents()
        if(len(self.recipeList) > 0):
            self.recipePage.recipeProgressBar.show()
            self.searchThread.start()
            self.searchThread.recipes.connect(self.addRecipeToTable)
            self.searchThread.progress.connect(self.updateProgressBar)
        else:
            self.noRecipeWarning = QMessageBox.warning(self.mainPage,"No Recipes!","No Recipes Found!")

    def updateFavoriteRecipes(self)->None:
        if(self.recipePage.sender().isFavorite == 0):
            self.databaseConnection.executeQuery("UPDATE Recipe SET favorite = 1 WHERE name = '%s'" %(self.recipePage.sender().recipeName))
            self.recipePage.sender().isFavorite = 1
            self.recipePage.sender().setStyleSheet("background-color: red;")
        else:
            self.databaseConnection.executeQuery("UPDATE Recipe SET favorite = 0 WHERE name = '%s'" %(self.recipePage.sender().recipeName))
            self.recipePage.sender().isFavorite = 0
            self.recipePage.sender().setStyleSheet("background-color: transparent;")
        self.databaseConnection.commit()

class SearchThread(QThread):
    progress = pyqtSignal(int)
    recipes = pyqtSignal(dict)
    def __init__(self,controller:PageController):
        self.controller = controller
        super().__init__()

    def run(self):
        data = {"searchButtonLinks":[],"recipes":[]}
        i = 1
        for recipe in self.controller.recipeList:
                topSearchResult = search(recipe,num=1,pause=1)
                topSearchResult = next(topSearchResult)
                data["searchButtonLinks"].append(topSearchResult)
                self.progress.emit(i)
                i += 1
        self.recipes.emit(data)
