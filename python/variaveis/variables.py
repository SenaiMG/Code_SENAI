x = 5
y = "John"
print(x)
print(y)
#------------------------------------
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
#-----------------------------
# se você deseja força o tipo da variavel
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#----------------------------------------
# para você saber sobre o tipo da variavel só utilizar a função type
x = 5
y = "John"
print(type(x))
print(type(y))
#-----------------------------------------------------------
#aspas duplas ou simples são reconhecidas como string
x = "John"
# is the same as
x = 'John'
print(x)
#-------------------------------------------------------------
#python é case sensitive ele diferencia letras maiúsculas de minúsculas
a = 4
A = "Sally"
print(a)
print(A)
#A will not overwrite a
#------------------------------------------------------------------------
#nomes de variaveis e regras


#Uma variável pode ter um nome curto (como x e y) ou um nome mais descritivo (age, carname, total_volume). Regras para variáveis ​​Python:
#Um nome de variável deve começar com uma letra ou o caractere sublinhado
#Um nome de variável não pode começar com um número
#Um nome de variável pode conter apenas caracteres alfanuméricos e sublinhados (Az, 0-9 e _ )
#Os nomes das variáveis ​​diferenciam maiúsculas de minúsculas (idade, idade e IDADE são três variáveis ​​diferentes)

#nomes permitidos exemplos:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


#nomes não permitidos exemplos:
#2myvar = "John"
#my-var = "John"
#my var = "John"
#----------------------------------------------------------------------------
#multiplas atribuições

x, y, z = "Orange", "Banana", "Cherry"
print(x)# saida orange
print(y)# saida banana
print(z)# saida cherry
#-----------------------------------------------------------------------
# atribuição mutiplas do mesmo valor
x = y = z = "Orange"
print(x)# saida Orange
print(y)# saida Orange
print(z)# saida Orange
#--------------------------------------------------------------------------
#descompatar uma lista ou uma tupla em outras linguagens conhecidas como arrays

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)#saida apple
print(y)# saida banana
print(z)#saida cherry

#------------------------------------------------------------------------
#variaveis de saida é a função print
x = "Python is awesome"
print(x)
#saida Python is awesome
x = "Python"
y = "is"
z = "awesome"
#ele irá fazer a concatenação e juntar as frases
print(x, y, z)
# saida Python is awesome
x = "Python "
y = "is "
z = "awesome"
#pode se usar o + para concatenação
print(x + y + z)
# saida Python is awesome
#já se for numeros ele terá o efeito matemático e efetuara a soma
x = 5
y = 10
print(x + y)
#saida 15
#ele não suporta fazer a mesclagem de uma frase com numero trazendo um erro na tela
x = 5
y = "John"
print(x + y)
# saida TypeError: unsupported operand type(s) for +: 'int' and 'str'
# em caso de junção de string e numeros utilize a virgula
x = 5
y = "John"
print(x, y)
# saida 5 John
#--------------------------------------------------------------------------
#variaveis globais
#Variáveis ​​criadas fora de uma função (como em todos os exemplos acima) são conhecidas como variáveis ​​globais.
#As variáveis ​​globais podem ser usadas por todos, tanto dentro das funções quanto fora delas.
x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()

#exemplo de utilização de variaveis globais e locais com mesmo nomes
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
  #saida Python is fantastic
myfunc()
print("Python is " + x)
# saida Python is awesome

#Normalmente, quando você cria uma variável dentro de uma função, essa variável é local e só pode ser usada dentro dessa função.
#Para criar uma variável global dentro de uma função, você pode usar a palavra- globalchave.
#exemplo
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
# saida Python is fantastic

x = "awesome"# variavel com escopo global
def myfunc():
  global x # foi definida que a variavel local será global e vai sobrescrever a outra variavel
  x = "fantastic"

myfunc()

print("Python is " + x)
#saida Python is fantastic
