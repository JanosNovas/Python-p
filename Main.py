import time

from Softcom import softcom
from Czc import czc
from Shoda import shoda
from SmazatShodu import smazs
from Zapis import zapis
from Resetovani import resetP

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

class Opakovani:
    """
    Spustí funkci Zopakuj, která obsahuje funkci main. Také tvoří ukazatel odpočtu času a spouští main v časových intervalech. Interval je nastaven na 5 minut.
    """
    def Zopakuj():
        while True:
            cas = 300
            main()
            while cas:
                mins, secs = divmod(cas, 60)
                timer = '{:02d}:{:02d}'.format(mins,secs)
                print(timer, end="\r")
                time.sleep(1)
                cas -= 1

def main():
    """
    Funkce main obsahuje všechny funkce programu.
    """
    czc.CZC(headers)
    softcom.Softcom(headers)
    shoda.Shoda()
    smazs.DelShody()
    zapis.ZapisDoTabulky()
    resetP.reset()


Opakovani.Zopakuj()