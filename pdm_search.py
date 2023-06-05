from tkinter import *
from decoding import open_file_encoding
from gui import ask_multiple_choice_question
from gui import Mbox
from gui import select_file


# Choose separator for search
csv_sep = "|"


# run function - window with selection window
result = ask_multiple_choice_question(
    "PDM search engine",
    ["Files with revision: PDF, DXF, STP",
        "Solid Works Files"],
    [";",
     ","],
    [3, 2, 1, 4, 5]
)
csv_delimiter = str(result[1])
part_column = int(result[2]-1)


# run window file_path = filedialog.askopenfilename()
open_file = select_file()


# Loop try to decode .csv files
decoding_list = ["latin-1", "utf-16-le", "utf-8"]
i = 0
for decode in decoding_list:
    try:
        csv_encode = decoding_list[i]
        # merging text function
        merged_text = open_file_encoding(open_file, csv_encode, result,
                                         csv_delimiter, csv_sep, part_column)
        break
    except:
        print("Decoding", decoding_list[i], "do not work")
        i = i+1


# Final message
Message_01 = str("Source file path: " + str(open_file) +
                 str("\n") + str("\n") + "Number of files: " + str(merged_text[0]))
print(Message_01)
Mbox("Wyszukiwarka PDM via CSV", Message_01, 1)
