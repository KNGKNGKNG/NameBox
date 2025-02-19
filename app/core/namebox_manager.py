import os
import logging
import xlwings as xw

logging.basicConfig(level=logging.DEBUG, filename="py_log.log", filemode="w",
                    format="%(lineno)d - %(funcName)s() - %(levelname)s - %(message)s")

def getNameBoxList(folder_path: str) -> dict:
    """폴더 내 엑셀 파일의 이름상자 목록을 가져오는 함수"""
    excel_extensions = ('.xls', '.xlsx', '.xlsm')

    files = [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if file.endswith(excel_extensions) and not file.startswith('~')
    ]

    logging.debug("파일 로드 성공")

    name_box_data = {}
    with xw.App(visible=False) as app:
        logging.debug("엑셀 프로세스 로드 성공")

        for excelFile in files:
            name_box_set = set()
            try:
                with app.books.open(excelFile) as wb:
                    name_box_list = wb.names
                    for x in name_box_list:
                        if "_FilterDatabase" in x.name or "#REF" in x.name or "#NAME?" in x.refers_to:
                            continue

                        try:
                            address = x.refers_to_range
                        except:
                            address = x.refers_to.split("!")[1]

                        name_box_set.add((x.name, x.refers_to, address))

                name_box_data[excelFile] = name_box_set
            except Exception as e:
                logging.error(f"{excelFile} - 엑셀 워크북 오류 발생: {e}")

    return name_box_data
