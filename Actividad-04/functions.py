import literales as l
import csv
def menu_principal(menu):
    match menu:
        case 1:
            datos()
        case 2:
            imprimir()



def tecnologia():
    menu = int(input(l.TECH))
    tech =""
    if menu == 1:
        tech ="Mysql"
    elif menu == 2:
        tech ="PHP"
    elif menu == 3:
        tech ="Python"
    print(tech)
    return tech 

        

def datos():
    name = str(input(l.NAME))
    last_name = str(input(l.LAST_NAME))
    age = int(input(l.AGE))
    tech = tecnologia()
    identifier = name[:2].upper() +'-'+ last_name[-2:].upper()+'-' + str(age)
    print(l.SUCESS)
        
    with open('files/alumnos.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['Nombre', 'Apellido', 'Edad', 'Tecnologia', 'Identificador']
        writeCSV = csv.DictWriter(csvfile, fieldnames)
        writeCSV.writerow({'Nombre': name, 'Apellido': last_name, 'Edad' : age, 'Tecnologia': tech, 'Identificador': identifier})

def imprimir():
    with open('files/alumnos.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        for row in readCSV:
            print(', '.join(row))