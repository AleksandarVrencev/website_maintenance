# website_maintenance
program za održavanje veb sajta
python, openpyxl, srtools, excel, tkinter, os 

# funkcije

funkcija sredi_cene() služi za objedinjavanje više različitih funkcija

funkcija ucitaj() čita podatke iz uvezenih datoteka, inicijalizuje i dodeljuje vrednosti promenljivama, takođe liste se pune prečišćenim podacima

funkcija promena_opisa() služi za proveru i pretvaranje ćiriličnih slova u latinična

funkcije uvoz_fisherman, uvoz_zalihe i uvoz_kategorije se koriste za korisniči izbor i uvoz datoteka isključivo u excel formatu

funkcija novi_proizvodi() sve proizvode koji su u datoteci zalihe i kojih nema u datoteci fisherman upisuje u posebnu listu, dodaje nove proizvode u fisherman i nudi mogućnost izrade izveštaja u formi nove excel datoteke pod nazivom report.xlsx

funkcija promena_kategorije() koristi datoteke fisherman i kategorije za poređenje upisanih kategorija, datoteka kategorije ima prednost

funkcija poredjenje_cena() poredi cene iz datoteka zalihe i fisherman, datoteka zalihe ima prednost

funkcije promena_cene_zalihe() i promena_cene_stanje() postavljaju cene proizvoda na nulu ako proizvod je proizvod u datoteci zalihe, stanje mu je manje od jedan i cena mu se razlikuje od nule ili ako proizvod ne postoji u datoteci zalihe

funkcija pretraga_po_sifri() omogućava pretragu na osnovu upisanog naziva ili upisane šifre proizvoda, funkcija vraća rezultat samo u slučaju potpunog podudaranja, za napredne korisnike postoji mogućnost listanja svih proizvoda čiji naziv ili šifra sadrži upisani pojam

funkcija save_excel() služi za čuvanje rezultata rada programa

# dugmad

