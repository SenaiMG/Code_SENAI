#Lista
#As listas são usadas para armazenar vários itens em uma única variável.
#As listas são um dos 4 tipos de dados internos do Python usados ​​para armazenar
#coleções de dados, os outros 3 são Tuple , Set e Dictionary , todos com qualidades e usos diferentes.
#As listas são criadas usando colchetes:
thislist = ["apple", "banana", "cherry"]
print(thislist)# saida ['apple', 'banana', 'cherry']

#------------------------------------------------------------------------------
#lista de itens
#Os itens da lista são ordenados, alteráveis ​​e permitem valores duplicados.
#Os itens da lista são indexados, o primeiro item possui índice [0], o segundo item possui índice [1]etc.

#Encomendado
#Quando dizemos que as listas estão ordenadas, significa que os itens têm uma ordem definida, e essa ordem não será alterada.
#Se você adicionar novos itens a uma lista, os novos itens serão colocados no final da lista.
#------------------------------------------------------------------------------
#Mutável
#A lista é mutável, o que significa que podemos alterar, adicionar e remover itens em uma lista após ela ter sido criada.

#Permitir duplicatas
#Como as listas são indexadas, as listas podem ter itens com o mesmo valor:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)# saida ['apple', 'banana', 'cherry', 'apple', 'cherry']
#------------------------------------------------------------------------------
#Comprimento da lista
#Para determinar quantos itens uma lista possui, use a len()função:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))# saida 3
#------------------------------------------------------------------------------
#Listar itens - Tipos de dados
#Os itens da lista podem ser de qualquer tipo de dados:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)# saida ['apple', 'banana', 'cherry']
print(list2)# saida [1, 5, 7, 9, 3]
print(list3)# saida [True, False, False]
#------------------------------------------------------------------------------
list1 = ["abc", 34, True, 40, "male"]
print(list1)# saida ['abc', 34, True, 40, 'male']
#------------------------------------------------------------------------------
#modelo()
#Da perspectiva do Python, as listas são definidas como objetos com o tipo de dados 'list':
mylist = ["apple", "banana", "cherry"]
print(type(mylist))# saida <class 'list'>
#------------------------------------------------------------------------------
#O construtor list()
#Também é possível usar o construtor list() ao criar uma nova lista.
thislist = list(("apple", "banana", "cherry"))
print(thislist)# saida ['apple', 'banana', 'cherry']
#------------------------------------------------------------------------------
#Coleções Python (matrizes)
#Existem quatro tipos de dados de coleção na linguagem de programação Python:

#Lista é uma coleção que é ordenada e mutável. Permite membros duplicados.
#Tupla é uma coleção ordenada e imutável. Permite membros duplicados.
#Set é uma coleção não ordenada, imutável* e não indexada. Nenhum membro duplicado.
#Dicionário é uma coleção ordenada** e mutável. Nenhum membro duplicado.
#Os itens do conjunto são imutáveis, mas você pode remover e/ou adicionar itens sempre que quiser.
#A partir da versão 3.7 do Python, os dicionários são ordenados . No Python 3.6 e anteriores, os dicionários não são ordenados .
#------------------------------------------------------------------------------
#Acessar itens
#Os itens da lista são indexados e você pode acessá-los consultando o número do índice:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])# saida banana
#------------------------------------------------------------------------------
#Indexação negativa
#Indexação negativa significa começar do fim
#-1refere-se ao último item, -2refere-se ao penúltimo item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])# saida cherry
#------------------------------------------------------------------------------
#Faixa de índices
#Você pode especificar um intervalo de índices especificando onde começar e onde terminar o intervalo.
#Ao especificar um intervalo, o valor de retorno será uma nova lista com os itens especificados.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])# saida ['cherry', 'orange', 'kiwi']
#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included
#------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])# saida ['apple', 'banana', 'cherry', 'orange']
#This will return the items from index 0 to index 4.
#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included
#------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])# saida ['cherry', 'orange', 'kiwi', 'melon', 'mango']
#This will return the items from index 2 to the end.
#Remember that index 0 is the first item, and index 2 is the third
#------------------------------------------------------------------------------
#Faixa de índices negativos
#Especifique índices negativos se desejar iniciar a pesquisa a partir do final da lista:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])# saida ['orange', 'kiwi', 'melon']
#Negative indexing means starting from the end of the list.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,
#------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")# saida Yes, 'apple' is in the fruits list
#------------------------------------------------------------------------------
#Alterar valor do item
#Para alterar o valor de um item específico, consulte o número do índice:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)# saida ['apple', 'blackcurrant', 'cherry']
#------------------------------------------------------------------------------
#Alterar um intervalo de valores de itens
#Para alterar o valor dos itens dentro de um intervalo específico,
#defina uma lista com os novos valores e consulte o intervalo de números de índice onde deseja inserir os novos valores:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)# saida ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
#------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)# saida ['apple', 'blackcurrant', 'watermelon', 'cherry']
#------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)#saida ['apple', 'watermelon']
#------------------------------------------------------------------------------
#Inserir itens
#Para inserir um novo item de lista, sem substituir nenhum dos valores existentes, podemos usar o insert()método.
#O insert()método insere um item no índice especificado:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #saida ['apple', 'banana', 'watermelon', 'cherry']
#------------------------------------------------------------------------------
#Anexar itens
#Para adicionar um item ao final da lista, use o método append() :
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)# saida ['apple', 'banana', 'cherry', 'orange']
#------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)# saida ['apple', 'orange', 'banana', 'cherry']
#------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)# saida ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
#------------------------------------------------------------------------------
#Adicionar qualquer iterável
#O extend()método não precisa anexar listas , você pode adicionar qualquer objeto
#iterável (tuplas, conjuntos, dicionários etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #saida ['apple', 'banana', 'cherry', 'kiwi', 'orange']
#------------------------------------------------------------------------------
#Remover item especificado
#O remove()método remove o item especificado.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)# saida ['apple', 'cherry']
#------------------------------------------------------------------------------
#Remover índice especificado
#O pop()método remove o índice especificado.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)# saida ['apple', 'cherry']
#------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)# saida ['apple', 'banana']
#------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)# saida ['banana', 'cherry']
#------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".
# saida Traceback (most recent call last):
  #File "demo_list_del2.py", line 3, in <module>
