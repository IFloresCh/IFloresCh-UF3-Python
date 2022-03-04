import literales as l
def show_file(file_name):
    try:
        file = open(file_name, "r")
    except:
        print(l.ERROR)
    else:
        print(file.read())
        file.close()