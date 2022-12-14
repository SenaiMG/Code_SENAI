import numpy as np


arr = np.array([1, 2, 3, 4, 5])

print(arr)
#saida [1 2 3 4 5]

#Verificando a versão do NumPy
#A string da versão é armazenada no __version__ atributo.

print(np.__version__)#saida 1.16.3
#----------------------------------------------------------------------------------------------------
#Crie um objeto ndarray NumPy
#NumPy é usado para trabalhar com arrays. O objeto array em NumPy é chamado ndarray.

#Podemos criar um ndarrayobjeto NumPy usando a array()função.
arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))
#saida [1 2 3 4 5]
#<class 'numpy.ndarray'>

#type(): Esta função interna do Python nos informa o tipo do objeto passado para ela.
# Como no código acima, mostra que arré numpy.ndarraytype.

#----------------------------------------------------------------------------------------------------
#Para criar um ndarray, podemos passar uma lista, tupla ou qualquer objeto
# semelhante a um array para o array() método, e ele será convertido em um ndarray:
arr = np.array((1, 2, 3, 4, 5))

print(arr)#saida [1 2 3 4 5]

#----------------------------------------------------------------------------------------------------
#Dimensões em Matrizes
#Uma dimensão em arrays é um nível de profundidade de array (arrays aninhados).

#array aninhado: são arrays que possuem arrays como seus elementos.

#Matrizes 0-D
#Matrizes 0-D, ou escalares, são os elementos em uma matriz.
#Cada valor em uma matriz é uma matriz 0-D.
arr = np.array(42)

print(arr)#saida 42

#----------------------------------------------------------------------------------------------------
#Matrizes 1-D
#Uma matriz que tem matrizes 0-D como seus elementos é chamada de matriz unidimensional ou 1-D.

#Estas são as matrizes mais comuns e básicas.
arr = np.array([1, 2, 3, 4, 5])

print(arr)#saida [1 2 3 4 5]

#----------------------------------------------------------------------------------------------------
#Matrizes 2-D
#Uma matriz que tem matrizes 1-D como seus elementos é chamada de matriz 2-D.

#Estes são frequentemente usados ​​para representar matrizes ou tensores de 2ª ordem.

#O NumPy possui um submódulo inteiro dedicado às operações de matriz chamadas numpy.mat

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)
#saida [[1 2 3]
# [4 5 6]]
#----------------------------------------------------------------------------------------------------
#matrizes 3-D
#Uma matriz que possui matrizes 2-D (matrizes) como seus elementos é chamada de matriz 3-D.

#Estes são frequentemente usados ​​para representar um tensor de 3ª ordem.

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)
#saida [[[1 2 3]
#  [4 5 6]]
# [[1 2 3]
#  [4 5 6]]]

#----------------------------------------------------------------------------------------------------
#Verificar Número de Dimensões?
#NumPy Arrays fornece o ndimatributo que retorna um inteiro que
# nos diz quantas dimensões o array tem.
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)#saida 0
print(b.ndim)#saida 1
print(c.ndim)#saida 2
print(d.ndim)#saida 3

#----------------------------------------------------------------------------------------------------
#Matrizes Dimensionais Superiores
#Uma matriz pode ter qualquer número de dimensões.

#Quando a matriz é criada, você pode definir o número de dimensões usando o ndminargumento.

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)#saida [[[[[1 2 3 4]]]]]
print('number of dimensions :', arr.ndim)#saida number of dimensions : 5


#Neste array a dimensão mais interna (5º dim) tem 4 elementos,
# o 4º dim tem 1 elemento que é o vetor,
# o 3º dim tem 1 elemento que é a matriz com o vetor,
# o 2º dim tem 1 elemento que é o array 3D e
# 1º dim tem 1 elemento que é uma matriz 4D.


#----------------------------------------------------------------------------------------------------
#Acessar Elementos da Matriz
#A indexação de array é o mesmo que acessar um elemento de array.

#Você pode acessar um elemento de array referindo-se ao seu número de índice.

#Os índices nas matrizes NumPy começam com 0, o que significa que o primeiro elemento
# tem índice 0 e o segundo tem índice 1, etc.
arr = np.array([1, 2, 3, 4])

print(arr[0])#saida 1

arr = np.array([1, 2, 3, 4])

print(arr[1])#saida 2

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])#saida 7


#----------------------------------------------------------------------------------------------------
#Acessar matrizes 2-D
#Para acessar elementos de arrays 2-D, podemos usar inteiros separados
# por vírgula representando a dimensão e o índice do elemento.

#Pense em matrizes 2-D como uma tabela com linhas e colunas,
# onde a linha representa a dimensão e o índice representa a coluna.

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])
#saida 2nd element on 1st dim:  2

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])
#saida 5th element on 2nd dim:  10

#----------------------------------------------------------------------------------------------------
#Acessar matrizes 3-D
#Para acessar elementos de arrays 3-D, podemos usar inteiros separados
# por vírgula representando as dimensões e o índice do elemento.
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])#saida 6


#Exemplo explicado
#arr[0, 1, 2]imprime o valor 6.

#E é por isso que:

#O primeiro número representa a primeira dimensão, que contém duas matrizes:
#[[1, 2, 3], [4, 5, 6]]
#e:
#[[7, 8, 9], [10, 11, 12]]
#Desde selecionamos 0, ficamos com o primeiro array:
#[[1, 2, 3], [4, 5, 6]]

#O segundo número representa a segunda dimensão, que também contém duas matrizes:
#[1, 2, 3]
#e:
#[4, 5, 6]
#Como selecionamos 1, ficamos com a segunda matriz:
#[4, 5, 6]

#O terceiro número representa a terceira dimensão, que contém três valores:
#4
#5
#6
#Como selecionamos 2, terminamos com o terceiro valor:
#6

#----------------------------------------------------------------------------------------------------
#Indexação negativa
#Use a indexação negativa para acessar uma matriz do final.
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])
#saida Last element from 2nd dim:  10

