from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QVBoxLayout, QWidget

app = QApplication([])  # QApplication nesnesi yaratma

global ad_edit
global link_edit
global gonderilecek_sayi_edit

ad_edit = QLineEdit()  
link_edit = QLineEdit()  
gonderilecek_sayi_edit = QLineEdit() 

class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.gonder_button = QPushButton("Gönder", self)

        layout = QVBoxLayout(self)
        layout.addWidget(ad_edit)
        layout.addWidget(link_edit)
        layout.addWidget(gonderilecek_sayi_edit)
        layout.addWidget(self.gonder_button)

        self.gonder_button.clicked.connect(self.gonder)

        ad_edit.setPlaceholderText("Saldırılacak kişi:")
        link_edit.setPlaceholderText("Gönderilecek fotoğrafın linki: ")
        gonderilecek_sayi_edit.setPlaceholderText("Fotoğrafın kaç defa gönderilmesini istiyorsunuz:")
    
    def gonder(self):
        global ad
        global link
        global gonderilecek_sayi
        ad = ad_edit.text()
        link = link_edit.text()
        gonderilecek_sayi = gonderilecek_sayi_edit.text()
        app.exit()


form = Form()
form.show()
app.exec_()


