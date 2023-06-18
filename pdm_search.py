from decoding import open_file_encoding
from def_excel import read_excel_BOM
from gui import GUI


# Choose separator for search
csv_sep = "|"


# run function - window with selection window
result = GUI.ask_multiple_choice_question(
    "PDM search engine",
    ["Files with revision: PDF, DXF, STP",
        "Solid Works Files",
        "Braki w Excel"],
    [";",
     ","],
    [3, 2, 1, 4, 5]
)
csv_delimiter = str(result[1])
part_column = int(result[2]-1)


# run window file_path = filedialog.askopenfilename()
open_file = GUI.select_file()

# Loop fo searching missing drawings in excel
if result[0] == "Braki w Excel":
    merged_text = read_excel_BOM(open_file)
    Message_01 = str("Source file path: " + str(open_file) +
                     str("\n") + str("\n") + "Number of missing files: " + str(merged_text[0]))

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
