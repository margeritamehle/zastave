import os
import random
from PIL import Image

celina = input('''Izberi celino. Na voljo so: Afrika, Avstralija
                    in Oceanija, Azija, Evropa, Juzna Amerika,
                    Severna in Srednja Amerika. ''')
datoteka = None
slovar_slik = {}
stevilo_drzav = 0

                      
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

def pot_do_datotek():
    os.chdir("C:/Users/MMArgerita/zastave")
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

def naredi_slovar_slik():
    izbira_datoteke(celina)
    global slovar_slik
    with open(datoteka) as dat:
        for vrstica in dat:
            besedi = vrstica.strip().split(":")
            if len(besedi) == 2:
                slika = besedi[0]
                ime_slike = besedi[1]
                slovar_slik[slika] = ime_slike
    return slovar_slik



def prikaz_slike():
    naredi_slovar_slik()
    global nakljucna_zastava

    nakljucna_zastava = random.choice(list(slovar_slik.items()))
    print(nakljucna_zastava)

    pot_do_slik(celina)
    
    im = Image.open(nakljucna_zastava[0])
    im.show()

    pot_do_datotek()
    
def dolzina_datotek():
    global stevilo_drzav
    if celina == "Afrika":
        stevilo_drzav = 54
    elif celina == "Avstralija in Oceanija":
        stevilo_drzav = 16
    elif celina == "Azija":
        stevilo_drzav = 46
    elif celina == "Severna in Srednja Amerika":
        stevilo_drzav = 24
    elif celina == "Evropa":
        stevilo_drzav = 46
    elif celina == "Juzna Amerika":
        stevilo_drzav = 12
    else:
        stevilo_drzav = 0
    return stevilo_drzav

        
def vprasanje():
    print("Kateri državi pripada ta zastava?")
    prikaz_slike()
    print(len(slovar_slik))
    
    global nakljucna_zastava
    
    
    pravilen_odgovor = nakljucna_zastava[1]
    print(pravilen_odgovor)

    #nov slovar, kjer ni pravilne rešitve. Iz njega izbiramo moznosti
    #za odgovore
    nov_slovar = {}
    del slovar_slik[nakljucna_zastava[0]]
    nov_slovar = slovar_slik
    


    moznosti = {}
    global stevilo_drzav
    dolzina_datotek()
    
    while len(nov_slovar) > stevilo_drzav - 4:
        prva_moznost = random.choice(list(nov_slovar.items()))
        moznosti[prva_moznost[0]] = prva_moznost[1]
        del nov_slovar[prva_moznost[0]]
        
    
    moznosti[nakljucna_zastava[0]] = nakljucna_zastava[1]
    mozni_odgovori = list(moznosti.items())
    
    prvi_odgovor = mozni_odgovori[0]
    drugi_odgovor = mozni_odgovori[1]
    tretji_odgovor = mozni_odgovori[2]
    cetrti_odgovor = mozni_odgovori[3]
    
    odgovor_a = prvi_odgovor[1]
    odgovor_b = drugi_odgovor[1]
    odgovor_c = tretji_odgovor[1]
    odgovor_d = cetrti_odgovor[1]
    
    print("Izberi enega izmed odgovorov.")
    print("A) {}".format(odgovor_a))
    print("B) {}".format(odgovor_b))
    print("C) {}".format(odgovor_c))
    print("D) {}".format(odgovor_d))
    
    odgovor = input("Vpiši svojo izbiro. ")
    if odgovor == pravilen_odgovor:
        print("Bravo!")
    else:
        print("Napačno. Pravilen odgovor je {}.".format(pravilen_odgovor))
        
