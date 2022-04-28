import pandas
import numpy as np

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
    global media_ataque, media_defensa, media_hp, media_sp_ataque, media_sp_defensa, media_speed
    print("="*50)
    # crea una lista con los nombres de los pokemon
    lista = df["Name"].tolist()
    # crea una lista con los nombres de los pokemon aleatorios
    lista_aleatoria = np.random.choice(lista, 3, replace=False)
    # muestra los nombres de los pokemon aleatorios
    print("Los nombres de los pokemon aleatorios son: ", lista_aleatoria)
    # muestra los datos de los pokemon aleatorios
    print("Los datos de los pokemon aleatorios son: ", df.loc[df["Name"].isin(lista_aleatoria)])
    #calcula la media de ataque de los pokemon aleatorios
    media_ataque = df.loc[df["Name"].isin(lista_aleatoria)]["Attack"].mean()
    #calcula la media de defensa de los pokemon aleatorios
    media_defensa = df.loc[df["Name"].isin(lista_aleatoria)]["Defense"].mean()
    #calcula la media de hp de los pokemon aleatorios
    media_hp = df.loc[df["Name"].isin(lista_aleatoria)]["HP"].mean()
    #calcula la media de sp. ataque de los pokemon aleatorios
    media_sp_ataque = df.loc[df["Name"].isin(lista_aleatoria)]["Sp. Atk"].mean()
    #calcula la media de sp. defensa de los pokemon aleatorios
    media_sp_defensa = df.loc[df["Name"].isin(lista_aleatoria)]["Sp. Def"].mean()
    #calcula la media de speed de los pokemon aleatorios
    media_speed = df.loc[df["Name"].isin(lista_aleatoria)]["Speed"].mean()
    # imprime las medias de los pokemon aleatorios
    print("Media de ataque de los pokemon aleatorios: ", media_ataque,"\nMedia de defensa de los pokemon aleatorios: ", media_defensa,"\nMedia de hp de los pokemon aleatorios: ", media_hp,"\nMedia de sp. ataque de los pokemon aleatorios: ", media_sp_ataque,"\nMedia de sp. defensa de los pokemon aleatorios: ", media_sp_defensa,"\nMedia de speed de los pokemon aleatorios: ", media_speed)
grupo(df)
