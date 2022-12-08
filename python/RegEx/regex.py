#Um RegEx, ou Expressão Regular, é uma sequência de caracteres que forma um padrão de pesquisa.

#RegEx pode ser usado para verificar se uma string contém o padrão de pesquisa especificado.

#Módulo RegEx
#Python tem um pacote interno chamado re, que pode ser usado para trabalhar com Expressões Regulares.

#Importe o remódulo: import re


#RegEx em Python
#Depois de importar o remódulo, você pode começar a usar expressões regulares:

#Exemplo
#Pesquise a string para ver se ela começa com "The" e termina com "Spain":

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
#saida YES! We have a match!

#----------------------------------------------------------------------------------------------------
#Funções RegEx
#O remódulo oferece um conjunto de funções que nos permite pesquisar 
#uma string em busca de uma correspondência:

#A função findall()
#A findall()função retorna uma lista contendo todas as correspondências.
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)#saida ['ai', 'ai']

#A lista contém as correspondências na ordem em que foram encontradas.
#Se nenhuma correspondência for encontrada, uma lista vazia será retornada:
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
  #saida [] No match
#----------------------------------------------------------------------------------------------------
#A função search()
#A search()função pesquisa a string em busca de uma correspondência e
# retorna um objeto Match se houver uma correspondência.
#Se houver mais de uma correspondência, apenas a primeira ocorrência da
# correspondência será retornada:

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 
#saida The first white-space character is located in position: 3

#Se nenhuma correspondência for encontrada, o valor Noneé retornado:

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)#saida None

#----------------------------------------------------------------------------------------------------
#A função split()
#A split()função retorna uma lista onde a string foi dividida em cada correspondência:

#Exemplo
#Dividir em cada caractere de espaço em branco:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)#saida ['The', 'rain', 'in', 'Spain']

#Você pode controlar o número de ocorrências especificando o maxsplit parâmetro:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)#saida ['The', 'rain in Spain']

#----------------------------------------------------------------------------------------------------
#A função sub()
#A sub()função substitui as correspondências pelo texto de sua escolha:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)#saida The9rain9in9Spain

#Você pode controlar o número de substituições especificando o count parâmetro:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)#saida The9rain9in Spain

#----------------------------------------------------------------------------------------------------
#Metacaracteres
#Metacaracteres são caracteres com um significado especial:
txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)#saida ['h', 'e', 'a', 'i', 'i', 'a', 'i']
#----------------------------------------------------------------------------------------------------
txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)#saida ['5', '9']

#----------------------------------------------------------------------------------------------------
txt = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)#saida ['hello']

#----------------------------------------------------------------------------------------------------
txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
#saida Yes, the string starts with 'hello'

#----------------------------------------------------------------------------------------------------
txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
#saida Yes, the string ends with 'planet'

#----------------------------------------------------------------------------------------------------
txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)
print(x)#saida ['hello']
#----------------------------------------------------------------------------------------------------
txt = "hello planet"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.findall("he.+o", txt)
print(x)#saida ['hello']
#----------------------------------------------------------------------------------------------------
txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt)

print(x)#saida []

#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"


#----------------------------------------------------------------------------------------------------
txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x)#saida ['hello']

#----------------------------------------------------------------------------------------------------
txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  #saida ['falls']
#Yes, there is at least one match!

#----------------------------------------------------------------------------------------------------
#Sequências Especiais
#Uma sequência especial é \seguida por um dos caracteres da lista abaixo e tem um significado especial:
txt = "The rain in Spain"

#Check if the string starts with "The":

x = re.findall("\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")
  #saida ['The']
#Yes, there is a match!
#----------------------------------------------------------------------------------------------------
txt = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  #saida []
#No match


#----------------------------------------------------------------------------------------------------
txt = "The rain in Spain"

#Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  #saida ['ain', 'ain']
#Yes, there is at least one match!


#----------------------------------------------------------------------------------------------------
txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the beginning of a word:

