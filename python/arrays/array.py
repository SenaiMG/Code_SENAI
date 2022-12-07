#Nota: Python não tem suporte integrado para Arrays, mas Python Lists pode ser usado em seu lugar.
#Matrizes
#Nota: Esta página mostra como usar LISTS como ARRAYS, porém, para trabalhar com arrays em 
# Python você terá que importar uma biblioteca, como a biblioteca NumPy .


#Arrays são usados ​​para armazenar vários valores em uma única variável:
cars = ["Ford", "Volvo", "BMW"]

print(cars)
#saida ['Ford', 'Volvo', 'BMW']
#----------------------------------------------------------------------------------------------------
#O que é uma Matriz?
#Uma matriz é uma variável especial, que pode conter mais de um valor por vez.
#Se você tiver uma lista de itens (uma lista de nomes de carros, por exemplo), 
# armazenar os carros em variáveis ​​únicas pode ser assim:
#car1 = "Ford"
#car2 = "Volvo"
#car3 = "BMW"
#No entanto, e se você quiser percorrer os carros e encontrar um específico? 
# E se você não tivesse 3 carros, mas 300?
#A solução é um array!
#Uma matriz pode conter muitos valores sob um único nome e você pode acessar 
# os valores referindo-se a um número de índice.

#----------------------------------------------------------------------------------------------------
#Acessar os elementos de um array
#Você se refere a um elemento de array referindo-se ao número do índice .

cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

print(x)
#saida Ford
#----------------------------------------------------------------------------------------------------
#modificar um item do array

cars = ["Ford", "Volvo", "BMW"]

cars[0] = "Toyota"

print(cars)#saida ['Toyota', 'Volvo', 'BMW']

#----------------------------------------------------------------------------------------------------
#O comprimento de uma array "matriz"
#Use o len()método para retornar o comprimento de uma matriz (o número de elementos em uma matriz).
cars = ["Ford", "Volvo", "BMW"]

x = len(cars)

print(x)
#saida 3

#OBS: O comprimento de uma matriz é sempre um a mais que o índice de matriz mais alto.


#----------------------------------------------------------------------------------------------------
#Elementos de matriz em loop
#Você pode usar o for inloop para percorrer todos os elementos de uma matriz.
cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)
#saida Ford
#Volvo
#BMW

#----------------------------------------------------------------------------------------------------
#Adicionando Elementos de Matriz
#Você pode usar o append()método para adicionar um elemento a uma matriz.
cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda")

print(cars)
#saida ['Ford', 'Volvo', 'BMW', 'Honda']

#----------------------------------------------------------------------------------------------------
#Removendo Elementos da Matriz
#Você pode usar o pop()método para remover um elemento da matriz.
cars = ["Ford", "Volvo", "BMW"]

cars.pop(1)

print(cars)
#saida ['Ford', 'BMW']

#Você também pode usar o remove()método para remover um elemento da matriz.
cars = ["Ford", "Volvo", "BMW"]

cars.remove("Volvo")

print(cars)
#saida ['Ford', 'BMW']
#----------------------------------------------------------------------------------------------------
#metodos para usar com arrays
#Definição e Uso
#O append()método acrescenta um elemento ao final da lista.

#Sintaxe
#list.append(elmnt)
fruits = ["apple", "banana", "cherry"]

fruits.append("orange")

print(fruits)
#saida ['apple', 'banana', 'cherry', 'orange']
#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O clear()método remove todos os elementos de uma lista.

#Sintaxe
#list.clear()
fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits)
#saida []
#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O copy()método retorna uma cópia da lista especificada.

#Sintaxe
#list.copy()
fruits = ["apple", "banana", "cherry"]

x = fruits.copy()

print(x)
#saida ['apple', 'banana', 'cherry']

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O count()método retorna o número de elementos com o valor especificado.

#Sintaxe
#list.count(value)
fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(x)#saida 1

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O extend()método adiciona os elementos de lista especificados (ou qualquer iterável) 
# ao final da lista atual.

#Sintaxe
#list.extend(iterable)
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)
#saida ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O index()método retorna a posição na primeira ocorrência do valor especificado.

#Sintaxe
#list.index(elmnt)
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)
#saida 2

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O insert()método insere o valor especificado na posição especificada.

#Sintaxe
#list.insert(pos, elmnt)
fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)
#saida ['apple', 'orange', 'banana', 'cherry']

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O pop()método remove o elemento na posição especificada.

#Sintaxe
#list.pop(pos)
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

print(fruits)
#saida ['apple', 'cherry']

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O remove()método remove a primeira ocorrência do elemento com o valor especificado.

#Sintaxe
#list.remove(elmnt)
cars = ["Ford", "Volvo", "BMW"]

cars.remove("Volvo")

print(cars)
#saida ['Ford', 'BMW']

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O reverse()método inverte a ordem de classificação dos elementos.

#Sintaxe
#list.reverse()
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)
#saida ['cherry', 'banana', 'apple']

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O sort()método classifica a lista em ordem crescente por padrão.

#Você também pode criar uma função para decidir o(s) critério(s) de classificação.

#Sintaxe
#list.sort(reverse=True|False, key=myFunc)

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)
#saida ['BMW', 'Ford', 'Volvo']
#----------------------------------------------------------------------------------------------------

