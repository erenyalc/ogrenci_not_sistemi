import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
# Gerekli kütüphaneleri import ettik.

class pencere(QDialog):
    def __init__(self):
        super().__init__()
        self.arayuz()
# PyQt5 ile arayüz oluşturmak için object-oriented bir blok oluşturduk.
    def arayuz(self):
        self.grid = QGridLayout()
        self.ogrno = QLabel("Öğrenci Numarası: ")
        self.ogrnoinput = QLineEdit()

        self.ograd = QLabel("Öğrenci Adı: ")
        self.ogradinput = QLineEdit()

        self.ogrsoyad = QLabel("Öğrenci Soyadı: ")
        self.ogrsoyadinput = QLineEdit()

        self.ogrnot = QLabel("Matematik Notu: ")
        self.ogrnotinput = QLineEdit()

        self.sonuc = QLabel("")
        self.sonuc1 = QLabel("")

        self.buton = QPushButton("Gönder")
# Arayüzün taslağını oluşturmak için oluşturduğumuz kodlar.

        self.grid.addWidget(self.ogrno, 1, 0)
        self.grid.addWidget(self.ogrnoinput, 1, 1)

        self.grid.addWidget(self.ograd, 2, 0)
        self.grid.addWidget(self.ogradinput, 2, 1)

        self.grid.addWidget(self.ogrsoyad, 3, 0)
        self.grid.addWidget(self.ogrsoyadinput, 3, 1)

        self.grid.addWidget(self.ogrnot, 4, 0)
        self.grid.addWidget(self.ogrnotinput, 4, 1)

        self.grid.addWidget(self.sonuc, 5, 1)
        self.grid.addWidget(self.sonuc1, 6, 1)

        self.grid.addWidget(self.buton, 7, 1)
# Oluşturulan blokların yerlerini belirlemek için oluşturduğumuz kod bloğu.


        self.buton.clicked.connect(self.gonder)
        self.setWindowTitle("Matematik Not Hesaplayıcı")
        self.setGeometry(100, 60, 500, 300)
        self.setLayout(self.grid)
        self.show()
# Butonun çalışması için fonksiyon oluşturma, başlık oluşturma, pozisyonu belirleme gibi işlemleri çalıştıran kod bloğu.


    def gonder(self):
        self.ID = self.ogrnoinput.text()
        self.Name = self.ogradinput.text()
        self.Surname = self.ogrsoyadinput.text()
        self.Grade = int(self.ogrnotinput.text())
        
        if 90 < self.Grade <= 100:
            self.sonuc.setText("Geçti")
            self.sonuc1.setText("AA")

        elif 85 <=self.Grade <=89:
            self.sonuc.setText("Geçti")
            self.sonuc1.setText("BA")

        elif 80<= self.Grade <=84:
            self.sonuc.setText("Geçti")
            self.sonuc1.setText("BB")

        elif 75 <=self.Grade <=79:
            self.sonuc.setText("Geçti")
            self.sonuc1.setText("CB")

        elif 70 <=self.Grade <=74:
            self.sonuc.setText("Geçti")
            self.sonuc1.setText("CC")

        elif 65 <=self.Grade <=69:
            self.sonuc.setText("Geçti")
            self.sonuc1.setText("DC")

        elif 60<= self.Grade <=64:
            self.sonuc.setText("Geçti")
            self.sonuc1.setText("DD")

        elif self.Grade <=59:
            self.sonuc.setText("Kaldı")
            self.sonuc1.setText("FF")
        
        self.sonuc.text()
        self.sonuc1.text()
# Fonksiyonun oluşturulması, değerlerin text formatında elde edilmesi ve koşullu durumların çalıştırılması işlemleri.

# Değişkenler bir dataframe'in içine gönderildi.
        self.df = pd.DataFrame(columns=["ID","Name","Surname","Grade","Lettergrade","Status"])
        self.df.loc[len(self.df.index)] = [self.ID,self.Name,self.Surname,self.Grade,self.sonuc1.text(),self.sonuc.text()]
        
# Oluşturulan dataframe excel'e gönderildi.
        self.writer = pd.ExcelWriter('output.xlsx')
        self.df.to_excel(self.writer)
        self.writer.save()

# Programın çalışması için gerekli kodlar.
app = QApplication(sys.argv)
pencere = pencere()
sys.exit(app.exec_())