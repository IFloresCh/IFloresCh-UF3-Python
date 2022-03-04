import csv
def main():
      with open('files/grades.csv') as csvfile:
          readCSV = csv.reader(csvfile, delimiter=';')
          for row in readCSV:
              print(f'\t Estudiant:{row[0]}, {row[1]} {row[2]}, a la matèria {row[3]} ha obtingut un {row[4]}.')
if __name__ == '__main__':
    main()