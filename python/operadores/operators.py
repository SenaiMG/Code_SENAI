print(10 + 5)#saida 15

#Python divide os operadores nos seguintes grupos:
#Operadores aritméticos
#Operadores de atribuição
#Operadores de comparação
#Operadores lógicos
#Operadores de identidade
#Operadores de associação
#Operadores bit a bit



#Operadores aritméticos Python

#adição
x = 5
y = 3
print(x + y)#saida 8
#------------------------------------------------------------------------------
#subtração
x = 5
y = 3
print(x - y)# saida 2
#------------------------------------------------------------------------------
#mutiplicação
x = 5
y = 3
print(x * y) # saida 15
#------------------------------------------------------------------------------
#divião
x = 12
y = 3
print(x / y)# saida 4
#------------------------------------------------------------------------------
#modulo resto da divisão
x = 5
y = 2
print(x % y)# saida 1
#------------------------------------------------------------------------------
#exponenciação
x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2
#saida 32
#------------------------------------------------------------------------------
#divisão por piso arredonda o valor para o numero inteiro mais próximo
x = 15
y = 2
print(x // y)# saida 7
#the floor division // rounds the result down to the nearest whole number
#------------------------------------------------------------------------------





#Operadores de atribuição



x = 5
print(x)# saida 5
#------------------------------------------------------------------------------
x = 5
x += 3
print(x)# saida 8
#------------------------------------------------------------------------------
x = 5
x -= 3
print(x)#saida 2
#------------------------------------------------------------------------------
x = 5
x *= 3
print(x)# saida 15
#------------------------------------------------------------------------------
x = 5
x /= 3
print(x)# saida 1.6666666666666667
#------------------------------------------------------------------------------
x = 5
x%=3
print(x)# saida 2
#------------------------------------------------------------------------------
x = 5
x//=3
print(x)# saida 1
#------------------------------------------------------------------------------
x = 5
x **= 3
print(x)# saida 125
#------------------------------------------------------------------------------
x = 5
x &= 3
print(x)#saida 1
#------------------------------------------------------------------------------
x = 5
x |= 3
print(x)# saida 7
#------------------------------------------------------------------------------
x = 5
x ^= 3
print(x)# saida 6
#------------------------------------------------------------------------------
x = 5
x >>= 3
print(x)#saida 0
#------------------------------------------------------------------------------
x = 5
x <<= 3
print(x)# saida 40
#------------------------------------------------------------------------------




#Operadores de comparação Python

x = 5
y = 3
print(x == y)#saida false
# returns False because 5 is not equal to 3
#------------------------------------------------------------------------------
x = 5
y = 3
print(x != y)# saida True
# returns True because 5 is not equal to 3
#------------------------------------------------------------------------------
x = 5
y = 3
print(x > y)#saida True
# returns True because 5 is greater than 3
#------------------------------------------------------------------------------
x = 5
y = 3
print(x < y)# saida false
# returns False because 5 is not less than 3
#------------------------------------------------------------------------------
x = 5
y = 3
print(x >= y)# saida true
# returns True because five is greater, or equal, to 3
#------------------------------------------------------------------------------
x = 5
y = 3
print(x <= y)# saida false
# returns False because 5 is neither less than or equal to 3
#------------------------------------------------------------------------------




#Operadores lógicos Python

x = 5
print(x > 3 and x < 10)#saida true
# returns True because 5 is greater than 3 AND 5 is less than 10
#------------------------------------------------------------------------------
x = 5
print(x > 3 or x < 4)# saida true
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
#------------------------------------------------------------------------------
x = 5
print(not(x > 3 and x < 10))# saida false
# returns False because not is used to reverse the result
#------------------------------------------------------------------------------




#Operadores de identidade Python
#Os operadores de identidade são usados ​​para comparar os objetos,
#não se forem iguais, mas se forem realmente o mesmo objeto, com a mesma localização de memória:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)# saida true
# returns True because z is the same object as x
print(x is y)# saida false
# returns False because x is not the same object as y, even if they have the same content
print(x == y)# saida true
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
#------------------------------------------------------------------------------
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)# saida false
# returns False because z is the same object as x
print(x is not y)# saida True
# returns True because x is not the same object as y, even if they have the same content
print(x != y)# saida false
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
#------------------------------------------------------------------------------



#Operadores de associação Python
#Os operadores de associação são usados ​​para testar se uma sequência é apresentada em um objeto:

x = ["apple", "banana"]
print("banana" in x)#saida true
# returns True because a sequence with the value "banana" is in the list
#------------------------------------------------------------------------------
x = ["apple", "banana"]
print("pineapple" not in x)# saida true
# returns True because a sequence with the value "pineapple" is not in the list
#------------------------------------------------------------------------------


#Operadores Bitwise Python
#Operadores bit a bit são usados ​​para comparar números (binários):

#              & 	AND     	Sets each bit to 1 if both bits are 1
#              |	OR	        Sets each bit to 1 if one of two bits is 1
#              ^	XOR	        Sets each bit to 1 if only one of two bits is 1
#              ~ 	NOT	        Inverts all the bits
#             <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
#             >>	Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
#------------------------------------------------------------------------------
