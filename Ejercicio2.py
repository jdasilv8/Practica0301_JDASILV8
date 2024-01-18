def Capitalizado(linea):
    linea[0] = (linea[0].title())
    return
def LetraDNI(linea):
    letras = "trwagmyfpdxbnjzsqvhlcke"
    letras = letras.upper()
    numero = int(linea[1])
    calculo = numero % 23
    linea[1] = str(linea[1]) + ' ' + letras[calculo]
    return linea
def LeerFichero(fichero):
    with open(fichero, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            Capitalizado(row)
            print (LetraDNI(row))
    return

import csv
import cProfile

L50 = "50.csv"
L1000 = "1000.csv"

cProfile.run("LeerFichero(L1000)")
