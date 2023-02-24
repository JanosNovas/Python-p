import requests
from bs4 import BeautifulSoup

class softcom:
    """
    Funkce Softcom najde všechny grafické karty na eshopu softcom.cz, získá jejich data a uloží je do pomocných listů, aby s nimi mohl program pracovat.
    """
    nazevKartyS = []
    cenaKartyS = []
    idKartyS = []
    def Softcom(headers):
        baseurlS = 'https://www.softcom.cz/eshop/'
        productlinksS = []
        newProductlistStringS = []
        productlistS = []
        celaUrlS = []
        for x in range(1):#8
            r = requests.get(f'https://www.softcom.cz/eshop/komponenty-graficke-karty_c4482.html?page={x}#prodlistanchor')
            soup = BeautifulSoup(r.content, 'lxml')

            productlistS += soup.find_all('div', class_='prodbox')
        print('Naslo se ',(len(productlistS)), 'produktu na SOFTCOM.CZ')
        for itemS in productlistS:
            for linkS in itemS.find_all('a', href=True):
                productlinksS.append(baseurlS + linkS['href'])
            productlistString = str(linkS)
            hrefPosZ = productlistString.find('href')
            hrefPosK = productlistString.find('html')
            newProductlistStringS.append(productlistString[43:hrefPosK + 4])

        for x in newProductlistStringS:
            celaUrlS.append(baseurlS + x)

        for i in celaUrlS:
            r = requests.get(i, headers=headers)
            soup = BeautifulSoup(r.content, 'lxml')

            jmenoS = soup.find('div', class_='headline').text.strip()
            
            cenaS = soup.find('td', class_='price')
            cenaS = str(cenaS)
            cenaZac = cenaS.find("K")
            cenaS = int((cenaS[18:cenaZac - 12])+(cenaS[cenaZac - 11:cenaZac - 8]))

            kodSpom = soup.find('tr', class_='partno')
            kodSpomS = str(kodSpom)
            kodSZ = kodSpomS.find('Part')
            kodSK = kodSpomS.find('<', kodSZ + 29)
            kodS = (kodSpomS[kodSZ+29:kodSK])

            try:
                cenaBezDPHS= soup.find('td', class_='price_without_vat').text.strip()
                cenaZac = cenaBezDPHS.find("K")
                cenaLen = (len(cenaBezDPHS))
                cenaBezDPHS = int((cenaBezDPHS[0:cenaZac - 8])+(cenaBezDPHS[cenaZac - 7:cenaZac - 1]))
            except:
                cenaBezDPHS = 0
            softcom.nazevKartyS.append(jmenoS)
            softcom.idKartyS.append(kodS)
            softcom.cenaKartyS.append(cenaS)    