from GUI.HomePage import HomePage
from GUI.RecipePage import RecipePage
from GUI.MainPage import MainPage
from GUI.IngredientForm import IngredientForm
from dataHandling.recipeDataHandler import RecipeDataHandler
from dataHandling.generateRecipe import generateRecipe
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from googlesearch import search
import operator
import webbrowser
class PageController: 
    def __init__(self,homePage: HomePage,recipePage :RecipePage,mainPage: MainPage):
        self.homePage = homePage
        self.recipePage = recipePage
        self.mainPage = mainPage
        self.connectToDB()

        self.searchThread = SearchThread(self.recipePage,self)

        self.homePage.generateRecipeButton.clicked.connect(self.generateAndShowRecipes)

        ingredientCompleter = QCompleter(self.getAllIngredientNames())
        ingredientCompleter.setCaseSensitivity(Qt.CaseInsensitive)
        self.homePage.ingredientField.setCompleter(ingredientCompleter)

    def generateAndShowRecipes(self) -> None:
        self.recipeList = generateRecipe(self.homePage.ingredientList,self.databaseConnection)
        if(len(self.recipeList) > 0):
            self.recipePage.recipeProgressBar.show()
            self.searchThread.start()
            self.searchThread.recipes.connect(self.addRecipeToTable)
            self.searchThread.progress.connect(self.updateProgressBar)
        else:
            self.noRecipeWarning = QMessageBox.warning(self.mainPage,"No Recipes!","No Recipes Found!")

    def connectToDB(self) -> None:
        self.databaseConnection = RecipeDataHandler()

    def openLink(self) -> None:
        link = self.recipePage.sender().link
        webbrowser.open(link)

    def addRecipeToTable(self,data:dict) -> None:
        recipes = data["recipes"]
        topSearchResults = data["searchButtonLinks"]
        for i in range(0,len(recipes)):
            recipe = recipes[i]
            recipe = ' '.join(recipe.split())
            recipeLabel = QLabel(recipe.title())
            self.recipePage.recipeTable.setCellWidget(i,0,recipeLabel)
            searchButton = QPushButton("Top Recipe")
            searchButton.setObjectName("linkButton")
            searchButton.link = topSearchResults[i]
            searchButton.clicked.connect(self.openLink)
            self.recipePage.recipeTable.setCellWidget(i,1,searchButton)
        self.recipePage.recipeProgressBar.hide()
    
    def updateProgressBar(self,val:int)->None:
        self.recipePage.recipeProgressBar.setValue(int((val/len(self.recipeList))*100))

    def getAllIngredientNames(self)->list:
        ingredients = self.databaseConnection.executeQuery("SELECT ingredient_name FROM Ingredients")
        ingredients = list(map(operator.itemgetter(0),ingredients))
        return [ingredient.capitalize() for ingredient in ingredients]

class SearchThread(QThread):
    progress = pyqtSignal(int)
    recipes = pyqtSignal(dict)
    def __init__(self,recipePage:RecipePage,controller:PageController):
        self.recipePage = recipePage
        self.controller = controller
        super().__init__()

    def run(self):
        data = {"searchButtonLinks":[],"recipes":[]}
        i = 1
        for recipe in self.controller.recipeList:
                data["recipes"].append(recipe)
                topSearchResult = search(recipe,num=1,pause=1)
                topSearchResult = next(topSearchResult)
                data["searchButtonLinks"].append(topSearchResult)
                self.progress.emit(i)
                i += 1
        self.recipes.emit(data)