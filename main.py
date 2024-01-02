import dataHandling.dbInit as dbInit
import dataHandling.recipeDataHandler as recipeDataHandler
import dataHandling.generateRecipe as generateRecipe
from PyQt5.QtWidgets import QApplication
from GUI.MainPage import MainPage
import sys

#password = input("Input Password: ")
#credentials = {"host":"localhost","user":"root","password":password,"database":"recipeDatabase"}
#database = recipeDataHandler.RecipeDataHandler(credentials)
#recipeList = generateRecipe.generateRecipe(["beef","cheese"],database)
#print(recipeList)

QApp = QApplication(sys.argv)
application = MainPage()
sys.exit(QApp.exec_())