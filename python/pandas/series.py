import pandas as pd
import numpy as np

#linhas é chamada de series
#e a tabela chamada de dataframe
#series é um array unidimensional


labels = ['a', 'b', 'c']
minha_lista = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {'a':10, 'b':20, 'c':30}

print(pd.Series(labels))
print(pd.Series(data=minha_lista))
x = pd.Series(data=minha_lista, index=labels)
print(x)

ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])
print(ser1)
print(ser2)
print("seleção de valor pelo indice:", ser1['USA'])
print("Soma de uma serie com outra:", ser1 + ser2)
#aonde ele não encontrar o valor ele coloca NaN por exemplo o valor da italy