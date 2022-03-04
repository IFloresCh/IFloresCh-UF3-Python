import literales as l
import csv
def total_projects():
    with open('files/projects_board.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        for row in readCSV:
            print(', '.join(row))
        
def total_factura():
    with open(l.FILE_DIR) as fin:
        headerline = fin.next()
        total = 0
        for row in csv.reader(fin):
            total += int(row[1])
        print(total)   
    