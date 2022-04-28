import pandas
import numpy as np
import matplotlib.pyplot as plt
# lee el archivo "Pokemon.csv" 
df = pandas.read_csv("Pokemon.csv")
print(df)

def media(df):
    # media de la variable Total
    mediatotal = df["Total"].mean()
    # media de la variable Attack
    mediaataque = df["Attack"].mean()
    # media de la variable Defense
    mediadefensa = df["Defense"].mean()
    # media de la variable HP
    mediahp = df["HP"].mean()
    # media de la variable Sp. Atk
    mediaspatk = df["Sp. Atk"].mean()
    # media de la variable Sp. Def
    mediaspdef = df["Sp. Def"].mean()
    # media de la variable Speed
    mediaspeed = df["Speed"].mean()
    print("Media de la variable Total: ", mediatotal,"\nMedia de la variable Attack: ", mediaataque,"\nMedia de la variable Defense: ", mediadefensa,"\nMedia de la variable HP: ", mediahp,"\nMedia de la variable Sp. Atk: ", mediaspatk,"\nMedia de la variable Sp. Def: ", mediaspdef,"\nMedia de la variable Speed: ", mediaspeed)
media(df)

def varianza(df):
    print("="*50)
    # varianza de la variable Total
    varianzatotal = df["Total"].var()
    # varianza de la variable Attack
    varianzaataque = df["Attack"].var()
    # varianza de la variable Defense
    varianzadefensa = df["Defense"].var()
    # varianza de la variable HP
    varianzahp = df["HP"].var()
    # varianza de la variable Sp. Atk
    varianzaspatk = df["Sp. Atk"].var()
    # varianza de la variable Sp. Def
    varianzaspdef = df["Sp. Def"].var()
    # varianza de la variable Speed
    varianzaspeed = df["Speed"].var()
    print("Varianza de la variable Total: ", varianzatotal,"\nVarianza de la variable Attack: ", varianzaataque,"\nVarianza de la variable Defense: ", varianzadefensa,"\nVarianza de la variable HP: ", varianzahp,"\nVarianza de la variable Sp. Atk: ", varianzaspatk,"\nVarianza de la variable Sp. Def: ", varianzaspdef,"\nVarianza de la variable Speed: ", varianzaspeed)
varianza(df)

def desviacion(df):
    print("="*50)
    # desviacion estandar de la variable Total
    desviaciontotal = df["Total"].std()
    # desviacion estandar de la variable Attack
    desviacionataque = df["Attack"].std()
    # desviacion estandar de la variable Defense
    desviaciondefensa = df["Defense"].std()
    # desviacion estandar de la variable HP
    desviacionhp = df["HP"].std()
    # desviacion estandar de la variable Sp. Atk
    desviacionspatk = df["Sp. Atk"].std()
    # desviacion estandar de la variable Sp. Def
    desviacionspdef = df["Sp. Def"].std()
    # desviacion estandar de la variable Speed
    desviacionspeed = df["Speed"].std()
    print("Desviacion estandar de la variable Total: ", desviaciontotal,"\nDesviacion estandar de la variable Attack: ", desviacionataque,"\nDesviacion estandar de la variable Defense: ", desviaciondefensa,"\nDesviacion estandar de la variable HP: ", desviacionhp,"\nDesviacion estandar de la variable Sp. Atk: ", desviacionspatk,"\nDesviacion estandar de la variable Sp. Def: ", desviacionspdef,"\nDesviacion estandar de la variable Speed: ", desviacionspeed)
desviacion(df)


def grupo(df):
    global lista_aleatoria
    print("="*50)
    # crea una lista con los nombres de los pokemon
    lista = df["Name"].tolist()
    # crea una lista con los nombres de los pokemon aleatorios
    lista_aleatoria = np.random.choice(lista, 3, replace=False)
    # muestra los nombres de los pokemon aleatorios
    print("Los nombres de los pokemon aleatorios son: ", lista_aleatoria)
    # muestra los datos de los pokemon aleatorios
    print("Los datos de los pokemon aleatorios son: ", df.loc[df["Name"].isin(lista_aleatoria)])
grupo(df)
# guarda los datos de los pokemon aleatorios en un archivo csv
df2 = df.loc[df["Name"].isin(lista_aleatoria)].to_csv("Pokemon_aleatorios.csv")
