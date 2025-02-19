import os
from PyQt6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PyQt6 import uic
from app.core.namebox_manager import getNameBoxList
from app.core.excel_handler import extractNameBoxToCsv

# UI 파일 경로
UI_FILE_PATH = os.path.join(os.path.dirname(__file__), r"C:\Users\DAPH-L\Desktop\namebox\mainWindow.ui")

class MyWindow(QDialog):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        uic.loadUi(UI_FILE_PATH, self)
        self.folder_path = QFileDialog.getExistingDirectory(self, "폴더 선택", "")

        if self.folder_path:
            self.nameBoxData = getNameBoxList(self.folder_path)
            self.initTable(self.nameBoxData)
        else:
            QMessageBox.warning(self, "경고", "폴더가 선택되지 않았습니다.")
            self.close()

    def exportToCsv(self):
        """이름상자 데이터를 CSV로 변환"""
        extractNameBoxToCsv(self.folder_path, self.nameBoxData)
