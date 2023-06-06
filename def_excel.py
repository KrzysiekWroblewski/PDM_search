import openpyxl
import pyperclip

# open_file = "sample.xlsx"


def read_excel_BOM(open_file):

    xl_part_column = 7
    csv_sep = "|"

    wrkbk = openpyxl.load_workbook(open_file)
    sh = wrkbk.active

    search_Path = ""
    number_of_files_merged = 0

    for j in range(6, sh.max_row+1):
        cell_obj = sh.cell(row=j, column=xl_part_column)
        # cell_revision = sh.cell(row=j, column=part_column+1)

        # Checking if  are some missing drawings
        for i in range(3, 6):
            if sh.cell(row=j, column=i).value == None:
                drawings = False
                break
            else:
                drawings = True

        if drawings == False:
            search_Path = search_Path + \
                str(cell_obj.value) + csv_sep
            number_of_files_merged = number_of_files_merged + 1

    try:
        if search_Path[-1] == "|":
            search_Path = search_Path[:-1]
    except:
        pass

    search_Path = search_Path.encode(
        'utf-8').decode('ascii', 'ignore')
    print(search_Path)

    print(number_of_files_merged)

    pyperclip.copy(search_Path)

    return (number_of_files_merged, search_Path)
# read_excel_BOM(open_file)
