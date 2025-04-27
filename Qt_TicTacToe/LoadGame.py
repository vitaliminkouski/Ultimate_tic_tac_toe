from PyQt6.QtWidgets import QFileDialog, QMessageBox, QLabel
from PyQt6.QtGui import QPixmap
from MainWindow_package import bigZeroOrCross, rgb_field_list, rgb_crosseAndZero_list

import json

parent=None
gameField=None
playerX=None
playerY=None
def getGameComponetsToLoad(_parent, _gameField, _playerX, _playerY):
    global parent, gameField, playerX, playerY
    parent=_parent
    gameField = _gameField
    playerX=_playerX
    playerY=_playerY

def loadGame():

    with open('test_file.json', 'r') as file:
        dataToLoad=json.load(file)

    global parent, gameField, playerX, playerY


    gameField.restartGameField()

    global rgb_field_list, rgb_crosseAndZero_list
    rgb_field_list=dataToLoad['gameField']['rgb_field_list']
    rgb_crosseAndZero_list=dataToLoad['gameField']['rgb_crosseAndZero_list']

    playerX.playerName.setText(dataToLoad['playerX']['name'])
    playerX.pixmap = QPixmap(dataToLoad['playerX']['picturePath'])
    playerX.pixmap = playerX.pixmap.scaled(300, 300)
    playerX.playerPicture.setPixmap(playerX.pixmap)
    playerX.label.setStyleSheet(dataToLoad['playerX']['styleSheet'])

    playerY.playerName.setText(dataToLoad['playerY']['name'])
    playerY.pixmap = QPixmap(dataToLoad['playerY']['picturePath'])
    playerY.pixmap = playerY.pixmap.scaled(300, 300)
    playerY.playerPicture.setPixmap(playerY.pixmap)
    playerY.label.setStyleSheet(dataToLoad['playerY']['styleSheet'])


    gameField.currentPlayer=dataToLoad['gameField']['currentPlayer']
    gameField.accessToAllButtons_flag=dataToLoad['gameField']['accessToAllButtons_flag']
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    gameField.cells[i][j].buttons[k][l].access=dataToLoad['gameField']['cells'][i][j][k][l]['access']
                    gameField.cells[i][j].buttons[k][l].setText(dataToLoad['gameField']['cells'][i][j][k][l]['text'])
                    gameField.cells[i][j].buttons[k][l].setStyleSheet(dataToLoad['gameField']['cells'][i][j][k][l]['styleSheet'])
                    if dataToLoad['gameField']['cells'][i][j][k][l]['isEnabled']:
                        gameField.cells[i][j].buttons[k][l].setEnabled(True)
                    else:
                        gameField.cells[i][j].buttons[k][l].setEnabled(False)

    for i in range(3):
        for j in range(3):
            if dataToLoad['gameField']['bigCrossAndZero_matrix'][i][j] is None:
                gameField.bigCrossAndZero_matrix[i][j]=None
            else:
                zeroOrCross=bigZeroOrCross(dataToLoad['gameField']['bigCrossAndZero_matrix'][i][j])
                gameField.layout_.addWidget(zeroOrCross, i, j)

    for i in range(3):
        for j in range(3):
            gameField.cells[i][j].vinner_in_cell=dataToLoad['gameField']['vinner_in_cell'][i][j]

    if dataToLoad['gameField']['x_of_cell_before'] is not None:
        gameField.cells[dataToLoad['gameField']['x_of_cell_before']][dataToLoad['gameField']['y_of_cell_before']].set_access_to_game_field(dataToLoad['gameField']['current_x_of_cell'], dataToLoad['gameField']['current_y_of_cell'])