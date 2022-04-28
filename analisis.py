
def leer_csv():
    with open('Pokemon.csv', 'r') as archivo:
        lineas = archivo.readlines()
        lineas = [linea.replace('\n', '') for linea in lineas]
        lineas = [linea.split(',') for linea in lineas]
        return lineas
print(leer_csv())