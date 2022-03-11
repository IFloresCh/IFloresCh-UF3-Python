import literales as l
import dbfunctions as db
import csv

def menu_principal(menu):
    match menu:
        case 1:
            n = int(input('Cuantos videos vas a ingresar?: '))
            create_dict(n)
            db.insert_data()
        case 2:
            db.select_data()
            
    
 

def create_dict(n):
    # crida a funció per crear header
    write_header()
    # crea un diccionari per a cada estudiant (tants com indica n)
    for i in range(n):
        singer = input(l.SINGER)
        song = input(l.SONG)
        date = input(l.DATE)
        visual = int(input(l.VISUAL))

        student = {
            "singer": singer,
            "song": song,
            "date": date,
            "visual": visual
        }
        write_CSV(student)


def read_CSV():
    with open('files/students.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        for row in read_csv:
            print(row)


def write_header():
    # crea el fitxer csv amb el header (capçalera)
    with open('files/videos.csv', 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['singer', 'song', 'date', 'visual']
        write_csv = csv.DictWriter(csvfile, fieldnames=fieldnames)
        write_csv.writeheader()


def write_CSV(std):
    # afegeix al csv creat el registre de cada estudiant
    with open('files/videos.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['singer', 'song', 'date', 'visual']
        write_csv = csv.DictWriter(csvfile, fieldnames=fieldnames)
        write_csv.writerow(std)        