#Uma função lambda é uma pequena função anônima.

#Uma função lambda pode receber qualquer número de argumentos, mas pode ter apenas uma expressão.

#Sintaxe
#lambda arguments : expression


x = lambda a: a + 10
print(x(5))
#saida 15

#----------------------------------------------------------------------------------------------------
#As funções do Lambda podem receber qualquer número de argumentos:
x = lambda a, b: a * b
print(x(5, 6))
#saida 30


x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
#saida 13
#----------------------------------------------------------------------------------------------------
#Por que usar funções Lambda?
#O poder de lambda é melhor mostrado quando você os usa como uma função anônima dentro de outra função.

#Digamos que você tenha uma definição de função que aceita um argumento e esse argumento
# será multiplicado por um número desconhecido:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
#saida 22



#----------------------------------------------------------------------------------------------------
#Ou use a mesma definição de função para fazer uma função que sempre triplica o número que você envia:
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
#saida 33
#----------------------------------------------------------------------------------------------------
#Ou use a mesma definição de função para fazer ambas as funções, no mesmo programa:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) #saida 22
print(mytripler(11)) #saida 33

#OBS: Use funções lambda quando uma função anônima for necessária por um curto período de tempo.
#----------------------------------------------------------------------------------------------------

