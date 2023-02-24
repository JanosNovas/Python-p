import mysql.connector
tabulka = mysql.connector.connect(host="localhost", user = "root", passwd="16091300", database = "vyrobky")
mycursor = tabulka.cursor()

from datetime import datetime

from Softcom import softcom
from Czc import czc
from Shoda import shoda
from PrimaryKey import primaryKey

class Produkt:
    """
    Classa Produkt před zapsáním dat do tabulky pomůže přeměnit získaná data do požadovaného formátu.
    """
    def __init__(self, id, nazev, cas, cena, cena2):
        self.id = id
        self.nazev = nazev
        self.cas = cas
        self.cena = cena
        self.cena2 = cena2


class zapis:
    primary = primaryKey.PrimaryKey()
    """
    Funkce ZapisDoTabulky zjistí auktuální čas, naše data uvede do vhodného formátu a následně je zapíše do tabulky v mysql workbench.
    """
    def ZapisDoTabulky():
        for i in range (0, len(czc.idKarty)):
            zapis.primary += 1
            casZapisu = datetime.now()
            casZ = str(casZapisu)
            prdk = Produkt(czc.idKarty[i], czc.nazevKarty[i], casZ, czc.cenaKarty[i], shoda.cenaProDruhyE[i])
            vysledna=(zapis.primary, prdk.id, prdk.nazev, prdk.cas, prdk.cena, prdk.cena2)
            print(vysledna)
            sqlFormula = "INSERT INTO tabulka_vyrobku(Primary_Key, ID, Nazev, Time_when, Cena_CZC, Cena_SOFTCOM) VALUES(%s,%s,%s,%s,%s,%s)"
            mycursor.execute(sqlFormula, vysledna)
            tabulka.commit()

        for i in range (0, len(softcom.idKartyS)):
            zapis.primary += 1
            casZapisu = datetime.now()
            casZ = str(casZapisu)
            prdk = Produkt(softcom.idKartyS[i], softcom.nazevKartyS[i], casZ, 0, softcom.cenaKartyS[i])
            vysledna=(zapis.primary, prdk.id, prdk.nazev, prdk.cas, prdk.cena, prdk.cena2)
            print(vysledna)
            sqlFormula = "INSERT INTO tabulka_vyrobku(Primary_Key, ID, Nazev, Time_when, Cena_CZC, Cena_SOFTCOM) VALUES(%s,%s,%s,%s,%s,%s)"
            mycursor.execute(sqlFormula, vysledna)
            tabulka.commit()