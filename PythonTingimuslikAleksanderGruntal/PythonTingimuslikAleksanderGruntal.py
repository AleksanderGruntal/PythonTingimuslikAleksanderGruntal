from math import *
from random import *
#1ÜL
while True:
    nimi=input("Mis on sinu nimi? ")
    if nimi.isalpha(): break

if nimi.upper()=="JUKU":
    while True:
        try:
            vanus=int(input("kui vana sa oled?"))
            break
        except:
           print("On vaja arvude tüüp kasutada")

    if 0<vanus<6:
        print("Tasuta")
    elif 6<vanus<=14:
        print("Lastepilet")
    elif 15<vanus<65:
        print("Täispilet")
    elif 65<=vanus<100:
        print("Sooduspilet")
    else:
        print("Vanus ei soobi!")
else:
    print("Ma otsi Juku!")

#2ÜL
while True:
  nimi1=input("1. Mis sinu nimi on?")
  if nimi1.isalpha(): break
while True:
  nimi2=input("2. Mis sinu nimi on?")
  if nimi2.isalpha(): break
if nimi1=="Anna" and nimi2=="Ala": print("Neid on täna pinginaabrid")


#3ÜL
while True:
      try:
          p=int(input("kui vana sa oled?"))
          if p>0: break
      except:
         print("On vaja numbreid kirjutada, mis on suurem kui 0")
while True:
    try:
        l=int(input("kui vana sa oled?"))
        if l>0: break
    except:
       print("On vaja numbreid kirjutada, mis on suurem kui 0")
while True:
    v=input("Kas tahad remonti teha? ")
    if v.upper()=="JAH" or v.upper()=="EI" : break
if v.upper()=="JAH":
    while True:
        try:
            hind=float(input("Kui palju maksma m^2"))
        except TypeError:
            print()
    hind=l*p*hind
    print(f"Remonti hind on {hind}")
else:
    pass
