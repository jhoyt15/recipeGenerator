from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class HomePage(QFrame):
    ingredientList = [] #List of all ingredients that the user has entered
    ingredientListWidgets = []

    def __init__(self):
        super(HomePage,self).__init__()
        self.setObjectName("HomePage")
        with open("GUI/Styles/HomePage.css","r") as file:
            self.setStyleSheet(file.read())
        self.createUI()
    
    def createUI(self) -> None:
        self.topLayout = QVBoxLayout() #Create top level layout

        self.topLayout.setSpacing(30)
        self.topLayout.setContentsMargins(20,20,20,20)

        self.createIngredientInput()

        self.ingredientAddGrid = QGridLayout()
        self.ingredientAddGridWidget = QWidget()
        self.ingredientAddGrid.setVerticalSpacing(20)
        self.ingredientAddGridWidget.setLayout(self.ingredientAddGrid)
        self.topLayout.addWidget(self.ingredientAddGridWidget)

        self.createAddIngredientButton()

        self.addSelectedIngredientsSection()
        
        self.addGenerateRecipeButton()

        topWidget = QtWidgets.QWidget()
        topWidget.setLayout(self.topLayout)
        
        self.setLayout(self.topLayout)

    #This function will create the image that is at the top of the application
    def createImage(self) -> None:
        self.imageLabel = QtWidgets.QLabel() #Label that will hold the image

        self.imageMap = QPixmap("GUI/Images/mainLogo.png") #Pixmap of the image

        self.imageLabel.setPixmap(self.imageMap) #Set the pixmap of the label

        self.imageLabel.resize(self.imageMap.width(),self.imageMap.height()) #Resize the label to fit the picture

        self.topLayout.addWidget(self.imageLabel,alignment= Qt.AlignmentFlag.AlignCenter) #Add the image to the top level layout

    #This function will create the area for users to input ingredients into the list
    def createIngredientInput(self) -> None:
        self.ingredientField = QtWidgets.QLineEdit()
        self.ingredientField.setObjectName("addIngredientField")

        self.ingredientLabel = QtWidgets.QLabel("Ingredient: ")
        self.ingredientLabel.setObjectName("ingredientLabel")

        self.ingredientFormLayout = QtWidgets.QFormLayout()

        self.ingredientFormLayout.addRow(self.ingredientLabel,self.ingredientField)

        self.topLayout.addLayout(self.ingredientFormLayout)

    def createAddIngredientButton(self) -> None:
        self.addIngredientButton = QtWidgets.QPushButton("Add Ingredient")
        self.addIngredientButtonIcon = QIcon("GUI/Images/plusIcon.png")
        self.addIngredientButton.setIcon(self.addIngredientButtonIcon)
        self.addIngredientButton.setObjectName("addIngredientButton")
        self.addIngredientButton.setEnabled(True)
        self.addIngredientButton.setStyleSheet("background-color: qlineargradient(x1:0,x1:0,x2:1,y2:0 stop: 0 #323aad, stop: 1 #288bb5);")
        self.ingredientAddGrid.addWidget(self.addIngredientButton)

    def deleteIngredient(self):
        button = self.sender()
        self.ingredientsTable.removeRow(self.ingredientListWidgets.index(button))
        self.ingredientList.pop(self.ingredientListWidgets.index(button))
        self.ingredientListWidgets.remove(button)

    #This function will initialize and add the list of selected ingredients
    def addSelectedIngredientsSection(self):
        self.ingredientsTable = QTableWidget()
        self.ingredientsTable.setObjectName("ingredientTable")
        self.ingredientsTable.setColumnCount(2)
        self.ingredientsTable.setHorizontalHeaderLabels(["Ingredient","Delete"])
        self.ingredientsTable.horizontalHeader().setSectionResizeMode(0,QtWidgets.QHeaderView.Stretch)

        self.topLayout.addWidget(self.ingredientsTable)

    def addGenerateRecipeButton(self) -> None:
        self.generateRecipeButton = QPushButton("Generate Recipes")
        self.generateRecipeButton.setObjectName("generateRecipeButton")
        self.generateRecipeButton.setStyleSheet("background: qlineargradient(x1:0,x1:0,x2:1,y2:0 stop: 0 #323aad, stop: 1 #288bb5);")
        self.ingredientAddGrid.addWidget(self.generateRecipeButton)

