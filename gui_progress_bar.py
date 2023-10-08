from tkinter import *
from tkinter import ttk

from tkinter import Tk, Label, Button, Radiobutton, IntVar, filedialog
from tkinter import Tk, simpledialog
import os


class Order():
    def __init__(self):
        self.excel_path = ""
        self.drawings_path = ""
        self.order_num = ""
        self.export_path = ""
        self.user = ""
        self.project_number = ""
        self.date = ""


def GUI_make_order(name):

    def select_file():
        open_file = filedialog.askopenfilename()
        return open_file

    def select_folder():
        open_directory = filedialog.askdirectory()
        return open_directory

    def Get_Excel_File_Path():
        name.excel_path = e1.get()
        return name.excel_path

    def Get_Drawings_Directory():
        name.drawings_path = e2.get()
        return name.drawings_path

    def Get_Order_Number():
        name.order_num = e3.get()
        return name.order_num

    def Get_Export_Path():
        name.export_path = e4.get()
        return name.export_path

    def input_to_entry(text, entry):
        entry.delete(0, END)
        entry.insert(0, text)

    def all():
        Get_Excel_File_Path()
        Get_Drawings_Directory()
        Get_Order_Number()
        Get_Export_Path()
        root.destroy()

    root = Tk()
    root.title("PDM_Search")
    root.geometry("900x400")

    ttk.Label(root,
              text="Excel File Path", width=20).grid(row=0)
    ttk.Label(root,
              text="Drawings Directory", width=20).grid(row=1)
    ttk.Label(root,
              text="Order Number", width=20).grid(row=2)
    ttk.Label(root,
              text="Select folder for export", width=20).grid(row=3)

    e1 = ttk.Entry(root, width=100)
    e2 = ttk.Entry(root, width=100)
    e3 = ttk.Entry(root, width=100)
    e4 = ttk.Entry(root, width=100)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)

    Select_Excel_File = ttk.Button(root,
                                   text='Select Excel File', width=25, command=lambda: input_to_entry(select_file(), e1))
    Select_Excel_File.grid(row=0, column=2, sticky=W, pady=4)

    Select_Drawings_Dir = ttk.Button(root,
                                     text='Select Drawings Directory', width=25, command=lambda: input_to_entry(select_folder(), e2))
    Select_Drawings_Dir.grid(row=1, column=2, sticky=W, pady=4)

    Select_Drawings_dir_to_export = ttk.Button(root,
                                               text='Select Path to save Order', width=25, command=lambda: input_to_entry(select_folder(), e4))
    Select_Drawings_dir_to_export.grid(row=3, column=2, sticky=W, pady=4)

    Quit = ttk.Button(root,
                      text='Quit', command=root.destroy).grid(row=4,
                                                              column=0,
                                                              sticky=W,
                                                              pady=4)

    ttk.Button(root, text='Generate Order', command=all).grid(row=4,
                                                              column=1,
                                                              sticky=W,
                                                              pady=4)

    root.mainloop()

    return (name.excel_path, name.drawings_path, name.order_num, name.export_path)


# https://python-course.eu/tkinter/entry-widgets-in-tkinter.php
