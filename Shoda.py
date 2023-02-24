from Softcom import softcom
from Czc import czc

class shoda:
    """
    Funkce Shoda najde produkty se stejným kódem výrobku, informace o nich dá k sobě a připraví program na smazání přebytečných duplikantů.
    """
    ShodaIndex = []
    cenaProDruhyE = []
    for i in range(300):
        cenaProDruhyE.append(0)
    def Shoda():
        shodap = 0
        for i in range (0, len(czc.idKarty)):
            for j in range (0,len(softcom.idKartyS)):
                if czc.idKarty[i]==softcom.idKartyS[j]:
                    shodap +=1
                    shoda.cenaProDruhyE[i] = softcom.cenaKartyS[j]
                    shoda.ShodaIndex.append(j)          
        print("Pocet shodnych produktu:", shodap)