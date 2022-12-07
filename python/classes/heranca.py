#Herança do Python
#A herança nos permite definir uma classe que herda todos os métodos e propriedades de outra classe.
#A classe pai é a classe da qual está sendo herdada, também chamada de classe base.
#Classe filha é a classe que herda de outra classe, também chamada de classe derivada.

#----------------------------------------------------------------------------------------------------
#Criar uma classe pai
#Qualquer classe pode ser uma classe pai, então a sintaxe é a mesma de criar qualquer outra classe:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()#saida John Doe


#----------------------------------------------------------------------------------------------------
#Criar uma classe filha
#Para criar uma classe que herde a funcionalidade de outra classe, envie a classe pai
#como parâmetro ao criar a classe filha:

# Exemplo
#class Student(Person):
#  pass
#Observação: use a palavra- pass chave quando não quiser adicionar 
# nenhuma outra propriedade ou método à classe.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()#saida Mike Olsen

#----------------------------------------------------------------------------------------------------
#Adicione a função __init__()
#Até agora criamos uma classe filha que herda as propriedades e métodos de seu pai.
#Queremos adicionar a __init__()função à classe filha (em vez da palavra- passchave).
#Nota: A __init__()função é chamada automaticamente toda vez que a classe está sendo 
#usada para criar um novo objeto.

#Quando você adiciona a __init__()função, a classe filha não herdará mais a __init__()função do pai.
#Observação:__init__() a função do filho substitui a herança da __init__()função do pai.
#Para manter a herança da __init__() função do pai, adicione uma chamada à __init__()função do pai:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()#saida Mike Olsen

#Agora adicionamos com sucesso a função __init__() 
#e mantivemos a herança da classe pai e estamos prontos para adicionar 
#funcionalidade na __init__()função.



#----------------------------------------------------------------------------------------------------
#Use a função super()
#Python também possui uma super()função que fará com que a
#classe filha herde todos os métodos e propriedades de sua classe pai:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()#saida Mike Olsen

#Ao usar a super()função, você não precisa usar o nome do elemento pai,
# ela herdará automaticamente os métodos e propriedades de seu pai.

#adicionar propriedades

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)#saida 2019


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)#saida 2019

#----------------------------------------------------------------------------------------------------
#adicionar metodos
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
#saida Welcome Mike Olsen to the class of 2019

#OBS: Se você adicionar um método na classe filha com o mesmo nome de uma função na classe pai,
# a herança do método pai será substituída.

#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------
