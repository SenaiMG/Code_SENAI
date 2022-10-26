#Os conjuntos são usados ​​para armazenar vários itens em uma única variável.
#Set é um dos 4 tipos de dados internos do Python usados ​​para armazenar coleções de dados,
#os outros 3 são List , Tuple e Dictionary , todos com qualidades e usos diferentes.
#Um conjunto é uma coleção não ordenada , imutável* e não indexada .
# Nota: Os itens definidos não podem ser alterados, mas você pode remover itens e adicionar novos itens.
#Os conjuntos são escritos com colchetes.

thisset = {"apple", "banana", "cherry"}
print(thisset)# saida {'apple', 'cherry', 'banana'}

# Note: the set list is unordered, meaning: the items will appear in a random order.
# Refresh this page to see the change in the result.
#Observação: os conjuntos não são ordenados, portanto, você não pode ter certeza em qual ordem os itens aparecerão.


#Os itens do conjunto não são ordenados, não podem ser alterados e não permitem valores duplicados.

#Não ordenado
#Não ordenado significa que os itens em um conjunto não têm uma ordem definida.

#Os itens do conjunto podem aparecer em uma ordem diferente toda vez que você os usa e não podem ser referenciados por índice ou chave.

#Imutável
#Os itens do conjunto são imutáveis, o que significa que não podemos alterar os itens após a criação do conjunto.

#Depois que um conjunto é criado, você não pode alterar seus itens, mas pode remover itens e adicionar novos itens.

#Duplicatas não permitidas
#Os conjuntos não podem ter dois itens com o mesmo valor.

#Valores duplicados serão ignorados:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)# saida {'banana', 'cherry', 'apple'}


#Obter o comprimento de um conjunto
#Para determinar quantos itens um conjunto possui, use a len() função.
thisset = {"apple", "banana", "cherry"}
print(len(thisset))# saida 3

#Definir itens - Tipos de dados
#Os itens do conjunto podem ser de qualquer tipo de dados:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)# saida {'cherry', 'apple', 'banana'}
print(set2)# saida {1, 3, 5, 7, 9}
print(set3)# saida {False, True}

#Um conjunto pode conter diferentes tipos de dados:
set1 = {"abc", 34, True, 40, "male"}

print(set1)# saida {True, 34, 40, 'male', 'abc'}


#modelo()
#Da perspectiva do Python, os conjuntos são definidos como objetos com o tipo de dados 'set':
myset = {"apple", "banana", "cherry"}
print(type(myset))# saida <class 'set'>

#O construtor set()
#Também é possível usar o construtor set() para fazer um conjunto.
thisset = set(("apple", "banana", "cherry"))
print(thisset)# saida {'cherry', 'banana', 'apple'}
# Note: the set list is unordered, so the result will display the items in a random order.

#-------------------------------------------------------------------------------
#Acessar itens
#Você não pode acessar itens em um conjunto fazendo referência a um índice ou a uma chave.
#Mas você pode percorrer os itens do conjunto usando um for loop ou perguntar se um valor
#especificado está presente em um conjunto, usando a palavra- inchave.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#saida
#banana
#cherry
#apple


thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
#saida True

#-------------------------------------------------------------------------------
#Adicionar itens
#Depois que um conjunto é criado, você não pode alterar seus itens, mas pode adicionar novos itens.
#Para adicionar um item a um conjunto, use o add() método.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)# saida {'apple', 'orange', 'banana', 'cherry'}


#Adicionar conjuntos
#Para adicionar itens de outro conjunto ao conjunto atual, use o update() método.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)# saida {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

#Adicionar qualquer iterável
#O objeto no update()método não precisa ser um conjunto, pode ser qualquer objeto
#iterável (tuplas, listas, dicionários etc.).

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)#saida {'banana', 'cherry', 'apple', 'orange', 'kiwi'}

#-------------------------------------------------------------------------------
#Remover item
#Para remover um item em um conjunto, use o método remove(), ou .discard()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)# saida {'cherry', 'apple'}
#Nota: Se o item a ser removido não existir, remove()será gerado um erro.

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)# saida {'apple', 'cherry'}
#Nota: Se o item a ser removido não existir, NÃOdiscard() irá gerar um erro.

