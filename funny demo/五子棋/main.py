from game import Gomoku
from PyQt5.QtWidgets import QApplication
import sys
from window import GomokuWindow

def main():
    # g = Gomoku()
    # g.play()
    app = QApplication(sys.argv)
    ax = GomokuWindow()
    sys.eixt(app.exec_())


if __name__ == "__main__":
    main()
