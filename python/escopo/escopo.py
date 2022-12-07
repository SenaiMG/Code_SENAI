#Uma variável só está disponível dentro da região em que é criada. Isso é chamado de escopo .
#Escopo Local
#Uma variável criada dentro de uma função pertence ao escopo local dessa função e só pode 
# ser usada dentro dessa função.
def myfunc():
  x = 300
  print(x)

myfunc()
#saida 300

#----------------------------------------------------------------------------------------------------
#Função dentro da função
#Conforme explicado no exemplo acima, a variável xnão está disponível fora da função,
#mas está disponível para qualquer função dentro da função:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()#300

#----------------------------------------------------------------------------------------------------
#Âmbito global
#Uma variável criada no corpo principal do código Python é uma variável global e 
# pertence ao escopo global.
#As variáveis ​​globais estão disponíveis em qualquer escopo, global e local.
x = 300

def myfunc():
  print(x)

myfunc()#saida 300

print(x)#saida 300

#----------------------------------------------------------------------------------------------------
#Nomeando Variáveis
#Se você operar com o mesmo nome de variável dentro e fora de uma função, 
#o Python as tratará como duas variáveis ​​separadas, uma disponível no 
#escopo global (fora da função) e outra disponível no escopo local (dentro da função):
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()#saida 200

print(x)#saida 300
#----------------------------------------------------------------------------------------------------
#Palavra-chave global
#Se você precisar criar uma variável global, mas estiver preso no escopo local, 
#poderá usar a palavra- globalchave.
#A palavra- globalchave torna a variável global.
def myfunc():
  global x
  x = 300

myfunc()

print(x)#saida 300

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)#saida 200

#----------------------------------------------------------------------------------------------------