#----------------------------------------------------------------------------------------------------
#Slicing arrays
#Fatiar em python significa levar elementos de um determinado índice para outro determinado índice.
#Passamos slice ao invés de index assim: .[start:end]
#Também podemos definir a etapa, assim: .[start:end:step]
#Se não passarmos, o início é considerado 0
#Se não passarmos, termine seu comprimento considerado de matriz nessa dimensão
#Se não passarmos da etapa, é considerado 1


arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])#saida [2 3 4 5]


#Observação: o resultado inclui o índice inicial, mas exclui o índice final.
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])#saida [5 6 7]

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])#saida [1 2 3 4]
#----------------------------------------------------------------------------------------------------
#Corte Negativo
#Use o operador menos para se referir a um índice do final:

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])#saida [5 6]

#----------------------------------------------------------------------------------------------------
#DEGRAU
#Use o stepvalor para determinar a etapa do fatiamento:
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])
#saida [2 4]

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])
#saida [1 3 5 7]

#----------------------------------------------------------------------------------------------------
#Fatiando matrizes 2-D

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])
#saida [7 8 9]

#Nota: Lembre-se que o segundo elemento tem índice 1.

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])
#saida [[2 3 4]
# [7 8 9]]

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])
#saida [3 8]

#----------------------------------------------------------------------------------------------------
#Tipos de Dados em Python
#Por padrão, o Python tem esses tipos de dados:

#strings- usado para representar dados de texto, o texto é fornecido entre aspas.
# por exemplo, "ABCD"
#integer- usado para representar números inteiros. por exemplo -1, -2, -3
#float- usado para representar números reais. por exemplo, 1,2, 42,42
#boolean- usado para representar Verdadeiro ou Falso.
#complex- usado para representar números complexos. por exemplo, 1,0 + 2,0j, 1,5 + 2,5j
#Tipos de dados no NumPy
#O NumPy tem alguns tipos de dados extras e se refere a tipos de dados com um caractere,
# como iinteiros, uinteiros sem sinal, etc.

#Abaixo está uma lista de todos os tipos de dados no NumPy e
# os caracteres usados ​​para representá-los.

#i- inteiro
#b- boleano
#u- inteiro sem sinal
#f- flutuar
#c- flutuação complexa
#m- timedelta
#M- data hora
#O- objeto
#S- corda
#U- string unicode
#V- pedaço fixo de memória para outro tipo (void)

#Verificando o tipo de dados de uma matriz
#O objeto array NumPy tem uma propriedade chamada dtype que retorna o tipo de dado do array:
arr = np.array([1, 2, 3, 4])

print(arr.dtype)
#saida int64

#----------------------------------------------------------------------------------------------------
arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)#saida <U6

#----------------------------------------------------------------------------------------------------
#Criando Arrays com um Tipo de Dados Definido
#Usamos a array()função para criar arrays, esta função pode receber um argumento opcional:
# dtype que nos permite definir o tipo de dado esperado dos elementos do array:
arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)#saida [b'1' b'2' b'3' b'4']
print(arr.dtype)#saida |S1

#Para i, u, fe Stambém Upodemos definir o tamanho.

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)#saida [1 2 3 4]
print(arr.dtype)#saida int32

#----------------------------------------------------------------------------------------------------
#E se um valor não puder ser convertido?
#Se for fornecido um tipo no qual os elementos não podem ser convertidos,
# o NumPy gerará um ValueError.

#ValueError: Em Python ValueError é levantado quando o tipo de
# argumento passado para uma função é inesperado/incorreto.
arr = np.array(['a', '2', '3'], dtype='i')
#saida Traceback (most recent call last):
#  File "./prog.py", line 3, in
#ValueError: invalid literal for int() with base 10: 'a'

#----------------------------------------------------------------------------------------------------
#Convertendo tipo de dados em matrizes existentes
#A melhor maneira de alterar o tipo de dados de uma matriz existente é
# fazer uma cópia da matriz com o astype()método.

#A astype()função cria uma cópia da matriz e permite especificar
# o tipo de dados como um parâmetro.

#O tipo de dados pode ser especificado usando uma string,
# como 'f'para float, 'i'for integer etc. ou você pode usar o tipo de
# dados diretamente como floatpara float e intfor integer.
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)#saida [1 2 3]
print(newarr.dtype)#saida int32

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)#saida [1 2 3]
print(newarr.dtype)#saida int64

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)#saida [ True False True]
print(newarr.dtype)#saida bool

#----------------------------------------------------------------------------------------------------
#A diferença entre copiar e visualizar
#A principal diferença entre uma cópia e uma visualização de um array é
# que a cópia é um novo array e a visualização é apenas uma visualização do array original.

#A cópia possui os dados e quaisquer alterações feitas na cópia não afetarão o
# array original, e quaisquer alterações feitas no array original não afetarão a cópia.

#A exibição não possui os dados e quaisquer alterações feitas na exibição afetarão
# a matriz original, e quaisquer alterações feitas na matriz original afetarão a exibição.

#CÓPIA DE:
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)#saida [42  2  3  4  5]
print(x)#saida [1 2 3 4 5]

#OBS:A cópia NÃO DEVE ser afetada pelas alterações feitas no array original.
#----------------------------------------------------------------------------------------------------
#VISÃO:
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)#saida [42  2  3  4  5]
print(x)#saida [42  2  3  4  5]

#OBS:A exibição DEVE ser afetada pelas alterações feitas no array original.

#----------------------------------------------------------------------------------------------------
#Faça alterações na VISUALIZAÇÃO:
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)#saida [31  2  3  4  5]
print(x)#saida [31  2  3  4  5]

#OBS: A matriz original DEVE ser afetada pelas alterações feitas na exibição.

