import mysql.connector
class RecipeDataHandler:
    #Class variables
    cursor = None
    connection = None

    def __init__(self,credentials: dict):
        hostKey = credentials["host"]
        self.connection = mysql.connector.connect(
            host = hostKey,
            user = credentials["user"],
            password = credentials["password"],
            database = credentials["database"]
            )
        self.cursor = self.connection.cursor()
    
    #Execute a query and return the data in a numpy array
    def executeQuery(self,query: str) -> list:
        self.cursor.execute(query)
        queryResult = self.cursor.fetchall()
        return queryResult
    
    #Commit the database changes
    def commit(self) -> None:
        self.connection.commit()