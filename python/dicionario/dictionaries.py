#Dicionário
#Os dicionários são usados ​​para armazenar valores de dados em pares chave:valor.

#Um dicionário é uma coleção ordenada*, mutável e que não permite duplicatas.

#A partir da versão 3.7 do Python, os dicionários são ordenados . No Python 3.6 e anteriores, os dicionários não são ordenados .

#Os dicionários são escritos com colchetes e possuem chaves e valores:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)# saida {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#Ordenado ou Não Ordenado?
#A partir da versão 3.7 do Python, os dicionários são ordenados . No Python 3.6 e anteriores, os dicionários não são ordenados .

#Quando dizemos que os dicionários estão ordenados, significa que os itens têm uma ordem definida, e essa ordem não será alterada.

#Não ordenado significa que os itens não têm uma ordem definida, você não pode fazer referência a um item usando um índice.

#Mutável
#Os dicionários são mutáveis, o que significa que podemos alterar, adicionar ou remover itens após a criação do dicionário.

#Duplicatas não permitidas
#Os dicionários não podem ter dois itens com a mesma chave:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)# saida {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#-------------------------------------------------------------------------------
#Tamanho do dicionário
#Para determinar quantos itens um dicionário possui, use a len()função:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))#saida 3
#-------------------------------------------------------------------------------
#Itens do Dicionário - Tipos de Dados
#Os valores nos itens do dicionário podem ser de qualquer tipo de dados:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)#saida {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

#-------------------------------------------------------------------------------
#modelo()
#Da perspectiva do Python, os dicionários são definidos como objetos com o tipo de dados 'dict':
#<class 'dict'>
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))#saida <class 'dict'>


#Coleções Python (matrizes)
#Existem quatro tipos de dados de coleção na linguagem de programação Python:

#Lista é uma coleção que é ordenada e mutável. Permite membros duplicados.
#Tupla é uma coleção ordenada e imutável. Permite membros duplicados.
#Set é uma coleção não ordenada, imutável* e não indexada. Nenhum membro duplicado.
#Dicionário é uma coleção ordenada** e mutável. Nenhum membro duplicado.
#*Os itens do conjunto são imutáveis, mas você pode remover e/ou adicionar itens sempre que quiser.

#**A partir da versão 3.7 do Python, os dicionários são ordenados . No Python 3.6
#e anteriores, os dicionários não são ordenados .

#Ao escolher um tipo de coleção, é útil entender as propriedades desse tipo.
#Escolher o tipo certo para um determinado conjunto de dados pode significar
#retenção de significado e pode significar um aumento na eficiência ou segurança.

#-------------------------------------------------------------------------------
#Acessando itens
#Você pode acessar os itens de um dicionário consultando o nome da chave, entre colchetes:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)# saida Mustang

#Existe também um método chamado get()que lhe dará o mesmo resultado:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)# saida Mustang


#Obter chaves
#O keys()método retornará uma lista de todas as chaves do dicionário.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)#saida dict_keys(['brand', 'model', 'year'])

#A lista de chaves é uma visualização do dicionário, o que significa que quaisquer
#alterações feitas no dicionário serão refletidas na lista de chaves.


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #saida  dict_keys(['brand', 'model', 'year'])
#before the change
car["color"] = "white"

print(x) #saida dict_keys(['brand', 'model', 'year', 'color'])
#after the change


#Obter valores
#O values()método retornará uma lista de todos os valores do dicionário.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)#saida dict_values(['Ford', 'Mustang', 1964])

#A lista de valores é uma visualização do dicionário,
#o que significa que quaisquer alterações feitas no dicionário serão refletidas na lista de valores.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x)# saida dict_values(['Ford', 'Mustang', 1964])
#before the change

car["year"] = 2020

print(x)# saida dict_values(['Ford', 'Mustang', 2020])
#after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) # saida dict_values(['Ford', 'Mustang', 1964])
#before the change

car["color"] = "red"

print(x) # saida dict_values(['Ford', 'Mustang', 1964, 'red'])
#after the change


#Obter itens
#O items()método retornará cada item em um dicionário, como tuplas em uma lista.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()
print(x)# saida dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x)# saida dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
#before the change

car["year"] = 2020

print(x) # saida dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])
#after the change


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) # saida dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
#before the change

car["color"] = "red"

print(x) # saida dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])
#after the change

# verifica se a chave existe
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  #saida Yes, 'model' is one of the keys in the thisdict dictionary
#-------------------------------------------------------------------------------
#Mudar valores
#Você pode alterar o valor de um item específico consultando seu nome de chave:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018
print(thisdict)# saida {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

#Atualizar dicionário
#O update()método atualizará o dicionário com os itens do argumento fornecido.
#O argumento deve ser um dicionário ou um objeto iterável com pares chave:valor.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)# saida {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#-------------------------------------------------------------------------------
#Adicionando itens
#A adição de um item ao dicionário é feita usando uma nova chave de índice e atribuindo um valor a ela:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)# saida {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

#Atualizar dicionário
#O update()método atualizará o dicionário com os itens de um determinado argumento. Se o item não existir, o item será adicionado.
#O argumento deve ser um dicionário ou um objeto iterável com pares chave:valor.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)# saida {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
#-------------------------------------------------------------------------------
#Removendo itens
#Existem vários métodos para remover itens de um dicionário:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)# saida {'brand': 'Ford', 'year': 1964}

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)# saida {'brand': 'Ford', 'model': 'Mustang'}

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)# saida {'brand': 'Ford', 'year': 1964}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
# saida erro pois foi excluido inteiramente o dicionario


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)# saida {}