#----------------------------------------------------------------------------------------------------
#Verifique se o array possui seus dados
#Conforme mencionado acima, as cópias são proprietárias dos dados e as exibições não são proprietárias dos dados, mas como podemos verificar isso?

#Cada matriz NumPy possui o atributo baseque retorna Nonese a matriz possuir os dados.

#Caso contrário, o base  atributo se refere ao objeto original.

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)#saida None
print(y.base)#saida [1 2 3 4 5]

#A cópia retorna None.
#A exibição retorna a matriz original.

#----------------------------------------------------------------------------------------------------
#Forma de uma matriz
#A forma de uma matriz é o número de elementos em cada dimensão.

#Obter a forma de uma matriz
#As matrizes NumPy têm um atributo chamado shapeque retorna uma tupla com
# cada índice tendo o número de elementos correspondentes.
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)#saida (2, 4)

#O exemplo acima retorna (2, 4), o que significa que o array possui 2 dimensões,
# onde a primeira dimensão possui 2 elementos e a segunda possui 4.


arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)#saida [[[[[1 2 3 4]]]]]
print('shape of array :', arr.shape)#saida shape of array : (1, 1, 1, 1, 4)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)#saida [[[[[1 2 3 4]]]]]
print('shape of array :', arr.shape)#saida shape of array : (1, 1, 1, 1, 4)

#O que a tupla de forma representa?
#Inteiros em cada índice informa sobre o número de
# elementos que a dimensão correspondente possui.
#No exemplo acima no índice-4 temos o valor 4, então podemos dizer
# que a 5ª (4 + 1ª) dimensão tem 4 elementos.

#----------------------------------------------------------------------------------------------------
#Remodelando matrizes
#Remodelar significa alterar a forma de uma matriz.

#A forma de uma matriz é o número de elementos em cada dimensão.

#Ao remodelar, podemos adicionar ou remover dimensões ou alterar o número de elementos em cada dimensão.

#Remodelar de 1-D para 2-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
#saida [[ 1  2  3]
# [ 4  5  6]
# [ 7  8  9]
# [10 11 12]]
#----------------------------------------------------------------------------------------------------
#Remodelar de 1-D para 3-D

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)
#saida [[[ 1  2]
#  [ 3  4]
#  [ 5  6]]
# [[ 7  8]
#  [ 9 10]
#  [11 12]]]

#----------------------------------------------------------------------------------------------------
#Podemos remodelar em qualquer forma?
#Sim, desde que os elementos necessários para remodelar sejam iguais em ambas as formas.

#Podemos remodelar uma matriz 1D de 8 elementos em uma matriz 2D de 4
# elementos em 2 linhas, mas não podemos remodelá-la em uma matriz 2D de 3 linhas
# e 3 elementos, pois isso exigiria 3x3 = 9 elementos.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(3, 3)

print(newarr)
#saida Traceback (most recent call last):
#  File "demo_numpy_array_reshape_error.py", line 5, in <module>
#ValueError: cannot reshape array of size 8 into shape (3,3)


#----------------------------------------------------------------------------------------------------
#Retorna Copiar ou Visualizar?
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)#saida [1 2 3 4 5 6 7 8]

#----------------------------------------------------------------------------------------------------
#Dimensão Desconhecida
#Você tem permissão para ter uma dimensão "desconhecida".

#Isso significa que você não precisa especificar um número exato para uma das dimensões no método reshape.

#Passe -1como o valor e o NumPy calculará esse número para você.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)
#saida [[[1 2]
#  [3 4]]
#
# [[5 6]
#  [7 8]]]
#Nota: Não podemos passar -1para mais de uma dimensão.
#----------------------------------------------------------------------------------------------------
#Achatando os arrays
#Achatar a matriz significa converter uma matriz multidimensional em uma matriz 1D.

#Podemos usar reshape(-1)para fazer isso.
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)
#saida [1 2 3 4 5 6]

#Nota: Existem muitas funções para alterar as formas de arrays em numpy flatten,
# ravele também para reorganizar os elementos rot90, flip, fliplr, flipudetc.
# Elas se enquadram na seção Intermediário a Avançado de numpy.
#----------------------------------------------------------------------------------------------------
#Matrizes de iteração
#Iterar significa passar pelos elementos um por um.
#Como lidamos com arrays multidimensionais em numpy, podemos fazer isso usando forloop básico de python.
#Se iterarmos em uma matriz 1-D, ela passará por cada elemento, um por um.
arr = np.array([1, 2, 3])

for x in arr:
  print(x)
 #saida 1
#2
#3

#----------------------------------------------------------------------------------------------------
#Iterando Arrays 2-D
#Em uma matriz 2-D, ele percorrerá todas as linhas.

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

#saida [1 2 3]
#[4 5 6]

#----------------------------------------------------------------------------------------------------
#Se iterarmos em uma matriz n -D, ela passará pela n-1ª dimensão uma a uma.
#Para retornar os valores reais, os escalares, temos que iterar os arrays em cada dimensão.
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)
#saida 1
#2
#3
#4
#5
#6

#----------------------------------------------------------------------------------------------------
#Iterando Arrays 3-D
#Em uma matriz 3-D, ele passará por todas as matrizes 2-D.
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print("x represents the 2-D array:")
  print(x)
#saida x represents the 2-D array:
#[[1 2 3]
# [4 5 6]]
#x represents the 2-D array:
#[[ 7  8  9]
# [10 11 12]]

#Para retornar os valores reais, os escalares, temos que iterar os arrays em cada dimensão.

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)
#saida 1
#2
#3
#4
#5
#6
#7
#8
#9
#10
#11
#12

#----------------------------------------------------------------------------------------------------
#Iterando Arrays Usando nditer()
#A função nditer()é uma função auxiliar que pode ser usada desde iterações muito básicas até muito avançadas.
#Ele resolve alguns problemas básicos que enfrentamos na iteração, vamos passar por isso com exemplos.

