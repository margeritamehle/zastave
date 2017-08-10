import tkinter as tk

okno = tk.Tk()
zgoraj = tk.Frame(okno)
spodaj = tk.Frame(okno)
oznaka = tk.Label(zgoraj, text = '''Kako dobro poznaš zastave držav sveta?
Izberi kontinent.''')


gumb1 = tk.Button(spodaj, height = 2, width = 20, text = "Afrika")
gumb2 = tk.Button(spodaj, height = 2, width = 20, text = "Avstralija in Oceanija")
gumb3 = tk.Button(spodaj, height = 2, width = 20, text = "Azija")
gumb4 = tk.Button(spodaj, height = 2, width = 20, text = "Evropa")
gumb5 = tk.Button(spodaj, height = 2, width = 20, text = "Južna Amerika")
gumb6 = tk.Button(spodaj, height = 2, width = 20, text = "Severna in Srednja Amerika")

zgoraj.pack()
spodaj.pack()
oznaka.grid(row = 0, column = 0)


gumb1.grid(row = 1, column = 0)
gumb2.grid(row = 2, column = 0)
gumb3.grid(row = 3, column = 0)
gumb4.grid(row = 4, column = 0)
gumb5.grid(row = 5, column = 0)
gumb6.grid(row = 6, column = 0)

def odpri_novo_okno(event):
    okno_s_kvizom = tk.Tk()
    zgornji = tk.Frame(okno_s_kvizom)
    spodnji = tk.Frame(okno_s_kvizom)

    mesto_slike = tk.Label(zgornji, text = "tukaj bo slika")
    vprasanje = tk.Label(zgornji, text = "Kateri državi pripada zastava?")
    odgovor1 = tk.Button(spodnji, height = 2, width = 20)
    odgovor2 = tk.Button(spodnji, height = 2, width = 20)
    odgovor3 = tk.Button(spodnji, height = 2, width = 20)
    odgovor4 = tk.Button(spodnji, height = 2, width = 20)

    zgornji.pack()
    spodnji.pack()

    mesto_slike.grid(row = 0, column = 0)
    vprasanje.grid(row = 1, column = 0)
    odgovor1.grid(row = 0, column = 0)
    odgovor2.grid(row = 0, column = 1)
    odgovor3.grid(row = 1, column = 0)
    odgovor4.grid(row = 1, column = 1)
    
gumb1.bind("<Button-1>", odpri_novo_okno)
gumb2.bind("<Button-1>", odpri_novo_okno)
gumb3.bind("<Button-1>", odpri_novo_okno)
gumb4.bind("<Button-1>", odpri_novo_okno)
gumb5.bind("<Button-1>", odpri_novo_okno)
gumb6.bind("<Button-1>", odpri_novo_okno)



okno.mainloop()
