from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QMainWindow, QFormLayout, QVBoxLayout

class PasswordWindow(QMainWindow):
    def __init__(self):
        super(PasswordWindow,self).__init__()
        self.setWindowTitle("Enter Password")

    def createUI(self):
        self.topLayout = QVBoxLayout()

        self.formLayout = QFormLayout() #Create the layout for the window

        self.buttonLayout = QVBoxLayout() #Create the layout for the button

        self.passwordLabel = QtWidgets.QLabel() #Create the label for the user to enter their password
        self.passwordLabel.setText("Password:")

        self.enterInfoButton = QtWidgets.QPushButton(self) #Create the push button
        self.enterInfoButton.setText("Enter")
        self.enterInfoButton.clicked.connect(self.buttonPressed) #Set the function that will handle when the button is clicked

        self.passwordField = QtWidgets.QLineEdit() #Create the edit field for the password

        self.formLayout.addRow(self.passwordLabel,self.passwordField)

        self.buttonLayout.addWidget(self.enterInfoButton)

        self.topLayout.addLayout(self.formLayout)
        self.topLayout.addLayout(self.buttonLayout)

        topWidget = QtWidgets.QWidget()
        topWidget.setLayout(self.topLayout)
        self.setCentralWidget(topWidget)

        self.show()
    
    def buttonPressed(self):
        print("Button Clicked")
        self.update()

    def update(self):
        self.passwordLabel.adjustSize()