#Iterando em cada elemento escalar
#Em forloops básicos, iterando por cada escalar de uma matriz, precisamos usar n for loops,
# o que pode ser difícil de escrever para matrizes com dimensionalidade muito alta.
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)
#SAIDA  1
#2
#3
#4
#5
#6
#7
#8

#----------------------------------------------------------------------------------------------------
#Matriz de iteração com diferentes tipos de dados
#Podemos usar op_dtypeso argumento e passar o tipo de dados esperado para alterar
#o tipo de dados dos elementos durante a iteração.

#O NumPy não altera o tipo de dados do elemento in-place (onde o elemento está no array),
#então ele precisa de algum outro espaço para executar esta ação, esse espaço
# extra é chamado de buffer e, para habilitá-lo nditer(), passamos flags=['buffered'].

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
 #saida b'1'
#b'2'
#b'3'


#Iterando com tamanho de passo diferente
#Podemos usar filtragem e seguida de iteração.
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

#saida 1
#3
#5
#7


#----------------------------------------------------------------------------------------------------
#Iteração enumerada usando denumerate()
#Enumeração significa mencionar o número de sequência de algo um por um.

#Às vezes, exigimos o índice correspondente do elemento durante a iteração,
#o ndenumerate()método pode ser usado para esses casos de uso.
arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
 #saida (0,) 1
#(1,) 2
#(2,) 3


arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
#saida (0, 0) 1
#(0, 1) 2
#(0, 2) 3
#(0, 3) 4
#(1, 0) 5
#(1, 1) 6
#(1, 2) 7
#(1, 3) 8

#----------------------------------------------------------------------------------------------------
#Juntando matrizes NumPy
#Juntar significa colocar o conteúdo de dois ou mais arrays em um único array.
#No SQL, unimos tabelas com base em uma chave, enquanto no NumPy unimos matrizes por eixos.
#Passamos uma sequência de arrays que queremos juntar à concatenate()função,
#junto com o eixo. Se o eixo não for passado explicitamente, ele será considerado 0.

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)
#saida [1 2 3 4 5 6]

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)#saida [[1 2 5 6]
 #[3 4 7 8]]

#----------------------------------------------------------------------------------------------------
#Juntando Arrays Usando Funções de Pilha
#O empilhamento é o mesmo que a concatenação, a única diferença é que o empilhamento é feito ao longo de um novo eixo.
#Podemos concatenar duas matrizes 1-D ao longo do segundo eixo, o que resultaria em colocá-las uma sobre a outra, ou seja. empilhamento.
#Passamos uma sequência de arrays que queremos juntar ao stack()método junto com o eixo. Se o eixo não for passado explicitamente, ele será considerado 0.
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)
#saida [[1 4]
# [2 5]
# [3 6]]

#----------------------------------------------------------------------------------------------------
#Empilhamento ao longo das linhas
#O NumPy fornece uma função auxiliar: hstack() empilhar ao longo das linhas.
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)
#saida [1 2 3 4 5 6]

#----------------------------------------------------------------------------------------------------
#Empilhar Ao Longo Das Colunas
#O NumPy fornece uma função auxiliar: vstack()  empilhar ao longo das colunas.
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)#saida [[1 2 3]
# [4 5 6]]

#----------------------------------------------------------------------------------------------------
#Empilhamento ao longo da altura (profundidade)
#O NumPy fornece uma função auxiliar: dstack() empilhar ao longo da altura, que é o mesmo que profundidade.
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)#saida [[[1 4]
#  [2 5]
#  [3 6]]]

#----------------------------------------------------------------------------------------------------
#Dividindo matrizes NumPy
#A divisão é a operação inversa da junção.
#Joining mescla vários arrays em um e Splitting quebra um array em múltiplos.
#Usamos array_split()para dividir arrays, passamos a ele o array que queremos dividir e o número de divisões.
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)#siada [array([1, 2]), array([3, 4]), array([5, 6])]

#Observação: o valor de retorno é um array contendo três arrays.

#Se a matriz tiver menos elementos do que o necessário, ela será ajustada do final de acordo.

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)
#saida [array([1, 2]), array([3, 4]), array([5]), array([6])]

#Observação: também temos o método split()disponível, mas ele não ajustará os elementos
#quando houver menos elementos no array de origem para divisão, como no exemplo acima, array_split()funcionou corretamente, mas split()falharia.

#----------------------------------------------------------------------------------------------------
#Dividir em matrizes
#O valor de retorno do array_split()método é um array contendo cada divisão como um array.

#Se você dividir um array em 3 arrays, poderá acessá-los a partir do resultado como qualquer elemento do array:
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])#saida [1 2]
print(newarr[1])#saida [3 4]
print(newarr[2])#saida [5 6]


#----------------------------------------------------------------------------------------------------
#Divisão de matrizes 2-D
#Use a mesma sintaxe ao dividir matrizes 2-D.
#Use o array_split()método, passe o array que deseja dividir e o número de divisões que deseja fazer.
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
#saida [array([[1, 2],
#       [3, 4]]), array([[5, 6],
#       [7, 8]]), array([[ 9, 10],
#       [11, 12]])]

#O exemplo acima retorna três arrays 2-D.
#Vejamos outro exemplo, desta vez cada elemento nas matrizes 2-D contém 3 elementos.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)
#saida[array([[1, 2, 3],
#       [4, 5, 6]]), array([[ 7,  8,  9],
#       [10, 11, 12]]), array([[13, 14, 15],
#       [16, 17, 18]])]

#O exemplo acima retorna três arrays 2-D.
#Além disso, você pode especificar em qual eixo deseja fazer a divisão.
#O exemplo abaixo também retorna três arrays 2-D, mas eles são divididos ao longo da linha (eixo=1).
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)
#saida [array([[ 1],
#       [ 4],
#       [ 7],
#       [10],
#       [13],
#       [16]]), array([[ 2],
#       [ 5],
#       [ 8],
#       [11],
#       [14],
#       [17]]), array([[ 3],
#       [ 6],
#       [ 9],
#       [12],
#       [15],
#       [18]])]


