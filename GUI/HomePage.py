from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon

class HomePage(QMainWindow):
    def __init__(self):
        super(HomePage,self).__init__()
        self.setWindowTitle("Recipe Generator")
        self.setWindowIcon(QIcon("GUI/HomePageIcon.jpg"))
    
    def createUI(self) -> None:
        self.topLayout = QVBoxLayout() #Create top level layout

        self.topLayout.setSpacing(30)
        self.topLayout.setContentsMargins(20,20,20,20)

        self.createImage()

        self.createIngridientInput()

        self.createAddIngredientButton()

        topWidget = QtWidgets.QWidget()
        topWidget.setLayout(self.topLayout)
        self.setCentralWidget(topWidget)

        self.show()

    #This function will create the image that is at the top of the application
    def createImage(self) -> None:
        self.imageLabel = QtWidgets.QLabel() #Label that will hold the image

        self.imageMap = QPixmap("GUI/HomePageImage.jpg") #Pixmap of the image

        self.imageLabel.setPixmap(self.imageMap) #Set the pixmap of the label

        self.imageLabel.resize(self.imageMap.width(),self.imageMap.height()) #Resize the label to fit the picture

        self.topLayout.addWidget(self.imageLabel) #Add the image to the top level layout

    #This function will create the area for users to input ingredients into the list
    def createIngridientInput(self) -> None:
        self.ingredientField = QtWidgets.QLineEdit()

        self.ingredientField.textChanged.connect(self.ingredientRecommend)

        self.ingredientFormLayout = QtWidgets.QFormLayout()

        self.ingredientFormLayout.addRow("Ingredient: ",self.ingredientField)

        self.topLayout.addLayout(self.ingredientFormLayout)

    def createAddIngredientButton(self) -> None:
        self.addIngredientButton = QtWidgets.QPushButton("Add Ingredient")
        self.addIngredientButton.resize(self.addIngredientButton.width()//2,self.addIngredientButton.height()*2)
        self.addIngredientButton.clicked.connect(self.addIngredient)

        self.topLayout.addWidget(self.addIngredientButton)

    #This function will add the ingredient to the ingredients list
    def addIngredient(self) -> None:
        pass


    def ingredientRecommend(self) -> None:
        pass