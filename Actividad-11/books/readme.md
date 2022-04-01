#Afegir un diccionari a un fitxer .CSV
### 1. Introducció
En primer lloc, caldrà importar el mòdul de gestió de fitxers **.csv**:

```python
import csv
```
i generem el diccionari, introduïnt les dades per teclat:
```python
book = dict()
book['isbn'] = input("Introdueix l'isbn del llibre: ")
book['title'] = input("Introdueix el títol del llibre: ")
book['author'] = input("Introdueix l'autor del llibre: ")
book['editorial'] = input("Introdueix l'editorial del llibre: ")
book['pub_date'] = input("Introdueix la data de publicació del llibre: ")
```
Un cop disposem de la informació, el primer pas és obrir el fitxer i indicar el mode en el que s'obrirà. Escollim el mode "append", per tal de no sobreescriure la informació que pugui contenir el fitxer (si aquest ja existeix):
```python
with open('files/books.csv', 'a', encoding='utf-8', newline='') as csvfile:
```
Indiquem la capçalera del fitxer, on cada clau del diccionari serà un element de la llista i enviem a la funció d'escriptura el fitxer i la llista de la capçalera:
```python
fieldnames = ['isbn', 'title', 'author', 'editorial', 'pub_date']
writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
```
Si el fitxer s'ha creat per primer cop, cal afegir la capçalera, mitjançant la instrucció:
```python
writeCSV.writeheader()
```
i afegir la informació del diccionari. En cas contrari, només afegirem el diccionari al document:
```python
try:
    writeCSV.writerow(book)
except:
    print("No s'ha pogut inserir el registre.")
else:
    print("El registre s'ha inserit correctament.")
```