#Uma solução alternativa é usar o hsplit()oposto de hstack()
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)
#saida [array([[ 1],
#       [ 4],
#       [ 7],
#       [10],
#       [13],
#       [16]]), array([[ 2],
#       [ 5],
#       [ 8],
#       [11],
#       [14],
#       [17]]), array([[ 3],
#       [ 6],
#       [ 9],
#       [12],
#       [15],
#       [18]])]

#Observação: Alternativas semelhantes a vstack()e dstack()estão disponíveis como vsplit()e dsplit().

#----------------------------------------------------------------------------------------------------
#Pesquisando Matrizes
#Você pode procurar um determinado valor em uma matriz e retornar os índices que obtiverem uma correspondência.

#Para pesquisar uma matriz, use o where()método.
arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)#saida (array([3, 5, 6]),)

#O exemplo acima retornará uma tupla:(array([3, 5, 6],)
#O que significa que o valor 4 está presente nos índices 3, 5 e 6.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)
#saida (array([1, 3, 5, 7]),)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x)#saida (array([0, 2, 4, 6]),)


#----------------------------------------------------------------------------------------------------
#Pesquisa Ordenada
#Existe um método chamado searchsorted()que realiza uma busca binária no array, e retorna o índice onde o valor especificado seria inserido para manter a ordem de busca.

#Supõe-se que o searchsorted()método seja usado em arrays classificados.
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)
#saida 1


#Exemplo explicado: O número 7 deve ser inserido no índice 1 para manter a ordem de classificação.

#O método inicia a busca pela esquerda e retorna o primeiro índice onde o número 7 não é maior que o próximo valor.

#Pesquisar do lado direito
#Por padrão, o índice mais à esquerda é retornado, mas podemos side='right'retornar o índice mais à direita.
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)
#saida 2

#Exemplo explicado: O número 7 deve ser inserido no índice 2 para manter a ordem de classificação.

#O método inicia a busca pela direita e retorna o primeiro índice onde o número 7 não é mais menor que o próximo valor.

#Valores Múltiplos
#Para pesquisar mais de um valor, use uma matriz com os valores especificados.
arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)
#saida [1 2 3]

#O valor de retorno é um array: [1 2 3]contendo os três índices onde 2, 4, 6 seriam inseridos no array original para manter a ordem.

#----------------------------------------------------------------------------------------------------
#Matrizes de classificação
#Classificar significa colocar elementos em uma sequência ordenada .

#Sequência ordenada é qualquer sequência que possui uma ordem correspondente aos elementos, como numérica ou alfabética, ascendente ou descendente.

#O objeto NumPy ndarray tem uma função chamada sort(), que classificará uma matriz especificada.
arr = np.array([3, 2, 0, 1])

print(np.sort(arr))
#saida [0 1 2 3]

#Observação: esse método retorna uma cópia do array, deixando o array original inalterado.

#Você também pode classificar matrizes de strings ou qualquer outro tipo de dados:

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))
#saida ['apple' 'banana' 'cherry']

arr = np.array([True, False, True])

print(np.sort(arr))
#saida [False True True]

#----------------------------------------------------------------------------------------------------
#Classificando uma matriz 2-D
#Se você usar o método sort() em uma matriz 2-D, ambas as matrizes serão classificadas:

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))
#saida [[2 3 4]
# [0 1 5]]


#----------------------------------------------------------------------------------------------------
#Matrizes de filtragem
#Obter alguns elementos de um array existente e criar um novo array a partir deles é chamado de filtragem .

#No NumPy, você filtra uma matriz usando uma lista de índices booleanos .

#Uma lista de índices booleanos é uma lista de booleanos correspondentes aos índices na matriz.

#Se o valor em um índice for Trueesse elemento contido na matriz filtrada, se o valor nesse índice for False, esse elemento será excluído da matriz filtrada.
arr = np.array([41, 42, 43, 44])

x = arr[[True, False, True, False]]

print(x)#saida [41 43]

#O exemplo acima retornará [41, 43], por quê?

#Porque o novo array contém apenas os valores onde o array do filtro tinha o valor True, neste caso, índice 0 e 2.


#----------------------------------------------------------------------------------------------------
#Criando a Matriz de Filtro
#No exemplo acima, codificamos os valores True e False, mas o uso comum é criar uma matriz de filtro com base nas condições.
arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)#saida [False, False, True, True]
print(newarr)#saida [43 44]



arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)#saida  [False, True, False, True, False, True, False]
print(newarr)#saida [2 4 6]

#----------------------------------------------------------------------------------------------------
#Criando Filtro Diretamente do Array
#O exemplo acima é uma tarefa bastante comum no NumPy e o NumPy fornece uma boa maneira de resolvê-lo.

#Podemos substituir diretamente a matriz em vez da variável iterável em nossa condição e ela funcionará exatamente como esperamos.

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)#saida [False False  True  True]
print(newarr)#saida [43 44]

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)#saida [False  True False  True False  True False
print(newarr)#saida [2 4 6]

#----------------------------------------------------------------------------------------------------
#O que é um número aleatório?
#Número aleatório NÃO significa um número diferente a cada vez. Aleatório significa algo que não pode ser previsto logicamente.

#Pseudo Aleatório e Verdadeiro Aleatório.
#Os computadores trabalham com programas, e os programas são um conjunto definitivo de instruções. Então isso significa que deve haver algum algoritmo para gerar um número aleatório também.

#Se houver um programa para gerar um número aleatório, ele pode ser previsto, portanto, não é verdadeiramente aleatório.

#Os números aleatórios gerados por meio de um algoritmo de geração são chamados de pseudo-aleatórios .

#Podemos fazer números verdadeiramente aleatórios?

