import functions as f
import literales as l

def main():
    menu = int(input(l.MENU))
    while menu != 0:
        match menu:
            case 1:
                file_name = input(l.FILE_NAME)
                f.create_file(l.FILE_DIRECTORY+file_name)
            case 2:
                file_name = input(l.FILE_NAME)
                f.show_file(l.FILE_DIRECTORY+file_name)
            case 3:
                file_name = input(l.FILE_NAME)
                f.modify_file(l.FILE_DIRECTORY+file_name)
        menu = int(input(l.MENU))
            
if __name__ == "__main__" :
   main()