from tkinter import Tk, Label, Button, Radiobutton, IntVar
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import csv
import pyperclip
import ctypes


def ask_multiple_choice_question(prompt, options):
    root = Tk()
    if prompt:
        Label(root, text=prompt).pack()
    v = IntVar()
    for i, option in enumerate(options):
        Radiobutton(root, text=option, variable=v, value=i).pack(anchor="w")
    Button(text="Akceptuj", command=root.destroy).pack()
    root.mainloop()
    if v.get() == 0:
        return None
    return options[v.get()]


result = ask_multiple_choice_question(
    "Jakie pliki chesz wyszukać",
    [
        "Pliki PDF, DXF, STP",
        "Pliki Solid Works",
    ]
)

# print("User's response was: {}".format(repr(result)))


root = tk.Tk()
root.withdraw()
# file_path = filedialog.askopenfilename()
open_file = filedialog.askopenfilename()


if result == "Pliki Solid Works":

    a = ""
    sep = "|"

    with open(open_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        for line in csv_reader:
            a = a + str(line[0]) + "-" + str(line[1]) + str(sep)
            pyperclip.copy(a)
            # print(a)


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


Mbox("Wyszukiwarka PDM via CSV", 'Skopiowano dane wyszukiwania do schowka', 1)
