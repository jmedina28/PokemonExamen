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
