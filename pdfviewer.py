from tkinter import *

from tkinter import ttk

from tkinter import filedialog as fd

import os

class pdfviewer:
    def __init__(self, master):
        self.master = master
        self.master.title = ('PDF Viewer')
        self.master.geometry('580x520+440+180')
        self.master.iconbitmap(self.master, 'assets/pdf.ico')

        self.path = None
        self.fileisopen = None
        self.author = None
        self.name = None
        self.current_page = 0
        self.numPages = None

        self.menu = Menu(self.master)
        self.master.config(menu = self.menu)
        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)

        self.filemenu.add_command(label="Open FIle")
        self.filemenu.add_command(label="Exit")

        self.top_frame = ttk.Frame(self.master, width=580, height=460)
        self.top_frame.grid(row=0, column = 0)
        self.top_frame.grid_propagate(False)
        
        self.bottom_frame = ttk.Frame(self.master, width=580, height=50)
        self.bottom_frame.grid(row=1, column=0)
        self.bottom_frame.grid_propagate(False)



root = Tk()
app = pdfviewer(root)
root.mainloop()