from PyQt6.QtWidgets import QFileDialog, QMessageBox
from MainWindow_package import rgb_field_list, rgb_crosseAndZero_list
import json

parent=None
gameField=None
playerX=None
playerY=None
def getGameComponets(_parent, _gameField, _playerX, _playerY):
    global parent, gameField, playerX, playerY
    parent=_parent
    gameField = _gameField
    playerX=_playerX
    playerY=_playerY



def saveGame():
    global parent, gameField, playerX, playerY, rgb_field_list, rgb_crosseAndZero_list
    dataToSave = {
        "gameField": {
            'rgb_field_list': rgb_field_list,
            'rgb_crosseAndZero_list': rgb_crosseAndZero_list,
            'vinner_in_cell': [[gameField.cells[i][j].vinner_in_cell for j in range(3)] for i in range(3)],
            'current_x_of_cell': gameField.current_x_of_cell,
            'current_y_of_cell': gameField.current_y_of_cell,
            'x_of_cell_before': gameField.x_of_cell_before,
            'y_of_cell_before': gameField.y_of_cell_before,
            'currentPlayer': gameField.currentPlayer,
            'accessToAllButtons_flag': gameField.accessToAllButtons_flag,
            'cells': [[cellState(gameField.cells[i][j].buttons) for j in range(3)] for i in range(3)],
            'bigCrossAndZero_matrix': [[getBigCrossAndZero_matrix(gameField.bigCrossAndZero_matrix[i][j]) for j in range(3)] for i in range(3)]
        },
        'playerX': getPlayerState(playerX),
        'playerY': getPlayerState(playerY)
    }
    with open('test_file.json', 'w') as f:
        json.dump(dataToSave, f)

    dialog = QMessageBox(parent)
    dialog.setWindowTitle('message')
    dialog.setIcon(QMessageBox.Icon.Information)
    dialog.setText("Game was saved")
    dialog.exec()

def buttonState(buttonPointer):
    return  {
        'access': buttonPointer.access,
        'text': buttonPointer.text(),
        'styleSheet': buttonPointer.styleSheet(),
        'isEnabled': buttonPointer.isEnabled()
    }

def cellState(cellPointer):
    return [[buttonState(cellPointer[i][j]) for j in range(3)] for i in range(3)]
def getBigCrossAndZero_matrix(pointer):
    if pointer is None:
        return None
    else:
        return pointer.symbol

def getPlayerState(playerPointer):
    return {
        'styleSheet': playerPointer.label.styleSheet(),
        'name': playerPointer.playerName.displayText(),
        'picturePath': playerPointer.picturePath
    }