import functions as f
import literales as l
def main():
    menu = int(input(l.MENU))
    i = 0
    while menu != 0 :
        match menu:
            case 1:
                while i < 3:
                    file_name = input(l.FILE_NAME)
                    if file_name == 'Registres.csv':
                        f.show_file(l.FILE_DIRECTORY+file_name)
                    i += 1
                    
            case 3:
                file_name = input(l.FILE_NAME)
                f.modify_file(l.FILE_DIRECTORY+file_name)
        menu = int(input(l.MENU))
            
if __name__ == "__main__" :
   main()