#Sim. Para gerar um número verdadeiramente aleatório em nossos computadores, precisamos obter os dados aleatórios de alguma fonte externa. Essa fonte externa geralmente são nossas teclas digitadas, movimentos do mouse, dados na rede, etc.

#Não precisamos de números verdadeiramente aleatórios, a menos que estejam relacionados à segurança (por exemplo, chaves de criptografia) ou a base da aplicação seja a aleatoriedade (por exemplo, roletas digitais).

#Neste tutorial, usaremos números pseudo-aleatórios.


#----------------------------------------------------------------------------------------------------
#Gerar Número Aleatório
#O NumPy oferece o randommódulo para trabalhar com números aleatórios.
from numpy import random

x = random.randint(100)

print(x)#saida 16

#----------------------------------------------------------------------------------------------------
#Gerar flutuação aleatória
#O rand()método do módulo aleatório retorna um float aleatório entre 0 e 1.

x = random.rand()

print(x)#saida 0.9718760413795016


#----------------------------------------------------------------------------------------------------
#Gerar Matriz Aleatória
#No NumPy trabalhamos com arrays, e você pode usar os dois métodos dos exemplos acima para fazer arrays aleatórios.

#inteiros
#O randint()método usa um size parâmetro onde você pode especificar a forma de uma matriz.
x=random.randint(100, size=(5))

print(x)
#saida [30 53 16 45 99]

x = random.randint(100, size=(3, 5))

print(x)
#saida [[80 54 19 74 65]
# [26 60 69 34 25]
# [50 16 53 84 90]]


x = random.rand(5)

print(x)#saida [0.5991753 0.8419630 0.8052172 0.5513319 0.5135624]

x = random.rand(3, 5)

print(x)
#saida [[0.03379952 0.78263517 0.9834899  0.47851523 0.02948659]
# [0.36284007 0.10740884 0.58485016 0.20708396 0.00969559]
# [0.88232193 0.86068608 0.75548749 0.61233486 0.06325663]]


#----------------------------------------------------------------------------------------------------
#Gerar número aleatório da matriz
#O choice()método permite gerar um valor aleatório com base em uma matriz de valores.

#O choice()método recebe um array como parâmetro e retorna aleatoriamente um dos valores.
x = random.choice([3, 5, 7, 9])

print(x)#saida 5

#O choice()método também permite que você retorne uma matriz de valores.

#Adicione um sizeparâmetro para especificar a forma da matriz.

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)#saida [[5 9 7 5 9]
# [3 7 7 9 7]
# [3 7 9 9 5]]


#----------------------------------------------------------------------------------------------------
#O que é Distribuição de Dados?
#Distribuição de dados é uma lista de todos os valores possíveis e com que frequência cada valor ocorre.

#Essas listas são importantes ao trabalhar com estatísticas e ciência de dados.

#O módulo random oferece métodos que retornam distribuições de dados geradas aleatoriamente.

#Distribuição aleatória
#Uma distribuição aleatória é um conjunto de números aleatórios que seguem uma determinada função de densidade de probabilidade .

#Função de densidade de probabilidade: Uma função que descreve uma probabilidade contínua. ou seja, probabilidade de todos os valores em uma matriz.

#Podemos gerar números aleatórios com base em probabilidades definidas usando o choice()método do randommódulo.

#O choice()método nos permite especificar a probabilidade para cada valor.

#A probabilidade é definida por um número entre 0 e 1, onde 0 significa que o valor nunca ocorrerá e 1 significa que o valor sempre ocorrerá.

#Exemplo
#Gere uma matriz 1-D contendo 100 valores, onde cada valor deve ser 3, 5, 7 ou 9.

#A probabilidade de o valor ser 3 é definida como 0,1
#A probabilidade de o valor ser 5 é definida como 0,3
#A probabilidade de o valor ser 7 é definida como 0,6
#A probabilidade de o valor ser 9 é definida como 0
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)
#saida [7 7 5 5 7 7 5 3 7 5 5 3 5 5 5 3 7 5 5 7 5 5 3 5 7 7 7 5 5 7 7 7 5 7 5 7 5
# 7 7 5 7 7 7 5 5 7 5 7 7 5 5 5 7 7 7 5 5 5 7 7 7 7 5 7 5 7 7 5 3 7 7 5 7 5
# 3 7 5 7 3 7 7 7 3 7 3 7 7 7 3 7 7 7 7 7 7 7 5 5 7 7]



#A soma de todos os números de probabilidade deve ser 1.

#Mesmo que você execute o exemplo acima 100 vezes, o valor 9 nunca ocorrerá.

#Você pode retornar arrays de qualquer forma e tamanho especificando a forma no sizeparâmetro.
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)#saida [[7 7 7 7 7]
# [7 5 3 7 7]
# [7 7 7 7 5]]

#----------------------------------------------------------------------------------------------------
#Permutações Aleatórias de Elementos
#Uma permutação refere-se a um arranjo de elementos. por exemplo, [3, 2, 1] é uma permutação de [1, 2, 3] e vice-versa.

#O módulo NumPy Random fornece dois métodos para isso: shuffle()e permutation().

#Embaralhando Arrays
#Shuffle significa alterar a disposição dos elementos no local. ou seja, no próprio array.

from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)
#saida [2 5 1 4 3]

#OBS: O shuffle()método faz alterações na matriz original.

#----------------------------------------------------------------------------------------------------
#Gerando Permutação de Arrays
arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))#saida [2 4 5 1 3]


#OBS:O permutation()método retorna um array reorganizado (e deixa o array original inalterado).

#----------------------------------------------------------------------------------------------------
#Visualize Distribuições com Seaborn
#Seaborn é uma biblioteca que usa o Matplotlib abaixo para plotar gráficos. Ele será usado para visualizar distribuições aleatórias.


#Instale o Seaborn.
#Se você já tiver o Python e o PIP instalados em um sistema, instale-o usando este comando:

