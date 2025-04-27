from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtWidgets import QGridLayout, QLabel, QPushButton, QLineEdit, QWidget, QMessageBox
from PyQt6.QtGui import QPixmap, QPainter, QColor, QPalette

rgb_field_list=[0, 0, 139]
rgb_crosseAndZero_list=[0, 0, 0]
class GameFieldButton(QPushButton):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(30)
        self.setStyleSheet(f"color: rgb({rgb_crosseAndZero_list[0]}, {rgb_crosseAndZero_list[1]}, {rgb_crosseAndZero_list[2]});"
                           f" background-color: white; font-size: 35px; min-width: 40px; min-height: 40px; ")
        self.setFixedHeight(30)
        self.access=True




class GameFieldCell_wdg(QWidget):
    def __init__(self, _gameField):
        super().__init__()

        self._gameFieldPointer=_gameField


        self.vinner_in_cell=None

        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)


        self.buttons = [
            [GameFieldButton() for _ in range(3)] for _ in range(3)
        ]


        for i in range(3):
            for j in range(3):
                self.buttons[i][j].clicked.connect(lambda _, x_of_button=i, y_of_button=j: self.button_clicked(x_of_button, y_of_button))
                self.layout.addWidget(self.buttons[i][j], i, j)

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = QRect(5, 9, self.width()-12, self.height())
        painter.fillRect(rect, QColor("black"))

    def button_clicked(self, x_of_button, y_of_button):
        name_of_button=self.buttons[x_of_button][y_of_button]

        for i in range(3):
            for j in range(3):
                if self._gameFieldPointer.cells[i][j]==self:
                    self._gameFieldPointer.x_of_cell_before=i
                    self._gameFieldPointer.y_of_cell_before=j
        self._gameFieldPointer.current_x_of_cell=x_of_button
        self._gameFieldPointer.current_y_of_cell=y_of_button

        if not name_of_button.access:
            return


        if self._gameFieldPointer.currentPlayer=='x':
            name_of_button.setText("x")
            name_of_button.setStyleSheet(f"color: rgb({rgb_crosseAndZero_list[0]}, {rgb_crosseAndZero_list[1]}, {rgb_crosseAndZero_list[2]});"
                           f" background-color: white; font-size: 35px; min-width: 40px; min-height: 40px; ")
            self._gameFieldPointer.functionOfChangeCurrentPlayer('o')
            self._gameFieldPointer.currentPlayer='o'
        else:
            name_of_button.setText("o")
            name_of_button.setStyleSheet(f"color: rgb({rgb_crosseAndZero_list[0]}, {rgb_crosseAndZero_list[1]}, {rgb_crosseAndZero_list[2]});"
                           f" background-color: white; font-size: 35px; min-width: 40px; min-height: 40px; ")
            self._gameFieldPointer.functionOfChangeCurrentPlayer('x')
            self._gameFieldPointer.currentPlayer='x'

        name_of_button.access=False
        self.check_vinner_in_cells()
        self.set_access_to_game_field(x_of_button, y_of_button)





    def check_vinner_in_cells(self):
        if(self.buttons[0][0].text()==self.buttons[1][1].text()==self.buttons[2][2].text()=='x' or
           self.buttons[0][2].text()==self.buttons[1][1].text()==self.buttons[2][0].text()=='x' or
            self.buttons[0][0].text()==self.buttons[0][1].text()==self.buttons[0][2].text()=='x' or
            self.buttons[1][0].text()==self.buttons[1][1].text()==self.buttons[1][2].text()=='x' or
            self.buttons[2][0].text()==self.buttons[2][1].text()==self.buttons[2][2].text()=='x' or
            self.buttons[0][0].text()==self.buttons[1][0].text()==self.buttons[2][0].text()=='x' or
            self.buttons[0][1].text()==self.buttons[1][1].text()==self.buttons[2][1].text()=='x' or
            self.buttons[0][2].text()==self.buttons[1][2].text()==self.buttons[2][2].text()=='x'):

            self.vinner_in_cell='x'
            for i in range(3):
                for j in range(3):
                    if(self._gameFieldPointer.cells[i][j]==self):
                        self._gameFieldPointer.bigCrossAndZero_matrix[i][j] = bigZeroOrCross('x')
                        self._gameFieldPointer.layout_.addWidget(self._gameFieldPointer.bigCrossAndZero_matrix[i][j], i, j)

        elif (self.buttons[0][0].text()==self.buttons[1][1].text()==self.buttons[2][2].text()=='o' or
           self.buttons[0][2].text()==self.buttons[1][1].text()==self.buttons[2][0].text()=='o' or
            self.buttons[0][0].text()==self.buttons[0][1].text()==self.buttons[0][2].text()=='o' or
            self.buttons[1][0].text()==self.buttons[1][1].text()==self.buttons[1][2].text()=='o' or
            self.buttons[2][0].text()==self.buttons[2][1].text()==self.buttons[2][2].text()=='o' or
            self.buttons[0][0].text()==self.buttons[1][0].text()==self.buttons[2][0].text()=='o' or
            self.buttons[0][1].text()==self.buttons[1][1].text()==self.buttons[2][1].text()=='o' or
            self.buttons[0][2].text()==self.buttons[1][2].text()==self.buttons[2][2].text()=='o'):

            self.vinner_in_cell = 'o'
            for i in range(3):
                for j in range(3):
                    if (self._gameFieldPointer.cells[i][j] == self):
                        self._gameFieldPointer.bigCrossAndZero_matrix[i][j]=bigZeroOrCross('o')

                        self._gameFieldPointer.layout_.addWidget(self._gameFieldPointer.bigCrossAndZero_matrix[i][j], i, j)
        elif(self.buttons[0][0].access==False and self.buttons[0][1].access==False and self.buttons[0][2].access==False and
        self.buttons[1][0].access==False and self.buttons[1][1].access==False and self.buttons[1][2].access==False and
        self.buttons[2][0].access==False and self.buttons[2][1].access==False and self.buttons[2][2].access==False):
            self.vinner_in_cell = 0
        else:
            return

        self.check_vinner_on_all_field()

    def check_vinner_on_all_field(self):
        cells=self._gameFieldPointer.cells
        if (cells[0][0].vinner_in_cell==cells[1][1].vinner_in_cell==cells[2][2].vinner_in_cell=='x' or
        cells[0][2].vinner_in_cell==cells[1][1].vinner_in_cell==cells[2][0].vinner_in_cell=='x' or
        cells[0][0].vinner_in_cell==cells[0][1].vinner_in_cell==cells[0][2].vinner_in_cell=='x' or
        cells[1][0].vinner_in_cell == cells[1][1].vinner_in_cell == cells[1][2].vinner_in_cell == 'x' or
        cells[2][0].vinner_in_cell == cells[2][1].vinner_in_cell == cells[2][2].vinner_in_cell == 'x' or
        cells[0][0].vinner_in_cell==cells[1][0].vinner_in_cell==cells[2][0].vinner_in_cell=='x' or
        cells[0][1].vinner_in_cell==cells[1][1].vinner_in_cell==cells[2][1].vinner_in_cell=='x' or
        cells[0][2].vinner_in_cell==cells[1][2].vinner_in_cell==cells[2][2].vinner_in_cell=='x'):
            self.dialog=QMessageBox()
            self.dialog.setWindowTitle('message')
            self.dialog.setIcon(QMessageBox.Icon.Information)
            self.dialog.setText("Player x won")
            self.dialog.exec()
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        for l in range(3):
                            cells[i][j].buttons[k][l].access = False
            return
        elif (cells[0][0].vinner_in_cell==cells[1][1].vinner_in_cell==cells[2][2].vinner_in_cell=='o' or
        cells[0][2].vinner_in_cell==cells[1][1].vinner_in_cell==cells[2][0].vinner_in_cell=='o' or
        cells[0][0].vinner_in_cell==cells[0][1].vinner_in_cell==cells[0][2].vinner_in_cell=='o' or
        cells[1][0].vinner_in_cell == cells[1][1].vinner_in_cell == cells[1][2].vinner_in_cell == 'o' or
        cells[2][0].vinner_in_cell == cells[2][1].vinner_in_cell == cells[2][2].vinner_in_cell == 'o' or
        cells[0][0].vinner_in_cell==cells[1][0].vinner_in_cell==cells[2][0].vinner_in_cell=='o' or
        cells[0][1].vinner_in_cell==cells[1][1].vinner_in_cell==cells[2][1].vinner_in_cell=='o' or
        cells[0][2].vinner_in_cell==cells[1][2].vinner_in_cell==cells[2][2].vinner_in_cell=='o'):
            self.dialog = QMessageBox()
            self.dialog.setWindowTitle('message')
            self.dialog.setIcon(QMessageBox.Icon.Information)
            self.dialog.setText("Player o won")
            self.dialog.exec()
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        for l in range(3):
                            cells[i][j].buttons[k][l].access = False
            return
        elif(( not (cells[0][0].vinner_in_cell is None))and( not (cells[0][1].vinner_in_cell is None)) and
            (not (cells[0][2].vinner_in_cell is None))and( not (cells[1][0].vinner_in_cell is None)) and
            (not (cells[1][1].vinner_in_cell is None))and( not (cells[1][2].vinner_in_cell is None))and
            (not (cells[2][0].vinner_in_cell is None))and( not (cells[2][1].vinner_in_cell is None))and
            (not (cells[2][2].vinner_in_cell is None))):
            self.dialog = QMessageBox()
            self.dialog.setWindowTitle('message')
            self.dialog.setIcon(QMessageBox.Icon.Information)
            self.dialog.setText("A draw game")
            self.dialog.exec()
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        for l in range(3):
                            cells[i][j].buttons[k][l].access = False
    def set_access_to_game_field(self, x_of_button, y_of_button):
        if (self == self._gameFieldPointer.cells[x_of_button][y_of_button] and (self.vinner_in_cell is None) ):
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        for l in range(3):
                            self._gameFieldPointer.cells[i][j].buttons[k][l].setEnabled(False)
                            self._gameFieldPointer.cells[i][j].buttons[k][l].setStyleSheet(
                                f"color: rgb({rgb_crosseAndZero_list[0]}, {rgb_crosseAndZero_list[1]}, {rgb_crosseAndZero_list[2]});"
                                f" background-color: #D3D3D3; font-size: 35px; min-width: 40px; min-height: 40px; ")
            for i in range(3):
                for j in range(3):
                    if (self._gameFieldPointer.cells[x_of_button][y_of_button].buttons[i][j].access == True):
                        self._gameFieldPointer.cells[x_of_button][y_of_button].buttons[i][j].setEnabled(True)
                        self._gameFieldPointer.cells[x_of_button][y_of_button].buttons[i][j].setStyleSheet(f"color: rgb({rgb_crosseAndZero_list[0]}, {rgb_crosseAndZero_list[1]}, {rgb_crosseAndZero_list[2]});"
                           f" background-color: white; font-size: 35px; min-width: 40px; min-height: 40px; ")
        elif(self == self._gameFieldPointer.cells[x_of_button][y_of_button] and not (self.vinner_in_cell is None)):
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        for l in range(3):
                            if(self._gameFieldPointer.cells[i][j].buttons[k][l].access==True):
                                self._gameFieldPointer.cells[i][j].buttons[k][l].setEnabled(True)
                                self._gameFieldPointer.cells[i][j].buttons[k][l].setStyleSheet(f"color: rgb({rgb_crosseAndZero_list[0]}, {rgb_crosseAndZero_list[1]}, {rgb_crosseAndZero_list[2]});"
                           f" background-color: white; font-size: 35px; min-width: 40px; min-height: 40px; ")



        if( not (self._gameFieldPointer.cells[x_of_button][y_of_button].vinner_in_cell is None)):
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        for l in range(3):
                            if (self._gameFieldPointer.cells[i][j].buttons[k][l].access == True):
                                self._gameFieldPointer.cells[i][j].buttons[k][l].setEnabled(True)
                                self._gameFieldPointer.cells[i][j].buttons[k][l].setStyleSheet(f"color: rgb({rgb_crosseAndZero_list[0]}, {rgb_crosseAndZero_list[1]}, {rgb_crosseAndZero_list[2]});"
                           f" background-color: white; font-size: 35px; min-width: 40px; min-height: 40px; ")

        else:
            if(self._gameFieldPointer.accessToAllButtons_flag):
                for i in range(3):
                    for j in range(3):
                            for k in range(3):
                                for l in range(3):
                                    self._gameFieldPointer.cells[i][j].buttons[k][l].setEnabled(False)
                                    self._gameFieldPointer.cells[i][j].buttons[k][l].setStyleSheet(f"color: rgb({rgb_crosseAndZero_list[0]}, {rgb_crosseAndZero_list[1]}, {rgb_crosseAndZero_list[2]});"
                           f" background-color: #D3D3D3; font-size: 35px; min-width: 40px; min-height: 40px; ")

            else:
                for button in self.buttons:
                    button.setEnabled(False)

            for i in range(3):
                for j in range(3):
                    if (self._gameFieldPointer.cells[x_of_button][y_of_button].buttons[i][j].access == True):
                        self._gameFieldPointer.cells[x_of_button][y_of_button].buttons[i][j].setEnabled(True)
                        self._gameFieldPointer.cells[x_of_button][y_of_button].buttons[i][j].setStyleSheet(f"color: rgb({rgb_crosseAndZero_list[0]}, {rgb_crosseAndZero_list[1]}, {rgb_crosseAndZero_list[2]});"
                           f" background-color: white; font-size: 35px; min-width: 40px; min-height: 40px; ")






