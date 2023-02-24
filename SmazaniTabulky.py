import mysql.connector
tabulka = mysql.connector.connect(host="localhost", user = "root", passwd="16091300", database = "vyrobky")
mycursor = tabulka.cursor()

mycursor.execute('DELETE FROM tabulka_vyrobku')
tabulka.commit()

#Tento soubor není nijak propojen se zbytkem programu. Pouze slouží k vymazání dat z celé tabulky.



