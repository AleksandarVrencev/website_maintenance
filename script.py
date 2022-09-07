from tabnanny import filename_only
from tkinter import messagebox
from tkinter.simpledialog import askstring
from openpyxl import Workbook, load_workbook
from srtools import *
from tkinter import filedialog as fd
import tkinter as tk
#from tkinter import ttk
from tkinter.messagebox import showinfo
import os

top = tk.Tk()
top.title("Front")
top.geometry("500x300")

def sredi_cene():
    promena_opisa()
    poredjenje_cena()
    promena_cene_zalihe()
    promena_cene_stanje()
    promena_kategorije()
    save_excel()

def ucitaj():
    global fisherman_front, zalihe_front, kategorije_front
    global fisherman_book, zalihe_book, kategorije_book
    global fisherman, zalihe, kategorije
    global naslov_fisherman, cena_fisherman, kategorija_fisherman, opis_fisherman, sifra_fisherman
    global artikal_zalihe, naziv_zalihe, cena_zalihe, stanje_zalihe
    global artikal_kategorije, kategorija_kategorije
    global artikal_list, sifra_list, novi_proizvodi_list, stanje_list

    # ucitavanje excel fajlova na osnovu izabranih fajlova u front.py 
    #fisherman_book = load_workbook(filename='fisherman.xlsx')
    fisherman_book = load_workbook(filename=fisherman_front)
    #zalihe_book = load_workbook(filename='zalihe.xlsx')
    zalihe_book = load_workbook(filename=zalihe_front)
    #kategorije_book = load_workbook(filename='kategorije.xlsx')
    kategorije_book = load_workbook(filename=kategorije_front)
    fisherman = fisherman_book.active
    zalihe = zalihe_book.active
    kategorije = kategorije_book.active
    # access the active worksheet data
    naslov_fisherman = fisherman["A"]
    sifra_fisherman = fisherman["B"]
    cena_fisherman = fisherman["C"]
    kategorija_fisherman = fisherman["K"]
    opis_fisherman = fisherman["H"]
    cena_zalihe = zalihe["D"]
    artikal_zalihe = zalihe["A"]
    stanje_zalihe = zalihe["C"]
    naziv_zalihe = zalihe["B"]
    artikal_kategorije = kategorije["A"]
    kategorija_kategorije = kategorije["D"]
    # store cell values in a list for comparing
    sifra_list = []
    artikal_list = []
    stanje_list = []
    novi_proizvodi_list = []

    for row in sifra_fisherman:
        sifra_list.append(row.value.strip())

    for row in artikal_zalihe:
        artikal_list.append(row.value.strip())

    for row in stanje_zalihe:
        stanje_list.append(row.value)


# uvoz izabranih fajlova
filetypes = (('excel', '*.xls'), ('excel', '*.xlsx'), ('excel', '*.xlsm'))

def uvoz_fisherman():
    global fisherman_front, fisherman_path
    filename = fd.askopenfilename(title='Open a file', initialdir='/Desktop', filetypes=filetypes)
    fisherman_front = filename
    #print(fisherman_front)
    #fisherman_path = os.path.dirname(fisherman_front)
    #showinfo(title='Selected File', message=filename)

def uvoz_zalihe():
    global zalihe_front, zalihe_path
    filename = fd.askopenfilename(title='Open a file', initialdir='/Desktop', filetypes=filetypes)
    zalihe_front = filename
    zalihe_path = os.path.dirname(zalihe_front)
    print(zalihe_front)

def uvoz_kategorije():
    global kategorije_front, kategorije_path
    filename = fd.askopenfilename(title='Open a file', initialdir='/Desktop', filetypes=filetypes)
    kategorije_front = filename
    head, tail = os.path.split(kategorije_front)
    print(kategorije_front)
    print(tail)

# provera kolone opis i promena cirilice u latinicu
def promena_opisa():
    for i in range(opis_fisherman.__len__()):
        if opis_fisherman[i].value != None:
            opis_fisherman[i].value = cyrillic_to_latin(opis_fisherman[i].value)
            #print("stara vrednost: " + opis_fisherman[i].value + " nova vrednost: " + cyrillic_to_latin(opis_fisherman[i].value))
        else:
            continue

