#Formato de string
#Como aprendemos no capítulo Variáveis ​​do Python, não podemos combinar strings e números assim:
# Exemplo que vai retorna erro:
age = 36
txt = "My name is John, I am " + age
print(txt) #saida Traceback (most recent call last):
  #File "demo_string_format_error.py", line 2, in <module>
    #txt = "My name is John, I am " + age
#TypeError: must be str, not int

#Mas podemos combinar strings e números usando o format()método!
#O format()método pega os argumentos passados, os formata e os coloca na string onde {}estão os espaços reservados:

#Use o format()método para inserir números em strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))# saida My name is John, and I am 36

#O método format() recebe um número ilimitado de argumentos e são colocados nos respectivos espaços reservados:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) # saida I want 3 pieces of item 567 for 49.95 dollars.

#Você pode usar números de índice {0}para garantir que os argumentos sejam colocados nos espaços reservados corretos:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))# saida I want to pay 49.95 dollars for 3 pieces of item 567
