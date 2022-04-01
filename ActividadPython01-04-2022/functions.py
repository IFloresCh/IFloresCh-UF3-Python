import email
import string
import literales as l
import dbfunctions as db
import csv
import pandas as pd

def menu_principal(menu):
    if menu == 1:
        db.select_day()
    elif menu == 2:
        print("Has escogido 2")
    elif menu == 3:
        print("Has escogido 3")
    elif menu == 4:
        print("Has escogido 4")    
    elif menu == 5:
        create_user()
    elif menu == 6:
        create_reserve()
        

def create_user():
    # crea un diccionario para cada usuario

    nif = input(l.NIF)
    nom = input(l.NAME)
    cognom1 = input(l.COGNOM1)
    cognom2 = int(input(l.COGNOM2))
    address = input(l.ADDRESS)
    provincia = input(l.PROVINCE)
    poblacio = input(l.POBLACION)
    telefon = int(input(l.TELEFON))
    email = input(l.EMAIL)
    datanaixement = input(l.DATANAIXEMENT)
    
    

    user = {
        "nif": nif,
        "nom": nom,
        "cognom1": cognom1,
        "cognom2": cognom2,
        "address": address,
        "provincia": provincia,
        "poblacio": poblacio,
        "telefon": telefon,
        "email": email,
        "datanaixement": datanaixement
 }
    return user

def create_reserve():
    # crea un diccionario para cada reserva
    
    nif = input(l.NIF)
    motiu = input(l.MOTIVO)
    servei = int(input(l.SERVICIO))


    reserva = {
        "nif": nif,
        "motiu": motiu,
        "servei": servei
        
 }
    return reserva






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