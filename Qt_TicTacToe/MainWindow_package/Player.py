from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QFileDialog, QWidget, QLineEdit
from PyQt6.QtGui import QPixmap
class Player(QWidget):
    def __init__(self, playerSymbol):
        super().__init__()

        self.layout = QVBoxLayout()

        self.playerSymbol =playerSymbol

        self.picturePath=None
        self.label=QLabel('Player '+str(playerSymbol))
        self.label.setStyleSheet("background-color: white; font-size: 30px")
        self.layout.addWidget(self.label, 1)

        self.playerName=QLineEdit("Player name")
        self.layout.addWidget(self.playerName, 1)
        self.playerName.editingFinished.connect(self.savingName)

        self.playerPicture=QLabel()
        self.layout.addWidget(self.playerPicture, 7)
        self.playerPicture.setScaledContents(True)

        self.button=QPushButton("Open")
        self.layout.addWidget(self.button, 1)
        self.button.clicked.connect(self.showImage)

        self.layout.addWidget(QLabel(), 4)

        self.setLayout(self.layout)

    def savingName(self):
        self.name=self.playerName.displayText()

    def showImage(self):
        file=QFileDialog()
        self.picturePath=file.getOpenFileName()[0]
        self.pixmap = QPixmap(self.picturePath)
        self.pixmap=self.pixmap.scaled(300, 300)
        self.playerPicture.setPixmap(self.pixmap)


