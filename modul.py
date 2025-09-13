#Ez egy proba modul


def osszeg ():
    egyik = int(input("Kerek egy szamot:"))
    masik = int(input("Kerek egy masik szamot:"))

    eredmeny= egyik+masik

    print ("Az eredmeny erteke" . center(50))
    print (str(egyik).rjust(50, "_"))
    print (str(masik).rjust(50, "_"))
    print("+")
    print (str(eredmeny).rjust(50, "_"))
    return

def szorzas ():
    egyik = int(input("Kerek egy szamot:"))
    masik = int(input("Kerek egy masik szamot:"))

    eredmeny= egyik*masik

    print ("Az eredmeny erteke" . center(50))
    print (str(egyik).rjust(50, "_"))
    print (str(masik).rjust(50, "_"))
    print("*")
    print (str(eredmeny).rjust(50, "_"))
    return