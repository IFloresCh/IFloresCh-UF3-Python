import mysql.connector
from mysql.connector import errorcode

connection_args = {
    'host': 'localhost',
    'user': 'adminPG',
    'password': '123'
}


def create_db():
    try:
        # obrim connexió a la bbdd amb els paràmetres de connection_args
        cnx = mysql.connector.connect(**connection_args)
        # definim la sentència sql per a crear la bbdd
        sql = ("Create database db_students")
        # creem el cursor, executem la sentència i fem commit
        crs = cnx.cursor()
        crs.execute(sql)
        cnx.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuari o contrassenya incorrectes")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de dades indicada no existeix")
        else:
            print(err)
    else:
        # s'executarà només si try no genera excepció
        cnx.close()


def create_table():
    # afegim al dictionary a quina bbdd volem accedir
    connection_args.update({'database': 'db_students'})
    try:
        # obrim connexió a la bbdd amb els paràmetres de connection_args
        cnx = mysql.connector.connect(**connection_args)
        # definim la sentència sql per a crear la bbdd
        table = (
            "CREATE TABLE `grades` ("
            "  `student_ID` int(11) NOT NULL AUTO_INCREMENT,"
            "  `first_name` varchar(14) NOT NULL,"
            "  `last_name` varchar(16) NOT NULL,"
            "  `subject` varchar(2) NOT NULL,"
            "  `grade` int(2) NOT NULL,"
            "  PRIMARY KEY (`student_ID`)"
            ") ENGINE=InnoDB")
        '''creem el cursor,
        executem la sentència i fem commit
        '''
        crs = cnx.cursor()
        crs.execute(table)
        cnx.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuari o contrassenya incorrectes")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de dades indicada no existeix")
        else:
            print(err)
    else:
        cnx.close()


def insert_data():
    try:
        # obrim connexió a la bbdd amb els paràmetres de connection_args
        cnx = mysql.connector.connect(**connection_args)
        # definim la sentència sql per a crear la bbdd
        sql = ("INSERT INTO grades "
               "(student_ID,first_name,last_name,subject,grade) "
               "VALUES (%s, %s, %s, %s, %s)")
        # indiquem els valors (tupla) que han de substituir els placeholders (%s)
        data = ('null', 'Miguel', 'Pérez', 'PB', 7)
        # creem el cursor, executem la sentència (passant la tupla també) i fem commit
        crs = cnx.cursor()
        crs.execute(sql, data)
        cnx.commit()
        # mostra per pantalla quants registres s'han inserit
        print(crs.rowcount, "registres inserits.")
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
        sql = ("SELECT * FROM grades")
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
        
if __name__ == '__main__':
    main()