from Softcom import softcom
from Czc import czc 
from Shoda import shoda

class resetP:
    """
    Funkce resetP musí existovat, aby mohl program pracovat s informacemi vícekrát za jedno spuštění. Jediné co funkce dělá je, že vynuluje pomocné listy a připraví je na znovupoužití.
    """
    def reset():
        softcom.nazevKartyS.clear()
        softcom.cenaKartyS.clear()
        softcom.idKartyS.clear()
        czc.nazevKarty.clear()
        czc.cenaKarty.clear()
        czc.idKarty.clear()
        shoda.ShodaIndex.clear()
        shoda.cenaProDruhyE.clear()
        for i in range(300):
            shoda.cenaProDruhyE.append(0)