

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
import os
import file_extension_select_func_2
import file_extension_select_gui

#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self, master, *args, **kwargs)

        #define our master frame configuration
        self.master = master
        self.master.minsize(481, 180) 
        self.master.maxsize(1000, 1000)
        self.master.title("file_extension database search ")
        self.master.configure(bg="#F0F0F0")

        for x in range(4):  
            self.master.grid_columnconfigure(x, weight=1)
            self.master.grid_rowconfigure(x, weight=1)




        #This protocol method is a tkinter build-in method to catch if
        #the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: file_extension_select_func_2.ask_quit(self))
        arg = self.master

        #load in the GUI widgets from a separate module,
        #keeping your code comparmentalized and clutter free
        file_extension_select_gui.load_gui(self)




if __name__=="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
