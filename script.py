from openpyxl import Workbook, load_workbook
from srtools import *

fisherman_book = load_workbook(filename='fisherman.xlsx')
zalihe_book = load_workbook(filename='zalihe.xlsx')
kategorije_book = load_workbook(filename='kategorije.xlsx')

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
    print("novi proizvodi: ")
    for i in range(1,artikal_list.__len__()):
        if artikal_list[i] not in sifra_list:
            print("artikal: " + artikal_zalihe[i].value + "\nnaziv: " + naziv_zalihe[i].value + "\nstanje: " + str(stanje_zalihe[i].value) + "\ncena: " + str(cena_zalihe[i].value))
            novi_proizvodi_list.append([artikal_zalihe[i].value, naziv_zalihe[i].value, stanje_zalihe[i].value, cena_zalihe[i].value])
            if stanje_zalihe[i].value > 0:
                counter = 1
                fisherman.cell(row=fisherman.max_row + counter, column=1).value = naziv_zalihe[i].value
                fisherman.cell(row=fisherman.max_row , column=2).value = artikal_zalihe[i].value
                fisherman.cell(row=fisherman.max_row , column=3).value = cena_zalihe[i].value
                fisherman.cell(row=fisherman.max_row , column=4).value = "kom"
                fisherman.cell(row=fisherman.max_row , column=13).value = "2021-04-30 00:00:13"
                     
    print("lista novih proizvoda: " + str(novi_proizvodi_list))

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
def pretraga_po_sifri(pojam_za_pretragu):
        for i in range(sifra_fisherman.__len__()):
            if pojam_za_pretragu == sifra_fisherman[i].value:
                print("naziv: " + naslov_fisherman[i].value + "\nsifra: " + sifra_fisherman[i].value + "\ncena: " + str(cena_fisherman[i].value))
                break
            else:
                continue

# zapamti u excel
def save_excel():
    fisherman_book.save('fisherman.xlsx')
    zalihe_book.save('zalihe.xlsx')
    kategorije_book.save('kategorije.xlsx')

# red izvršavanja funkcija je važan
# promena_opisa()
# poredjenje_cena()
# promena_cene_zalihe()
# promena_cene_stanje()
# promena_kategorije()
# novi_proizvodi()
# pretraga_po_sifri('02000')
save_excel()