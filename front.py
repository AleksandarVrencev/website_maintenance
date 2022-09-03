import tkinter
top = tkinter.Tk()
top.title("Front")
top.geometry("400x200")


def save():
    print("Save")

def preview():
    print("Preview")

def import_fisherman():
    print("Import Fisherman")

def import_zalihe():
    print("Import Zalihe")

def import_kategorije():
    print("Import Kategorije")


btn_save = tkinter.Button(top, text="Save", command=save)
btn_save.pack()
btn_preview = tkinter.Button(top, text="Preview", command=preview)
btn_preview.pack()
btn_import_fisherman = tkinter.Button(top, text="Import Fisherman", command=import_fisherman)
btn_import_fisherman.pack()
btn_import_zalihe = tkinter.Button(top, text="Import Zalihe", command=import_zalihe)
btn_import_zalihe.pack()
btn_import_kategorije = tkinter.Button(top, text="Import Kategorije", command=import_kategorije)


top.mainloop()