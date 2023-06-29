import openpyxl
from EXCEL_report_generator import Report
from List_sorting import Sort
from gui import GUI


# def check selected file, returns type of file and file_path


def check_file_type(file: str):
    if file[-4:] == ".txt":
        # print("wybrano txt", open_file[-4:])
        type = "txt"
    elif file[-5:] == ".xlsx":
        # print("wybrano plik excel", open_file[-5:])
        type = "xlsx"
    else:
        # print("inny plik")
        type = False
    return type


def list_of_excel_files_from_txt(open_file):
    # select txt file with file paths of many files each in new line

    encode_list = ["latin-1", "utf-16-le", "utf-8", "CP-1250"]

    i = 0
    list_of_files = []
    for _ in encode_list:
        try:
            # merging text function
            with open(open_file, encoding=encode_list[i], mode='r') as file:
                # print('open_file: ', open_file)
                for line in file:
                    line = line.strip()
                    list_of_files.append(line)
            break

        except:
            print("Decoding", encode_list[i], "do not work")
            i = i + 1

    return list_of_files


# find missing orders from each excel file
# make report in txt from missing orders

# append new report to existing txt file

def EXCEL_missing_orders():
    open_file = GUI.select_file()
    List_of_items = write_excel_BOM_to_list(open_file)

    index_numer_zamowienia = znajdz_indeks(List_of_items, "Numer zamówienia")
    print('index_numer_zamowienia: ', index_numer_zamowienia)

    List_of_items_with_missing_values = find_items_without_value_in_cell(
        List_of_items, index_numer_zamowienia)

    sorted_list_of_items_with_missing_values = Sort.list_sort_by_index(
        List_of_items_with_missing_values.copy(), 5)

    Message_01 = "Utworzono raport z braków zamówien"

    Report.generate_report_txt(sorted_list_of_items_with_missing_values, "name_of_filestr", "search_Path_sld_prt: bytes".encode(
        "utf-8"), "search_Path_sld_prt_revision: bytes".encode("utf-8"), [0, 1, 2, 3, 4, 5, 6, 7, 8])


def write_excel_BOM_to_list(open_file: str) -> list[str]:
    """Def open active sheet of work book and write rows to lists

    Args:
        open_file (str): Path to file which is rewrite to list

    Returns:
        list[str]: strings in list are encoded to bytes
    """

    wrkbk = openpyxl.load_workbook(open_file)
    sh = wrkbk.active

    list_of_records = []

    for i in range(5, sh.max_row+1):
        details_of_record = []
        for j in range(1, sh.max_column+1):
            details_of_record.append(
                str(sh.cell(row=i, column=j).value).encode("utf-8"))
        list_of_records.append(details_of_record)
    print('list_of_records: ', list_of_records)

    return list_of_records


def find_items_without_value_in_cell(list_of_items: list[str], searched_column: int):
    list_of_found_items = []
    for item in list_of_items:

        if "none" in item[searched_column].decode("utf-8").lower():
            list_of_found_items.append(item)
            print("i Found unordered item!")
            continue

    print('list_of_found_items: ', list_of_found_items)
    return list_of_found_items


def znajdz_indeks(lista, szukany_element):
    for indeks, element in enumerate(lista[0]):
        if element.decode("utf-8") in szukany_element:
            return indeks
    return -1  # zwracamy -1, jeśli element nie został znaleziony


"""List_of_items = write_excel_BOM_to_list(open_file)
List_of_items_with_missing_values = find_items_without_value_in_cell(
    List_of_items, 19)
sorted_list_of_items_with_missing_values = Sort.list_sort_by_index(
    List_of_items_with_missing_values.copy(), 5)

print(sorted_list_of_items_with_missing_values)
Report.generate_report_txt(sorted_list_of_items_with_missing_values, "name_of_filestr", "search_Path_sld_prt: bytes".encode(
    "utf-8"), "search_Path_sld_prt_revision: bytes".encode("utf-8"), [0, 1, 2, 3, 4, 5, 6, 7, 8])"""


def mega_def():
    # checking type of selected file txt or xlsx
    file = check_file_type()
    open_file = file[0]
    # print('open_file: ', open_file)
    type = file[1]
    # print('type: ', type)

    if type == "txt":
        list_to_report = list_of_excel_files_from_txt(open_file)
        # print('list_to_report: ', list_to_report)

    return True


print(mega_def())
