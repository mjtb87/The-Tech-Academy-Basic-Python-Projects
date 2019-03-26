
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
import os
import file_extension_select_func_2
import file_extension_select_main



def load_gui(self):
    self.source_string = StringVar()
    self.destination_string = StringVar()

    # this creates a button and text field for the users selected source directory.
    self.txt_source_dir = tk.Entry(self.master, textvariable=self.source_string)
    self.txt_source_dir.grid(row=1, column=1, columnspan=3, padx=15, sticky='EW')

    self.btn_source_dir = tk.Button(self.master, width=16, height=1, text='Source Directory', command=lambda: file_extension_select_func_2.file_dialog(self.source_string))
    self.btn_source_dir.grid(row=1)

    # this creates a button and text field for the users selected destination directory.
    self.txt_dest_dir = tk.Entry(self.master, textvariable=self.destination_string)
    self.txt_dest_dir.grid(row=2, column=1, columnspan=3, padx=15, sticky='EW')

    self.btn_dest_dir = tk.Button(self.master, width=16, height=1, text='Destination Directory', command=lambda: file_extension_select_func_2.file_dialog(self.destination_string))
    self.btn_dest_dir.grid(row=2)

    # this creates a button that will call the function to iterate through the users selected source folder for files with a .txt extension and move them to the selected destination folder.
    self.btn_source_dir = tk.Button(self.master, width=16, height=1, text='Move text files', command=lambda: file_extension_select_func_2.process_files(self.source_string, self.destination_string))
    self.btn_source_dir.grid(row=3)

    # this button creates a promt asking they user if they are sure they want to close the program
    self.btn_close = tk.Button(self.master, width=12, height=1, text='Close Program', command=lambda: self.ask_quit())
    self.btn_close.grid(row=3, column=3, padx=15, sticky='E')




if __name__=="__main__":
    pass