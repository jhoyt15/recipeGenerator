from dataHandling.recipeDataHandler import RecipeDataHandler
import re

#This function gets recipe recommendations using a list of user provided ingredients
def generateRecipe(ingredients: list, database: RecipeDataHandler) -> list:
    recipeList = [] #Return value
    foundRecipes = {} #Dictionary to store all recipes and how much overlap there is between recipes
    for ingredient in ingredients:
        ingredient_id = database.executeQuery("SELECT ingredient_id FROM Ingredients WHERE '%s' = ingredient_name" % (ingredient)) #Get the ingredient_id from DB
        if(len(ingredient_id) == 0):
            print("Ingredients Not Found")
        else: 
            ingredient_id = ingredient_id[0][0] #Get the ingredient ID (Value is stored within a tuple)
            recipe_id = database.executeQuery("SELECT rec_id FROM IngredientsToRecipe WHERE ingredient_id = %d" %ingredient_id) #Get all recipes that contain that ingredient
            for id in recipe_id:
                recipe = database.executeQuery("SELECT name FROM Recipe WHERE rec_id = %d" %(id))[0] #Get names of recipes with the current id
                if(recipe in foundRecipes):
                    foundRecipes[recipe] = foundRecipes[recipe]+1 #We have already seen this recipe
                else:
                    foundRecipes[recipe] = 1 #New recipe was found
    if(len(foundRecipes) != 0):
        foundRecipes = sorted(foundRecipes.items(), key=lambda x:x[1],reverse = True) #Sort the recipes based on the number of times they have been found
        numRecommendations = 5 if len(foundRecipes) > 5 else len(foundRecipes) #Recommend a maximum of 5 recipes
        for i in range(0,numRecommendations):
            recipeList.append(foundRecipes[i][0][0]) #Add recipe names to recipe list
    return recipeList