#    print(thislist) #this will cause an error because you have succsesfully deleted "thislist".
#NameError: name 'thislist' is not defined
#------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)# saida []
#------------------------------------------------------------------------------
#Percorrer uma lista
#Você pode percorrer os itens da lista usando um for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  # saida apple
#banana
#cherry
#------------------------------------------------------------------------------
#Percorrer os números de índice
#Você também pode percorrer os itens da lista consultando seu número de índice.
#Use as funções range()e len()para criar um iterável adequado.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])# saida  apple
 #banana
 #cherry
#------------------------------------------------------------------------------
#Usando um loop while
#Você pode percorrer os itens da lista usando um whileloop.
#Use a len()função para determinar o comprimento da lista, então comece em 0 e
#faça um loop pelos itens da lista consultando seus índices.
#Lembre-se de aumentar o índice em 1 após cada iteração.
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
# saida
# apple
# banana
# cherry
#------------------------------------------------------------------------------
#Loop usando compreensão de lista
#O List Comprehension oferece a sintaxe mais curta para percorrer listas:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#saida
# apple
# banana
# cherry
#------------------------------------------------------------------------------
#Compreensão da lista
#A compreensão de lista oferece uma sintaxe mais curta quando você deseja criar uma nova lista com base nos valores
#de uma lista existente.
#Exemplo:
#Com base em uma lista de frutas, você deseja uma nova lista, contendo apenas as frutas com a letra "a" no nome.
#Sem compreensão de lista, você terá que escrever uma fordeclaração com um teste condicional dentro:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)# saida ['apple', 'banana', 'mango']
#------------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)# saida ['apple', 'banana', 'mango']
#------------------------------------------------------------------------------
#A Sintaxe
#newlist = [expression for item in iterable if condition == True]
#O valor de retorno é uma nova lista, deixando a lista antiga inalterada.
#Doença
#A condição é como um filtro que aceita apenas os itens que avaliam como True.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)# saida ['banana', 'cherry', 'kiwi', 'mango']
#A condição if x != "apple"  retornará Truepara todos os elementos exceto "maçã",
#fazendo com que a nova lista contenha todas as frutas, exceto "maçã".
#A condição é opcional e pode ser omitida:

#sem if
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)# saida ['apple', 'banana', 'cherry', 'kiwi', 'mango']
#------------------------------------------------------------------------------
#Iterável
#O iterável pode ser qualquer objeto iterável, como uma lista, tupla, conjunto etc.
#Você pode usar a range()função para criar um iterável:
newlist = [x for x in range(10)]
print(newlist)# saida [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#------------------------------------------------------------------------------
newlist = [x for x in range(10) if x < 5]
print(newlist)# saida [0, 1, 2, 3, 4]
#------------------------------------------------------------------------------
#Expressão
#A expressão é o item atual na iteração, mas também é o resultado, que você pode
#manipular antes de terminar como um item de lista na nova lista:
#Exemplo:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)# saida ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
#------------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)# saida ['hello', 'hello', 'hello', 'hello', 'hello']
#------------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)# saida ['apple', 'orange', 'cherry', 'kiwi', 'mango']
#------------------------------------------------------------------------------
#Classificar lista alfanumérica
#Objetos de lista possuem um sort()método que ordenará a lista de forma alfanumérica, em ordem crescente, por padrão:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)#saida ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
#------------------------------------------------------------------------------
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)# saida [23, 50, 65, 82, 100]
#------------------------------------------------------------------------------
#Classificação decrescente
#Para classificar de forma decrescente, use o argumento de palavra-chave reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)# saida ['pineapple', 'orange', 'mango', 'kiwi', 'banana']
#------------------------------------------------------------------------------
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)# saida [100, 82, 65, 50, 23]
#------------------------------------------------------------------------------
#Personalizar a função de classificação
#Você também pode personalizar sua própria função usando o argumento de palavra-chave .key = function

