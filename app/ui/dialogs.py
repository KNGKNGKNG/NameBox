from PyQt6.QtWidgets import QMessageBox, QFileDialog

def showWarning(message: str):
    QMessageBox.warning(None, "경고", message)

def showInfo(message: str):
    QMessageBox.information(None, "알림", message)

def selectFolder():
    return QFileDialog.getExistingDirectory(None, "폴더 선택", "")