x = re.findall(r"\Bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  
#saida ['ain', 'ain']
#Yes, there is at least one match!


#----------------------------------------------------------------------------------------------------
txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the end of a word:

x = re.findall(r"ain\B", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  
#saida []
#No match


#----------------------------------------------------------------------------------------------------
txt = "The rain in Spain"

#Check if the string contains any digits (numbers from 0-9):

x = re.findall("\d", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#saida []
#No match


#----------------------------------------------------------------------------------------------------
txt = "The rain in Spain"

#Return a match at every no-digit character:

x = re.findall("\D", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#saida ['T', 'h', 'e', ' ', 'r', 'a', 'i', 'n', ' ', 'i', 'n', ' ', 'S', 'p', 'a', 'i', 'n']
#Yes, there is at least one match! 


#----------------------------------------------------------------------------------------------------
txt = "The rain in Spain"

#Return a match at every white-space character:

x = re.findall("\s", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#saida [' ', ' ', ' ']
#Yes, there is at least one match!

#----------------------------------------------------------------------------------------------------
txt = "The rain in Spain"

#Return a match at every NON white-space character:

x = re.findall("\S", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#saida ['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']
#Yes, there is at least one match!

#----------------------------------------------------------------------------------------------------
txt = "The rain in Spain"

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\w", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#saida ['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']
#Yes, there is at least one match!

#----------------------------------------------------------------------------------------------------
txt = "The rain in Spain"

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

x = re.findall("\W", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#saida [' ', ' ', ' ']
#Yes, there is at least one match!


#----------------------------------------------------------------------------------------------------
txt = "The rain in Spain"

#Check if the string ends with "Spain":

x = re.findall("Spain\Z", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")
#saida ['Spain']
#Yes, there is a match!


#----------------------------------------------------------------------------------------------------
#Conjuntos
#Um conjunto é um conjunto de caracteres dentro de um par de colchetes []com um significado especial:

txt = "The rain in Spain"

#Check if the string has any a, r, or n characters:

x = re.findall("[arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#saida ['r', 'a', 'n', 'n', 'a', 'n']
#Yes, there is at least one match!
#----------------------------------------------------------------------------------------------------
txt = "The rain in Spain"

#Check if the string has any characters between a and n:

x = re.findall("[a-n]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#saida ['h', 'e', 'a', 'i', 'n', 'i', 'n', 'a', 'i', 'n']
#Yes, there is at least one match!


#----------------------------------------------------------------------------------------------------
txt = "The rain in Spain"

#Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  #saida ['T', 'h', 'e', ' ', 'i', ' ', 'i', ' ', 'S', 'p', 'i']
#Yes, there is at least one match!


#----------------------------------------------------------------------------------------------------
txt = "The rain in Spain"

#Check if the string has any 0, 1, 2, or 3 digits:

x = re.findall("[0123]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  #saida []
#No match


#----------------------------------------------------------------------------------------------------
txt = "8 times before 11:45 AM"

#Check if the string has any digits:

x = re.findall("[0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  #saida ['8', '1', '1', '4', '5']
#Yes, there is at least one match!

#----------------------------------------------------------------------------------------------------
txt = "8 times before 11:45 AM"

#Check if the string has any two-digit numbers, from 00 to 59:

x = re.findall("[0-5][0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  #saida ['11', '45']
#Yes, there is at least one match!

#----------------------------------------------------------------------------------------------------
txt = "8 times before 11:45 AM"

#Check if the string has any characters from a to z lower case, and A to Z upper case:

x = re.findall("[a-zA-Z]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  #saida ['t', 'i', 'm', 'e', 's', 'b', 'e', 'f', 'o', 'r', 'e', 'A', 'M']
#Yes, there is at least one match!

#----------------------------------------------------------------------------------------------------
txt = "8 times before 11:45 AM"

#Check if the string has any + characters:

x = re.findall("[+]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  #saida []
#No match


#----------------------------------------------------------------------------------------------------
#Objeto correspondente
#Um Match Object é um objeto que contém informações sobre a pesquisa e o resultado.

#Observação: Caso não haja correspondência, Noneserá retornado o valor, 
#no lugar do Objeto de correspondência.
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)
#saida <_sre.SRE_Match object; span=(5, 7), match='ai'>

#O objeto Match possui propriedades e métodos usados ​​para recuperar 
# informações sobre a pesquisa e o resultado:

#.span()retorna uma tupla contendo as posições inicial e final da correspondência.
#.stringretorna a string passada para a função
#.group()retorna a parte da string onde houve uma correspondência

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
#saida (12, 17)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
#saida The rain in Spain

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
#saida Spain

#Observação: Caso não haja correspondência, Noneserá retornado o valor,
# no lugar do Objeto de correspondência.
#----------------------------------------------------------------------------------------------------