class GameField(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.currentPlayer='x'
        self.accessToAllButtons_flag=True
        self.didFirstClickBe = False
        self.setAutoFillBackground(True)
        self.current_x_of_cell=None
        self.current_y_of_cell=None
        self.x_of_cell_before=None
        self.y_of_cell_before=None

        self.functionOfChangeCurrentPlayer = None

        self.bigCrossAndZero_matrix=[[None for _ in range(3)] for _ in range(3)]
        self.layout_ = QGridLayout()
        self.layout_.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout_)


        self.cells=[[GameFieldCell_wdg(self) for _ in range(3)] for _ in range(3)]


        for i in range(3):
            for j in range(3):
                self.layout_.addWidget(self.cells[i][j], i, j)

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = QRect(5, 9, self.width()-12, self.height()+5)

        global rgb_field_list

        painter.fillRect(rect, QColor(rgb_field_list[0], rgb_field_list[1], rgb_field_list[2]))

    def restartGameField(self):
        self.currentPlayer='x'
        self.functionOfChangeCurrentPlayer('x')
        for i in range(3):
            for j in range(3):
                if(not (self.bigCrossAndZero_matrix[i][j] is None)):
                    widget = self.bigCrossAndZero_matrix[i][j]
                    self.layout_.removeWidget(widget)
                    widget.setParent(None)
                    widget.deleteLater()

                    self.bigCrossAndZero_matrix[i][j] = None
        for i in range(3):
            for j in range(3):
                self.cells[i][j].vinner_in_cell=None
                for k in range(3):
                    for l in range(3):
                        self.cells[i][j].buttons[k][l].access=True
                        self.cells[i][j].buttons[k][l].setEnabled(True)
                        self.cells[i][j].buttons[k][l].setText('')
                        self.cells[i][j].buttons[k][l].setStyleSheet(f"color: rgb({rgb_crosseAndZero_list[0]}, {rgb_crosseAndZero_list[1]}, {rgb_crosseAndZero_list[2]});"
                           f" background-color: white; font-size: 35px; min-width: 40px; min-height: 40px; ")

    def showCurrentPlayerForX(self, function_from_menu):
        self.functionOfChangeCurrentPlayer = function_from_menu

    def showCurrentPlayerForO(self, function_from_menu):
        self.functionOfChangeCurrentPlayer = function_from_menu


class bigZeroOrCross(QLabel):
    def __init__(self, symbol):
        super().__init__()

        self.symbol = symbol
        self.setGeometry(8, 5, 145, 143)
        self.pen = QtGui.QPen()
        self.pen.setWidth(10)
        self.pen.setColor(QColor(rgb_crosseAndZero_list[0], rgb_crosseAndZero_list[1], rgb_crosseAndZero_list[2]))

        self.canvas=QtGui.QPixmap(self.width(), self.height())
        self.canvas.fill(Qt.GlobalColor.white)
        self.setPixmap(self.canvas)

        self.painter = QtGui.QPainter(self.canvas)
        self.painter.setPen(self.pen)

        if(symbol=='o'):
            self.painter.drawEllipse(20, 20, self.width()-40, self.height()-40)
            self.painter.end()
        elif(symbol=='x'):
            self.painter.drawLine(20, 20, self.width()-20, self.height()-20)
            self.painter.drawLine(self.width()-20, 20, 20, self.height()-20)
            self.painter.end()
        self.setPixmap(self.canvas)







