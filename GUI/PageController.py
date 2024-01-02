from GUI.HomePage import HomePage
from GUI.RecipePage import RecipePage
from dataHandling.recipeDataHandler import RecipeDataHandler
from dataHandling.generateRecipe import generateRecipe
class PageController: 
    def __init__(self,homePage: HomePage,recipePage :RecipePage):
        self.homePage = homePage
        self.recipePage = recipePage

        self.connectToDB()

        self.homePage.generateRecipeButton.clicked.connect(self.generateAndShowRecipes)

    def generateAndShowRecipes(self) -> None:
        recipeList = generateRecipe(self.homePage.ingredientList,self.databaseConnection)

    def connectToDB(self) -> None:
        credentials = 1
        self.databaseConnection = RecipeDataHandler(credentials)