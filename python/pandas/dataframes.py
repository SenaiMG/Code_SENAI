import pandas as pd
import numpy as np
from numpy.random import randn
#dataframe é uma tabela uma composição de series

de = pd.DataFrame(randn(4,4),index=["C","H", "G", "F"],columns=["W","Y", "Z", "T"])
df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print(de)
print(df)
print("Seleção de coluna com series:\n", de[['W']])
print("Seleção de coluna:\n", df['W'])
print("Seleção de um dado:", df['W']['A'])

#criar uma nova coluna
df['new'] = df['W'] + df['Y']
print("Adicionando uma nova coluna, com a soma de valores:\n", df)

#deletar uma coluna
del df['new']
de["soma"] = de["W"] + de["Y"]
print(de)
#outra forma de deletar uma coluna o axis 1 é para coluna e o 0 é para linha
# o inplace é para deletar de fato a coluna
# o drop retorna um dataframe copia
de2 = de.drop('soma', axis=1)
print(de2)
df.drop('W', axis=1, inplace=True)
print(df)