import dataHandling.dbInit as dbInit
import dataHandling.recipeDataHandler as recipeDataHandler
import dataHandling.generateRecipe as generateRecipe
from GUI.PasswordWindow import PasswordWindow
from PyQt5.QtWidgets import QApplication
import sys

#password = input("Input Password: ")
#credentials = {"host":"localhost","user":"root","password":password,"database":"recipeDatabase"}
#database = recipeDataHandler.RecipeDataHandler(credentials)
#recipeList = generateRecipe.generateRecipe(["beef","cheese"],database)
#print(recipeList)

QApp = QApplication(sys.argv)
application = PasswordWindow()
application.createUI()
sys.exit(QApp.exec_())