import literales as l

def create_file(file_name):
    try:
        file = open(file_name, "w")
    except:
        print(l.ERROR)
    else:
        file.close()
    
def show_file(file_name):
    try:
        file = open(file_name, "r")
    except:
        print(l.ERROR)
    else:
        print(file.read())
        file.close()
    
def modify_file(file_name):
    try:
        file = open(file_name, "a")
    except:
        print(l.ERROR)
    else:
        str = input(l.ADD_TO_FILE)
        file.write(str)
        file.close()