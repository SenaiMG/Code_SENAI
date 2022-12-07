#Python é uma linguagem de programação orientada a objetos.
#Quase tudo em Python é um objeto, com suas propriedades e métodos.
#Uma classe é como um construtor de objetos ou um "projeto" para criar objetos.
class MyClass:
  x = 5

print(MyClass)#saida <class '__main__.MyClass'>

#----------------------------------------------------------------------------------------------------
#Criar um objeto
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)#saida 5
#----------------------------------------------------------------------------------------------------
#A Função __init__() é um construtor 
#Os exemplos acima são classes e objetos em sua forma mais simples e 
#não são realmente úteis em aplicações da vida real.
#Para entender o significado das classes, temos que entender a função interna __init__().
#Todas as classes possuem uma função chamada __init__(), que sempre é executada quando 
#a classe está sendo iniciada.
#Use a função __init__() para atribuir valores às propriedades do objeto ou outras 
#operações que são necessárias quando o objeto está sendo criado:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)#saida John
print(p1.age)#saida 36


#OBS:A __init__()função é chamada automaticamente toda vez que a classe está sendo 
# usada para criar um novo objeto.
#----------------------------------------------------------------------------------------------------
#A Função __str__() é como a to_string do php
#A função __str__() controla o que deve ser retornado quando o objeto de classe 
# é representado como uma string.
#Se a função __str__() não for definida, a representação de string do objeto é retornada:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)#saida <__main__.Person object at 0x15039e602100>


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"    

p1 = Person("John", 36)

print(p1)#saida John(36)

#----------------------------------------------------------------------------------------------------
#Métodos de objeto
#Objetos também podem conter métodos. Métodos em objetos são funções que pertencem ao objeto.
#Vamos criar um método na classe Person:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
#saida Hello my name is John

#Observação: o selfparâmetro é uma referência à instância atual da classe e
# é usado para acessar as variáveis ​​pertencentes à classe.

#----------------------------------------------------------------------------------------------------
#O parâmetro auto
#O selfparâmetro é uma referência à instância atual da classe e
# é usado para acessar as variáveis ​​pertencentes à classe.
#Não precisa ser nomeado self, você pode chamar como quiser, 
# mas tem que ser o primeiro parâmetro de qualquer função da classe:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
#saida Hello my name is John

#----------------------------------------------------------------------------------------------------
#Modificar Propriedades do Objeto
#Você pode modificar as propriedades em objetos como este:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)#saida 40

#----------------------------------------------------------------------------------------------------
#Excluir propriedades do objeto
#Você pode excluir propriedades em objetos usando a delpalavra-chave:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age

print(p1.age)
#saida Traceback (most recent call last):
  #File "demo_class7.py", line 13, in <module>
  #  print(p1.age)
#AttributeError: 'Person' object has no attribute 'age'

#----------------------------------------------------------------------------------------------------
#Excluir objetos
#Você pode excluir objetos usando a delpalavra-chave:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

print(p1)
#saida Traceback (most recent call last):
 # File "demo_class8.py", line 13, in <module>
 #   print(p1)
#NameError: 'p1' is not defined

#----------------------------------------------------------------------------------------------------
#A declaração de passagem
#classas definições não podem estar vazias, mas se por algum motivo você tiver 
#uma classdefinição sem conteúdo, coloque a passinstrução para evitar erros.
class Person:
  pass

# ter uma definição de classe vazia como esta geraria um erro sem a instrução pass


#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------