#Você também pode usar o pop()método para remover um item, mas esse
#método removerá o último item. Lembre-se de que os conjuntos não são ordenados, então você não saberá qual item será removido.
#O valor de retorno do pop()método é o item removido.

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item saida cherry
print(thisset) #the set after removal saida {'apple', 'banana'}
#Nota: Os conjuntos não são ordenados , portanto, ao usar o pop()método, você não sabe qual item será removido.

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)# saida set()

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists
#saida Traceback (most recent call last):
 # File "demo_set_del.py", line 5, in <module>
#    print(thisset) #this will raise an error because the set no longer exists
#NameError: name 'thisset' is not defined

#-------------------------------------------------------------------------------
#loop e set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  #saida
  #apple
  #banana
  #cherry

#-------------------------------------------------------------------------------
#Junte dois conjuntos
#Existem várias maneiras de unir dois ou mais conjuntos em Python.

#Você pode usar o union()método que retorna um novo conjunto contendo todos os
#itens de ambos os conjuntos ou o update()método que insere todos os itens de um conjunto em outro:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)# saida {1, 'b', 'c', 3, 2, 'a'}

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)# saida {'b', 2, 'c', 1, 'a', 3}

#Mantenha APENAS as duplicatas
#O intersection_update()método manterá apenas os itens presentes em ambos os conjuntos.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)# saida {'apple'}

#O intersection()método retornará um novo conjunto, que contém apenas os itens presentes em ambos os conjuntos.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)#saida {'apple'}

#Mantenha tudo, mas não as duplicatas
#O symmetric_difference_update()método manterá apenas os elementos que NÃO estão presentes em ambos os conjuntos.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)# saida {'google', 'banana', 'microsoft', 'cherry'}

#O symmetric_difference()método retornará um novo conjunto,
#que contém apenas os elementos que NÃO estão presentes em ambos os conjuntos.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)# saida {'google', 'banana', 'microsoft', 'cherry'}

#-------------------------------------------------------------------------------
#metodos python para o set

#Definição e uso
#O add()método adiciona um elemento ao conjunto.
#Se o elemento já existir, o add()método não adiciona o elemento.

#Sintaxe
#set.add(elmnt)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)# saida {'orange', 'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry"}
thisset.add("apple")
print(thisset)# saida {'cherry', 'apple', 'banana'}

#-------------------------------------------------------------------------------
#Definição e uso
#O clear()método remove todos os elementos de um conjunto.
#Sintaxe
#set.clear()
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)# saida set()

#-------------------------------------------------------------------------------
#Definição e uso
#O copy()método copia o conjunto.

#Sintaxe
#set.copy()
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)# saida {'apple', 'banana', 'cherry'}

#-------------------------------------------------------------------------------
#Definição e uso
#O difference()método retorna um conjunto que contém a diferença entre dois conjuntos.

#Significado: O conjunto retornado contém itens que existem apenas no primeiro conjunto e não nos dois conjuntos.

#Sintaxe
#set.difference(set)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)# saida {'cherry', 'banana'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x)
print(z)# saida {'google', 'microsoft'}

#-------------------------------------------------------------------------------
#Definição e uso
#O difference_update()método remove os itens que existem em ambos os conjuntos.
#O difference_update()método é diferente do difference()método, pois o difference() método retorna um novo conjunto , sem os itens indesejados, e o difference_update()método remove os itens indesejados do conjunto original.

#Sintaxe
#set.difference_update(set)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)
print(x)# saida {'banana', 'cherry'}


#-------------------------------------------------------------------------------
#Definição e uso
#O discard()método remove o item especificado do conjunto.

#Esse método é diferente do remove()método, porque o remove() método gerará um erro se o item especificado não existir e o discard()método não .

#Sintaxe
#set.discard(value)
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)# saida {'cherry', 'apple'}

#-------------------------------------------------------------------------------
#Definição e uso
#O intersection()método retorna um conjunto que contém a semelhança entre dois ou mais conjuntos.
#Significado: O conjunto retornado contém apenas itens que existem em ambos os conjuntos, ou em todos os conjuntos se a comparação for feita com mais de dois conjuntos.

