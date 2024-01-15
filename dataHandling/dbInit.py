import dataHandling.recipeDataHandler as recipeDataHandler
import csv
#This function will initialize the database by creating SQL queries
def databaseInitialize(database: recipeDataHandler.RecipeDataHandler) -> None:
    database.executeQuery("CREATE TABLE Recipe (name varchar(255), rec_id int NOT NULL PRIMARY KEY)")
    database.executeQuery("CREATE TABLE Ingredients (ingredient_id int NOT NULL PRIMARY KEY, ingredient_name varchar(255))")
    database.executeQuery("CREATE TABLE IngredientsToRecipe (rec_id int NOT NULL, ingredient_id int NOT NULL, FOREIGN KEY(rec_id) REFERENCES Recipe(rec_id),FOREIGN KEY(ingredient_id) REFERENCES Ingredients (ingredient_id))")

    fileName ='recipeData/RAW_recipes.csv'
    with open(fileName,encoding = "utf8") as csvFile:
        rowReader = csv.reader(csvFile)
        for row in rowReader:
            database.executeQuery("INSERT INTO Recipe VALUES ('%s', %d)" %(row[0],int(row[1])))

    fileName = 'recipeData/ingredients_map.csv'
    seenIngredients = {}
    with open(fileName) as csvFile:
        rowReader = csv.reader(csvFile)
        for row in rowReader:
            if row[7] not in seenIngredients: #Handle duplicate ingredients
                database.executeQuery("INSERT INTO Ingredients VALUES (%d,'%s')" %(int(row[7]),row[5].replace("'","")))
                seenIngredients[row[7]] = row[5]

    fileName = 'recipeData/PP_recipes.csv'
    with open(fileName) as csvFile:
        rowReader = csv.reader(csvFile)
        for row in rowReader:
            for x in row[7][1:len(row[7])-1].split(','):
                database.executeQuery("INSERT INTO IngredientsToRecipe VALUES (%d,%d)" %(int(row[0]),int(x)))
    database.commit()


#name,id,minutes,contributor_id,submitted,tags,nutrition,n_steps,steps,description,ingredients,n_ingredients
#index,raw_ingr,raw_words,processed,len_proc,replaced,count,id
#id,i,name_tokens,ingredient_tokens,steps_tokens,techniques,calorie_level,ingredient_ids

