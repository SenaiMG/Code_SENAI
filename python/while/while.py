#O loop while
#Com o loop while podemos executar um conjunto de instruções desde que uma condição seja verdadeira.
i = 1
while i < 6:
  print(i)
  i += 1
  # saida
  #1
  #2
  #3
  #4
  #5

#Nota: lembre-se de incrementar i, senão o loop continuará para sempre.

#O loop while requer que as variáveis ​​relevantes estejam prontas, neste exemplo
#precisamos definir uma variável de indexação, i , que definimos como 1.
#-------------------------------------------------------------------------------
#A declaração de pausa
#Com a instrução break podemos parar o loop mesmo se a condição while for verdadeira:

i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

# saida 1
# 2
# 3

#------------------------------------------------------------------------------
#A declaração continua
#Com a instrução continue podemos parar a iteração atual e continuar com a próxima:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#saida 1
# 2
# 4
# 5
# 6

# Note that number 3 is missing in the result
#------------------------------------------------------------------------------
#A declaração else
#Com a instrução else podemos executar um bloco de código uma vez quando a condição não for mais verdadeira:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#saida 1
#2
#3
#4
#5
#i is no longer less than 6

#-------------------------------------------------------------------------------
