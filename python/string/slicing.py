#Fatiamento
#Você pode retornar um intervalo de caracteres usando a sintaxe de fatia.
#Especifique o índice inicial e o índice final, separados por dois pontos, para retornar uma parte da string.
b = "Hello, World!"
print(b[2:5])#saida llo
# quando você não passa  inicio ele começa na primeira posição
print(b[:5]) #saida Hello
# quando você não especifica o final ele vai até a ultima posição
b = "Hello, World!"
print(b[2:]) #saida llo, World!
# em casos de indice negativo ele vai começar do ultimo
#Use índices negativos para iniciar a fatia a partir do final da string:
b = "Hello, World!"
print(b[-5:-2])# saida orl
