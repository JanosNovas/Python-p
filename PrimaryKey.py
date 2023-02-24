import mysql.connector
tabulka = mysql.connector.connect(host="localhost", user = "root", passwd="16091300", database = "vyrobky")
mycursor = tabulka.cursor()

class primaryKey:
    """
    Funkce PrimaryKey stáhne sloupec Primary_Key z mysql tabulky a najde nejvyšší hodnotu. Podle ní nastaví následující hodnotu pro ukládání nových informací do tabulky.
    """
    def PrimaryKey():
        PrimaryK = 0
        mycursor.execute('SELECT Primary_Key FROM tabulka_vyrobku')
        results = mycursor.fetchall()
        if results:
            maxR = str(max(results))
            maxH = int(maxR[1:(len(maxR))-2])
            PrimaryK = maxH
        return PrimaryK