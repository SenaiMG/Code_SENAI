#O try bloco permite que você teste um bloco de código em busca de erros.

#O except bloco permite lidar com o erro.

#O else bloco permite executar o código quando não há erro.

#O finally bloco permite que você execute o código, 
# independentemente do resultado dos blocos try e except.

#Manipulação de exceção
#Quando ocorre um erro, ou exceção, como chamamos, o 
# Python normalmente para e gera uma mensagem de erro.

#Essas exceções podem ser tratadas usando a tryinstrução:

#O try bloco irá gerar uma exceção, pois xnão está definido:
try:
  print(x)
except:
  print("An exception occurred")#saida An exception occurred
  
#Como o bloco try gera um erro, o bloco except será executado.

#Sem o bloco try, o programa falhará e gerará um erro:
print(x)
#saida  Traceback (most recent call last):
#  File "demo_try_except_error.py", line 3, in <module>
#    print(x)
#NameError: name 'x' is not defined


#----------------------------------------------------------------------------------------------
#Muitas Exceções
#Você pode definir quantos blocos de exceção quiser, por exemplo, 
# se quiser executar um bloco de código especial para um tipo especial de erro:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
#saida Variable x is not defined

#----------------------------------------------------------------------------------------------
#Senão
#Você pode usar a else palavra-chave para definir um bloco de código a
# ser executado se nenhum erro for gerado:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
#saida Hello
#Nothing went wrong

#----------------------------------------------------------------------------------------------
#Finalmente
#O finally bloco, se especificado, será executado independentemente se o 
# bloco try gerar um erro ou não.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
#saida Something went wrong
#The 'try except' is finished

#OBS:Isso pode ser útil para fechar objetos e limpar recursos:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  
  #saida Something went wrong when writing to the file
#----------------------------------------------------------------------------------------------
#Levantar uma exceção
#Como desenvolvedor Python, você pode optar por lançar uma exceção se ocorrer uma condição.

#Para lançar (ou gerar) uma exceção, use a palavra- raise chave.

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
#saida Traceback (most recent call last):
#  File "demo_ref_keyword_raise.py", line 4, in <module>
#    raise Exception("Sorry, no numbers below zero")
#Exception: Sorry, no numbers below zero

#A raise palavra-chave é usada para gerar uma exceção.
#Você pode definir que tipo de erro gerar e o texto a ser impresso para o usuário.
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
#saida Traceback (most recent call last):
#  File "demo_ref_keyword_raise2.py", line 4, in <module>
#    raise TypeError("Only integers are allowed")
#TypeError: Only integers are allowed
#----------------------------------------------------------------------------------------------
