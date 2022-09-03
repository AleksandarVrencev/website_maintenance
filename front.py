import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from script import *


top = tk.Tk()
top.title("Front")
top.geometry("400x200")


def save():
    pass

def preview():
    print("Preview")

def import_fisherman():
    print("Import Fisherman")

def import_zalihe():
    print("Import Zalihe")

def import_kategorije():
    print("Import Kategorije")

fisherman_front = ''
zalihe_front = ''
kategorije_front = ''

# uvoz izabranih fajlova
def uvoz_fisherman():
    filetypes = (('excel', '*.xls'), ('excel', '*.xlsx'), ('excel', '*.xlsm'))
    filename = fd.askopenfilename(title='Open a file', initialdir='/Desktop', filetypes=filetypes)
    fisherman_front = filename
    print(fisherman_front)
    #showinfo(title='Selected File', message=filename)

def uvoz_zalihe():
    filetypes = (('excel', '*.xls'), ('excel', '*.xlsx'), ('excel', '*.xlsm'))
    filename = fd.askopenfilename(title='Open a file', initialdir='/Desktop', filetypes=filetypes)
    zalihe_front = filename
    print(zalihe_front)

def uvoz_kategorije():
    filetypes = (('excel', '*.xls'), ('excel', '*.xlsx'), ('excel', '*.xlsm'))
    filename = fd.askopenfilename(title='Open a file', initialdir='/Desktop', filetypes=filetypes)
    kategorije_front = filename
    print(kategorije_front)
    
btn_save = tk.Button(top, text="Save", command=import_fisherman)
btn_save.pack()
btn_preview = tk.Button(top, text="Preview", command=preview)
btn_preview.pack()
btn_import_fisherman = tk.Button(top, text="Import Fisherman", command=uvoz_fisherman)
btn_import_fisherman.pack()
btn_import_zalihe = tk.Button(top, text="Import Zalihe", command=uvoz_zalihe)
btn_import_zalihe.pack()
btn_import_kategorije = tk.Button(top, text="Import Kategorije", command=uvoz_kategorije)
btn_import_kategorije.pack()

top.mainloop()