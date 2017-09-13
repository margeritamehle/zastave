import tkinter as tk
import model
from PIL import Image, ImageTk


class Aplikacija:
    def __init__(self, master):
      okvir = tk.Frame(master)
      okvir.grid(row=0, column=0)

      okvir1 = tk.Frame(master)
      okvir1.grid(row=1, column=0)

      self.navodila = tk.Label(okvir, text ='''Kako dobro poznaš zastave držav sveta?
Preizkusi se. Klikni nova igra, da pričneš s kvizom.''')
      self.navodila.grid(row=0, column=0)

      self.pricni_igro = tk.Button(okvir1, text = "Nova igra",
                                   height = 2, width = 20,
                                   command=self.okno_z_izbiro)
      self.pricni_igro.grid(row = 1, column = 0)


    def okno_z_izbiro(self):
        class Izbira:
            def __init__(self, master):
                self.master = master
                self.zgoraj = tk.Frame(master)
                self.zgoraj.grid(row=0, column=0)

                self.spodaj = tk.Frame(master)
                self.spodaj.grid(row=1, column=0)

                self.oznaka = tk.Label(self.zgoraj, text = '''Izberi kontinent.''')
                self.oznaka.grid(row=0, column=0)

                self.gumb1 = tk.Button(self.spodaj, height = 2, width = 20,
                                       text = "Afrika", command = model.Celina("Afrika", "kontinent1.txt"))
                
                self.gumb1.grid(row = 0, column = 0)
                self.gumb2 = tk.Button(self.spodaj, height = 2, width = 20,
                      text = "Avstralija in Oceanija")
                self.gumb2.grid(row = 1, column = 0)
                self.gumb3 = tk.Button(self.spodaj, height = 2, width = 20,
                                       text = "Azija")
                self.gumb3.grid(row = 2, column = 0)
                self.gumb4 = tk.Button(self.spodaj, height = 2, width = 20,
                                       text = "Evropa")
                self.gumb4.grid(row = 3, column = 0)
                self.gumb5 = tk.Button(self.spodaj, height = 2, width = 20,
                                       text = "Južna Amerika")
                self.gumb5.grid(row = 4, column = 0)
                self.gumb6 = tk.Button(self.spodaj, height = 2, width = 20,
                                       text = '''Severna in Srednja Amerika''')
                self.gumb6.grid(row = 5, column = 0)
                self.vrnitev = tk.Button(self.spodaj, height = 3, width = 20,
                                         text = '''Vrni se na glavni meni.''')
                self.vrnitev.bind("<Button-1>", self.zapri)
                self.vrnitev.grid(row = 7, column = 1)
                self.gumb1.bind("<Button-1>", self.odpri_kviz1)
                self.gumb2.bind("<Button-1>", self.odpri_kviz2)
                self.gumb3.bind("<Button-1>", self.odpri_kviz3)
                self.gumb4.bind("<Button-1>", self.odpri_kviz4)
                self.gumb5.bind("<Button-1>", self.odpri_kviz5)
                self.gumb6.bind("<Button-1>", self.odpri_kviz6)

                
#zapre okno
            def zapri(self, event):
                self.master.destroy()

