import sys
from PyQt6.QtWidgets import QApplication
from app.ui.mainUi import MyWindow

def main():
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
