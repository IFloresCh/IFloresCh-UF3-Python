import literales as l
import csv
def read_file(fname):
    try:
        with open(fname ) as file:
            readfile = csv.reader(file, delimiter=',')
            for row in readfile:
                  print(f'\t {row[0]} \t{row[1]} \t{row[2]} \t{row[3]} \t{row[4]} \t{row[5]} \t{row[6]}\t{row[4]}')

    except FileNotFoundError as e:
       return False
    else:
        file.close()
           
