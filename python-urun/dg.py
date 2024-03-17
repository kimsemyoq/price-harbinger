import threading
import time

import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import ctypes
import customtkinter
import sqlite3
from tkinter import filedialog
import os
ana_gui = customtkinter.CTk()

anlatma = customtkinter.CTk()
ana_gui.after(0, lambda: ana_gui.state("zoomed"))

import yagmail


# nasıl kullanıcıgınızı göstermek için


class FiyatKontrol:
    def __init__(self, master):

        self.guncellenen_urun_sayisi = 0
        self.urunfiyatgui = customtkinter.CTk()


        super().__init__()
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2892.39 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 (1a9b3ef7-0bfa-4c04-952e-638c53cbd39a)",
            "Mozilla/5.0 (Linux; Android 10; moto g(7) play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro Max) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 6.0.1; SM-G900V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.0; .NET CLR 2.1.13080)",
            "Mozilla/5.0 (Linux; Android 11; Hisense E50 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 OcIdWebView ({\x22os\x22:\x22Android\x22,\x22osVersion\x22:\x2230\x22,\x22app\x22:\x22com.google.android.gms\x22,\x22appVersion\x22:\x22219\x22,\x22style\x22:2,\x22isDarkTheme\x22:false})",
            "Mozilla/5.0 (Linux; Android 5.1.1; Coolpad E561 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 11; 100003562) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 9; vivo 1916) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Safari/537.36 OcIdWebView ({\x22os\x22:\x22Android\x22,\x22osVersion\x22:\x2229\x22,\x22app\x22:\x22com.google.android.gms\x22,\x22appVersion\x22:\x22219\x22,\x22style\x22:2,\x22isDarkTheme\x22:false})",
            "Mozilla/5.0 (Linux; Android 11; CPH2123) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 (f9fe3006-f825-45d7-8552-77ef0af1b65c)",
            "Mozilla/5.0 (Linux; Android 10; M2003J15SC Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 OcIdWebView ({\x22os\x22:\x22Android\x22,\x22osVersion\x22:\x2229\x22,\x22app\x22:\x22com.google.android.gms\x22,\x22appVersion\x22:\x22219\x22,\x22style\x22:2,\x22isDarkTheme\x22:true})",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29 OpenWave/95.4.7703.4",
            "Mozilla/5.0 (Linux; Android 11; RMX2170 Build/RKQ1.200903.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 OPT/2.9",
            "Mozilla/5.0 (Linux; Android 9; rk3399) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 9; SM-M205G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 11; SM-A715F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 EdgW/1.0",
            "Mozilla/5.0 (Linux; Android 9; T10L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.111 Mobile Safari/537.36 GSA/11.21.9.21.arm64",
            "Mozilla/5.0 (iPad; CPU OS 12_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/119.0.324025186 Mobile/16G102 Safari/604.1",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; wbx 1.0.0; Microsoft Outlook 14.0.7248; ms-office; MSOffice 14)",
            "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950F/G950FXXU5DSFB) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 10; SM-G975F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.89 Mobile Safari/537.36 GSA/11.21.9.21.arm64",
            "Mozilla/5.0 (Linux; Android 8.1.0; CPH1901 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36 GSA/10.0.6.21.arm64",
            "Mozilla/5.0 (Linux; Android 9; W-K510-EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 9; JKM-LX1; HMSCore 5.0.0.304; GMSCore 20.26.14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 HuaweiBrowser/10.1.3.321 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 9; VTR-L29 Build/HUAWEIVTR-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.111 Mobile Safari/537.36 GSA/11.20.15.21.arm64",
            "Mozilla/5.0 (Linux; Android 8.1.0; CPH1809 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 GSA/8.65.4.21.arm64",
        ]




        self.gonderici = "yourproductbot@gmail.com"
        self.flag = True
        self.fiyat_alma_butondurdur = customtkinter.CTkButton(
            self.urunfiyatgui,
            text="Press to stop update!",
            border_color="white",
            fg_color="black",
            font=("Times New Roman", 20),
            command=self.urunfiyatguncelthearffalse
        )

        self.fiyat_alma_butondurdur.place(relx=0.001, rely=0.4)

        self.price_whole = 0
        self.price_ready_event = threading.Event()
        self.anaguidonurun = customtkinter.CTkButton(self.urunfiyatgui, text="Go back to adding products!",
                                                     border_color="white",
                                                     font=("Times New Roman", 20), fg_color="black",
                                                     command=self.uruneklegizle)
        self.anaguidonurun.place(relx=0.001, rely=0.2)

        self.urunleriminfiyatiguncel = customtkinter.CTkButton(self.urunfiyatgui, text="Click to update the price of the products",
                                                               font=("Times New Roman", 20), fg_color="black",
                                                               border_color="white",
                                                               command=self.urunffiyatgunceltheard)
        self.urunleriminfiyatiguncel.place(relx=0.001, rely=0.3)

        self.master = master

        self.urun = None
        self.adi_etiketleri = []
        self.rely_value = 0.5
        self.para = 0
        self.gmailgiris = customtkinter.CTkEntry(self.master, fg_color="black", font=("Times New Roman", 20),
                                                 border_color="white")
        plt.switch_backend('agg')


        self.conn = None

        self.cursor = None
        self.current_price = None
        self.hedef_fiyat = 0
        self.hedefad_deger = 0
        self.veritabanisecildi = False
        self.checkbar = customtkinter.StringVar(value="on")
        self.checkbarshowvariable = customtkinter.StringVar(value="on")

        self.gmailcheck = customtkinter.CTkCheckBox(self.master, text="Click if you want e-mail",
                                                    font=("Times New Roman", 20),
                                                    onvalue="on", offvalue="off", variable=self.checkbar
        ,corner_radius=50)
        self.gmailcheck.place(relx=0.1, rely=0.703)

        self.checkbarshow = customtkinter.CTkCheckBox(self.master,text="Click for warning window", font=("Times New Roman", 20)
         ,onvalue="on",offvalue="off",variable=self.checkbarshowvariable,corner_radius=50)

        self.checkbarshow.place(relx=0.24,rely=0.703)

        self.urunfiyatguncellemecheckvariable = customtkinter.StringVar(value="off")
        self.urunfiyatguncellemecheck = customtkinter.CTkCheckBox(self.urunfiyatgui,
                                                                   font=("Times New Roman", 20),
                                                                  text="Click for it to constantly upgrade!",
                                                                  onvalue="on",
                                                                  offvalue="off",
                                                                  corner_radius=50,


                                                                  variable=self.urunfiyatguncellemecheckvariable)
        self.urunfiyatguncellemecheck.place(relx=0.001,rely=0.25)




    def sqlbaglan(self):
        c_diski_klasoru = r"C:\\vıra"
        os.makedirs(c_diski_klasoru, exist_ok=True)

        # SQLite veritabanını oluştur ve bağlan
        self.db_dosya_yolu = "products.db"  # Bu  satırı ekledim, lütfen dosya adını doğrulayın
        self.dosya_yolu = os.path.join(c_diski_klasoru, self.db_dosya_yolu) #klosor ile olusturlan şeyi birleştiriyo
        self.conn = sqlite3.connect(self.dosya_yolu, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS urunler (
                urunlink TEXT,
                urunadi TEXT,
                fiyat REAL,
                urunfiyat INTEGER,
                gmail TEXT
            )
        ''')
        self.conn.commit()

    def anaguigizle(self):
        self.master.withdraw()

        ana_gui.deiconify()

    def uruneklegizle(self):

        self.urunfiyatgui.withdraw()
        ana_gui.deiconify()

    def guiekle(self):


        self.tikla = customtkinter.CTkButton(self.master, text="Click to compare!",
                                             font=("Times New Roman", 20), border_color="white", fg_color="black",
                                             command=self.karsilastartheard)
        self.tikla.place(relx=0.001, rely=0.7 )



        self.urun = customtkinter.CTkEntry(self.master, fg_color="black", border_color="white",
                                           font=("Times New Roman", 20))
        self.urun.place(relx=0.001, rely=0.2, anchor="w")
        self.anaguidon = customtkinter.CTkButton(self.master, fg_color="black", border_color="white",
                                                 command=self.anaguigizle, text="Go back to adding products!",
                                                 font=("Times New Roman", 20))

        self.gmailgir = customtkinter.CTkLabel(self.master,
                                               text="If you would like to receive email notifications when the price of your product drops please enter",
                                               font=("Times New Roman", 20), )
        self.gmailgir.place(relx=0.1, rely=0.5)


        self.anaguidon.place(relx=0.001, rely=0.09)

        self.hedefad = customtkinter.CTkEntry(self.master, fg_color="black", border_color="white",
                                              font=("Times New Roman", 20))

        self.hedefad.place(relx=0.001, rely=0.3, anchor="w")

        self.hedefadgir = customtkinter.CTkLabel(self.master, text="Please enter the name of the product",
                                                 font=("Times New Roman", 20))
        self.hedefadgir.place(relx=0.1, rely=0.3, anchor="w")

        self.hedef = customtkinter.CTkEntry(self.master, fg_color="black", border_color="white",
                                            font=("Times New Roman", 20))
        self.hedef.place(relx=0.001, rely=0.4, anchor="w")  # ghedef fiyat

        self.bildirim = customtkinter.CTkLabel(self.master, font=("Times New Roman", 20),
                                               text="Please specify the target price for notification. If the product price falls below this target"
                                               )
        self.bildirim.place(relx=0.1, rely=0.39)

        self.gmailgiris = customtkinter.CTkEntry(self.master, fg_color="black", font=("Times New Roman", 20),
                                                 border_color="white")
        self.gmailgiris.place(relx=0.001, rely=0.5)

        self.fiyat_alma_buton = customtkinter.CTkButton(
            self.master,
            command=self.baslattheardt,
            text="Click to pull data",
            border_color="white", font=("Times New Roman", 20), fg_color="black")

        self.fiyat_alma_buton.place(relx=0.001, rely=0.6, anchor="w")

        self.urun_bilgi = customtkinter.CTkLabel(self.master, text="Please enter the link of the product",
                                                 font=("Times New Roman", 20))
        self.urun_bilgi.place(relx=0.1, rely=0.2, anchor="w")





    def urunsil(self):
        self.sqlbaglan()
        self.cursor.execute(f"DELETE FROM urunler WHERE urunadi ='{self.urunsilmeentry.get()}' ")
        self.conn.commit()

    def fiyat_kontrola(self):

        for user in self.user_agents:
            headers = {"User-Agent": user}
            sayfa = requests.get(self.urun.get(),headers=headers)
            soup = BeautifulSoup(sayfa.content, 'html.parser')


            self.para = soup.find('span', class_='a-price-whole')

            if self.para:
                self.price_whole = self.para.getText().strip().replace(',', '')

                try:
                    self.current_price = float(self.price_whole)
                except ValueError:

                    print("Geçersiz fiyat formatı.")

                print(f"Günccel Fiyat: {self.current_price}")
                self.fiyat_alma_buton.configure(text="The product has been registered!")






            else:
                if hasattr(self, "bulunamadi"):
                    self.bulunamadi.destroy()
                self.bulunamadi = customtkinter.CTkLabel(self.master, font=("Times New Roman", 20),
                                                         text="We're sorry, we couldn't find the price of your product")
                self.bulunamadi.place(relx=0.1, rely=0.586)
                self.master.after(3000, lambda: self.bulunamadi.destroy())
                print(sayfa.content.decode())
                break


        return self.current_price

    def show_message(self):
        self.sqlbaglan()
        self.cursor.execute("SELECT * FROM urunler")
        self.veriler = self.cursor.fetchall()

        for urun in self.veriler:
            if urun[3] > urun[2]:
                ctypes.windll.user32.MessageBoxW(0,
                                                 f"The price of {urun[1]} has changed. Current price:{urun[2]}",
                                                 "", 0x30)

    def gmail(self):
        #tick işlemi eklenicek
        if self.gmailgiris.get() is None:
            return False

        self.sqlbaglan()
        self.cursor.execute("SELECT * FROM urunler")
        self.veriler = self.cursor.fetchall()

        self.yag = yagmail.SMTP(self.gonderici, "lluk uvcm qcvd scof")

        # E-postayı gönder
        for urun in self.veriler:
            if urun[3] > urun[2]:
                self.yag.send(
                    to=self.gmailgiris.get(),
                    subject="The price of your product has dropped!",
                    contents=f"The price of {urun[1]} has changed. Current price: {urun[2]}",
                )



    def vur(self):
        self.degisenyok.place(relx=0.005, rely=0.75)

    def karsilastar(self):
                self.sqlbaglan()
                self.cursor.execute("SELECT * FROM urunler")
                self.veriler = self.cursor.fetchall()



                if self.veriler:




                    for urun in self.veriler:


                        if self.checkbar.get() == "off" and self.checkbarshowvariable.get() == "off":
                            if hasattr(self, "birinisec"):
                                self.birinisec.destroy()
                            self.birinisec = customtkinter.CTkLabel(self.master, font=("Times New Roman", 20)
                                                                    ,
                                                                    text="You have to choose one of two options!")
                            self.birinisec.place(relx=0.001, rely=0.8)
#kullanıcın bi kapatıp bi açması durumundanı düşüncez
                            self.master.after(3000, lambda: self.birinisec.destroy())
                            break
                        self.tikla.configure(text="Your products are being compared..")
                        if urun[3] > urun[2]: # normaldede alıncak
                            self.tikla.configure(text="comparing...")





                            if self.checkbar.get() == "on" and self.checkbarshowvariable.get() == "off":
                                self.tikla.configure(text="comparing...")


                                self.gmail()
                                self.tikla.configure(text="Click to compare!")
                            elif self.checkbar.get() == "on" and self.checkbarshowvariable.get() == "on":

                                self.gmail()

                                self.show_message()
                                self.tikla.configure(text="Click to compare!")
                            elif self.checkbar.get() == "off" and self.checkbarshowvariable.get() == "on":


                                self.show_message()
                                self.tikla.configure(text="Click to compare!")


                            else:
                                print("sa")

                                self.birinisec = customtkinter.CTkLabel(self.master, font=("Times New Roman", 20)
                                                                        ,
                                                                        text="You have to choose one of two options!")
                                self.birinisec.place(relx=0.001, rely=0.8)



                                self.master.after(3000,lambda  : self.birinisec.destroy())












                            self.master.after(2000, lambda: self.tikla.configure(text="Click to compare!"))

                        else:
                            if hasattr(self,"degisenyok"):
                                self.degisenyok.destroy()
                            self.degisenyok = customtkinter.CTkLabel(self.master,
                                                                         font=("Times New Roman", 20),
                                                                         text="sorry no change")





                            self.master.after(2000, lambda: self.tikla.configure(text="Click to compare!"))
                            self.master.after(2000,self.vur)

                            self.master.after(4000,lambda  : self.degisenyok.destroy())



                            print("ürün fiyatı değişmedi")






                else:
                    if hasattr(self, 'aktıfyok'):
                        self.aktıfyok.destroy()  # Eğer varsa, önceki etiketi yok et
                    self.aktıfyok = customtkinter.CTkLabel(self.master, text="Product not found!",
                                                           font=("Times New Roman", 20))
                    self.aktıfyok.place(relx=0.001, rely=0.74)
                    self.master.after(3000, lambda: self.aktıfyok.destroy())



            # compareyi değiştircez

            #compareyi değiştircez










    def karsilastartheard(self):
        threading.Thread(target=self.karsilastar).start()

    def urunfiyatguncelleme(self):
            taranan_urunler = set()


            self.sqlbaglan()

            cursor_fetch = self.conn.cursor()
            cursor_fetch.execute("SELECT urunlink FROM urunler")
            self.urunler = cursor_fetch.fetchall()



            if self.urunler:
                    for urun in self.urunler:

                        self.urunleriminfiyatiguncel.configure(text="updating...")




                        if urun[0] not in taranan_urunler:
                            taranan_urunler.add(urun[0])

                            for user in self.user_agents:
                                if self.flag == False:
                                    break
                                headers = {"User-Agent": user}

                                sayfa = requests.get(urun[0], headers=headers)
                                soup = BeautifulSoup(sayfa.content, 'html.parser')

                                para = soup.find('span', class_='a-price-whole')

                                if para:

                                    fiyat_tam = para.getText().strip().replace(',', '')
                                    print(fiyat_tam)
                                    cursor_fetch.execute('''
                                        UPDATE urunler
                                        SET fiyat = ?
                                        WHERE urunlink = ?
                                    ''', (fiyat_tam, urun[0]))
                                    self.guncellenen_urun_sayisi += 1
                                    if hasattr(self, "oldu"):
                                        self.oldu.destroy()
                                    self.oldu = customtkinter.CTkLabel(
                                        self.urunfiyatgui,
                                        text="Scanning of your products has been completed and the changes will be applied when you restart.",
                                        font=("Times New Roman", 20)
                                    )
                                    self.oldu.place(relx=0.15, rely=0.30)
                                    self.urunfiyatgui.after(45000, lambda: self.oldu.destroy())
                                    self.urunleriminfiyatiguncel.configure(text="Update the price of products!"),
                                    break







            elif self.urunler == []:
                    if hasattr(self, "urunyoklabel"):
                        self.urunyoklabel.destroy()
                    self.urunyoklabel = customtkinter.CTkLabel(self.urunfiyatgui, text="you have no active product!",
                                                               font=("Times New Roman", 20))

                    self.urunyoklabel.place(relx=0.5, rely=0.3)
                    self.urunfiyatgui.after(3000, lambda: self.urunyoklabel.destroy())










    def on_enter(self, event):
        event.widget.config(bg="red", cursor="hand2")

    def on_leave(self, event):
        event.widget.config(bg="SystemButtonFace", cursor="arrow")

    def on_click(self, event):
        event.widget.destroy()

    def urunsilmetehardd(self):
        threading.Thread(target=self.urunsil).start()
        threading.Thread(target=self.degisikinfokomut).start()
        self.urunfiyatgui.update_idletasks()

    def degisikinfokomut(self):
        if hasattr(self, "degisikinfo"):
            self.degisikinfo.destroy()
        self.degisikinfo = customtkinter.CTkLabel(self.urunfiyatgui,
                                                  text="After you close the program, your products will be deleted!",
                                                  font=("Times New Roman", 20))

        self.degisikinfo.place(relx=0.136, rely=0.62)
        self.urunfiyatgui.after(3000, lambda: self.degisikinfo.destroy())

    def hepsinisilme(self):
        self.sqlbaglan()
        self.cursor.execute("DELETE FROM urunler")
        self.conn.commit()

    def hepsinisilmetheard(self):

        self.sqlbaglan()

        self.veriler = self.cursor.fetchall()
        threading.Thread(target=self.hepsinisilme).start()
        if hasattr(self, "info"):
            self.info.destroy()
        self.info = customtkinter.CTkLabel(self.urunfiyatgui, text="All will be deleted when the program is restarted"
                                           , font=("Times New Roman", 20))
        self.info.place(relx=0.14, rely=0.72)
        self.urunfiyatgui.after(3000, lambda: self.info.destroy())

    def urunekledb(self):
        try:
            self.sqlbaglan()
            self.cursor.execute("SELECT * FROM urunler")
            self.veriler = self.cursor.fetchall()


            self.herseyisil = customtkinter.CTkButton(self.urunfiyatgui, text="Click to delete all products!",
                                                      border_color="white", fg_color="black",
                                                      font=("Times New Roman", 20), command=self.hepsinisilmetheard)
            self.herseyisil.place(relx=0.001, rely=0.72)

            self.urunsilmeentry = customtkinter.CTkEntry(self.urunfiyatgui, fg_color="black", border_color="white",
                                                         font=("Times New Roman", 20))
            self.urunsilmeentry.place(relx=0.002, rely=0.54)

            self.urunsilmeinfo = customtkinter.CTkLabel(self.urunfiyatgui, font=("Times New Roman", 20),
                                                        text="Enter the name of the product you want to delete"
                                                        , width=10, height=10)
            self.urunsilmeinfo.place(relx=0.09, rely=0.54)

            self.urunsilmebuton = customtkinter.CTkButton(self.urunfiyatgui,
                                                          command=self.urunsilmetehardd,
                                                          text="Click to delete the product!",
                                                          border_color="white",
                                                          font=("Times New Roman", 20),
                                                          fg_color="black"
                                                          )
            self.urunsilmebuton.place(relx=0.001, rely=0.62)

            urunleriniz = customtkinter.CTkLabel(self.urunfiyatgui, font=("Times New Roman", 20), text="your products:")
            urunleriniz.place(relx=0.33, rely=0.315, anchor="w")

            for i, veri in enumerate(self.veriler):
                urunadiniz = customtkinter.CTkLabel(self.urunfiyatgui, text="your product names", text_color="white",
                                                    font=("Times New Roman", 20))
                urunadiniz.place(relx=0.39, rely=0.25)
                urunsuankifiyat = customtkinter.CTkLabel(self.urunfiyatgui, text="current prices of your products",
                                                         text_color="white", font=("Times New Roman", 20))
                urunsuankifiyat.place(relx=0.496, rely=0.25)
                urunhedef = customtkinter.CTkLabel(self.urunfiyatgui, text="asking price and below", text_color="white",
                                                   font=("Times New Roman", 20))
                urunhedef.place(relx=0.65, rely=0.25)

                label1 = customtkinter.CTkLabel(self.urunfiyatgui,
                                                text=veri[1].strip().replace("(", "").replace(")", "").replace("'", ""),
                                                width=20, height=2, text_color="white", font=("Times New Roman", 20))
                label1.place(relx=0.42, rely=0.315 + i * 0.06, anchor="w")

                label2 = customtkinter.CTkLabel(self.urunfiyatgui, text=veri[2], width=20, height=2, text_color="white",
                                                font=("Times New Roman", 20))  # urun gercke fiyatı
                label2.place(relx=0.53, rely=0.315 + i * 0.06, anchor="w")

                label3 = customtkinter.CTkLabel(self.urunfiyatgui, text=veri[3], width=20, height=2, text_color="white",
                                                font=("Times New Roman", 20))
                label3.place(relx=0.69, rely=0.315 + i * 0.06, anchor="w")  # gmaile gönderilcek

                fiyat_alma_buton = customtkinter.CTkButton(self.master, command=self.urunffiyatgunceltheard,
                                                           text="Click to update the price of the products!",
                                                           border_color="white", font=("Times New Roman", 20),
                                                           fg_color="black")
                fiyat_alma_buton.place(relx=0.001, rely=0.45, anchor="w")






        except Exception as e:
            print("Hata:", e)

    def urunffiyatgunceltheard(self):
        if  self.urunfiyatguncellemecheckvariable.get() == "off":
            threading.Thread(target=self.urunfiyatguncelleme).start()

        elif self.urunfiyatguncellemecheckvariable.get() == "on":
            threading.Thread(target=self.sonsuz).start()







        if hasattr(self, "degisikinfo2"):
            self.degisikinfo2.destroy()

        self.degisikinfo2 = customtkinter.CTkLabel(self.master,
                                                   text="The price of your products will be updated after the program restarts",
                                                   font=("Times New Roman", 20))
        self.degisikinfo2.place(relx=0.146, rely=0.7)
        self.urunfiyatgui.after(3000, lambda: self.degisikinfo2.destroy())
        plt.switch_backend('agg')

    def sonsuz(self):
        taranan_urunler = set()

        self.sqlbaglan()

        cursor_fetch = self.conn.cursor()
        cursor_fetch.execute("SELECT urunlink FROM urunler")
        self.urunler = cursor_fetch.fetchall()

        while self.flag:



         if self.urunler:

            for urun in self.urunler:








                if self.flag == False:
                    break


                if urun[0] not in taranan_urunler:
                    taranan_urunler.add(urun[0])

                    for user in self.user_agents:

                        headers = {"User-Agent": user}

                        sayfa = requests.get(urun[0], headers=headers)
                        soup = BeautifulSoup(sayfa.content, 'html.parser')

                        para = soup.find('span', class_='a-price-whole')

                        if para:
                            self.urunleriminfiyatiguncel.configure(text="updating...")



                            if self.flag == False:
                                if hasattr(self, "oldu"):
                                    self.oldu.destroy()
                                self.oldu = customtkinter.CTkLabel(
                                    self.urunfiyatgui,
                                    text="Scanning of your products has been completed and the changes will be applied when you restart.",
                                    font=("Times New Roman", 20)
                                )
                                self.oldu.place(relx=0.15, rely=0.30)
                                self.urunfiyatgui.after(2000,lambda  : self.oldu.destroy())
                                self.urunleriminfiyatiguncel.configure(text = "Update the price of products!"),
                                break

                            fiyat_tam = para.getText().strip().replace(',', '')
                            print(fiyat_tam)
                            cursor_fetch.execute('''
                                             UPDATE urunler
                                             SET fiyat = ?
                                             WHERE urunlink = ?
                                         ''', (fiyat_tam, urun[0]))
                            self.guncellenen_urun_sayisi += 1






         elif self.urunler == []:

             if hasattr(self, "urunyoklabel1"):
                 self.urunyoklabel1.destroy()
             self.urunyoklabel1 = customtkinter.CTkLabel(self.urunfiyatgui, text="you have no active product!",
                                                        font=("Times New Roman", 20))

             self.urunyoklabel1.place(relx=0.15, rely=0.3)
             self.urunfiyatgui.after(3000, lambda: self.urunyoklabel1.destroy())
             break


    def urunfiyatguncelthearffalse(self):
      self.flag = False






    def baslat(self):
        global urun
        self.hedefad_deger = self.hedefad.get()
        self.url = self.urun.get()
        self.gmailgirisget = self.gmailgiris.get()

        self.uruncek()

        self.rely_value += 0.1
        self.urun.delete(0, customtkinter.END)
        self.hedefad.delete(0, customtkinter.END)
        self.hedef.delete(0, customtkinter.END)
        if self.gmailgirisget:
         self.gmailgirisget.delete(0, customtkinter.END)

    def baslat_thread(self):

        self.para = self.fiyat_kontrola()
        self.baslat()




    def baslattheardt(self):
        threading.Thread(target=self.baslat_thread).start()
        self.master.after(5300, lambda: self.fiyat_alma_buton.configure(text="click to pull data!"))

    def uruncek(self):
        try:
            self.sqlbaglan()
            self.hedefw = self.hedef.get()
            self.gmailgirisget = self.gmailgiris.get()

            if self.para is not None:
                self.cursor.execute('''
                     INSERT INTO urunler (urunlink,urunadi,fiyat,urunfiyat,gmail)
                     VALUES (?,?,?,?,?) 
                 ''', (self.url, self.hedefad_deger, self.para, self.hedefw, self.gmailgirisget))
                self.conn.commit()
        except Exception as e:
            print(f"{e}")




    def discordname(self):
        self.info.clipboard_clear()
        self.info.clipboard_append("._rmonster")
        self.info.update()
        self.mydiscordn.configure(text="copied successfully!")
        self.info.after(1300,lambda  : self.mydiscordn.configure(text="._rmonster"))

    def gmailcopy(self):
        self.info.clipboard_clear()
        self.info.clipboard_append("yourproductbot@gmail.com")
        self.info.update()
        self.mygmailadress.configure(text="copied successfully!")
        self.info.after(1300, lambda: self.mygmailadress.configure(text="yourproductbot@gmail.com"))

    def isteisim(self):
        self.info = customtkinter.CTk()
        self.info.after(0, lambda: self.info.state("zoomed"))


        self.mydiscord = customtkinter.CTkLabel(self.info, text="my discord :", font=("Times New Roman", 20))
        self.mydiscord.place(relx=0.002, rely=0.3)

        self.mydiscordn = customtkinter.CTkButton(self.info, text="._rmonster", font=("Times New Roman", 20),
                                                  command=self.discordname,fg_color="black",width=3,height=3)
        self.mydiscordn.place(relx=0.06, rely=0.3)

        self.mygmail = customtkinter.CTkLabel(self.info, text="my gmail :", font=("Times New Roman", 20))
        self.mygmail.place(relx=0.001, rely=0.38)

        self.mygmailadress = customtkinter.CTkButton(self.info, text="yourproductbot@gmail.com",
                                                     font=("Times New Roman", 20),fg_color="black",command=self.gmailcopy)
        self.mygmailadress.place(relx=0.05, rely=0.38)
        self.anaguidonurun2 = customtkinter.CTkButton(self.info, text="Go back to adding products!",
                                                     border_color="white",
                                                     font=("Times New Roman", 20), fg_color="black",
                                                     command=self.uruneklegizle)
        self.anaguidonurun2.place(relx=0.001, rely=0.2)

        self.info.mainloop()



def yeni_urun():
    global yeni_fiyat_kontrol
    urunisimleri = []
    yeni_gui = customtkinter.CTk()


    yeni_fiyat_kontrol = FiyatKontrol(yeni_gui)
    yeni_gui.after(0, lambda: yeni_gui.state("zoomed"))
    yeni_fiyat_kontrol.guiekle()
    hedefad_deger = yeni_fiyat_kontrol.hedefad.get()
    urunisimleri.append(hedefad_deger)
    yeni_gui.geometry("1920x1080")
    yeni_gui.mainloop()


def yengui():
    yeni_fiyat_kontrol.urunfiyatgui.after(0, lambda: yeni_fiyat_kontrol.urunfiyatgui.state("zoomed"))

    yeni_fiyat_kontrol.urunekledb()

    yeni_fiyat_kontrol.urunfiyatgui.mainloop()









if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    yeni_gui = customtkinter.CTk()

    yeni_fiyat_kontrol = FiyatKontrol(yeni_gui)





    urungoster = customtkinter.CTkButton(ana_gui, width=5, height=5, fg_color="black", border_color="white",
                                         font=("Times New Roman", 20),
                                         command=yengui, text="Show products!")

    urungoster.place(relx=0.002, rely=0.30)

    benimifo = customtkinter.CTkButton(ana_gui,font=("Times New Roman", 20),text="For communication",fg_color="black",
    command=yeni_fiyat_kontrol.isteisim)
    benimifo.place(relx=0.001,rely=0.68)


    urunsilme = customtkinter.CTk()

    yeni_urun_button = customtkinter.CTkButton(
        ana_gui,
        border_color="white",


        command=yeni_urun,
        text="Add New Product",
        fg_color="black", font=("Times New Roman", 20))


    yeni_urun_button.place(relx=0.002, rely=0.5, anchor="w")
    ana_gui.after(0, lambda: ana_gui.state("zoomed"))

    ana_gui.geometry("1920x1080")

    ana_gui.mainloop()