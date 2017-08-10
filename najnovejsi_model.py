import os
import random
from PIL import Image

celina = input('''Izberi celino. Na voljo so: Afrika, Avstralija
                    in Oceanija, Azija, Evropa, Juzna Amerika,
                    Severna in Srednja Amerika. ''')
datoteka = None
seznam_slik = []
seznam_imen = []
nakljucna_zastava = ""
                        
def pot_do_slik(celina):
    if celina == "Afrika":
        os.chdir("C:/Users/MMArgerita/zastave/slike_zastav/Afrika")
    elif celina == "Avstralija in Oceanija":
        os.chdir("C:/Users/MMArgerita/zastave/slike_zastav/Avstralija_in_Oceanija")
    elif celina == "Azija":
        os.chdir("C:/Users/MMArgerita/zastave/slike_zastav/Azija")
    elif celina == "Evropa":
        os.chdir("C:/Users/MMArgerita/zastave/slike_zastav/Evropa")
    elif celina == "Juzna Amerika":
        os.chdir("C:/Users/MMArgerita/zastave/slike_zastav/Juzna_Amerika")
    elif celina == "Severna in Srednja Amerika":
        os.chdir("C:/Users/MMArgerita/zastave/slike_zastav/Severna_in_Srednja_Amerika")
    kje = os.getcwd()
    return kje

def izbira_datoteke(celina):
    global datoteka
    if celina == "Afrika":
        datoteka = "kontinent1.txt"
    elif celina == "Avstralija in Oceanija":
        datoteka = "kontinent2.txt"
    elif celina == "Azija":
        datoteka = "kontinent3.txt"
    elif celina == "Evropa":
        datoteka = "kontinent4.txt"
    elif celina == "Juzna Amerika":
        datoteka = "kontinent5.txt"
    else:
        datoteka = "kontinent6.txt"
    return datoteka

def naredi_seznam_slik():
    izbira_datoteke(celina)
    global seznam_slik
    with open(datoteka) as dat:
        for vrstica in dat:
            besede = vrstica.strip().split(":")
            if len(besede) == 2:
                slika = besede[0]
                seznam_slik.append(slika)
    return seznam_slik

def naredi_seznam_imen():
    izbira_datoteke(celina)
    global seznam_imen
    with open(datoteka) as dat:
        for vrstica in dat:
            besede = vrstica.strip().split(":")
            if len(besede) == 2:
                ime = besede[1]
                seznam_imen.append(ime)
    return seznam_imen

def prikaz_slike():
    naredi_seznam_slik()
    global nakljucna_zastava

    nakljucna_zastava = random.choice(seznam_slik)
    print(nakljucna_zastava)

    pot_do_slik(celina)
    
    im = Image.open(nakljucna_zastava)
    im.show()

def vprasanje():
    print("Kateri državi pripada ta zastava?")
    naredi_seznam_imen()
    print(seznam_imen)
    prikaz_slike()
    
    global nakljucna_zastava
    
    razdeljeno_ime = nakljucna_zastava.split(".")
    print(razdeljeno_ime)
    pravilen_odgovor = razdeljeno_ime[0]
    print(pravilen_odgovor)

    


    return True
    
