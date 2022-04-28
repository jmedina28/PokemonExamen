import pandas
import numpy as np
# lee el archivo "Pokemon.csv" 
df = pandas.read_csv("Pokemon.csv")
print(df)

# media de la variable Attack
print(df["Attack"].mean())