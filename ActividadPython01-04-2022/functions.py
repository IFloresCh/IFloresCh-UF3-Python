import string
import literales as l
import dbfunctions as db
import csv
import pandas as pd

def menu_principal(menu):
    if menu == 1:
        print("has escogido 1")
    elif menu == 2:
        print("Has escogido 2")
    elif menu == 3:
        print("Has escogido 3")
    elif menu == 4:
        print("Has escogido 4")
        

def create_dict(n):
    # crear la funcion header
    write_header()
    # crea un diccionario para cada reserva
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


def multiply_by_2(n):
    # multiplica el valor de n per 2
    return n * 2

    
    
    
    
    


        
    
        


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