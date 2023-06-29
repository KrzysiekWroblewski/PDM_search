import tkinter as tk
import ctypes
from tkinter import Tk, Label, Button, Radiobutton, IntVar, filedialog
import sys


class GUI:

    @staticmethod
    def ask_multiple_choice_question(prompt, options, separators, part_column_positions):

        root = Tk()

        # Wykonaj pewne czynności przed zamknięciem okna
        root.protocol("WM_DELETE_WINDOW", GUI.on_closing)

        if prompt:
            Label(root, text=prompt).pack()

        v = IntVar()
        v2 = IntVar()
        v3 = IntVar()

        T = tk.Text(root, height=2, width=60)
        T.pack()
        T.insert(tk.END, "Wybierz jakie pliki chcesz wyszukać")

        for i, option in enumerate(options):
            Radiobutton(root, text=option, variable=v,
                        value=i).pack(anchor="w")

        T = tk.Text(root, height=2, width=60)
        T.pack()
        T.insert(tk.END, "Wybierz separator kolumn w .csv")

        for i, separator in enumerate(separators):
            Radiobutton(root, text=separator, variable=v2,
                        value=i).pack(anchor="w")

        T = tk.Text(root, height=5, width=60)
        T.pack()
        T.insert(tk.END, "Wybierz nr kolumny w której znajduje się nr części" + "\n" + "(bazowo 3 kolumna)" + "\n" + "\n" +
                 "-1--|-2-|------3-----|4|----5----|" + "\n" +
                 "2011;901;PRT-A0069990;A;Mocowanie"
                 )

        for i, part_column_position in enumerate(part_column_positions):
            Radiobutton(root, text=part_column_position, variable=v3,
                        value=i).pack(anchor="w")

        Button(text="Akceptuj", command=root.destroy).pack()

        root.mainloop()

        return options[v.get()], separators[v2.get()], part_column_positions[v3.get()]

    @staticmethod
    def on_closing():
        sys.exit()

    @staticmethod
    def Mbox(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    @staticmethod
    def select_file():
        root = tk.Tk()
        root.withdraw()
        open_file = filedialog.askopenfilename()
        return open_file

    @staticmethod
    def select_folder():
        root = tk.Tk()
        root.withdraw()
        open_directory = filedialog.askdirectory()
        return open_directory
