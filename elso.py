import random

from modul import osszeg as szum

# from modul import *
# import modul as m


'''
ez egy
tobsoros komment




kor = 50
nev = "Guszti"
hazas = True

kor += 5

print ("Felhasznalo: ", kor, nev, hazas)

szoveg = "Rendszamtarto"

print(szoveg[0:4])
print(szoveg[4:8])
print(szoveg[-5:])

lista = ["Rend", "szam", "tarto"]
print(lista)
print(lista[0],lista[1],lista[2], sep="")

lista.append ("tabla")
print(lista)

halmaz = {1,2,3, "negy", 1}
print(halmaz)

szotar = {"nev": "Jozsi", "kor": 40, "hazas": True}
print(szotar)
'''

#kor = int(input("Hany eves vagy: "))
kor =50
print ("A felhasznalo kora:".rjust(50,"_"))
print(f"A felhasznalo kora: {kor}")
print("A felhasznalo kora: {0}". format(kor))
print (random.randint(5,20))

szum()