#A função retornará um número que será usado para ordenar a lista (o número mais baixo primeiro):

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)# saida [50, 65, 23, 82, 100]
#------------------------------------------------------------------------------
#Classificação sem distinção entre maiúsculas e minúsculas
#Por padrão, o sort()método diferencia maiúsculas de minúsculas,
#resultando em todas as letras maiúsculas classificadas antes das minúsculas:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)#saida ['Kiwi', 'Orange', 'banana', 'cherry']
#------------------------------------------------------------------------------
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)# saida ['banana', 'cherry', 'Kiwi', 'Orange']
#------------------------------------------------------------------------------
#Ordem reversa
#E se você quiser inverter a ordem de uma lista, independentemente do alfabeto?
#O reverse()método inverte a ordem de classificação atual dos elementos.

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # saida ['cherry', 'Kiwi', 'Orange', 'banana']
#------------------------------------------------------------------------------
#Copiar uma lista
#Você não pode copiar uma lista simplesmente digitando list2 = list1,
#porque: list2será apenas uma referência a list1, e as alterações feitas list1automaticamente também serão feitas em list2.
#Existem maneiras de fazer uma cópia, uma delas é usar o método List interno copy().
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)# saida ['apple', 'banana', 'cherry']
#------------------------------------------------------------------------------
#Outra maneira de fazer uma cópia é usar o método interno list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)# saida ['apple', 'banana', 'cherry']
#------------------------------------------------------------------------------
#Junte-se a duas listas
#Existem várias maneiras de unir ou concatenar duas ou mais listas em Python.
#Uma das maneiras mais fáceis é usando o + operador.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)# saida ['a', 'b', 'c', 1, 2, 3]
#------------------------------------------------------------------------------
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)# saida ['a', 'b', 'c', 1, 2, 3]
#------------------------------------------------------------------------------
# Ou você pode usar o extend() método, cuja finalidade é adicionar elementos de uma lista para outra lista:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)# saida ['a', 'b', 'c', 1, 2, 3]
#------------------------------------------------------------------------------


#Listar métodos
#Python tem um conjunto de métodos integrados que você pode usar em listas.
#São eles :
#------------------------------------------------------------------------------
# sort() sintaxe list.sort(reverse=True|False, key=myFunc)
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)# saida ['BMW', 'Ford', 'Volvo']

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)# saida ['Volvo', 'Ford', 'BMW']

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)# saida ['VW', 'BMW', 'Ford', 'Mitsubishi']

def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)#saida [{'car': 'Mitsubishi', 'year': 2000}, {'car': 'Ford', 'year': 2005}, {'car': 'VW', 'year': 2011}, {'car': 'BMW', 'year': 2019}]

# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)# saida ['Mitsubishi', 'Ford'', 'BMW', 'VW']
#------------------------------------------------------------------------------
# O reverse()método inverte a ordem de classificação dos elementos.
# sintaxe list.reverse()
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)# saida ['cherry', 'banana', 'apple']
#------------------------------------------------------------------------------
# O remove()método remove a primeira ocorrência do elemento com o valor especificado.
#list.remove(elmnt)
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)# saida ['apple', 'cherry']
#------------------------------------------------------------------------------
# O pop()método remove o elemento na posição especificada.
# sintaxe list.pop(pos)
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)# saida ['apple', 'cherry']

fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x)# saida banana
#------------------------------------------------------------------------------
# O insert()método insere o valor especificado na posição especificada.
# sintaxe list.insert(pos, elmnt)
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)# saida ['apple', 'orange', 'banana', 'cherry']
#------------------------------------------------------------------------------
#O index()método retorna a posição na primeira ocorrência do valor especificado.
# sintaxe list.index(elmnt)
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)# saida 2

fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)# saida 3
#------------------------------------------------------------------------------
#O extend()método adiciona os elementos de lista especificados (ou qualquer iterável) ao final da lista atual.
#sintaxe list.extend(iterable)

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)# saida ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)# saida ['apple', 'banana', 'cherry', 1, 4, 5, 9]
#------------------------------------------------------------------------------
#O count()método retorna o número de elementos com o valor especificado.
#sintaxe list.count(value)
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)# saida 1

fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = fruits.count(9)
print(x)# saida 2
#------------------------------------------------------------------------------
#O copy()método retorna uma cópia da lista especificada.
# sintaxe list.copy()

fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)# saida ['apple', 'banana', 'cherry']
#------------------------------------------------------------------------------
#O clear()método remove todos os elementos de uma lista.
# sintaxe list.clear()
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)# saida []
#------------------------------------------------------------------------------
# O append()método anexa um elemento ao final da lista.
#sintaxe list.append(elmnt)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)#saida ['apple', 'banana', 'cherry', 'orange']

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)# ['apple', 'banana', 'cherry', ["Ford", "BMW", "Volvo"]
#------------------------------------------------------------------------------
