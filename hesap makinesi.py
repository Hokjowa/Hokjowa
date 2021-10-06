import tkinter as tk

def topla ():
 s1 = int(sayi1.get())
 s2 = int(sayi2.get())
 sonuc['text'] = str(s1+s2)

def cikar ():
 s1 = int(sayi1.get())
 s2 = int(sayi2.get())
 sonuc['text'] = str(s1-s2)

def carp ():
 s1 = int(sayi1.get())
 s2 = int(sayi2.get())
 sonuc['text'] = str(s1*s2)

def bol ():
 s1 = float(sayi1.get())
 s2 = float(sayi2.get())
 sonuc['text'] = str(s1/s2)



# yükseklik
pencere = tk.Tk()
pencere.geometry("300x300")

sayi1 = tk.Entry(width=10)
sayi1.place(x=20,y=20)

sayi2 = tk.Entry(width=10)
sayi2.place(x=100,y=20)

# Yazı
sonuc = tk.Label(text="Sonuc",bg="gray")
sonuc['font'] = "Verdana 12 bold"
sonuc['fg'] = "#FB8102" #hex code renk tanımlamasını kabul eder
sonuc.place(x=180,y=20)

yapimci = tk.Label(text="Yapımcı Hokjowa",bg="purple")
yapimci['font'] = "Verdana 12 bold"
yapimci['fg'] = "#9893DA" #hex code renk tanımlamasını kabul eder
yapimci.place(x=50,y=180)

btopla = tk.Button(text="+",bg="gray",font="Verdana 18 bold", command=topla).place(x=20,y=60)
bcikar = tk.Button(text="-",bg="gray",font="Verdana 18 bold", command=cikar).place(x=80,y=60)
bcarp = tk.Button(text="x",bg="gray",font="Verdana 18 bold", command=carp).place(x=140,y=60)
bbol = tk.Button(text="/",bg="gray",font="Verdana 18 bold", command=bol).place(x=200,y=60)

pencere.mainloop()