#Sintaxe
#set.intersection(set1, set2 ... etc)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)# saida {'apple'}

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result)# saida {'c'}
#-------------------------------------------------------------------------------
#Definição e uso
#O intersection_update()método remove os itens que não estão presentes em ambos os conjuntos (ou em todos os conjuntos se a comparação for feita entre mais de dois conjuntos).
#O intersection_update()método é diferente do intersection()método, pois o intersection() método retorna um novo conjunto , sem os itens indesejados, e o intersection_update()método remove os itens indesejados do conjunto original.

#Sintaxe
#set.intersection_update(set1, set2 ... etc)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)# saida {'apple'}
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x)# saida {'c'}
#-------------------------------------------------------------------------------
#Definição e uso
#O isdisjoint()método retorna True se nenhum dos itens estiver presente em ambos os conjuntos, caso contrário, retorna False.

#Sintaxe
#set.isdisjoint(set)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)# saida True

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print(z)# saida False
#-------------------------------------------------------------------------------
#Definição e uso
#O issubset()método retornará True se todos os itens do conjunto existirem no conjunto especificado, caso contrário, retornará False.

#Sintaxe
#set.issubset(set)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)# saida True

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print(z)# saida false
#-------------------------------------------------------------------------------
#Definição e uso
#O issuperset()método retornará True se todos os itens do conjunto especificado existirem no conjunto original, caso contrário, retornará False.

#Sintaxe
#set.issuperset(set)
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)# saida True

x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)# saida false


#-------------------------------------------------------------------------------
#Definição e uso
#O pop()método remove um item aleatório do conjunto.

#Este método retorna o item removido.

#Sintaxe
#set.pop()
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)# saida {'cherry', 'apple'}

fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(x)# saida banana

#-------------------------------------------------------------------------------
#Definição e uso
#O remove()método remove o elemento especificado do conjunto.

#Esse método é diferente do discard()método, porque o remove() método gerará um erro se o item especificado não existir e o discard()método não .

#Sintaxe
#set.remove(item)
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)# saida {'apple', 'cherry'}

#-------------------------------------------------------------------------------
#Definição e uso
#O symmetric_difference()método retorna um conjunto que contém todos os itens de ambos os conjuntos, mas não os itens presentes em ambos os conjuntos.
#Significado: O conjunto retornado contém uma mistura de itens que não estão presentes em ambos os conjuntos.

#Sintaxe
#set.symmetric_difference(set)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print(z)# saida {'google', 'cherry', 'banana', 'microsoft'}


#-------------------------------------------------------------------------------
#Definição e uso
#O symmetric_difference_update()método atualiza o conjunto original removendo os itens presentes em ambos os conjuntos e inserindo os outros itens.

#Sintaxe
#set.symmetric_difference_update(set)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)# saida {'google', 'microsoft', 'cherry', 'banana'}


#-------------------------------------------------------------------------------
#Definição e uso
#O union()método retorna um conjunto que contém todos os itens do conjunto original e todos os itens do(s) conjunto(s) especificado(s).

#Você pode especificar quantos conjuntos quiser, separados por vírgulas.

#Não precisa ser um conjunto, pode ser qualquer objeto iterável.

#Se um item estiver presente em mais de um conjunto, o resultado conterá apenas uma aparição desse item.

#Sintaxe
#set.union(set1, set2...)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)
print(z)# saida {'banana', 'cherry', 'microsoft', 'google', 'apple'}


x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)
print(result)# saida {'f', 'b', 'e', 'c', 'a', 'd'}
#-------------------------------------------------------------------------------
#Definição e uso
#O update()método atualiza o conjunto atual, adicionando itens de outro conjunto (ou qualquer outro iterável).
#Se um item estiver presente em ambos os conjuntos, apenas uma aparência desse item estará presente no conjunto atualizado.

#Sintaxe
#set.update(set)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)
print(x)# saida {'cherry', 'apple', 'google', 'microsoft', 'banana'}
#-------------------------------------------------------------------------------
