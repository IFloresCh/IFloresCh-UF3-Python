MSG_1 = "Introduce una frase: "
def file_add_st(fname):
  f = open(fname, "a+")
  str = input(MSG_1)
  f.write(str)
  print(f.read())
  f.close()