#C:\Users\Your Name>pip install seaborn
#Se você usa o Jupyter, instale o Seaborn usando este comando:

#C:\Users\Your Name>!pip install seaborn
#Distplots
#Distplot significa plotagem de distribuição, ele toma como entrada uma matriz e plota uma curva correspondente à distribuição de pontos na matriz.

#Importar Matplotlib
#Importe o objeto pyplot do módulo Matplotlib em seu código usando a seguinte instrução:
#import matplotlib.pyplot as plt
#Você pode aprender sobre o módulo Matplotlib em nosso Tutorial Matplotlib .

#Importar Seaborn
#Importe o módulo Seaborn em seu código usando a seguinte declaração:
#import seaborn as sns

#Traçando um Distplot
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

#----------------------------------------------------------------------------------------------------
#Traçando um Distplot sem o Histograma

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()


#Observação: usaremos: sns.distplot(arr, hist=False)para visualizar distribuições aleatórias neste tutorial.

#----------------------------------------------------------------------------------------------------
#Distribuição normal
#A Distribuição Normal é uma das distribuições mais importantes.

#Também é chamada de Distribuição Gaussiana em homenagem ao matemático alemão Carl Friedrich Gauss.

#Ele se ajusta à distribuição de probabilidade de muitos eventos, por exemplo. Pontuações de QI, batimentos cardíacos, etc.

#Use o random.normal()método para obter uma distribuição de dados normal.

#Possui três parâmetros:

#loc- (Médio) onde existe o pico do sino.

#scale- (Desvio padrão) quão plana deve ser a distribuição do gráfico.

#size- A forma da matriz retornada.

from numpy import random

x = random.normal(size=(2, 3))

print(x)
#saida [[-0.69902572  0.61792792  0.22591971]
# [ 0.58832013 -1.8639458  -0.8140681 ]]

x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)
#saida [[ 1.15089313  2.80958695  0.9175154 ]
# [ 0.94468562 -1.86406821  4.16048633]]


#----------------------------------------------------------------------------------------------------
#Visualização da Distribuição Normal
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)

plt.show()

#Nota: A curva de uma distribuição normal também é conhecida como curva de sino por causa da curva em forma de sino.


#----------------------------------------------------------------------------------------------------
#Distribuição binomial
#A Distribuição Binomial é uma Distribuição Discreta .

#Ele descreve o resultado de cenários binários, por exemplo, lançamento de uma moeda, será cara ou coroa.

#Possui três parâmetros:

#n- número de tentativas.

#p- probabilidade de ocorrência de cada tentativa (por exemplo, para lançamento de uma moeda 0,5 cada).

#size- A forma da matriz retornada.

#Distribuição Discreta: A distribuição é definida em um conjunto separado de eventos, por exemplo,
# o resultado de uma moeda ao ar é discreto, pois pode ser apenas cara ou coroa,
#enquanto a altura das pessoas é contínua, pois pode ser 170, 170,1, 170,11 e assim por diante.

from numpy import random

x = random.binomial(n=10, p=0.5, size=10)

print(x)
#saida [6 3 5 5 4 4 4 4 5 6]

#----------------------------------------------------------------------------------------------------
#Visualização da Distribuição Binomial
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

plt.show()

#----------------------------------------------------------------------------------------------------
#Diferença entre distribuição normal e binomial
#A principal diferença é que a distribuição normal é contínua, enquanto a binomial é discreta,
# mas se houver pontos de dados suficientes, será bastante semelhante à distribuição normal com certo local e escala.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()

#----------------------------------------------------------------------------------------------------
#Distribuição de veneno
#A distribuição de Poisson é uma distribuição discreta .

#Ele estima quantas vezes um evento pode acontecer em um tempo especificado. por exemplo, se alguém come duas vezes ao dia, qual é a probabilidade de comer três vezes?

#Possui dois parâmetros:

#lam- taxa ou número conhecido de ocorrências, por exemplo, 2 para o problema acima.

#size- A forma da matriz retornada.

from numpy import random

x = random.poisson(lam=2, size=10)

print(x)#saida [1 4 2 0 1 3 1 4 2 0]

#----------------------------------------------------------------------------------------------------
#Visualização da Distribuição de Poisson
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()
#----------------------------------------------------------------------------------------------------
#Diferença entre distribuição normal e de Poisson
#A distribuição normal é contínua enquanto Poisson é discreta.

#Mas podemos ver que semelhante ao binomial para uma distribuição de poisson grande o suficiente,
# ela se tornará semelhante à distribuição normal com certo padrão de desenvolvimento e média.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')

plt.show()

#----------------------------------------------------------------------------------------------------
#Diferença entre distribuição de Poisson e distribuição binomial
#A diferença é muito sutil, pois a distribuição binomial é para tentativas discretas, enquanto a distribuição de Poisson é para tentativas contínuas.

#Mas para uma distribuição binomial muito grande ne próxima de zero pé quase idêntica à distribuição de Poisson tal que n * pé quase igual a lam.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')

plt.show()

#----------------------------------------------------------------------------------------------------
#Distribuição uniforme
#Usado para descrever a probabilidade em que cada evento tem chances iguais de ocorrer.

#Ex. Geração de números aleatórios.

#Possui três parâmetros:

#a- limite inferior - padrão 0 .0.

#b- limite superior - padrão 1.0.

#size- A forma da matriz retornada.
from numpy import random

x = random.uniform(size=(2, 3))

print(x)#saida [[0.03520856 0.54371233 0.52513912]
# [0.2531509  0.05726849 0.80873404]]

#----------------------------------------------------------------------------------------------------
#Visualização da Distribuição Uniforme
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform(size=1000), hist=False)

plt.show()


#----------------------------------------------------------------------------------------------------
#Distribuição Logística
#A distribuição logística é usada para descrever o crescimento.

#Usado extensivamente em aprendizado de máquina em regressão logística, redes neurais etc.

