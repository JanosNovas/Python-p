from Softcom import softcom
from Shoda import shoda

class smazs:
    """
    Funkce smazs vymaže data ze stránky Softcom.cz, která by tvořily duplikanty k již existujícím produktům.
    """
    def DelShody():
        for j in range (0, len(shoda.ShodaIndex)):
            del softcom.idKartyS[j]
            del softcom.cenaKartyS[j]
            del softcom.nazevKartyS[j]