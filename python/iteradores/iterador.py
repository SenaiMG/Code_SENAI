#Iteradores do Python
#Um iterador é um objeto que contém um número contável de valores.

#Um iterador é um objeto que pode ser iterado, o que significa que você pode percorrer 
# todos os valores.

#Tecnicamente, em Python, um iterador é um objeto que implementa o protocolo do iterador,
# que consiste nos métodos __iter__() e __next__().
#----------------------------------------------------------------------------------------------------
#Iterador vs Iterável
#Listas, tuplas, dicionários e conjuntos são todos objetos iteráveis. 
# Eles são contêineres iteráveis ​​dos quais você pode obter um iterador.
#Todos esses objetos possuem um iter()método que é usado para obter um iterador:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))#saida apple
print(next(myit))#saida banana
print(next(myit))#saida cherry

#Strings pares são objetos iteráveis ​​e podem retornar um iterador:

mystr = "banana"
myit = iter(mystr)

print(next(myit))#saida b
print(next(myit))#saida a
print(next(myit))#saida n
print(next(myit))#saida a
print(next(myit))#saida n
print(next(myit))#saida a
#----------------------------------------------------------------------------------------------------
#Fazendo um loop através de um iterador
#Também podemos usar um forloop para iterar por meio de um objeto iterável:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
  #saida apple
#banana
#cherry

mystr = "banana"

for x in mystr:
  print(x)
  #saida 
  #b
  #a
  #n
  #a
  #n
  #a
#----------------------------------------------------------------------------------------------------
#Criar um iterador
#Para criar um objeto/classe como um iterador, você deve implementar os métodos __iter__()e
# __next__()para o seu objeto.

#Como você aprendeu no capítulo Classes/Objetos do Python , todas as classes têm uma 
# função chamada __init__(), que permite que você faça algumas inicializações quando o 
# objeto está sendo criado.

#O __iter__()método age de forma semelhante, você pode fazer operações (inicializar etc.),
# mas sempre deve retornar o próprio objeto iterador.

#O __next__()método também permite fazer operações, devendo retornar o próximo item da sequência.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))#saida 1
print(next(myiter))#saida 2
print(next(myiter))#saida 3
print(next(myiter))#saida 4
print(next(myiter))#saida 5
#----------------------------------------------------------------------------------------------------
#StopIteration
#O exemplo acima continuaria indefinidamente se você tivesse instruções next()
#suficientes ou se fosse usado em um forloop.
#Para evitar que a iteração continue para sempre, podemos usar a StopIterationinstrução.
#No __next__()método, podemos adicionar uma condição de finalização para gerar um erro 
#se a iteração for feita um número especificado de vezes:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
  #saida 
#1
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
#13
#14
#15
#16
#17
#18
#19
#20

#----------------------------------------------------------------------------------------------------
