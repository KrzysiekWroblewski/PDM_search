from decoding import open_file_encoding
from def_excel import read_excel_BOM
from gui import GUI
from test import write_excel_BOM_to_list
from test import find_items_without_value_in_cell
from test import znajdz_indeks
from excel_raport_generator import Report
from List_sorting import Sort


# Choose separator for search
csv_sep = "|"


# run function - window with selection window
result = GUI.ask_multiple_choice_question(
    "PDM search engine",
    ["Files with revision: PDF, DXF, STP",
        "Solid Works Files",
        "Braki rysunków w Excel",
        "Braki zamówień w Excel"],
    [";",
     ","],
    [3, 2, 1, 4, 5]
)
csv_delimiter = str(result[1])
part_column = int(result[2]-1)


# run window file_path = filedialog.askopenfilename()
open_file = GUI.select_file()

# Loop fo searching missing drawings in excel
if result[0] == "Braki rysunków w Excel":
    merged_text = read_excel_BOM(open_file)
    Message_01 = str("Source file path: " + str(open_file) +
                     str("\n") + str("\n") + "Number of missing files: " + str(merged_text[0]))

if result[0] == "Braki zamówień w Excel":
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

# Loop try to decode .csv files
if result[0] == "Solid Works Files" or result[0] == "Files with revision: PDF, DXF, STP":
    decoding_list = ["latin-1", "utf-16-le", "utf-8"]
    i = 0
    decoded = False
    for decode in decoding_list:
        try:
            csv_encode = decoding_list[i]
            # merging text function
            merged_text = open_file_encoding(open_file, csv_encode, result,
                                             csv_delimiter, csv_sep, part_column)
            decoded = True
            break
        except:
            print("Decoding", decoding_list[i], "do not work")
            i = i + 1

    if decoded != True:
        GUI.Mbox("Wyszukiwarka PDM via CSV",
                 "Błędna operacja lub błędny wybór kolumny numeru części", 1)

    Message_01 = str("Source file path: " + str(open_file) +
                     str("\n") + str("\n") + "Number of files: " + str(merged_text[0]))


print(Message_01)
GUI.Mbox("Wyszukiwarka PDM via CSV", Message_01, 1)
