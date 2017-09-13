import os
import random
from PIL import Image, ImageTk


slovar_slik = {}
stevilo_drzav = 0




class Celina:
    def __init__(self, ime="", datoteka=""):
        self.ime = ime
        self.datoteka = datoteka
        self.slovar_slik = {}
        self.kljuci_na_voljo = []
        self.stevilo_drzav = 0
        self.nakljucna_zastava = []
        self.im = ""
        self.testni_seznam = []
        self.moznosti = []
        self.prvi_odgovor = ""
        self.drugi_odgovor = ""
        self.tretji_odgovor = ""
        self.cetrti_odgovor = ""
        self.pravilen_odgovor = ""
        


    def __repr__(self):
        return "Celina({},{})".format(self.ime, self.datoteka)
    
    #iz izbrane datoteke naredi slovar slik
    def naredi_slovar_slik(self):
        with open(self.datoteka) as dat:
            for vrstica in dat:
                besedi = vrstica.strip().split(":")
                if len(besedi) == 2:
                    slika = besedi[0]
                    ime_slike = besedi[1]
                    self.slovar_slik[slika] = ime_slike
        return self.slovar_slik
    
    #seznam kljucev = drzave.jpg
    def seznam_kljucev(self):
        self.naredi_slovar_slik()
        self.kljuci_na_voljo = list(self.slovar_slik.keys())
        return self.kljuci_na_voljo

    ##da prikažeš sliko moraš biti v tisti mapi, kjer je slika.
    def pot_do_slik(self):
        trenutni_direktorij = os.getcwd()
        ime_mape = "\\\\slike_zastav\\\\" + "_".join(self.ime.split(" "))
        os.chdir(trenutni_direktorij + ime_mape)
        kje = os.getcwd()
        return kje
    
    #kje se nahajajo datoteke z državami
    def pot_do_datotek(self):
        trenutni_direktorij = os.getcwd()
        os.chdir("../..")
        kje = os.getcwd()
        return kje
        
        return trenutni_direktorij
    
    #prikaze sliko
    def prikaz_slike(self):
        test1 = self.preveri()
        self.pot_do_slik()

        if test1 == False:
            return False
        else:
            self.im = Image.open(self.nakljucna_zastava[0])
            slika = self.im.draft(mode="RGB", size=(100, 100))
            #slika.show()
            self.pot_do_datotek()
            return self.im
    
    def izberi_zastavo(self):
        #izberi nakljucno zastavo
        self.kljuci_na_voljo
        if self.kljuci_na_voljo == []:
            return False
        kljuc = random.choice(self.kljuci_na_voljo)
        self.nakljucna_zastava = (kljuc, self.slovar_slik[kljuc])
        print(self.nakljucna_zastava)
        del self.kljuci_na_voljo[self.kljuci_na_voljo.index(kljuc)]
        return self.nakljucna_zastava
    
    def preveri(self):
        self.izberi_zastavo()
        self.dolzina_datotek()
        #ko je dolžina kljucev o vrni false
        if len(self.testni_seznam) == self.stevilo_drzav:
            return False    
        elif len(self.kljuci_na_voljo) == 0:
            test = self.testni_seznam.append(self.nakljucna_zastava[0])
            test = self.testni_seznam
            return self.testni_seznam
        #ce zastave ni v testnem seznamu jo dodej na seznam in prikazi vrni self.ime
        elif self.nakljucna_zastava not in self.testni_seznam:
            test = self.testni_seznam.append(self.nakljucna_zastava[0])
            test = self.testni_seznam
            return self.testni_seznam
        #ce pa je zastava notri potem izberi drugo zastavo
        else:
            self.izberi_zastavo()
            self.preveri()
       


    #kako velika je datoteka
    def dolzina_datotek(self):
        if self.ime == "Afrika":
            self.stevilo_drzav = 54
        elif self.ime == "Avstralija in Oceanija":
            self.stevilo_drzav = 16
        elif self.ime == "Azija":
            self.stevilo_drzav = 46
        elif self.ime == "Severna in Srednja Amerika":
            self.stevilo_drzav = 24
        elif self.ime == "Evropa":
            self.stevilo_drzav = 46
        elif self.ime == "Juzna Amerika":
            self.stevilo_drzav = 12
        else:
            self.stevilo_drzav = 0
        return self.stevilo_drzav
#naredi mnozico iz katere izbiramo odgovore
    def odgovori(self):
        self.moznosti = []
        self.pravilen_odgovor = self.nakljucna_zastava[1].strip()
        print(self.pravilen_odgovor)
        self.moznosti.append(self.pravilen_odgovor)
        while len(self.moznosti) < 4:
            kljuc = random.choice(self.kljuci_na_voljo)
            self.moznosti.append(kljuc.strip().split(".")[0])
        return self.moznosti
        
    def odgovor1(self):
        self.prvi_odgovor = random.choice(self.moznosti)
        self.moznosti.remove(self.prvi_odgovor)
        return self.prvi_odgovor

    def odgovor2(self):
        self.drugi_odgovor = random.choice(self.moznosti)
        self.moznosti.remove(self.drugi_odgovor)
        return self.drugi_odgovor
    
    def odgovor3(self):
        self.tretji_odgovor = random.choice(self.moznosti)
        self.moznosti.remove(self.tretji_odgovor)
        return self.tretji_odgovor
    def odgovor4(self):
        self.cetrti_odgovor = random.choice(self.moznosti)
        return self.cetrti_odgovor
    


        

afrika = Celina("Afrika", "kontinent1.txt")
avstralija = Celina("Avstralija in Oceanija", "kontinent2.txt")
azija = Celina("Azija", "kontinent3.txt")
evropa = Celina("Evropa", "kontinent4.txt")
juzna_amerika = Celina("Juzna Amerika", "kontinent5.txt")
severna_amerika = Celina("Severna in Srednja Amerika", "kontinent6.txt")
        
        
        
#....že igrano
    


