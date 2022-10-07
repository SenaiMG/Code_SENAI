#A conversão em python é, portanto, feita usando funções construtoras:

#int() - constrói um número inteiro a partir de um literal inteiro, um literal float (removendo todos os decimais)
#ou um literal de string (desde que a string represente um número inteiro)
#float() - constrói um número float a partir de um literal inteiro, um literal float ou
#um literal de string (desde que a string represente um float ou um inteiro)
#str() - constrói uma string a partir de uma ampla variedade de tipos de dados, incluindo strings, literais inteiros e
#literais float


#exemplo inteiro
x = int(1)
y = int(2.8)
z = int("3")
print(x) #saida 1
print(y) #saida 2
print(z) #saida 3


#exemplo float
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)# saida 1.0
print(y)# saida 2.8
print(z)# saida 3.0
print(w)# saida 4.2


#exemplo str "string"
x = str("s1")
y = str(2)
z = str(3.0)
print(x)# saida s1
print(y)# saida 2
print(z)# saida 3.0
