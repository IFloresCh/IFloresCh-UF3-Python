import functions as f
import literales as l
def main():
    tech ="Mysql"
    print(tech)
    menu = int(input(l.MENU))
    while menu != 0:
        match menu:
            case 1:
                f.datos()
            case 2:
                f.imprimir()
                
        menu = input(l.MENU)    
    

if __name__ == "__main__" :
   main()