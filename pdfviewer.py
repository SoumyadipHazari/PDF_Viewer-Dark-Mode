from tkinter import *

from tkinter import ttk

from tkinter import filedialog as fd

import os

class pdfviewer:
    def __init__(self, master):
        self.master = master
        self.master.title = ('PDF Viewer')
        self.master.geometry('580x520+440+180')
        self.master.iconbitmap(self.master, 'assets/pdf.ico') #<a href="https://www.flaticon.com/free-icons/pdf" title="pdf icons">Pdf icons created by rizal2109 - Flaticon</a>

        self.path = None
        self.fileisopen = None
        self.author = None
        self.name = None
        self.current_page = 0
        self.numPages = None
#Adding menu

        self.menu = Menu(self.master)
        self.master.config(menu = self.menu)
        self.filemenu = Menu(self.menu)
#Adding menu option
        self.menu.add_cascade(label="File", menu=self.filemenu)

        self.filemenu.add_command(label="Open FIle")
        self.filemenu.add_command(label="Exit")
#Adding top frame

        self.top_frame = ttk.Frame(self.master, width=580, height=460)
        self.top_frame.grid(row=0, column = 0)
        self.top_frame.grid_propagate(False)
#Adding bottom frame        

        self.bottom_frame = ttk.Frame(self.master, width=580, height=50)
        self.bottom_frame.grid(row=1, column=0)
        self.bottom_frame.grid_propagate(False)
#Adding scrollbar

        self.scroll = Scrollbar(self.top_frame, orient=VERTICAL)
        self.scroll.grid(row=0, column=1, sticky=(N,S))

        self.scrollx = Scrollbar(self.top_frame, orient=HORIZONTAL)
        self.scrollx.grid(row=1, column=0, sticky=(W, E))

        self.output = Canvas(self.top_frame, bg='#ECE8F3', width=560, height=435)
        self.output.configure(yscrollcommand=self.scroll.set, xscrollcommand=self.scrollx.set)
        self.output.grid(row=0, column=0)
        self.scroll.configure(command=self.output.yview)
        self.scrollx.configure(command=self.output.xview)
#adding button png

        self.uparrow_icon = PhotoImage(file="assets/arrow.png")#<a href="https://www.flaticon.com/free-icons/uparrow" title="uparrow icons">Uparrow icons created by kowshal-kumar - Flaticon</a>
        self.downarrow_icon = PhotoImage(file= 'assets/arrows.png')#<a href="https://www.flaticon.com/free-icons/downarrow" title="downarrow icons">Downarrow icons created by kowshal-kumar - Flaticon</a>
#resizing png

        self.uparrow = self.uparrow_icon.subsample(3,3)
        self.downarrow = self.downarrow_icon.subsample(3,3)
#creating upper button


        self.upb = ttk.Button(self.bottom_frame, image=self.uparrow)
        self.upb.grid(row=0, column=1, padx=(270, 5), pady=8)

#creating down button

        self.downb = ttk.Button(self.bottom_frame, image=self.downarrow)
        self.downb.grid(row=0, column=3, pady=8)

#label for displaying page no.

        self.page_label= ttk.Label(self.bottom_frame, text='page')
        self.page_label.grid(row=0, column=4, padx=5)






root = Tk()
app = pdfviewer(root)
root.mainloop()