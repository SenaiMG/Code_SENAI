#Strings em python são cercadas por aspas simples ou aspas duplas.
#'olá' é o mesmo que "olá" .
#Você pode exibir um literal de string com a print()função:
print("Hello")#saida Hello
print('Hello')#saida Hello
#outra forma atribuindo a uma variavel
a = "Hello"
print(a)#saida Hello
#você pode atribuir uma string a mais de uma linha usando 3 aspas duplas
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#você pode atribuir uma string a mais de uma linha usando 3 aspas simples
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings são Arrays
#Como muitas outras linguagens de programação populares, strings em Python são arrays de bytes
#que representam caracteres unicode.
#No entanto, o Python não possui um tipo de dados de caractere, um único caractere é simplesmente uma string
#com um comprimento de 1.
#Colchetes podem ser usados ​​para acessar elementos da string.
a = "Hello, World!"
print(a[1])#saida e

#fazendo um loop com a string
for x in "banana":
  print(x)
#saida
#b
#a
#n
#a
#n
#a


#para verificar um comprimento da string utilizamos a função len()
a = "Hello, World!"
print(len(a))#saida 13


#Para verificar se uma determinada frase ou caractere está presente em uma string, podemos usar a palavra-chave in.
txt = "The best things in life are free!"
print("free" in txt)# saida true

#uso do if em uma string
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")# saida Yes, 'free' is present.


#Para verificar se uma determinada frase ou caractere NÃO está presente em uma string, podemos usar a palavra-chave not in.
txt = "The best things in life are free!"
print("expensive" not in txt)#saida true

#uso do not in no if
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")#saida No, 'expensive' is NOT present.
