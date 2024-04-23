import pandas as pd
import numpy as np
from numpy.random import randn



df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)
# loc e iloc são usados para selecionar linhas e colunas
loc = df.loc[['A','B'],['W']] 
print(loc)

iloc = df.iloc[1:4, 1:3]
print(iloc)
#seleção de valores maiores que 0
print(df > 0)
print(df[df > 0])
print(df["Y"] > 0)
#seleção de valores maiores que 0 e retorne o dataframe
print(df[df["Y"] > 0])

#seleções com and
print(df[(df["W"] > 0) & (df["Y"] > 0)])
