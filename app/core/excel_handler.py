import os
import csv
import xlwings as xw
from xlwings import Book
from PyQt6.QtWidgets import QMessageBox

def extractNameBoxToCsv(folder_path: str, nameBoxData: dict):
    """이름상자 데이터를 CSV로 저장"""
    output_csv = os.path.join(folder_path, "output")
    if not os.path.exists(output_csv):
        os.mkdir(output_csv)

    with xw.App(visible=False) as app:
        for file_path, name_boxes in nameBoxData.items():
            wb = app.books.open(file_path)
            for name_box in name_boxes:
                sheet_name, rng = name_box[1].split("!")
                save_csv(wb, sheet_name.strip("="), name_box[0], rng, output_csv)
            wb.close()

    QMessageBox.information(None, "작업 완료", "이름상자 목록을 CSV로 내보냈습니다.")

def save_csv(wb: Book, sheet_name: str, nameBoxName: str, rng: str, output_folder: str):
    """엑셀 데이터를 CSV로 저장"""
    output_csv = os.path.join(output_folder, f"{nameBoxName}.csv")

    try:
        ws = wb.sheets[sheet_name]
        data_range = ws.range(rng).value

        if isinstance(data_range, list):
            if not isinstance(data_range[0], list):
                data_range = [data_range]
        else:
            data_range = [[data_range]]

        with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data_range)

        print(f"CSV 파일이 생성되었습니다: {output_csv}")
    except Exception as e:
        print(f"CSV 파일 생성 중 오류 발생: {e}")
