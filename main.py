# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Моя программа")
    window.setGeometry(150, 100, 500, 500)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()
