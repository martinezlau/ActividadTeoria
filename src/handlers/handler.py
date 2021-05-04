import csv
import json
from collections import Counter

def dataset1():
    """ Busco en el archivo csv los 10 paises con mas poblacion en el año 1960 y lo paso a json """
    
    archivo = open("C:/Users/Lautaro/Desktop/Python/Act100Puntos/Poblacion.csv","r",encoding="utf-8")
    csvreader = csv.reader(archivo, delimiter = ',')

    dicci1960 = {}

    for i in range(5):                      #salto las 4 primeras lineas
        encabezados = next(csvreader)

    for linea in csvreader:
        if linea[4] != "":
            dicci1960[linea[0]] = int(linea[4])
    
    dicci1960 = Counter(dicci1960)

    datos = open("C:/Users/Lautaro/Desktop/Python/Act100Puntos/DatosPoblacion.json","w")
    json.dump(dicci1960.most_common(10), datos, indent=4)

    archivo.close()
    datos.close()

def dataset2():
    """Busco en el archivo csv los 15 paises con mas gasto publico en educacion en el año 2020 y lo paso a json """

    archivo2 = open("C:/Users/Lautaro/Desktop/Python/Act100Puntos/GastoEducacion.csv","r",encoding="utf-8")
    csv_reader = csv.reader(archivo2, delimiter = ',')

    dicci2020 = {}
    
    for i in range(5):           #salto las 4 primeras lineas
        encabezados = next(csv_reader)

    for linea in csv_reader:
        if linea[63] != "":
            dicci2020[linea[0]] = float(linea[63])
    
    dicci2020 = Counter(dicci2020)

    data = open("C:/Users/Lautaro/Desktop/Python/Act100Puntos/DatosGastosEducacion.json", "w")
    json.dump(dicci2020.most_common(15), data, indent=4)

    archivo2.close()
    data.close()