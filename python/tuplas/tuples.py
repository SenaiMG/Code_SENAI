#Tuplas
#Tuplas são usadas para armazenar vários itens em uma única variável.
#Tuple é um dos 4 tipos de dados internos do Python usados ​​para armazenar coleções de dados, os outros 3 são List , Set e Dictionary , todos com qualidades e usos diferentes.
#Uma tupla é uma coleção ordenada e imutável .
#Tuplas são escritas com colchetes.
thistuple = ("apple", "banana", "cherry")
print(thistuple)# saida ('apple', 'banana', 'cherry')

#Itens de Tupla
#Os itens de tupla são ordenados, imutáveis ​​e permitem valores duplicados.
#Os itens de tupla são indexados, o primeiro item possui índice [0], o segundo item possui índice [1]etc.

#Encomendado
#Quando dizemos que as tuplas estão ordenadas, significa que os itens têm uma ordem definida, e essa ordem não será alterada.

#Imutável
#As tuplas são imutáveis, o que significa que não podemos alterar, adicionar ou remover itens após a criação da tupla.

#Permitir duplicatas
#Como as tuplas são indexadas, elas podem ter itens com o mesmo valor:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)#saida ('apple', 'banana', 'cherry', 'apple', 'cherry')


#------------------------------------------------------------------------------
#Comprimento da Tupla
#Para determinar quantos itens uma tupla possui, use a len()função:

thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))#saida 3

#------------------------------------------------------------------------------
#Criar Tupla Com Um Item
#Para criar uma tupla com apenas um item, você deve adicionar uma vírgula após o item,
#caso contrário, o Python não o reconhecerá como uma tupla.

thistuple = ("apple",)
print(type(thistuple)) # saida <class 'tuple'>


#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) # saida <class 'str'>


#------------------------------------------------------------------------------
#Itens de Tupla - Tipos de Dados
#Os itens de tupla podem ser de qualquer tipo de dados:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)# saida ('apple', 'banana', 'cherry')
print(tuple2)#saida (1, 5, 7, 9, 3)
print(tuple3)#saida (True, False, False)

#Uma tupla pode conter diferentes tipos de dados:

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)# saida ('abc', 34, True, 40, 'male')

#------------------------------------------------------------------------------
#modelo()
#Da perspectiva do Python, as tuplas são definidas como objetos com o tipo de dados 'tupla':
#<class 'tuple'>
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))#saida <class 'tuple'>
#------------------------------------------------------------------------------
#O construtor tupla()
#Também é possível usar o construtor tuple() para fazer uma tupla.
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)#saida ('apple', 'banana', 'cherry')

#diferenças
#Lista é uma coleção que é ordenada e mutável. Permite membros duplicados.
#Tupla é uma coleção ordenada e imutável. Permite membros duplicados.
#Set é uma coleção não ordenada, imutável* e não indexada. Nenhum membro duplicado.
#Dicionário é uma coleção ordenada** e mutável. Nenhum membro duplicado.
#------------------------------------------------------------------------------
#Acessar itens de tupla
#Você pode acessar os itens da tupla consultando o número do índice, entre colchetes:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])#saida banana

#Indexação negativa
#Indexação negativa significa começar do fim.

#-1refere-se ao último item, -2refere-se ao penúltimo item etc.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])# saida cherry

#Faixa de índices
#Você pode especificar um intervalo de índices especificando onde começar e onde terminar o intervalo.
#Ao especificar um intervalo, o valor de retorno será uma nova tupla com os itens especificados.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])# saida ('cherry', 'orange', 'kiwi')
#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) #saida ('apple', 'banana', 'cherry', 'orange')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) # saida ('cherry', 'orange', 'kiwi', 'melon', 'mango')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) #saida ('orange', 'kiwi', 'melon')
#Negative indexing means starting from the end of the tuple.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,

#verificação se o item existe na tupla
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")# saida Yes, 'apple' is in the fruits tuple

#------------------------------------------------------------------------------
#As tuplas são imutáveis, o que significa que você não pode alterar, adicionar ou remover itens depois que a tupla for criada.

#Mas existem algumas soluções alternativas.

#Alterar valores da tupla
#Depois que uma tupla é criada, você não pode alterar seus valores. Tuplas são imutáveis , ou imutáveis , como também é chamado.

