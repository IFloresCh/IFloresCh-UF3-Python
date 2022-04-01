import literales as l
import dbfunctions as db
import csv
import pandas as pd

 

def create_dict(n):

    # crea un diccionari per a cada estudiant (tants com indica n)
    for i in range(n):
        nom = input(l.NOM)
        autor = input(l.AUTOR)
        date = int(input(l.DATE))
        idioma = input(l.IDIOMA)
        genere = input(l.GENERO)

        libro = {
            "nom": nom,
            "autor": autor,
            "date": date,
            "idioma": idioma,
            "genere": genere
        }
        write_CSV(libro)
        


def read_CSV():
    with open('files/students.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        for row in read_csv:
            print(row)


def write_CSV(libro):
    # afegeix al csv creat el registre de cada estudiant
    with open(l.FILE_DIRECTORY, 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['nom', 'autor', 'date', 'idioma', 'genere']
        write_csv = csv.DictWriter(csvfile, fieldnames=fieldnames)
        write_csv.writerow(libro)
        
def show_tables():
    datos = pd.read_csv(l.FILE_DIRECTORY)
    print(datos)
    
def count_datos():
    with open(l.FILE_DIRECTORY) as csvfile:
            read_csv = csv.reader(csvfile, delimiter=',')
            next(read_csv)
            row_count = sum(1 for row in read_csv)
            print('Tienes ' + str(row_count) + ' registros en el CSV')   
        
def menu_principal(menu):
    if menu == 1:
        db.insert_data()
    elif menu == 2:
        n = int(input('Introduce el numero de registros: '))
        create_dict(n)
        db.insert_data()
    elif menu == 3:
        show_tables()
    elif menu == 4:
        count_datos()
            
    