# novi proizvodi koji se nalaze u zalihama ali nisu u fishermanu 
def novi_proizvodi():
    global artikal_list, sifra_list, novi_proizvodi_list, stanje_list
    global artikal_zalihe, naziv_zalihe, cena_zalihe, stanje_zalihe
    #novi_proizvodi_list.clear()
    print("novi proizvodi: ")
    print("lista: " + str(novi_proizvodi_list))
    for i in range(1,artikal_list.__len__()):
        if artikal_list[i] not in sifra_list:
            print("artikal: " + artikal_zalihe[i].value + "\nnaziv: " + naziv_zalihe[i].value + "\nstanje: " + str(stanje_zalihe[i].value) + "\ncena: " + str(cena_zalihe[i].value))
            novi_proizvodi_list.append([artikal_zalihe[i].value, naziv_zalihe[i].value, stanje_zalihe[i].value, cena_zalihe[i].value])
            #novi proizvod moze da ima stanje manje od 0 ako ovu funkciju preklopis sa funkcijom promena_cene_stanje()
            if stanje_zalihe[i].value > 0:
                counter = 1
                fisherman.cell(row=fisherman.max_row + counter, column=1).value = naziv_zalihe[i].value
                fisherman.cell(row=fisherman.max_row , column=2).value = artikal_zalihe[i].value
                fisherman.cell(row=fisherman.max_row , column=3).value = cena_zalihe[i].value
                fisherman.cell(row=fisherman.max_row , column=4).value = "kom"
                fisherman.cell(row=fisherman.max_row , column=13).value = "2021-04-30 00:00:13"
                     
    print("lista novih proizvoda: " + str(novi_proizvodi_list))
    save_excel()
    # izrada izvestaja o novim proizvodima
    # report = messagebox.askquestion("Report", "Da li zelite da sacuvate report u excel fajl?")
    # if report == 'yes':
    #     report_book = Workbook()
    #     report_sheet = report_book.active
    #     report_sheet.append(["artikal", "naziv", "stanje", "cena"])
    #     for i in range(novi_proizvodi_list.__len__()):
    #         report_sheet.append(novi_proizvodi_list[i])
    #     report_book.save("report.xlsx")
    #     showinfo(title='Report', message="Report je sacuvan u report.xlsx fajlu")

# funkcija za proveru i promenu kategorije
def promena_kategorije():
    for i in range(artikal_kategorije.__len__()):
        for i in range(sifra_fisherman.__len__()):
            if artikal_kategorije[i].value == sifra_fisherman[i].value:
                kategorija_fisherman[i].value = kategorija_kategorije[i].value
                print(kategorija_fisherman[i].value)
            else:
                continue

# proizvodi kojih nema na zalihama ili su na zalihama ali ih nema na stanju, promeni cenu na nulu
# funkcije su razdvojene zbog performansi
def promena_cene_zalihe():
    for i in range(sifra_fisherman.__len__()):
        if sifra_fisherman[i].value not in artikal_list and cena_fisherman[i].value != 0:
            print("fisherman: " + sifra_fisherman[i].value + " cena: " + str(cena_fisherman[i].value) + " nova cena: 0")
            cena_fisherman[i].value = 0
        else:
            continue

def promena_cene_stanje():
    for i in range(sifra_fisherman.__len__()):
        for j in range(artikal_zalihe.__len__()):
            if sifra_fisherman[i].value == artikal_zalihe[j].value and cena_fisherman[i].value != 0 and stanje_zalihe[j].value < 1:
                print("fisherman: " + sifra_fisherman[i].value + " cena: " + str(cena_fisherman[i].value) + " nova cena: 0")
                cena_fisherman[i].value = 0
            else:
                continue

# funkcija za poredjenje cena na zalihama i u fishermanu
def poredjenje_cena():
    for i in range(sifra_fisherman.__len__()):
        for j in range(artikal_zalihe.__len__()):
            if sifra_fisherman[i].value == artikal_zalihe[j].value and cena_fisherman[i].value != cena_zalihe[j].value:
                print("fisherman: " + sifra_fisherman[i].value + " cena: " + str(cena_fisherman[i].value) + " nova cena: " + str(cena_zalihe[j].value))
                cena_fisherman[i].value = cena_zalihe[j].value

# pretraga proizvoda po sifri
def pretraga_po_sifri():
    value = askstring("Pretraga", "Unesite trazeni pojam: ")
    for i in range(sifra_fisherman.__len__()):
        if value in sifra_fisherman[i].value or value in naslov_fisherman[i].value:
            print("naziv: " + naslov_fisherman[i].value + "\nsifra: " + sifra_fisherman[i].value + "\ncena: " + str(cena_fisherman[i].value))
            #break
        else:
            continue

# zapamti u excel
def save_excel():
    # fisherman_book.save('fisherman.xlsx')
    # zalihe_book.save('zalihe.xlsx')
    # kategorije_book.save('kategorije.xlsx')
    fisherman_book.save(fisherman_front)
    zalihe_book.save(zalihe_front)
    kategorije_book.save(kategorije_front)

btn_sredi_cene = tk.Button(top, text="Sredi cene", command=sredi_cene)
btn_sredi_cene.pack()
btn_novi_proizvodi = tk.Button(top, text="Novi proizvodi", command=novi_proizvodi)
btn_novi_proizvodi.pack()
btn_pretraga = tk.Button(top, text="Pretrazi" , command=pretraga_po_sifri)
btn_pretraga.pack()
btn_import_fisherman = tk.Button(top, text="Import Fisherman", command=uvoz_fisherman)
btn_import_fisherman.pack()
btn_import_zalihe = tk.Button(top, text="Import Zalihe", command=uvoz_zalihe)
btn_import_zalihe.pack()
btn_import_kategorije = tk.Button(top, text="Import Kategorije", command=uvoz_kategorije)
btn_import_kategorije.pack()
btn_ucitaj = tk.Button(top, text="ucitaj", command=ucitaj)
btn_ucitaj.pack()
top.mainloop()