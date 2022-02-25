MSG_1 = "Introduce una frase maximo 100 caracteres: "
MSG_2 = 'Introduce una frase para agregar al archivo anterior. Maximo 100 caracteres'

def file_create_str(fname):
    file = open(fname, "w")
    str = input(MSG_1)
    while len(str) > 10:
      str = input(MSG_1)
    file.write(str)
    print(file.read())
    file.close()


def file_add_st(fname):
    file = open(fname, "a")
    str = input(MSG_2)
    while len(str) > 10:
      str = input(MSG_2)
    file.write(str)
    print(file.read())
    file.close()
