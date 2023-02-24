import requests
from bs4 import BeautifulSoup

class czc:
    """
    Funkce CZC najde všechny grafické karty na eshopu czc.cz, získá jejich data a uloží je do pomocných listů, aby s nimi mohl program pracovat.
    """
    nazevKarty = []
    cenaKarty = []
    idKarty = []
    def CZC(headers):
        baseurlC = 'https://www.czc.cz/'
        productlistC = []
        productlinksC = []
        newProductlistStringC = []
        celaUrlC = []
        for x in range(1):#12
            r = requests.get(f'https://www.czc.cz/herni-graficke-karty/produkty?q-first={27*(x-1)}')
            soup = BeautifulSoup(r.content, 'lxml')

            productlistC += soup.find_all('div', class_='new-tile')
        print('Naslo se ',(len(productlistC)), 'produktu na CZC.CZ')

        for itemC in productlistC:
            for linkC in itemC.find_all('a', href=True):
                productlinksC.append(baseurlC + linkC['href'])
            productlistStringC = str(linkC)
            hrefPosZC = productlistStringC.find('href')
            hrefPosKC = productlistStringC.find('produkt')
            newProductlistStringC.append(productlistStringC[hrefPosZC+7:hrefPosKC+7])

        for x in newProductlistStringC:
            celaUrlC.append(baseurlC+x)

        for i in celaUrlC:
            r = requests.get(i, headers=headers)
            soup = BeautifulSoup(r.content, 'lxml')

            jmenoC = soup.find('h1', title=True).text.strip()
            cenaCpom = soup.find('div', class_='pd-price-wrapper')
            
            try:
                for j in cenaCpom.find('span', class_='price-vatin'):
                    cenaZac = j.find("K")
                    cenaC = int((j[0:cenaZac - 5])+(j[cenaZac-4:cenaZac-1]))
            except:
                cenaC = 0

            try:
                for q in cenaCpom.find('span', class_='price-vatex'):
                    cenaZac = q.find("K")
                    cenaBezDPHC = int((q[0:cenaZac - 5])+(q[cenaZac-4:cenaZac-1]))
            except:
                cenaBezDPHC = 0
            kodCpom = soup.find_all('p', class_='clearfix')
            kodCpomS = str(kodCpom)
            KodCPosZC = kodCpomS.find('Kód výrobce:')
            KodCPosKC = kodCpomS.find('strong', KodCPosZC+28)
            kodC = (kodCpomS[KodCPosZC + 28: KodCPosKC-2])

            czc.nazevKarty.append(jmenoC)
            czc.idKarty.append(kodC)
            czc.cenaKarty.append(cenaC)        