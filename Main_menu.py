import literales as l
import functions as f

def main():
    menu = int(input(l.MENU))
    f.menu_principal(menu)
    while menu != 0:
        menu = int(input(l.MENU))
        f.menu_principal(menu)  
    
if __name__ == "__main__":
    main()
    
#literales.py

MENU = '\n1. Introducir videos\n2. Select\n0. Salir\n'

#functions.py

def menu_principal(menu):
    if menu == 1:
        print("has escogido 1")
    elif menu == 2:
        print("Has escogido 2")
