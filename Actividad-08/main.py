import literales as l
import functions as f
def main():
    menu=input(l.MENU)
    while menu != 0:
        match menu:
            case 1:
                f.total_projects()
            case 2:
                f.total_factura()
    
if __name__ == "__main__" :
    main()