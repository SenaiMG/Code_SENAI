#Condições do Python e instruções If
#Python suporta as condições lógicas usuais da matemática:

#Igual a: a == b
#Diferentes: a != b
#Menor que: a < b
#Menor ou igual a: a <= b
#Maior que: a > b
#Maior ou igual a: a >= b
#Essas condições podem ser usadas de várias maneiras, mais comumente em "instruções if" e loops.

#Uma "instrução if" é escrita usando a palavra-chave if .

a = 33
b = 200

if b > a:
  print("b is greater than a")#saida b is greater than a


#-------------------------------------------------------------------------------
#Python conta com recuo (espaço em branco no início de uma linha)
#para definir o escopo no código. Outras linguagens de programação costumam usar colchetes para essa finalidade.
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error

#-------------------------------------------------------------------------------
#Elif
#A palavra-chave elif é uma maneira pythons de dizer "se as condições anteriores não forem verdadeiras, tente esta condição".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  #saida a and b are equal
#-------------------------------------------------------------------------------
#Senão
#A palavra-chave else captura qualquer coisa que não seja capturada pelas condições anteriores.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  #saida a is greater than b


a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#saida b is not greater than a
#-------------------------------------------------------------------------------
#Mão curta Se
#Se você tiver apenas uma instrução para executar, poderá colocá-la na mesma linha da instrução if.
a = 200
b = 33

if a > b: print("a is greater than b")# saida "a is greater than b"
#-------------------------------------------------------------------------------
#Mão curta Se... Senão
#Se você tiver apenas uma instrução para executar, uma para if e outra para else, você pode colocar tudo na mesma linha:
a = 2
b = 330

print("A") if a > b else print("B")# saida B
#Essa técnica é conhecida como Operadores Ternários ou Expressões Condicionais .
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")# saida =
#-------------------------------------------------------------------------------
# and

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")# saida Both conditions are True

#-------------------------------------------------------------------------------
# OR
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")# saida At least one of the conditions is True

#-------------------------------------------------------------------------------
#Se aninhado
#Você pode ter ifinstruções dentro ifde instruções, isso é chamado de instruções aninhadas if .
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    #saida Above ten,
    #and also above 20!
#-------------------------------------------------------------------------------
#A declaração de passagem
#ifdeclarações não podem ser vazias, mas se você por algum motivo tiver uma if
#declaração sem conteúdo, coloque a passdeclaração para evitar erros.
a = 33
b = 200

if b > a:
  pass

# having an empty if statement like this, would raise an error without the pass statement
#-------------------------------------------------------------------------------
