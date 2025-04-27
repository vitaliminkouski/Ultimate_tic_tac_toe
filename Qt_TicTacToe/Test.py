from MainWindow_package import GameField, Menu, Player
from PyQt6.QtWidgets import QFileDialog, QMessageBox
import json
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QGridLayout, QWidget, QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QVBoxLayout
from SaveGame import saveGame, getGameComponets
from LoadGame import getGameComponetsToLoad, loadGame
import sys

app=QApplication(sys.argv)
window=QMainWindow()
window.setGeometry(200, 100, 1100, 650)
window.setWindowTitle('Tic tac toe')

menu=Menu(window)
gameField=GameField(window)
playerX=Player( 'x')
playerO=Player( 'o')

menu.restartGameAction(gameField.restartGameField)
getGameComponets(window, gameField, playerX, playerO)
getGameComponetsToLoad(window, gameField, playerX, playerO)


menu.saveGameAction(saveGame)
menu.loadGameAction(loadGame)

window.setMenuBar(menu)

layout=QHBoxLayout()

layout1=QVBoxLayout()
layout1.addWidget(QLabel(), 1)
layout1.addWidget(gameField, 7)
layout1.addWidget(QLabel(), 1)

wdg=QWidget(window)
wdg.setLayout(layout1)


playerX.label.setStyleSheet("background-color: #90EE90; font-size: 30px")

def showCurrentPlayer( currentPlayerSymbol):
    if currentPlayerSymbol == 'x':
        playerX.label.setStyleSheet("background-color: #90EE90; font-size: 30px")
        playerO.label.setStyleSheet("background-color: white; font-size: 30px")
    else:
        playerO.label.setStyleSheet("background-color: #90EE90; font-size: 30px")
        playerX.label.setStyleSheet("background-color: white; font-size: 30px")

gameField.showCurrentPlayerForO(showCurrentPlayer)
gameField.showCurrentPlayerForX(showCurrentPlayer)



layout.addWidget(playerX, 3)
layout.addWidget(wdg, 5)
layout.addWidget(playerO, 3)

widget=QWidget()
widget.setLayout(layout)

window.setCentralWidget(widget)

window.show()
sys.exit(app.exec())


