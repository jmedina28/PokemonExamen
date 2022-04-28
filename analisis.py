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