#Possui três parâmetros:

#loc- quer dizer, onde está o pico. Padrão 0.

#scale- desvio padrão, o nivelamento da distribuição. Padrão 1.

#size- A forma da matriz retornada.

from numpy import random

x = random.logistic(loc=1, scale=2, size=(2, 3))

print(x)#saida [[ 1.61136254 -0.18371581  6.36029879]
# [-4.27928744  2.45762335  1.70592501]]

#----------------------------------------------------------------------------------------------------
#Visualização da Distribuição Logística
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.logistic(size=1000), hist=False)

plt.show()


#----------------------------------------------------------------------------------------------------
#Diferença entre distribuição logística e normal
#Ambas as distribuições são quase idênticas, mas a distribuição logística tem mais área sob as caudas,
# o que significa que representa mais possibilidade de ocorrência de um evento mais distante da média.

#Para valores mais altos de escala (desvio padrão), as distribuições normal e logística são quase idênticas, exceto pelo pico.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')

plt.show()

#----------------------------------------------------------------------------------------------------
#Distribuição Multinomial
#A distribuição multinomial é uma generalização da distribuição binomial.

#Ele descreve os resultados de cenários multinomiais, ao contrário do binomial, onde os cenários devem ser apenas um dos dois. por exemplo, tipo de sangue de uma população, resultado da rolagem de dados.

#Possui três parâmetros:

#n- número de resultados possíveis (por exemplo, 6 para lançamento de dados).

#pvals- lista de probabilidades de resultados (por exemplo, [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] para lançamento de dados).

#size- A forma da matriz retornada.
from numpy import random

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)#saida [2 1 0 1 0 2]

#Nota: Amostras multinomiais NÃO produzirão um único valor! Eles produzirão um valor para cada um pval.

#Nota: Como são generalizações de distribuição binomial, sua representação visual e similaridade de distribuição normal é a mesma de múltiplas distribuições binomiais.

#----------------------------------------------------------------------------------------------------
#Distribuição Exponencial
#A distribuição exponencial é usada para descrever o tempo até o próximo evento, por exemplo, falha/sucesso, etc.

#Possui dois parâmetros:

#scale- o inverso da taxa (veja lam na distribuição de poisson) assume como padrão 1,0.

#size- A forma da matriz retornada.
from numpy import random

x = random.exponential(scale=2, size=(2, 3))

print(x)#saida [[0.94828918 0.11756127 1.0921608 ]
# [3.89594216 4.66706236 1.11616961]]

#----------------------------------------------------------------------------------------------------
#Visualização da Distribuição Exponencial
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential(size=1000), hist=False)

plt.show()

#Relação entre Poisson e Distribuição Exponencial
#A distribuição de Poisson lida com o número de ocorrências de um evento em um período de tempo, enquanto a distribuição exponencial lida com o tempo entre esses eventos.
#----------------------------------------------------------------------------------------------------
#Distribuição qui-quadrado
#A distribuição Chi Square é usada como base para verificar a hipótese.

#Possui dois parâmetros:

#df- (grau de liberdade).

#size- A forma da matriz retornada.
from numpy import random

x = random.chisquare(df=2, size=(2, 3))

print(x)#saida [[1.65193855 1.08959916 0.68020384]
# [1.10387121 2.50694455 2.06669389]]

#----------------------------------------------------------------------------------------------------
#Visualização da distribuição do qui quadrado
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df=1, size=1000), hist=False)

plt.show()


#----------------------------------------------------------------------------------------------------
#Distribuição Rayleigh
#A distribuição de Rayleigh é usada no processamento de sinais.

#Possui dois parâmetros:

#scale- (desvio padrão) decide o quão plana a distribuição será padrão 1,0).

#size- A forma da matriz retornada.

from numpy import random

x = random.rayleigh(scale=2, size=(2, 3))

print(x)#saida [[6.03971993 3.20272009 2.71587145]
# [1.00167539 3.22170515 1.88295518]]
#----------------------------------------------------------------------------------------------------
#Visualização da distribuição de Rayleigh
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.rayleigh(size=1000), hist=False)

plt.show()
#Semelhança entre a distribuição de Rayleigh e Qui-quadrado
#Na unidade stddev e 2 graus de liberdade, rayleigh e qui quadrado representam as mesmas distribuições.

#----------------------------------------------------------------------------------------------------
#Distribuição de Pareto
#Uma distribuição seguindo a lei de Pareto, ou seja, distribuição 80-20 (fatores de 20% causam resultado de 80%).

#Possui dois parâmetros:

#a- parâmetro de forma.

#size- A forma da matriz retornada.
from numpy import random

x = random.pareto(a=2, size=(2, 3))

print(x)#saida [[0.81977761 0.36089322 1.63451817]
# [0.31261345 0.05994165 0.80895133]]


#----------------------------------------------------------------------------------------------------
#Visualização da Distribuição de Pareto
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a=2, size=1000), kde=False)

plt.show()

#----------------------------------------------------------------------------------------------------
#As distribuições Zipf são usadas para amostrar dados com base na lei de Zipf.

#Lei de Zipf: Em uma coleção, o n-ésimo termo comum é 1/n vezes o termo mais comum. Por exemplo, a 5ª palavra mais comum em inglês ocorre quase 1/5 vezes mais do que a palavra mais comum.

#Possui dois parâmetros:

#a- parâmetro de distribuição.

#size- A forma da matriz retornada.

from numpy import random

x = random.zipf(a=2, size=(2, 3))

print(x)#saida [[ 1  6 52]
# [ 1  1  1]]

#----------------------------------------------------------------------------------------------------
#Visualização da Distribuição Zipf
#Amostra 1.000 pontos, mas plotando apenas aqueles com valor < 10 para um gráfico mais significativo.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)

plt.show()


#----------------------------------------------------------------------------------------------------


# a continuação tem que ser numpy ufunc introdução a ufunc 



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------
