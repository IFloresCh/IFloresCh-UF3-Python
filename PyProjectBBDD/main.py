#main.py
import functions as fc
import csvfunctions as csv
import dbfunctions as db

def main():
    #mostra el menú i demana quants alumnes es volen introduir
    #num = fc.menu()
    #crida a la funció per a crear tants alumnes com conté num
    #csv.create_dict(num)
    #crida a la funció per a llegir el csv
    csv.read_CSV()
    #crida a la funció per a mostrar les dades tabulades
    #csv.show_table()
    # crida a la funció per a crear la bbdd
    #db.create_db()
    # crida a la funció per a crear la taula
    #db.create_table()
    # crida a la funció per a inserir dades a la taula
    #db.insert_data()
    #crida a la funció per a consultar dades de la taula
    db.select_data()

if __name__ == "__main__":
    main()