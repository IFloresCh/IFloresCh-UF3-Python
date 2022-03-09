import literales as l
import csv

def menu_principal(menu):
    match menu:
        case 1:
            total_projects()
        case 2:
            total_factura()
            
def total_projects():
    try:
        with open(l.FILE_DIR) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            row_count = sum(1 for row in readCSV)
    except:
        print(l.ERROR)
    else:
        print(l.PRINT, + row_count-1) # -1 para saltar el header)
        csvfile.close()
        
def total_factura():
    try:
        
        with open(l.FILE_DIR) as csv_file:
            readCSV = csv.reader(csv_file, delimiter=',')
            total = 0
            for row in readCSV:
                if readCSV.line_num == 1:
                    continue 
                total += int(row[4])
    except:
        print(l.ERROR)
    else:
        print(l.PRINT2, + total)
        csv_file.close()
    