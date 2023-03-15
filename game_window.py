from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QWidget, QGridLayout, QStatusBar

class GameWindow(QMainWindow):

    def __init__(self, app):

        # initialize the window
        super().__init__()
        self.player = 1 # 1 means player 1, 2 means player 2
        self.app = app
        self.moves = 0
        self.setWindowTitle("Tic Tac Toe")
        self.setStyleSheet("background-color: gray")
        self.setFixedHeight(300)
        self.setFixedWidth(300)

        # initializes menu bar
        toolbar = QToolBar("tst")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        # creates the "New Game" action
        action1 = QAction("New Game", self)
        action1.setStatusTip("Starts a new game")
        action1.setIcon(QIcon("plusicon.png"))
        action1.triggered.connect(self.newGame)
        toolbar.addAction(action1)

        # creates the "Quit" action
        action1 = QAction("Quit", self)
        action1.setStatusTip("Quits the app")
        action1.triggered.connect(self.quitGame)
        toolbar.addAction(action1)

        # sets up the buttons
        self.setup()

        self.setWhite()

        # starts the app with player 1 starting
        self.statusBar().showMessage("Player 1's turn (with the X)")

    def setXO(self):

        sender = self.sender()

        self.setWhite()

        if self.player == 1:

            character = "X"
            self.player = 2
            self.statusBar().showMessage("Player 2's turn (with the O)")

        else:

            character = "O"
            self.player = 1
            self.statusBar().showMessage("Player 1's turn (with the X)")
        
        if sender is self.button_1:

            if self.button_1.text() == "X" or self.button_1.text() == "O":
                
                return

            self.button_1.setText(character)
            self.button_1.setStyleSheet("background-color: green")            
            self.hasWon()
            self.moves += 1
            return
        
        if sender is self.button_2:

            if self.button_2.text() == "X" or self.button_2.text() == "O":
                
                return

            self.button_2.setText(character)
            self.button_2.setStyleSheet("background-color: green")            
            self.hasWon()
            self.moves += 1
            return
        
        if sender is self.button_3:

            if self.button_3.text() == "X" or self.button_3.text() == "O":
                
                return

            self.button_3.setText(character)
            self.button_3.setStyleSheet("background-color: green")            
            self.hasWon()
            self.moves += 1
            return
        
        if sender is self.button_4:

            if self.button_4.text() == "X" or self.button_4.text() == "O":
                
                return

            self.button_4.setText(character)
            self.button_4.setStyleSheet("background-color: green")            
            self.hasWon()
            self.moves += 1
            return
        
        if sender is self.button_5:

            if self.button_5.text() == "X" or self.button_5.text() == "O":
                
                return

            self.button_5.setText(character)
            self.button_5.setStyleSheet("background-color: green")            
            self.hasWon()
            self.moves += 1
            return
        
        if sender is self.button_6:

            if self.button_6.text() == "X" or self.button_6.text() == "O":
                
                return

            self.button_6.setText(character)
            self.button_6.setStyleSheet("background-color: green")            
            self.hasWon()
            self.moves += 1
            return
        
        if sender is self.button_7:

            if self.button_7.text() == "X" or self.button_7.text() == "O":
                
                return

            self.button_7.setText(character)
            self.button_7.setStyleSheet("background-color: green")            
            self.hasWon()
            self.moves += 1
            return
        
        if sender is self.button_8:

            if self.button_8.text() == "X" or self.button_8.text() == "O":
                
                return

            self.button_8.setText(character)
            self.button_8.setStyleSheet("background-color: green")
            self.hasWon()
            self.moves += 1
            return
        
        if sender is self.button_9:

            if self.button_9.text() == "X" or self.button_9.text() == "O":
                
                return

            self.button_9.setText(character)
            self.button_9.setStyleSheet("background-color: green")
            self.hasWon()
            self.moves += 1
            return
        
    def setWhite(self):

        self.button_1.setStyleSheet("background-color: white")
        self.button_2.setStyleSheet("background-color: white")
        self.button_3.setStyleSheet("background-color: white")
        self.button_4.setStyleSheet("background-color: white")
        self.button_5.setStyleSheet("background-color: white")
        self.button_6.setStyleSheet("background-color: white")
        self.button_7.setStyleSheet("background-color: white")
        self.button_8.setStyleSheet("background-color: white")
        self.button_9.setStyleSheet("background-color: white")
        
    def victory(self):

        self.button_1.setDisabled(True)
        self.button_2.setDisabled(True)
        self.button_3.setDisabled(True)
        self.button_4.setDisabled(True)
        self.button_5.setDisabled(True)
        self.button_6.setDisabled(True)
        self.button_7.setDisabled(True)
        self.button_8.setDisabled(True)
        self.button_9.setDisabled(True)

        if self.player == 1:

            self.statusBar().showMessage("Player 2 Has Won!")

        else:

            self.statusBar().showMessage("Player 1 Has Won!")

        return
    
    def hasWon(self):

        # check if player 1 has won first
        if self.button_1.text() == "X":

            if self.button_2.text() == "X":

                if self.button_3.text() == "X":

                    self.setWhite()
                    self.button_1.setStyleSheet("background-color: red")
                    self.button_2.setStyleSheet("background-color: red")
                    self.button_3.setStyleSheet("background-color: red")
                    self.victory()
                    return
                
        if self.button_4.text() == "X":

            if self.button_5.text() == "X":

                if self.button_6.text() == "X":

                    self.setWhite()
                    self.button_4.setStyleSheet("background-color: red")
                    self.button_5.setStyleSheet("background-color: red")
                    self.button_6.setStyleSheet("background-color: red")
                    self.victory()
                    return
                
        if self.button_7.text() == "X":

            if self.button_8.text() == "X":

                if self.button_9.text() == "X":

                    self.setWhite()
                    self.button_7.setStyleSheet("background-color: red")
                    self.button_8.setStyleSheet("background-color: red")
                    self.button_9.setStyleSheet("background-color: red")
                    self.victory()
                    return
                
        if self.button_1.text() == "X":

            if self.button_4.text() == "X":

                if self.button_7.text() == "X":

                    self.setWhite()
                    self.button_1.setStyleSheet("background-color: red")
                    self.button_4.setStyleSheet("background-color: red")
                    self.button_7.setStyleSheet("background-color: red")
                    self.victory()
                    return
                
        if self.button_2.text() == "X":

            if self.button_5.text() == "X":

                if self.button_8.text() == "X":

                    self.setWhite()
                    self.button_2.setStyleSheet("background-color: red")
                    self.button_5.setStyleSheet("background-color: red")
                    self.button_8.setStyleSheet("background-color: red")
                    self.victory()
                    return
                
        if self.button_3.text() == "X":

            if self.button_6.text() == "X":

                if self.button_9.text() == "X":

                    self.setWhite()
                    self.button_3.setStyleSheet("background-color: red")
                    self.button_6.setStyleSheet("background-color: red")
                    self.button_9.setStyleSheet("background-color: red")
                    self.victory()
                    return
                
        if self.button_1.text() == "X":

            if self.button_5.text() == "X":

                if self.button_9.text() == "X":

                    self.setWhite()
                    self.button_1.setStyleSheet("background-color: red")
                    self.button_5.setStyleSheet("background-color: red")
                    self.button_9.setStyleSheet("background-color: red")
                    self.victory()
                    return
                
        if self.button_3.text() == "X":

            if self.button_5.text() == "X":

                if self.button_7.text() == "X":

                    self.setWhite()
                    self.button_3.setStyleSheet("background-color: red")
                    self.button_5.setStyleSheet("background-color: red")
                    self.button_7.setStyleSheet("background-color: red")
                    self.victory()
                    return
                
        # check if player 2 won next
        if self.button_1.text() == "O":

            if self.button_2.text() == "O":

                if self.button_3.text() == "O":

                    self.setWhite()
                    self.button_1.setStyleSheet("background-color: blue")
                    self.button_2.setStyleSheet("background-color: blue")
                    self.button_3.setStyleSheet("background-color: blue")
                    self.victory()
                    return
                
        if self.button_4.text() == "O":

            if self.button_5.text() == "O":

                if self.button_6.text() == "O":

                    self.setWhite()
                    self.button_4.setStyleSheet("background-color: blue")
                    self.button_5.setStyleSheet("background-color: blue")
                    self.button_6.setStyleSheet("background-color: blue")
                    self.victory()
                    return
                
        if self.button_7.text() == "O":

            if self.button_8.text() == "O":

                if self.button_9.text() == "O":

                    self.setWhite()
                    self.button_7.setStyleSheet("background-color: blue")
                    self.button_8.setStyleSheet("background-color: blue")
                    self.button_9.setStyleSheet("background-color: blue")
                    self.victory()
                    return
                
        if self.button_1.text() == "O":

            if self.button_4.text() == "O":

                if self.button_7.text() == "O":

                    self.setWhite()
                    self.button_1.setStyleSheet("background-color: blue")
                    self.button_4.setStyleSheet("background-color: blue")
                    self.button_7.setStyleSheet("background-color: blue")
                    self.victory()
                    return
                
        if self.button_2.text() == "O":

            if self.button_5.text() == "O":

                if self.button_8.text() == "O":

                    self.setWhite()
                    self.button_2.setStyleSheet("background-color: blue")
                    self.button_5.setStyleSheet("background-color: blue")
                    self.button_8.setStyleSheet("background-color: blue")
                    self.victory()
                    return
                
        if self.button_3.text() == "O":

            if self.button_6.text() == "O":

                if self.button_9.text() == "O":

                    self.setWhite()
                    self.button_3.setStyleSheet("background-color: blue")
                    self.button_6.setStyleSheet("background-color: blue")
                    self.button_9.setStyleSheet("background-color: blue")
                    self.victory()
                    return
                
        if self.button_1.text() == "O":

            if self.button_5.text() == "O":

                if self.button_9.text() == "O":

                    self.setWhite()
                    self.button_1.setStyleSheet("background-color: blue")
                    self.button_5.setStyleSheet("background-color: blue")
                    self.button_9.setStyleSheet("background-color: blue")
                    self.victory()
                    return
                
        if self.button_3.text() == "O":

            if self.button_5.text() == "O":

                if self.button_7.text() == "O":

                    self.setWhite()
                    self.button_3.setStyleSheet("background-color: blue")
                    self.button_5.setStyleSheet("background-color: blue")
                    self.button_7.setStyleSheet("background-color: blue")
                    self.victory()
                    return
                
        # if all the if statements ran and the entire board is full, then that means it is a cats game
        if self.moves == 8:

            self.setWhite()
            self.button_1.setDisabled(True)
            self.button_2.setDisabled(True)
            self.button_3.setDisabled(True)
            self.button_4.setDisabled(True)
            self.button_5.setDisabled(True)
            self.button_6.setDisabled(True)
            self.button_7.setDisabled(True)
            self.button_8.setDisabled(True)
            self.button_9.setDisabled(True)

            self.statusBar().showMessage("Cat's Game! Its a draw...")
            return

    def setup(self):

        # setup the game
        self.widget = QWidget()
        self.layout = QGridLayout(self.widget)

        # creates the tic tac toe buttons
        self.button_1 = QPushButton()
        self.button_2 = QPushButton()
        self.button_3 = QPushButton()
        self.button_4 = QPushButton()
        self.button_5 = QPushButton()
        self.button_6 = QPushButton()
        self.button_7 = QPushButton()
        self.button_8 = QPushButton()
        self.button_9 = QPushButton()

        # creates the self.button slots
        self.button_1.clicked.connect(self.setXO)
        self.button_2.clicked.connect(self.setXO)
        self.button_3.clicked.connect(self.setXO)
        self.button_4.clicked.connect(self.setXO)
        self.button_5.clicked.connect(self.setXO)
        self.button_6.clicked.connect(self.setXO)
        self.button_7.clicked.connect(self.setXO)
        self.button_8.clicked.connect(self.setXO)
        self.button_9.clicked.connect(self.setXO)

        # sets the button height
        size = 75

        self.button_1.setFixedHeight(size)
        self.button_2.setFixedHeight(size)
        self.button_3.setFixedHeight(size)
        self.button_4.setFixedHeight(size)
        self.button_5.setFixedHeight(size)
        self.button_6.setFixedHeight(size)
        self.button_7.setFixedHeight(size)
        self.button_8.setFixedHeight(size)
        self.button_9.setFixedHeight(size)

        # add buttons to the layout
        self.layout.addWidget(self.button_1, 0, 0)
        self.layout.addWidget(self.button_2, 1, 0)
        self.layout.addWidget(self.button_3, 2, 0)
        self.layout.addWidget(self.button_4, 0, 1)
        self.layout.addWidget(self.button_5, 1, 1)
        self.layout.addWidget(self.button_6, 2, 1)
        self.layout.addWidget(self.button_7, 0, 2)
        self.layout.addWidget(self.button_8, 1, 2)
        self.layout.addWidget(self.button_9, 2, 2)

        # sets up the status bar
        self.setStatusBar(QStatusBar(self))

        # show all buttons on the window
        self.setCentralWidget(self.widget)

    def newGame(self):

        self.setWhite()

        self.button_1.setDisabled(False)
        self.button_2.setDisabled(False)
        self.button_3.setDisabled(False)
        self.button_4.setDisabled(False)
        self.button_5.setDisabled(False)
        self.button_6.setDisabled(False)
        self.button_7.setDisabled(False)
        self.button_8.setDisabled(False)
        self.button_9.setDisabled(False)

        self.button_1.setText("")
        self.button_2.setText("")
        self.button_3.setText("")
        self.button_4.setText("")
        self.button_5.setText("")
        self.button_6.setText("")
        self.button_7.setText("")
        self.button_8.setText("")
        self.button_9.setText("")

        self.moves = 0
        self.statusBar().showMessage("Player 1's turn (with the X)")

    def quitGame(self):

        self.app.quit()
