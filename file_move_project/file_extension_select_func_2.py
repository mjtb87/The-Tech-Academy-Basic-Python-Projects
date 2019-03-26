from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
import tkinter as tk
import os
import file_extension_select_main
import file_extension_select_gui
import sqlite3
import shutil

def file_dialog(txt_entry):
    txt_entry.set(filedialog.askdirectory())



def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes the app
        self.master.destroy()
        os._exit(0)

def getTextFiles(source_string):
    file_list = os.listdir(source_string)
    text_file_list = []
    for i in file_list:
        if '.txt' in i:
            text_file_list.append(i)
    return(text_file_list)

def getModTime(file_path):
    return datetime.fromtimestamp(os.path.getmtime(file_path))

def process_files(source, destination):
    createTable()
    for i in getTextFiles(source.get()):
        source_path = os.path.join(source.get(), i)
        destination_path = destination.get()

        modtime = getModTime(source_path)
        createRows(i, modtime)
        move_files(source_path, destination_path)
        print("source: {} \nmod time: {}".format(i, modtime))

def move_files(source_string, destination_string):
    shutil.move(source_string, destination_string)


def createTable():
    conn = sqlite3.connect('python_txt_ext_database_project.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_file_move_time( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, col_mtime TEXT)")
        conn.commit()
    conn.close()



def createRows(file_name, mtime):
    conn = sqlite3.connect('python_txt_ext_database_project.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_file_move_time (col_fname, col_mtime) VALUES (?,?)", (file_name,mtime))
        conn.commit()
    conn.close()


if __name__=="__main__":
    pass
