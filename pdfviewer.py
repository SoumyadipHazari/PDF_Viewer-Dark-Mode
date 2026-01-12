from tkinter import *

from tkinter import ttk

from tkinter import filedialog as fd

import os

class pdfviewer:
    def __init__(self, master):
        self.master = master
        self.master.title = ('PDF Viewer')
        self.master.geometry('580x520+440+180')
        self.master.resizable(width = 0, height = 0)
        self.master.iconbitmap(self.master, 'assets/pdf.ico')

        self.path = None
        self.fileisopen = None
        self.author = None
        self.name = None
        self.current_page = 0
        self.numPages = None

root = Tk()
app = pdfviewer(root)
root.mainloop()