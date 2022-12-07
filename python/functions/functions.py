#Em Python, uma função é definida usando a palavra-chave def :
def my_function():
  print("Hello from a function")
  
  
def my_function1():
  print("Hello from a function")

my_function1()

#-------------------------------------------------------------------------------
#Argumentos
#As informações podem ser passadas para funções como argumentos.
#Os argumentos são especificados após o nome da função, dentro dos parênteses. 
#Você pode adicionar quantos argumentos quiser, basta separá-los com uma vírgula.
#O exemplo a seguir tem uma função com um argumento (fname). 
#Quando a função é chamada, passamos um primeiro nome, que é usado dentro da função para 
#imprimir o nome completo:


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
#saida Emil Refsnes
#Tobias Refsnes
#Linus Refsnes


#OBS : Os argumentos geralmente são abreviados para args nas documentações do Python.

#-------------------------------------------------------------------------------
#Parâmetros ou Argumentos?
#Os termos parâmetro e argumento podem ser usados ​​para a mesma coisa: 
#    informações que são passadas para uma função.

#Do ponto de vista de uma função:

#Um parâmetro é a variável listada entre parênteses na definição da função.
#Um argumento é o valor que é enviado para a função quando ela é chamada.

#Número de argumentos
#Por padrão, uma função deve ser chamada com o número correto de argumentos.
#O que significa que, se sua função espera 2 argumentos, você deve chamar a função com 2 argumentos,
#nem mais nem menos.
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
#saida Emil Refsnes


#exemplo de erro

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
#saida Traceback (most recent call last):
  #File "demo_function_args_error.py", line 4, in <module>
 #   my_function("Emil")
#TypeError: my_function() missing 1 required positional argument: 'lname'

#-------------------------------------------------------------------------------
#Argumentos arbitrários, *args
#Se você não souber quantos argumentos serão passados ​​para sua função, 
# adicione um *antes do nome do parâmetro na definição da função.

#Desta forma a função receberá uma tupla de argumentos, podendo acessar os itens de acordo:


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#saida The youngest child is Linus

#OBS: Os argumentos arbitrários geralmente são abreviados para *args nas documentações do Python.

#Argumentos de palavras-chave
#Você também pode enviar argumentos com a sintaxe chave = valor .

#Desta forma, a ordem dos argumentos não importa.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#saida The youngest child is Linus

#OBS: A frase Keyword Arguments é frequentemente abreviada para kwargs nas documentações do Python.


#-------------------------------------------------------------------------------
#Argumentos arbitrários de palavras-chave, **kwargs
#Se você não souber quantos argumentos de palavra-chave serão passados ​​para sua função, 
#adicione dois asteriscos: **antes do nome do parâmetro na definição da função.

#Desta forma a função receberá um dicionário de argumentos, podendo acessar os itens de acordo:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
#saida His last name is Refsnes

#OBS: Argumentos Kword arbitrários são frequentemente abreviados para **kwargs nas documentações do Python.


#-------------------------------------------------------------------------------
#Valor do parâmetro padrão
#O exemplo a seguir mostra como usar um valor de parâmetro padrão.

#Se chamarmos a função sem argumento, ela usará o valor padrão:
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden") #saida I am from Sweden
my_function("India")# saida I am from India
my_function()#saida I am from Norway
my_function("Brazil")#saida I am from Brazil

#-------------------------------------------------------------------------------
#Passando uma lista como um argumento
#Você pode enviar quaisquer tipos de dados de argumento para 
# uma função (string, número, lista, dicionário etc.) e eles serão tratados
# como o mesmo tipo de dados dentro da função.

#Por exemplo, se você enviar uma lista como argumento, ainda será uma lista quando chegar à função:

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#saida apple
#banana
#cherry

#-------------------------------------------------------------------------------
#Valores de retorno
#Para permitir que uma função retorne um valor, use a return instrução:
def my_function(x):
  return 5 * x

print(my_function(3))#saida 15
print(my_function(5))#saida 25
print(my_function(9))#saida 45
#-------------------------------------------------------------------------------
#A declaração de passagem
#functionas definições não podem estar vazias, mas se por algum motivo 
#você tiver uma functiondefinição sem conteúdo, coloque a passinstrução para evitar erros.
def myfunction():
  pass

# OBS: ter uma definição de função vazia como esta geraria um erro sem a instrução pass

#-------------------------------------------------------------------------------
#Recursão
#Python também aceita recursão de função, o que significa que uma função definida
#pode chamar a si mesma.
#
#A recursão é um conceito matemático e de programação comum. 
# Isso significa que uma função chama a si mesma. 
# Isso tem a vantagem de significar que você pode percorrer os dados para chegar a um resultado.
#O desenvolvedor deve ter muito cuidado com a recursão, pois pode ser muito fácil escrever
# uma função que nunca termina ou uma que usa quantidades excessivas de memória 
# ou poder do processador. No entanto, quando escrita corretamente, 
# a recursão pode ser uma abordagem de programação muito eficiente e matematicamente elegante.
#Neste exemplo, tri_recursion() é uma função que definimos para chamar a si mesma ("recurse").
# Usamos a variável k como dados, que decrementa ( -1 ) toda vez que recursamos.
# A recursão termina quando a condição não é maior que 0 (ou seja, quando é 0).
#Para um novo desenvolvedor, pode levar algum tempo para descobrir exatamente como 
# isso funciona, a melhor maneira de descobrir é testando e modificando-o.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Exemplo")
tri_recursion(6)
#saida Recursion Exemplo
#1
#3
#6
#10
#15
#21



#-------------------------------------------------------------------------------
