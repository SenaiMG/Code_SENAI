#Caractere de Fuga
#Para inserir caracteres ilegais em uma string, use um caractere de escape.
#Um caractere de escape é uma barra invertida \seguida pelo caractere que você deseja inserir.
#Um exemplo de um caractere ilegal é uma aspa dupla dentro de uma string que é cercada por aspas duplas:
#Exemplo de erro:
txt = "We are the so-called "Vikings" from the north."
#saida   File "demo_string_escape_error.py", line 1
    #txt = "We are the so-called "Vikings" from the north."
    #                                   ^
#SyntaxError: invalid syntax

#Para corrigir esse problema, use o caractere de escape \":
txt = "We are the so-called \"Vikings\" from the north."
print(txt) # saida We are the so-called "Vikings" from the north.

#Exemplos de escapes

#citação única
txt = 'It\'s alright.'
print(txt) #saida It's alright.

# Barra invertida
txt = "This will insert one \\ (backslash)."
print(txt) # saida This will insert one \ (backslash).

#Nova Linha
txt = "Hello\nWorld!"
print(txt)
#saida Hello
#World

#Devolução de carro
txt = "Hello\rWorld!"
print(txt) #saida Hello
#World!

#tab
txt = "Hello\tWorld!"
print(txt)# saida Hello   World!

#Retrocesso
txt = "Hello \bWorld!"
print(txt) # saida HelloWorld!

#valor octal
txt = "\110\145\154\154\157"
print(txt)# saida Hello

#valor hexadecimal
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) #saida Hello
