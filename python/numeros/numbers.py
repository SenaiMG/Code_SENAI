#existem 3 tipos de numeros em python que são
#int
#float
#complex

#inteiros
#Int, ou inteiro, é um número inteiro, positivo ou negativo, sem decimais, de comprimento ilimitado.
x = 1
y = 35656222554887711
z = -3255522
print(type(x))#saida <class 'int'>
print(type(y))#saida <class 'int'>
print(type(z))#saida <class 'int'>
#-------------------------------------------------------------------------------
#float
#Float, ou "número de ponto flutuante" é um número, positivo ou negativo, contendo um ou mais decimais.
#Float também pode ser números científicos com um "e" para indicar a potência de 10.
x = 1.10
y = 1.0
z = -35.59
print(type(x))#saida <class 'float'>
print(type(y))#saida <class 'float'>
print(type(z))#saida <class 'float'>
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))#saida <class 'float'>
print(type(y))#saida <class 'float'>
print(type(z))#saida <class 'float'>
#-------------------------------------------------------------------------------
#complexos
#Os números complexos são escritos com um "j" como a parte imaginária:
x = 3+5j
y = 5j
z = -5j
print(type(x))#saida <class 'complex'>
print(type(y))#saida <class 'complex'>
print(type(z))#saida <class 'complex'>
#------------------------------------------------------------------------------
#gerando um numero aleatorio
import random
print(random.randrange(1, 10))
