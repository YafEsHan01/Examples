#VİRA BİSMİLLAH
from tkinter import *
from  tkinter import messagebox
import random
liste = []
pencere = Tk()
pencere.geometry("650x450")
pencere.tk_setPalette("lightblue")
başlık = pencere.title("Şanslı Kişi Uygulaması")
hg = Label(text="WELCOME",fg="red",font="algerian 20 bold")
hg.pack(side=TOP)
info = Label(text="Lütfen İSimleri Girdikten sonra kaydet butonuna basmayı unutmayınız",fg="black",font="Calibri 14 bold")
info.pack()

"""ybar = Scrollbar(pencere,orient=VERTICAL)
ybar.pack(side=RIGHT,fill=Y)
text = Text(yscrollcommand=ybar.set)
text.pack()
ybar.config(command=text.yview)"""

"""xbar = Scrollbar(pencere,orient=HORIZONTAL)
xbar.pack(side=BOTTOM,fill=X)
text1 = Text(wrap=NONE,xscrollcommand=xbar.set)
text1.pack()
xbar.config(command=text1.xview)"""



def kaydet():
   
    kayıt = veri.get(1.0,END)
    fp = open("kayıt.txt","w")
    fp.write(kayıt)

kaydet = Button(text="Kaydet",command=kaydet,font="Calibri 11 bold")
kaydet.pack(side=BOTTOM)

def seçim():
    fp = open("kayıt.txt","r")
    for i in fp:
        liste.append(i)
    seç = random.choice(liste)
    messagebox.showinfo("Şans","Şanslı Kişi:{}".format(seç))
    
find = Button(text="Şanslı Kişiyi Bul",command=seçim,font="Calibri 11 bold")
find.pack(side=BOTTOM)

ybar = Scrollbar(pencere,orient=VERTICAL)
veri = Text(yscrollcommand=ybar.set,font="calibri 13 bold",fg="black")
veri.pack()

mainloop()
