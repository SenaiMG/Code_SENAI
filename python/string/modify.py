#Python tem um conjunto de métodos integrados que você pode usar em strings.
#Maiúsculas
#O upper()método retorna a string em maiúsculas:
a = "Hello, World!"
print(a.upper())# saida HELLO, WORLD!

#Minúsculas
#O lower()método retorna a string em letras minúsculas:
a = "Hello, World!"
print(a.lower())#saida hello, world!

#Remover espaço em branco
#O strip()método remove qualquer espaço em branco do início ou do fim:
a = " Hello, World! "
print(a.strip())# saida Hello, World!

#Substituir Cadeia de caractere
#O replace()método substitui uma string por outra string:
a = "Hello, World!"
print(a.replace("H", "J"))#saida Jello, World!


#Sequência dividida
#O split()método retorna uma lista onde o texto entre o separador especificado se torna os itens da lista.
#O split()método divide a string em substrings se encontrar instâncias do separador:
a = "Hello, World!"
b = a.split(",")
print(b)# saida ['Hello', ' World!']