#Mas há uma solução alternativa. Você pode converter a tupla em uma lista, alterar a lista e convertê-la novamente em uma tupla.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)# saida ('apple', 'kiwi', 'cherry')

#------------------------------------------------------------------------------
#Adicionar itens
#Como as tuplas são imutáveis, elas não possuem um append()método embutido, mas existem outras maneiras de adicionar itens a uma tupla.

#1. Converter em uma lista : Assim como a solução alternativa para alterar uma tupla, você pode convertê-la em uma lista,
#adicionar seu(s) item(ns) e convertê-la novamente em uma tupla.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)# saida ('apple', 'banana', 'cherry', 'orange')

#2. Adicionar tupla a uma tupla . Você tem permissão para adicionar tuplas a tuplas,
#portanto, se você quiser adicionar um item (ou muitos), crie uma nova tupla com o(s) item(ns) e adicione-a à tupla existente:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)#saida ('apple', 'banana', 'cherry', 'orange')

#------------------------------------------------------------------------------
#Remover itens
#Nota: Você não pode remover itens em uma tupla.

#As tuplas não podem ser alteradas , portanto, você não pode remover itens dela,
#mas pode usar a mesma solução alternativa que usamos para alterar e adicionar itens de tupla:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)# saida ('banana', 'cherry')

# ou você exclui sua tupla completamente

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)# saida
#Traceback (most recent call last):
#  File "tuples.py", line 3, in <module>
#    print(thistuple) #this will raise an error because the tuple no longer exists
#NameError: name 'thistuple' is not defined
 #this will raise an error because the tuple no longer exists

#------------------------------------------------------------------------------
#Descompactando uma Tupla
#Quando criamos uma tupla, normalmente atribuímos valores a ela. Isso é chamado de "empacotar" uma tupla:
fruits = ("apple", "banana", "cherry")
print(fruits)#saida ('apple', 'banana', 'cherry')

#Mas, em Python, também podemos extrair os valores de volta para as variáveis. Isso é chamado de "descompactar":
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)#saida apple
print(yellow)#saida banana
print(red)#saida cherry


#Usando asterisco*
#Se o número de variáveis ​​for menor que o número de valores, você pode adicionar um
# *ao nome da variável e os valores serão atribuídos à variável como uma lista:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)# saida apple
print(yellow)# saida banana
print(red)# saida ['cherry', 'strawberry', 'raspberry']

#Se o asterisco for adicionado a outro nome de variável que não o último,
# o Python atribuirá valores à variável até que o número de valores restantes corresponda ao número de variáveis ​​restantes.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)# saida apple
print(tropic)# saida ['mango', 'papaya', 'pineapple']
print(red)# saida cherry
#------------------------------------------------------------------------------
#Percorrer uma Tupla
#Você pode percorrer os itens da tupla usando um forloop.

#Iterar pelos itens e imprimir os valores:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)# saida
#apple
#banana
#cherry
#------------------------------------------------------------------------------
#Percorrer os números de índice
#Você também pode percorrer os itens da tupla consultando seu número de índice.

#Use as funções range()e len()para criar um iterável adequado.
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])# saida
#apple
#banana
#cherry
#------------------------------------------------------------------------------
#Usando um loop while
#Você pode percorrer os itens da lista usando um whileloop.

#Use a len()função para determinar o comprimento da tupla, então comece em 0 e faça um loop pelos itens da tupla consultando seus índices.
#Lembre-se de aumentar o índice em 1 após cada iteração.
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  #saida
  #apple
  #banana
  #cherry

#------------------------------------------------------------------------------
#Junte-se a duas tuplas
#Para juntar duas ou mais tuplas você pode usar o + operador:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)# saida ('a', 'b', 'c', 1, 2, 3)

#Multiplicar Tuplas
#Se você quiser multiplicar o conteúdo de uma tupla um determinado número de vezes, você pode usar o * operador:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)# saida ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

#------------------------------------------------------------------------------
#Métodos de Tupla
#Python tem dois métodos integrados que você pode usar em tuplas.

#O count()método retorna o número de vezes que um valor especificado aparece na tupla.
#Sintaxe
#tuple.count(value)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)# saida 2

#------------------------------------------------------------------------------
#Definição e uso
#O index()método encontra a primeira ocorrência do valor especificado.
#O index()método gera uma exceção se o valor não for encontrado.

#Sintaxe
#tuple.index(value)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)# saida 3
#------------------------------------------------------------------------------
