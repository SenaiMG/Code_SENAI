#Um loop for é usado para iterar sobre uma sequência (que é uma lista, uma tupla, um dicionário, um conjunto ou uma string).

#Isso é menos parecido com a palavra-chave for em outras linguagens de programação e
#funciona mais como um método iterador, conforme encontrado em outras linguagens de programação orientadas a objetos.

#Com o loop for podemos executar um conjunto de instruções, uma vez para cada item de uma lista, tupla, conjunto etc.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# saida
#apple
#banana
#cherry


# DICA: O loop for não requer que uma variável de indexação seja definida antecipadamente.
#Fazendo um loop em uma string
#Mesmo as strings são objetos iteráveis, elas contêm uma sequência de caracteres:
for x in "banana":
  print(x)
# saida
#b
#a
#n
#a
#n
#a

#-------------------------------------------------------------------------------
#A declaração de pausa
#Com a instrução break podemos parar o loop antes que ele tenha percorrido todos os itens:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
# saida apple
#banana

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  # saida apple
#-------------------------------------------------------------------------------
#A declaração continua
#Com a instrução continue podemos parar a iteração atual do loop e continuar com a próxima:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
# saida apple
#cherry

#-------------------------------------------------------------------------------
#A função intervalo()
#Para percorrer um conjunto de código um determinado número de vezes, podemos usar a função range() ,
#A função range() retorna uma sequência de números, começando em 0 por padrão e incrementa em 1
#(por padrão) e termina em um número especificado.
for x in range(6):
  print(x)
  # saida 0
#1
#2
#3
#4
#5

#Observe que range(6) não são os valores de 0 a 6, mas os valores de 0 a 5.

#A função range() tem como padrão 0 como valor inicial, porém é possível
#especificar o valor inicial adicionando um parâmetro: range(2, 6) , que significa valores de 2 a 6 (mas não incluindo 6):

for x in range(2, 6):
  print(x)
# saida 2
#3
#4
#5

#A função range() padroniza para incrementar a sequência em 1,
#porém é possível especificar o valor do incremento adicionando um terceiro parâmetro: range(2, 30, 3 ) :

for x in range(2, 30, 3):
  print(x)
# saida
# 2
# 5
# 8
# 11
# 14
# 17
# 20
# 23
# 26
# 29

#-------------------------------------------------------------------------------
#Mais em For Loop
#A else palavra-chave em um forloop especifica um bloco de código a ser executado quando o loop for concluído:
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  # saida
  # 0
  # 1
  # 2
  # 3
  # 4
  # 5
  # Finally finished!

#Nota: O elsebloco NÃO será executado se o loop for interrompido por uma breakinstrução.

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
# saida 0
# 1
# 2
#If the loop breaks, the else block is not executed.


#-------------------------------------------------------------------------------
#Loops aninhados
#Um loop aninhado é um loop dentro de um loop.
#O "loop interno" será executado uma vez para cada iteração do "loop externo":

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# saida
#red apple
#red banana
#red cherry
#big apple
#big banana
#big cherry
#tasty apple
#tasty banana
#tasty cherry

#-------------------------------------------------------------------------------
#A declaração de passagem
#for loops não podem estar vazios, mas se por algum motivo você tiver um forloop sem conteúdo,
#coloque a passinstrução para evitar erros.
for x in [0, 1, 2]:
  pass

# having an empty for loop like this, would raise an error without the pass statement
