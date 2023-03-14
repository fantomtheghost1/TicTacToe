from PySide6.QtWidgets import QApplication
from game_window import GameWindow
import sys

app = QApplication(sys.argv)
window = GameWindow(app)

window.show()
app.exec()