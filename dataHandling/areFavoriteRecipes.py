from dataHandling.recipeDataHandler import RecipeDataHandler

def areFavoriteRecipes(databaseConnection:RecipeDataHandler,recipeList:list)->list:
    '''Checks database for whether or not each of the provided recipes have been marked as favorites.'''
    favorites = []
    for recipe in recipeList:
        isFavorite = databaseConnection.executeQuery("SELECT favorite FROM Recipe WHERE name = '%s'" %(recipe))
        favorites.append(isFavorite[0][0])
    return favorites