#-------------------------------------------------------------------------------
#Percorrer um dicionário
#Você pode percorrer um dicionário usando um forloop.

#Ao percorrer um dicionário, o valor de retorno são as chaves do dicionário,
#mas também existem métodos para retornar os valores .

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
  #saida
  #brand
  #model
  #year

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
  # saida
  #Ford
  #Mustang
  #1964



thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
  # saida
  #Ford
  #Mustang
  #1964

  thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
  #saida
  #brand
  #model
  #year

  thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
  # saida
  #brand Ford
  #model Mustang
  #year 1964
#-------------------------------------------------------------------------------
#Copiar um dicionário
#Você não pode copiar um dicionário simplesmente digitando dict2 = dict1, porque:
#dict2será apenas uma referência a dict1, e as alterações feitas em dict1serão feitas automaticamente também em dict2.

#Existem maneiras de fazer uma cópia, uma delas é usar o método interno do Dicionário copy().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)# saida {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)# saida {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#-------------------------------------------------------------------------------
#Dicionários aninhados
#Um dicionário pode conter dicionários, isso é chamado de dicionários aninhados.

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)# saida {'child1': {'name': 'Emil', 'year': 2004},'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

#outra forma de aninha
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)# saida {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

#-------------------------------------------------------------------------------
#metodos que podem ser utilizado com dicionarios

#Definição e uso
#O clear()método remove todos os elementos de um dicionário.

#Sintaxe
#dictionary.clear()

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car)# saida {}
#-------------------------------------------------------------------------------
#Definição e uso
#O copy()método retorna uma cópia do dicionário especificado.

#Sintaxe
#dictionary.copy()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()
print(x)# saida {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#-------------------------------------------------------------------------------
#Definição e uso
#O fromkeys()método retorna um dicionário com as chaves especificadas e o valor especificado.

#Sintaxe
#dict.fromkeys(keys, value)
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)# saida ['key1': 0, 'key2': 0, 'key3': 0]

#outro exemplo
x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)# saida ['key1': None, 'key2': None, 'key3': None]

#-------------------------------------------------------------------------------
#Definição e uso
#O get()método retorna o valor do item com a chave especificada.

#Sintaxe
#dictionary.get(keyname, value)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")
print(x)# saida Mustang

#outro exemplo
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)
print(x)# saida 15000

#-------------------------------------------------------------------------------
#Definição e uso
#O items()método retorna um objeto de exibição. O objeto view contém os pares chave-valor do dicionário, como tuplas em uma lista.

#O objeto de visualização refletirá quaisquer alterações feitas no dicionário, veja o exemplo abaixo.

#Sintaxe
#dictionary.items()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()
print(x)#saida dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

car["year"] = 2018
print(x)# saida dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2018)])
#-------------------------------------------------------------------------------
#Definição e uso
#O keys()método retorna um objeto de exibição. O objeto view contém as chaves do dicionário, como uma lista.

#O objeto de visualização refletirá quaisquer alterações feitas no dicionário, veja o exemplo abaixo.

#Sintaxe
#dictionary.keys()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()
print(x)# saida dict_keys(['brand', 'model', 'year'])

#Quando um item é adicionado ao dicionário, o objeto de visualização também é atualizado:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

car["color"] = "white"
print(x)# saida dict_keys(['brand', 'model', 'year', 'color'])
#-------------------------------------------------------------------------------
#Definição e uso
#O pop()método remove o item especificado do dicionário.

#O valor do item removido é o valor de retorno do pop() método, veja o exemplo abaixo.

#Sintaxe
#dictionary.pop(keyname, defaultvalue)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")
print(car)# saida {'brand': 'Ford', 'year': 1964}


#O valor do item removido é o valor de retorno do método pop()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.pop("model")
print(x)#saida Mustang
#-------------------------------------------------------------------------------
#Definição e uso
#O popitem()método remove o último item inserido no dicionário. Nas versões anteriores à 3.7, o popitem()método remove um item aleatório.

#O item removido é o valor de retorno do popitem() método, como uma tupla, veja o exemplo abaixo.

#Sintaxe
#dictionary.popitem()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()
print(car)# saida {'brand': 'Ford', 'model': 'Mustang'}

#item removido
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.popitem()
print(x)# saida ('year', 1964)
#-------------------------------------------------------------------------------
#Definição e uso
#O setdefault()método retorna o valor do item com a chave especificada.

#Se a chave não existir, insira a chave, com o valor especificado, veja o exemplo abaixo

#Sintaxe
#dictionary.setdefault(keyname, value)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")
print(x)# saida Mustang

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "White")
print(x)# saida White
#-------------------------------------------------------------------------------
#Definição e uso
#O update()método insere os itens especificados no dicionário.

#Os itens especificados podem ser um dicionário ou um objeto iterável com pares de valores-chave.

#Sintaxe
#dictionary.update(iterable)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})
print(car)# saida {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}

#-------------------------------------------------------------------------------
#Definição e uso
#O values()método retorna um objeto de exibição. O objeto view contém os valores do dicionário, como uma lista.

#O objeto de visualização refletirá quaisquer alterações feitas no dicionário, veja o exemplo abaixo.

#Sintaxe
#dictionary.values()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()
print(x)# saida dict_values(['Ford', 'Mustang', 1964])

#Quando um valor é alterado no dicionário, o objeto de visualização também é atualizado
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

car["year"] = 2018
print(x)# saida dict_values(['Ford', 'Mustang', 2018])

#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
