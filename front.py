import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from script import *

top = tk.Tk()
top.title("Front")
top.geometry("400x200")

fisherman_front = ''
zalihe_front = ''
kategorije_front = ''

# uvoz izabranih fajlova
def uvoz_fisherman():
    filetypes = (('excel', '*.xls'), ('excel', '*.xlsx'), ('excel', '*.xlsm'))
    filename = fd.askopenfilename(title='Open a file', initialdir='/Desktop', filetypes=filetypes)
    fisherman_front = filename
    print(fisherman_front)
    ucitavanje()
    #showinfo(title='Selected File', message=filename)

def uvoz_zalihe():
    filetypes = (('excel', '*.xls'), ('excel', '*.xlsx'), ('excel', '*.xlsm'))
    filename = fd.askopenfilename(title='Open a file', initialdir='/Desktop', filetypes=filetypes)
    zalihe_front = filename
    print(zalihe_front)
    ucitavanje()

def uvoz_kategorije():
    filetypes = (('excel', '*.xls'), ('excel', '*.xlsx'), ('excel', '*.xlsm'))
    filename = fd.askopenfilename(title='Open a file', initialdir='/Desktop', filetypes=filetypes)
    kategorije_front = filename
    print(kategorije_front)
    ucitavanje()
    
def sredi_cene():
    promena_opisa()
    poredjenje_cena()
    promena_cene_zalihe()
    promena_cene_stanje()
    promena_kategorije()
    novi_proizvodi()
    save_excel()

btn_sredi_cene = tk.Button(top, text="Sredi cene", command=sredi_cene)
btn_sredi_cene.pack()
btn_pretraga = tk.Button(top, text="Pretrazi" , command=pretraga_po_sifri)
btn_pretraga.pack()
btn_import_fisherman = tk.Button(top, text="Import Fisherman", command=uvoz_fisherman)
btn_import_fisherman.pack()
btn_import_zalihe = tk.Button(top, text="Import Zalihe", command=uvoz_zalihe)
btn_import_zalihe.pack()
btn_import_kategorije = tk.Button(top, text="Import Kategorije", command=uvoz_kategorije)
btn_import_kategorije.pack()

top.mainloop()