#okno s kvizom afrika
            def odpri_kviz1(self, event):
                model.afrika
                model.afrika.seznam_kljucev()
                
                class Orodje:
                    def __init__(self, master):
                        self.master = master
                        self.zgornji = tk.Frame(master)
                        self.zgornji.grid(row=0, column=0)
                        self.srednji = tk.Frame(master)
                        self.srednji.grid(row=1, column=0)
                        self.glavni = tk.Frame(master)
                        self.glavni.grid(row=2, column=0)
                        self.spodnji = tk.Frame(master)
                        self.spodnji.grid(row=3, column=0)

                        self.vprasaj = tk.Label(self.zgornji,
                                                text='''Zastava katere države je to?''')
                        self.vprasaj.grid(row=0, column=0)

                        self.stevec_tock = tk.Button(self.zgornji, height=2,
                                                     width=10, text=int("0"))
                        self.stevec_tock.grid(row=1, column=1)
                        self.stevec_tock.config(state="disabled")
                        
                        self.odziv = tk.Label(self.srednji)
                        self.odziv.grid(row=5, column=0)
                        self.odgovorA = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor1)
                        self.odgovorA.grid(row=2, column=0)
                        self.odgovorB = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor2)
                        self.odgovorB.grid(row=3, column=0)
                        self.odgovorC = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor3)
                        self.odgovorC.grid(row=2, column=1)
                        self.odgovorD = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor4)
                        self.odgovorD.grid(row=3, column=1)
                        self.analiza = tk.Button(self.spodnji, height=2,
                                                  width=10, text="Rezultat",
                                                 command=self.rezultat)
                        self.analiza.grid(row=5, column=6)
                        self.next = tk.Button(self.spodnji, height=2,
                                                  width=10, text="Naprej",
                                              command=self.slikica)
                        self.next.grid(row=5, column=8)
                        self.vrnitev1 = tk.Button(self.spodnji, height = 3,
                                                  width = 15,
                                                  text = '''Nazaj na izbor celin.''')
                        self.vrnitev1.bind("<Button-1>", self.zapri)
                        self.vrnitev1.grid(row = 6, column = 7)
                        
                        self.image = model.afrika.prikaz_slike()
                        self.prikaz = ImageTk.PhotoImage(model.afrika.im)
                        self.label = tk.Label(self.srednji, width=200,
                                              height=120, image=self.prikaz)
                        self.label.image = self.prikaz
                        self.label.grid(row=1, column=0)
                        odg = model.afrika.odgovori()
                        self.pravi = model.afrika.pravilen_odgovor
                        
                        odg1 = model.afrika.odgovor1()
                        self.odgovorA["text"] = odg1
                        odg2 = model.afrika.odgovor2()
                        self.odgovorB["text"] = odg2
                        odg3 = model.afrika.odgovor3()
                        self.odgovorC["text"] = odg3
                        odg4 = model.afrika.odgovor4()
                        self.odgovorD["text"] = odg4
                        
                    def slikica(self):
                        self.image = model.afrika.prikaz_slike()
                        self.prikaz = ImageTk.PhotoImage(model.afrika.im)
                        self.label = tk.Label(self.srednji, width=200,
                                              height=120, image=self.prikaz)
                        self.label.image = self.prikaz
                        self.label.grid(row=1, column=0)
                        if len(model.afrika.testni_seznam) == model.afrika.stevilo_drzav:
                            self.next.config(state="disabled")
                            return False
                        odg = model.afrika.odgovori()
                        self.pravi = model.afrika.pravilen_odgovor
                        odg1 = model.afrika.odgovor1()
                        self.odgovorA["text"] = odg1
                        odg2 = model.afrika.odgovor2()
                        self.odgovorB["text"] = odg2
                        odg3 = model.afrika.odgovor3()
                        self.odgovorC["text"] = odg3
                        odg4 = model.afrika.odgovor4()
                        self.odgovorD["text"] = odg4
                        self.odziv["text"] = ""
                    def zapri(self, event):
                        self.master.destroy()
                    def preveri_odgovor1(self):
                        if self.odgovorA["text"] == self.pravi:
                            self.odgovorA["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorA["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def preveri_odgovor2(self):
                        if self.odgovorB["text"] == self.pravi:
                            self.odgovorB["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorB["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def preveri_odgovor3(self):
                        if self.odgovorC["text"] == self.pravi:
                            self.odgovorC["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorC["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def preveri_odgovor4(self):
                        if self.odgovorD["text"] == self.pravi:
                            self.odgovorD["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorD["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def rezultat(self):
                        okvircek = tk.Label(self.spodnji, width=20, height=10)
                        okvircek["text"]= '''Bravo!
Dosegel si {}/{}!'''.format(self.stevec_tock["text"], model.afrika.stevilo_drzav)
                        okvircek.grid(row=6, column=6)
                        

                okno_s_kvizom = tk.Toplevel()
                moj_kviz = Orodje(okno_s_kvizom)
                okno_s_kvizom.mainloop()
#okno s kvizom za avstralijo
            def odpri_kviz2(self, event):
                model.avstralija
                model.avstralija.seznam_kljucev()
                class Orodje:
                    def __init__(self, master):
                        self.master = master
                        self.zgornji = tk.Frame(master)
                        self.zgornji.grid(row=0, column=0)
                        self.srednji = tk.Frame(master)
                        self.srednji.grid(row=1, column=0)
                        self.glavni = tk.Frame(master)
                        self.glavni.grid(row=2, column=0)
                        self.spodnji = tk.Frame(master)
                        self.spodnji.grid(row=3, column=0)

                        self.vprasaj = tk.Label(self.zgornji,
                                                text='''Zastava katere države je to?''')
                        self.vprasaj.grid(row=0, column=0)

                        self.stevec_tock = tk.Button(self.zgornji, height=2,
                                                     width=10, text=int("0"))
                        self.stevec_tock.grid(row=1, column=1)
                        self.stevec_tock.config(state="disabled")
                        
                        self.odziv = tk.Label(self.srednji)
                        self.odziv.grid(row=5, column=0)
                        self.odgovorA = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor1)
                        self.odgovorA.grid(row=2, column=0)
                        self.odgovorB = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor2)
                        self.odgovorB.grid(row=3, column=0)
                        self.odgovorC = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor3)
                        self.odgovorC.grid(row=2, column=1)
                        self.odgovorD = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor4)
                        self.odgovorD.grid(row=3, column=1)
                        self.analiza = tk.Button(self.spodnji, height=2,
                                                  width=10, text="Rezultat",
                                                 command=self.rezultat)
                        self.analiza.grid(row=5, column=6)
                        self.next = tk.Button(self.spodnji, height=2,
                                                  width=10, text="Naprej",
                                              command=self.slikica)
                        self.next.grid(row=5, column=8)
                        self.vrnitev1 = tk.Button(self.spodnji, height = 3,
                                                  width = 15,
                                                  text = '''Nazaj na izbor celin.''')
                        self.vrnitev1.bind("<Button-1>", self.zapri)
                        self.vrnitev1.grid(row = 6, column = 7)

                        self.image = model.avstralija.prikaz_slike()
                        self.prikaz = ImageTk.PhotoImage(model.avstralija.im)
                        self.label = tk.Label(self.srednji, width=200,
                                              height=120, image=self.prikaz)
                        self.label.image = self.prikaz
                        self.label.grid(row=1, column=0)
                        odg = model.avstralija.odgovori()
                        self.pravi = model.avstralija.pravilen_odgovor
                        odg1 = model.avstralija.odgovor1()
                        self.odgovorA["text"] = odg1
                        odg2 = model.avstralija.odgovor2()
                        self.odgovorB["text"] = odg2
                        odg3 = model.avstralija.odgovor3()
                        self.odgovorC["text"] = odg3
                        odg4 = model.avstralija.odgovor4()
                        self.odgovorD["text"] = odg4
                    def slikica(self):
                        self.image = model.avstralija.prikaz_slike()
                        self.prikaz = ImageTk.PhotoImage(model.avstralija.im)
                        self.label = tk.Label(self.srednji, width=200,
                                              height=120, image=self.prikaz)
                        self.label.image = self.prikaz
                        self.label.grid(row=1, column=0)
                        if len(model.avstralija.testni_seznam) == model.avstralija.stevilo_drzav:
                            self.next.config(state="disabled")
                            return False
                        odg = model.avstralija.odgovori()
                        self.pravi = model.avstralija.pravilen_odgovor
                        odg1 = model.avstralija.odgovor1()
                        self.odgovorA["text"] = odg1
                        odg2 = model.avstralija.odgovor2()
                        self.odgovorB["text"] = odg2
                        odg3 = model.avstralija.odgovor3()
                        self.odgovorC["text"] = odg3
                        odg4 = model.avstralija.odgovor4()
                        self.odgovorD["text"] = odg4
                        self.odziv["text"] = ""
                    def zapri(self, event):
                        self.master.destroy()
                    def preveri_odgovor1(self):
                        if self.odgovorA["text"] == self.pravi:
                            self.odgovorA["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorA["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def preveri_odgovor2(self):
                        if self.odgovorB["text"] == self.pravi:
                            self.odgovorB["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorB["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def preveri_odgovor3(self):
                        if self.odgovorC["text"] == self.pravi:
                            self.odgovorC["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorC["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def preveri_odgovor4(self):
                        if self.odgovorD["text"] == self.pravi:
                            self.odgovorD["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorD["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def rezultat(self):
                        okvircek = tk.Label(self.spodnji, width=20, height=10)
                        okvircek["text"]= '''Bravo!
Dosegel si {}/{}!'''.format(self.stevec_tock["text"], model.avstralija.stevilo_drzav)
                        okvircek.grid(row=6, column=6)
                        

                okno_s_kvizom = tk.Toplevel()
                moj_kviz = Orodje(okno_s_kvizom)
                okno_s_kvizom.mainloop()
#okno s kvizom za azijo
            def odpri_kviz3(self, event):
                model.azija
                model.azija.seznam_kljucev()
                class Orodje:
                    def __init__(self, master):
                        self.master = master
                        self.zgornji = tk.Frame(master)
                        self.zgornji.grid(row=0, column=0)
                        self.srednji = tk.Frame(master)
                        self.srednji.grid(row=1, column=0)
                        self.glavni = tk.Frame(master)
                        self.glavni.grid(row=2, column=0)
                        self.spodnji = tk.Frame(master)
                        self.spodnji.grid(row=3, column=0)

                        self.vprasaj = tk.Label(self.zgornji,
                                                text='''Zastava katere države je to?''')
                        self.vprasaj.grid(row=0, column=0)

                        self.stevec_tock = tk.Button(self.zgornji, height=2,
                                                     width=10, text=int("0"))
                        self.stevec_tock.grid(row=1, column=1)
                        self.stevec_tock.config(state="disabled")
                        
                        self.odziv = tk.Label(self.srednji)
                        self.odziv.grid(row=5, column=0)
                        self.odgovorA = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor1)
                        self.odgovorA.grid(row=2, column=0)
                        self.odgovorB = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor2)
                        self.odgovorB.grid(row=3, column=0)
                        self.odgovorC = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor3)
                        self.odgovorC.grid(row=2, column=1)
                        self.odgovorD = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor4)
                        self.odgovorD.grid(row=3, column=1)
                        self.analiza = tk.Button(self.spodnji, height=2,
                                                  width=10, text="Rezultat",
                                                 command=self.rezultat)
                        self.analiza.grid(row=5, column=6)
                        self.next = tk.Button(self.spodnji, height=2,
                                                  width=10, text="Naprej",
                                              command=self.slikica)
                        self.next.grid(row=5, column=8)
                        self.vrnitev1 = tk.Button(self.spodnji, height = 3,
                                                  width = 15,
                                                  text = '''Nazaj na izbor celin.''')
                        self.vrnitev1.bind("<Button-1>", self.zapri)
                        self.vrnitev1.grid(row = 6, column = 7)
 
                        self.image = model.azija.prikaz_slike()
                        self.prikaz = ImageTk.PhotoImage(model.azija.im)
                        self.label = tk.Label(self.srednji, width=200,
                                              height=120, image=self.prikaz)
                        self.label.image = self.prikaz
                        self.label.grid(row=1, column=0)
                        odg = model.azija.odgovori()
                        self.pravi = model.azija.pravilen_odgovor
                        odg1 = model.azija.odgovor1()
                        self.odgovorA["text"] = odg1
                        odg2 = model.azija.odgovor2()
                        self.odgovorB["text"] = odg2
                        odg3 = model.azija.odgovor3()
                        self.odgovorC["text"] = odg3
                        odg4 = model.azija.odgovor4()
                        self.odgovorD["text"] = odg4
                    def slikica(self):
                        self.image = model.azija.prikaz_slike()
                        self.prikaz = ImageTk.PhotoImage(model.azija.im)
                        self.label = tk.Label(self.srednji, width=200,
                                              height=120, image=self.prikaz)
                        self.label.image = self.prikaz
                        self.label.grid(row=1, column=0)
                        if len(model.azija.testni_seznam) == model.azija.stevilo_drzav:
                            self.next.config(state="disabled")
                            return False
                        odg = model.azija.odgovori()
                        self.pravi = model.azija.pravilen_odgovor
                        odg1 = model.azija.odgovor1()
                        self.odgovorA["text"] = odg1
                        odg2 = model.azija.odgovor2()
                        self.odgovorB["text"] = odg2
                        odg3 = model.azija.odgovor3()
                        self.odgovorC["text"] = odg3
                        odg4 = model.azija.odgovor4()
                        self.odgovorD["text"] = odg4
                        self.odziv["text"] = ""
                    def zapri(self, event):
                        self.master.destroy()
                    def preveri_odgovor1(self):
                        if self.odgovorA["text"] == self.pravi:
                            self.odgovorA["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorA["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def preveri_odgovor2(self):
                        if self.odgovorB["text"] == self.pravi:
                            self.odgovorB["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorB["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def preveri_odgovor3(self):
                        if self.odgovorC["text"] == self.pravi:
                            self.odgovorC["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorC["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def preveri_odgovor4(self):
                        if self.odgovorD["text"] == self.pravi:
                            self.odgovorD["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorD["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def rezultat(self):
                        okvircek = tk.Label(self.spodnji, width=20, height=10)
                        okvircek["text"]= '''Bravo!
Dosegel si {}/{}!'''.format(self.stevec_tock["text"], model.azija.stevilo_drzav)
                        okvircek.grid(row=6, column=6)
                        

                okno_s_kvizom = tk.Toplevel()
                moj_kviz = Orodje(okno_s_kvizom)
                okno_s_kvizom.mainloop()
#okno s kvizom za evropo               
            def odpri_kviz4(self, event):
                model.evropa
                model.evropa.seznam_kljucev()
        
                class Orodje:
                    def __init__(self, master):
                        self.master = master
                        self.zgornji = tk.Frame(master)
                        self.zgornji.grid(row=0, column=0)
                        self.srednji = tk.Frame(master)
                        self.srednji.grid(row=1, column=0)
                        self.glavni = tk.Frame(master)
                        self.glavni.grid(row=2, column=0)
                        self.spodnji = tk.Frame(master)
                        self.spodnji.grid(row=3, column=0)

                        self.vprasaj = tk.Label(self.zgornji,
                                                text='''Zastava katere države je to?''')
                        self.vprasaj.grid(row=0, column=0)

                        self.stevec_tock = tk.Button(self.zgornji, height=2,
                                                     width=10, text=int("0"))
                        self.stevec_tock.grid(row=1, column=1)
                        self.stevec_tock.config(state="disabled")
                        
                        self.odziv = tk.Label(self.srednji)
                        self.odziv.grid(row=5, column=0)
                        self.odgovorA = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor1)
                        self.odgovorA.grid(row=2, column=0)
                        self.odgovorB = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor2)
                        self.odgovorB.grid(row=3, column=0)
                        self.odgovorC = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor3)
                        self.odgovorC.grid(row=2, column=1)
                        self.odgovorD = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor4)
                        self.odgovorD.grid(row=3, column=1)
                        self.analiza = tk.Button(self.spodnji, height=2,
                                                  width=10, text="Rezultat",
                                                 command=self.rezultat)
                        self.analiza.grid(row=5, column=6)
                        self.next = tk.Button(self.spodnji, height=2,
                                                  width=10, text="Naprej",
                                              command=self.slikica)
                        self.next.grid(row=5, column=8)
                        self.vrnitev1 = tk.Button(self.spodnji, height = 3,
                                                  width = 15,
                                                  text = '''Nazaj na izbor celin.''')
                        self.vrnitev1.bind("<Button-1>", self.zapri)
                        self.vrnitev1.grid(row = 6, column = 7)
 
                        self.image = model.evropa.prikaz_slike()
                        self.prikaz = ImageTk.PhotoImage(model.evropa.im)
                        self.label = tk.Label(self.srednji, width=200,
                                              height=120, image=self.prikaz)
                        self.label.image = self.prikaz
                        self.label.grid(row=1, column=0)
                        odg = model.evropa.odgovori()
                        self.pravi = model.evropa.pravilen_odgovor
                        odg1 = model.evropa.odgovor1()
                        self.odgovorA["text"] = odg1
                        odg2 = model.evropa.odgovor2()
                        self.odgovorB["text"] = odg2
                        odg3 = model.evropa.odgovor3()
                        self.odgovorC["text"] = odg3
                        odg4 = model.evropa.odgovor4()
                        self.odgovorD["text"] = odg4
                        
                    def slikica(self):
                        self.image = model.evropa.prikaz_slike()
                        self.prikaz = ImageTk.PhotoImage(model.evropa.im)
                        self.label = tk.Label(self.srednji, width=200,
                                              height=120, image=self.prikaz)
                        self.label.image = self.prikaz
                        self.label.grid(row=1, column=0)
                        if len(model.evropa.testni_seznam) == model.evropa.stevilo_drzav:
                            self.next.config(state="disabled")
                            return False
                        odg = model.evropa.odgovori()
                        self.pravi = model.evropa.pravilen_odgovor
                        odg1 = model.evropa.odgovor1()
                        self.odgovorA["text"] = odg1
                        odg2 = model.evropa.odgovor2()
                        self.odgovorB["text"] = odg2
                        odg3 = model.evropa.odgovor3()
                        self.odgovorC["text"] = odg3
                        odg4 = model.evropa.odgovor4()
                        self.odgovorD["text"] = odg4
                        self.odziv["text"] = ""
                        
                    def zapri(self, event):
                        self.master.destroy()
                    def preveri_odgovor1(self):
                        if self.odgovorA["text"] == self.pravi:
                            self.odgovorA["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorA["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)                      
    
                    def preveri_odgovor2(self):
                        if self.odgovorB["text"] == self.pravi:
                            self.odgovorB["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorB["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def preveri_odgovor3(self):
                        if self.odgovorC["text"] == self.pravi:
                            self.odgovorC["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorC["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def preveri_odgovor4(self):
                        if self.odgovorD["text"] == self.pravi:
                            self.odgovorD["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorD["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def rezultat(self):
                        okvircek = tk.Label(self.spodnji, width=20, height=10)
                        okvircek["text"]= '''Bravo!
Dosegel si {}/{}!'''.format(self.stevec_tock["text"], model.evropa.stevilo_drzav)
                        okvircek.grid(row=6, column=6)
                okno_s_kvizom = tk.Toplevel()
                moj_kviz = Orodje(okno_s_kvizom)
                okno_s_kvizom.mainloop()
                
                #okno s kvizom za juzno ameriko
            def odpri_kviz5(self, event):
                model.juzna_amerika
                model.juzna_amerika.seznam_kljucev()
        
                class Orodje:
                    def __init__(self, master):
                        self.master = master
                        self.zgornji = tk.Frame(master)
                        self.zgornji.grid(row=0, column=0)
                        self.srednji = tk.Frame(master)
                        self.srednji.grid(row=1, column=0)
                        self.glavni = tk.Frame(master)
                        self.glavni.grid(row=2, column=0)
                        self.spodnji = tk.Frame(master)
                        self.spodnji.grid(row=3, column=0)

                        self.vprasaj = tk.Label(self.zgornji,
                                                text='''Zastava katere države je to?''')
                        self.vprasaj.grid(row=0, column=0)

                        self.stevec_tock = tk.Button(self.zgornji, height=2,
                                                     width=10, text=int("0"))
                        self.stevec_tock.grid(row=1, column=1)
                        self.stevec_tock.config(state="disabled")
                        
                        self.odziv = tk.Label(self.srednji)
                        self.odziv.grid(row=5, column=0)
                        self.odgovorA = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor1)
                        self.odgovorA.grid(row=2, column=0)
                        self.odgovorB = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor2)
                        self.odgovorB.grid(row=3, column=0)
                        self.odgovorC = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor3)
                        self.odgovorC.grid(row=2, column=1)
                        self.odgovorD = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor4)
                        self.odgovorD.grid(row=3, column=1)
                        self.analiza = tk.Button(self.spodnji, height=2,
                                                  width=10, text="Rezultat",
                                                 command=self.rezultat)
                        self.analiza.grid(row=5, column=6)
                        self.next = tk.Button(self.spodnji, height=2,
                                                  width=10, text="Naprej",
                                              command=self.slikica)
                        self.next.grid(row=5, column=8)
                        self.vrnitev1 = tk.Button(self.spodnji, height = 3,
                                                  width = 15,
                                                  text = '''Nazaj na izbor celin.''')
                        self.vrnitev1.bind("<Button-1>", self.zapri)
                        self.vrnitev1.grid(row = 6, column = 7)
 
                        self.image = model.juzna_amerika.prikaz_slike()
                        self.prikaz = ImageTk.PhotoImage(model.juzna_amerika.im)
                        self.label = tk.Label(self.srednji, width=200,
                                              height=120, image=self.prikaz)
                        self.label.image = self.prikaz
                        self.label.grid(row=1, column=0)
                        odg = model.juzna_amerika.odgovori()
                        self.pravi = model.juzna_amerika.pravilen_odgovor
                        odg1 = model.juzna_amerika.odgovor1()
                        self.odgovorA["text"] = odg1
                        odg2 = model.juzna_amerika.odgovor2()
                        self.odgovorB["text"] = odg2
                        odg3 = model.juzna_amerika.odgovor3()
                        self.odgovorC["text"] = odg3
                        odg4 = model.juzna_amerika.odgovor4()
                        self.odgovorD["text"] = odg4
                        
                    def slikica(self):
                        self.image = model.juzna_amerika.prikaz_slike()
                        self.prikaz = ImageTk.PhotoImage(model.juzna_amerika.im)
                        self.label = tk.Label(self.srednji, width=200,
                                              height=120, image=self.prikaz)
                        self.label.image = self.prikaz
                        self.label.grid(row=1, column=0)
                        if len(model.juzna_amerika.testni_seznam) == model.juzna_amerika.stevilo_drzav:
                            self.next.config(state="disabled")
                            return False
                        odg = model.juzna_amerika.odgovori()
                        self.pravi = model.juzna_amerika.pravilen_odgovor
                        odg1 = model.juzna_amerika.odgovor1()
                        self.odgovorA["text"] = odg1
                        odg2 = model.juzna_amerika.odgovor2()
                        self.odgovorB["text"] = odg2
                        odg3 = model.juzna_amerika.odgovor3()
                        self.odgovorC["text"] = odg3
                        odg4 = model.juzna_amerika.odgovor4()
                        self.odgovorD["text"] = odg4
                        self.odziv["text"] = ""
                        
                    def zapri(self, event):
                        self.master.destroy()
                    def preveri_odgovor1(self):
                        if self.odgovorA["text"] == self.pravi:
                            self.odgovorA["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorA["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)                      
    
                    def preveri_odgovor2(self):
                        if self.odgovorB["text"] == self.pravi:
                            self.odgovorB["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorB["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def preveri_odgovor3(self):
                        if self.odgovorC["text"] == self.pravi:
                            self.odgovorC["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorC["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def preveri_odgovor4(self):
                        if self.odgovorD["text"] == self.pravi:
                            self.odgovorD["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorD["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def rezultat(self):
                        okvircek = tk.Label(self.spodnji, width=20, height=10)
                        okvircek["text"]= '''Bravo!
Dosegel si {}/{}!'''.format(self.stevec_tock["text"], model.juzna_amerika.stevilo_drzav)
                        okvircek.grid(row=6, column=6)
                        

                            
                okno_s_kvizom = tk.Toplevel()
                moj_kviz = Orodje(okno_s_kvizom)
                okno_s_kvizom.mainloop()
                #okno s kvizom severna amerika
            def odpri_kviz6(self, event):
                model.severna_amerika
                model.severna_amerika.seznam_kljucev()
                class Orodje:
                    def __init__(self, master):
                        self.master = master
                        self.zgornji = tk.Frame(master)
                        self.zgornji.grid(row=0, column=0)
                        self.srednji = tk.Frame(master)
                        self.srednji.grid(row=1, column=0)
                        self.glavni = tk.Frame(master)
                        self.glavni.grid(row=2, column=0)
                        self.spodnji = tk.Frame(master)
                        self.spodnji.grid(row=3, column=0)

                        self.vprasaj = tk.Label(self.zgornji,
                                                text='''Zastava katere države je to?''')
                        self.vprasaj.grid(row=0, column=0)

                        self.stevec_tock = tk.Button(self.zgornji, height=2,
                                                     width=10, text=int("0"))
                        self.stevec_tock.grid(row=1, column=1)
                        self.stevec_tock.config(state="disabled")
                        
                        self.odziv = tk.Label(self.srednji)
                        self.odziv.grid(row=5, column=0)
                        self.odgovorA = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor1)
                        self.odgovorA.grid(row=2, column=0)
                        self.odgovorB = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor2)
                        self.odgovorB.grid(row=3, column=0)
                        self.odgovorC = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command =self.preveri_odgovor3)
                        self.odgovorC.grid(row=2, column=1)
                        self.odgovorD = tk.Button(self.glavni, height=2,
                                                  width=25,
                                                  command=self.preveri_odgovor4)
                        self.odgovorD.grid(row=3, column=1)
                        self.analiza = tk.Button(self.spodnji, height=2,
                                                  width=10, text="Rezultat",
                                                 command=self.rezultat)
                        self.analiza.grid(row=5, column=6)
                        self.next = tk.Button(self.spodnji, height=2,
                                                  width=10, text="Naprej",
                                              command=self.slikica)
                        self.next.grid(row=5, column=8)
                        self.vrnitev1 = tk.Button(self.spodnji, height = 3,
                                                  width = 15,
                                                  text = '''Nazaj na izbor celin.''')
                        self.vrnitev1.bind("<Button-1>", self.zapri)
                        self.vrnitev1.grid(row = 6, column = 7)

                        self.image = model.severna_amerika.prikaz_slike()
                        self.prikaz = ImageTk.PhotoImage(model.severna_amerika.im)
                        self.label = tk.Label(self.srednji, width=200,
                                              height=120, image=self.prikaz)
                        self.label.image = self.prikaz
                        self.label.grid(row=1, column=0)
                        odg = model.severna_amerika.odgovori()
                        self.pravi = model.severna_amerika.pravilen_odgovor
                        odg1 = model.severna_amerika.odgovor1()
                        self.odgovorA["text"] = odg1
                        odg2 = model.severna_amerika.odgovor2()
                        self.odgovorB["text"] = odg2
                        odg3 = model.severna_amerika.odgovor3()
                        self.odgovorC["text"] = odg3
                        odg4 = model.severna_amerika.odgovor4()
                        self.odgovorD["text"] = odg4
                    def slikica(self):
                        self.image = model.severna_amerika.prikaz_slike()
                        self.prikaz = ImageTk.PhotoImage(model.severna_amerika.im)
                        self.label = tk.Label(self.srednji, width=200,
                                              height=120, image=self.prikaz)
                        self.label.image = self.prikaz
                        self.label.grid(row=1, column=0)
                        if len(model.severna_amerika.testni_seznam) == model.severna_amerika.stevilo_drzav:
                            self.next.config(state="disabled")
                            return False
                        odg = model.severna_amerika.odgovori()
                        self.pravi = model.severna_amerika.pravilen_odgovor
                        odg1 = model.severna_amerika.odgovor1()
                        self.odgovorA["text"] = odg1
                        odg2 = model.severna_amerika.odgovor2()
                        self.odgovorB["text"] = odg2
                        odg3 = model.severna_amerika.odgovor3()
                        self.odgovorC["text"] = odg3
                        odg4 = model.severna_amerika.odgovor4()
                        self.odgovorD["text"] = odg4
                        self.odziv["text"] = ""
                    def zapri(self, event):
                        self.master.destroy()
                    def preveri_odgovor1(self):
                        if self.odgovorA["text"] == self.pravi:
                            self.odgovorA["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorA["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def preveri_odgovor2(self):
                        if self.odgovorB["text"] == self.pravi:
                            self.odgovorB["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorB["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def preveri_odgovor3(self):
                        if self.odgovorC["text"] == self.pravi:
                            self.odgovorC["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorC["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def preveri_odgovor4(self):
                        if self.odgovorD["text"] == self.pravi:
                            self.odgovorD["text"] = "✓"
                            self.odziv["text"]= "BRAVO!"
                            self.stevec_tock["text"] += 1
                        else:
                            self.odgovorD["text"] = "x"
                            self.odziv["text"]= "Ne, pravilen odgovor je {}!".format(self.pravi)
                    def rezultat(self):
                        okvircek = tk.Label(self.spodnji, width=20, height=10)
                        okvircek["text"]= '''Bravo!
Dosegel si {}/{}!'''.format(self.stevec_tock["text"], model.severna_amerika.stevilo_drzav)
                        okvircek.grid(row=6, column=6)
                    
                okno_s_kvizom = tk.Toplevel()
                moj_kviz = Orodje(okno_s_kvizom)
                okno_s_kvizom.mainloop()

        
        okno = tk.Tk()
        moje_okno = Izbira(okno)
        okno.mainloop()
      

glavno_okno = tk.Tk()
aplikacija = Aplikacija(glavno_okno)
glavno_okno.mainloop()
