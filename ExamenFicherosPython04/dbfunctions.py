
#iflores_pg
#wev6pimwmduULgs

import mysql.connector
from mysql.connector import errorcode
import literales as l
import csv

connection_args = {
    'host': 'mysql-iflores.alwaysdata.net',
    'user': 'iflores_pg',
    'password': 'wev6pimwmduULgs',
    'database': 'iflores_libreria'
}

def insert_data():
    sql = ("INSERT INTO libros "
               "(Nom,Autor,Any,Idioma,Gènere) "
               "VALUES (%s, %s, %s, %s, %s)")
    try:
        # obrim connexió a la bbdd amb els paràmetres de connection_args
        cnx = mysql.connector.connect(**connection_args)
        # definim la sentència sql per a crear la bbdd
        

        # indiquem els valors (tupla) que han de substituir els placeholders (%s)
        with open(l.FILE_DIRECTORY) as csvfile:
            read_csv = csv.reader(csvfile, delimiter=',')
            next(read_csv)
            for row in read_csv:
            
        # creem el cursor, executem la sentència (passant la tupla també) i fem commit
                crs = cnx.cursor()
                crs.execute(sql, row)
                cnx.commit()
        # mostra per pantalla quants registres s'han inserit
        print("\nRegistros insertados correctamente.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuari o contrassenya incorrectes")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de dades indicada no existeix")
        else:
            print(err)
    else:
        cnx.close()
        


def select_data():
    try:
        # obrim connexió a la bbdd amb els paràmetres de connection_args
        cnx = mysql.connector.connect(**connection_args)
        # definim la sentència sql per a crear la bbdd
        sql = ("SELECT * FROM tb_video")
        # creem el cursor, executem la sentència i fem fetchall (per obtenir tots els registres)
        crs = cnx.cursor()
        crs.execute(sql)
        result = crs.fetchall()
        # mostra tots els resultats
        for x in result:
            print(x)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuari o contrassenya incorrectes")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de dades indicada no existeix")
        else:
            print(err)
    else:
        cnx.close()