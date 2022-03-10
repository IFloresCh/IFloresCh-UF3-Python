import csv
#import pandas as pd


def create_dict(n):
    # crida a funció per crear header
    write_header()
    # crea un diccionari per a cada estudiant (tants com indica n)
    for i in range(n):
        student_ID = int(input("Introdueix l'identificador: "))
        first_name = input("Introdueix el nom de l'estudiant: ")
        last_name = input("Introdueix el cognom de l'estudiant: ")
        subject = input("Introdueix l'assignatura: ")
        grade = int(input("Introdueix la nota: "))

        student = {
            "student_ID": student_ID,
            "first_name": first_name,
            "last_name": last_name,
            "subject": subject,
            "grade": grade
        }
        write_CSV(student)


def read_CSV():
    with open('files/students.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        for row in read_csv:
            print(row)


def write_header():
    # crea el fitxer csv amb el header (capçalera)
    with open('files/students.csv', 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['student_ID', 'first_name', 'last_name', 'subject', 'grade']
        write_csv = csv.DictWriter(csvfile, fieldnames=fieldnames)
        write_csv.writeheader()


def write_CSV(std):
    # afegeix al csv creat el registre de cada estudiant
    with open('files/students.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['student_ID', 'first_name', 'last_name', 'subject', 'grade']
        write_csv = csv.DictWriter(csvfile, fieldnames=fieldnames)
        write_csv.writerow(std)


def show_table():
    # configuració per a mostrar totes les columnes i el màxim (perquè no faci truncate)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    # crea el dataframe a partir dels registres del csv i el mostra amb índex de la columna "first_name"
    df = pd.read_csv('files/students.csv', index_col='first_name')
    print(df)
