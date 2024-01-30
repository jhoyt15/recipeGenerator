from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class IngredientForm(QFrame):
    def __init__(self,ingredientList:list):
        super(IngredientForm,self).__init__()
        self.setObjectName("HomePage")
        with open("GUI/Styles/HomePage.css","r") as file:
            self.setStyleSheet(file.read())
        self.ingredientList = ingredientList
        self.createUI()

    def createUI(self)->None:
        self.mainLayout = QVBoxLayout()
        print(len(self.ingredientList))
        for i in range(0,100):
            ingredientSelectRadio = QRadioButton()
            ingredientSelectRadio.ingredient_id = self.ingredientList[i][0]
            ingredientSelectRadio.ingredient_name = self.ingredientList[i][1]
            ingredientSelectRadio.setText(ingredientSelectRadio.ingredient_name)
            ingredientSelectRadio.clicked.connect(self.ingredientSelected)
            self.mainLayout.addWidget(ingredientSelectRadio)

        self.setLayout(self.mainLayout)
        self.show()

    def ingredientSelected(self)->None:
        pass