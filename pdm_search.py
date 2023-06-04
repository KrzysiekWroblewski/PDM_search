# main branch

from tkinter import Tk, Label, Button, Radiobutton, IntVar
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import csv
import pyperclip
import ctypes


search_Path = u""
sep = "|"
user_delimiter = ';'
part_column = 3


def ask_multiple_choice_question(prompt, options, separators, part_column_positions):
    root = Tk()
    if prompt:
        Label(root, text=prompt).pack()

    v = IntVar()
    v2 = IntVar()
    v3 = IntVar()

    T = tk.Text(root, height=2, width=60)
    T.pack()
    T.insert(tk.END, "Wybierz jakie pliki chcesz wyszukać")

    for i, option in enumerate(options):
        Radiobutton(root, text=option, variable=v, value=i).pack(anchor="w")

    T = tk.Text(root, height=2, width=60)
    T.pack()
    T.insert(tk.END, "Wybierz separator kolumn w .csv")

    for i, separator in enumerate(separators):
        Radiobutton(root, text=separator, variable=v2,
                    value=i).pack(anchor="w")

    T = tk.Text(root, height=2, width=60)
    T.pack()
    T.insert(tk.END, "Wybierz nr kolumny w której znajduje się nr części")

    for i, part_column_position in enumerate(part_column_positions):
        Radiobutton(root, text=part_column_position, variable=v3,
                    value=i).pack(anchor="w")

    Button(text="Akceptuj", command=root.destroy).pack()

    root.mainloop()

    # if v.get() == 0:
    #    return None

    return options[v.get()], separators[v2.get()], part_column_positions[v3.get()]


result = ask_multiple_choice_question(
    "PDM search engine",
    ["Files with revision: PDF, DXF, STP",
        "Solid Works Files"],
    [";",
     ","],
    [3, 2, 1, 4, 5]
)


# print("User's response was: {}".format(repr(result)))
root = tk.Tk()
root.withdraw()
# file_path = filedialog.askopenfilename()
open_file = filedialog.askopenfilename()


# print(result)
user_delimiter = str(result[1])
part_column = int(result[2]-1)

# print(part_column)

number_of_files_merged = 0
with open(open_file, encoding='latin-1', mode='r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=user_delimiter)

    for line in csv_reader:

        # rows, should not have empty spaces, function delate them
        for word in range(0, len(line)):
            line[word] = line[word].replace(' ', '')

        # prevents from index error if row is empty
        if line == []:
            continue

        elif result[0] == "Files with revision: PDF, DXF, STP":
            search_Path = search_Path + \
                str(line[part_column]) + "-" + \
                str(line[part_column+1]) + str(sep)

        elif result[0] == "Solid Works Files":
            search_Path = search_Path + str(line[part_column]) + str(sep)

        number_of_files_merged = number_of_files_merged + 1

if search_Path[-1] == "|":
    search_Path = search_Path[:-1]

search_Path_encoded = search_Path.encode(encoding='latin-1', errors='strict')
search_Path_decoded = search_Path_encoded.decode('utf-8', 'strict')
pyperclip.copy(search_Path_decoded)


Message_01 = str("Source file path: " + str(open_file) +
                 str("\n") + str("\n") + "Number of files: " + str(number_of_files_merged))

print(Message_01)


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


Mbox("Wyszukiwarka PDM via CSV", Message_01, 1)
