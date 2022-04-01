import literales as l
import csv
import pandas as pd



        
def read_CSV():
    with open(l.FILE_DIRECTORY) as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        for row in read_csv:
            print(f'\t {row[5]} \t{row[6]} ')
    
        
def show_desc():
    read_CSV
def consumo():
    try:
   
        with open(l.FILE_DIRECTORY) as csv_file:
            readCSV = csv.reader(csv_file, delimiter=',')
            total = 0
            df = pd.DataFrame(readCSV)
            print(df)
            Total = df['Consum [kWh]'].sum()
            print ("Column 1 sum:",Total)
    except:
        print(l.ERROR)
    else:
        print(l.PRINT2, + total)
        csv_file.close()    
                   
                   
def menu_principal(menu):
    if menu == 1:
        read_CSV()
    elif menu == 2:
        consumo()                   