import dataHandling.dbInit as dbInit
import dataHandling.recipeDataHandler as recipeDataHandler
import dataHandling.generateRecipe as generateRecipe

password = input("Input Password: ")
credentials = {"host":"localhost","user":"root","password":password,"database":"recipeDatabase"}
database = recipeDataHandler.RecipeDataHandler(credentials)
recipeList = generateRecipe.generateRecipe(["beef","cheese"],database)
print(recipeList)
