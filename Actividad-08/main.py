import literales as l
import functions as f
import csv
def main():
    menu = int(input(l.MENU))
    f.menu_principal(menu)
    while menu != 0:
        menu = int(input(l.MENU))
        f.menu_principal(menu)       
    
if __name__ == "__main__" :
    main()