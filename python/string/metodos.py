#Métodos de string
#Python tem um conjunto de métodos integrados que você pode usar em strings.

#capitalize
#O capitalize()método retorna uma string onde o primeiro caractere é maiúsculo e o restante é minúsculo.
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)#saida  Hello, and welcome to my world.
#outro exemplo
txt = "python is FUN!"
x = txt.capitalize()
print (x)#saida Python is fun!
#se a primeira letra for numero
txt = "36 is my age."
x = txt.capitalize()
print (x)#saida 36 is my age
#---------------------------------------------------------------------------------
#O casefold() método retorna uma string onde todos os caracteres são minúsculos.
#Este método é semelhante ao método, mas o método é mais forte, mais agressivo, o que significa que ele
#converterá mais caracteres em minúsculas e encontrará mais correspondências ao comparar duas strings e
#mbas são convertidas usando o método. lower()casefold()casefold()

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)# saida hello, and welcome to my world!
#--------------------------------------------------------------------------------
#O center()método irá centralizar a string, usando um caractere especificado (o espaço é o padrão)
#como o caractere de preenchimento.
txt = "banana"
x = txt.center(20)
print(x)# saida        banana
#outro exemplo ele utiliza a letra "o" no auto preenchimento
txt = "banana"
x = txt.center(20, "O")
print(x)# saida OOOOOOObananaOOOOOOO
#--------------------------------------------------------------------------------
# O count()método retorna o número de vezes que um valor especificado aparece na string.
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)# saida 2
# para ele pesquisar da posição 10 a 24
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)# saida 1
#--------------------------------------------------------------------------------
#O encode()método codifica a string, usando a codificação especificada. Se nenhuma codificação for especificada, UTF-8 será usado.
txt = "My name is Ståle"
x = txt.encode()
print(x)# saida b'My name is St\xc3\xe5le'
#tipos de erros que podem ser retornados
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))# saida b'My name is St\\xe5le'
print(txt.encode(encoding="ascii",errors="ignore"))# saida b'My name is Stle'
print(txt.encode(encoding="ascii",errors="namereplace"))# saida b'My name is St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
print(txt.encode(encoding="ascii",errors="replace"))# saida b'My name is St?le'
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))# saida b'My name is Ståle'
#---------------------------------------------------------------------------------
# O endswith()método retorna True se a string terminar com o valor especificado, caso contrário, False.
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x) # saida true
#mais exemplo
txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)# saida true
# se a frase termina com my World
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)# saida False
#--------------------------------------------------------------------------------------
#O expandtabs()método define o tamanho da guia para o número especificado de espaços em branco.
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)# saida H e l l o
#outro exemplo
txt = "H\te\tl\tl\to"
print(txt)# saida H	e	l	l	o
print(txt.expandtabs())# saida H       e       l       l       o
print(txt.expandtabs(2))# saida H e l l o
print(txt.expandtabs(4))# saida H   e   l   l   o
print(txt.expandtabs(10))# saida H         e         l         l         o
#----------------------------------------------------------------------------------------
#O find()método encontra a primeira ocorrência do valor especificado.
#O find()método retorna -1 se o valor não for encontrado.
#O find()método é quase o mesmo que o index() método, a única diferença é que o index()
#método gera uma exceção se o valor não for encontrado. (Veja exemplo abaixo)

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)# saida 7
#outro Exemplo
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)# saida 1
#outro Exemplo
txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)# saida 8
# quando ele não encontra retorna o indice -1
txt = "Hello, welcome to my world."
print(txt.find("q")) # saida -1
print(txt.index("q"))
​# saida Traceback (most recent call last):
  #File "demo_ref_string_find_vs_index.py", line 4 in <module>
#    print(txt.index("q"))
#ValueError: substring not found
#------------------------------------------------------------------------------------
#O format()método formata o(s) valor(es) especificado(s) e os insere dentro do espaço reservado da string.
#O espaço reservado é definido usando colchetes: {}. Leia mais sobre os espaços reservados na seção Espaço reservado abaixo.
#O format()método retorna a string formatada.
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))# saida For only 49.00 dollars!
# usando espaços reservados
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)# saida My name is John, I'm 36
print(txt2)# saida My name is John, I'm 36
print(txt3)# saida My name is John, I'm 36

#Tipos de formatação
#Dentro dos espaços reservados você pode adicionar um tipo de formatação para formatar o resultado:

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "<" to left-align the value:
txt = "We have {:<8} chickens."
print(txt.format(49))# saida We have 49       chickens.

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use ">" to right-align the value:
txt = "We have {:>8} chickens."
print(txt.format(49))# saida We have       49 chickens.


#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "^" to center-align the value:
txt = "We have {:^8} chickens."
print(txt.format(49)) # saida We have    49    chickens.

#To demonstrate, we insert the number 8 to specify the available space for the value.
#Use "=" to place the plus/minus sign at the left most position:
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5)) # saida The temperature is -      5 degrees.

#Use "+" to always indicate if the number is positive or negative:
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))# saida The temperature is between -3 and +7 degrees celsius.

#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7)) # saida The temperature is between -3 and 7 degrees celsius.

#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))# saida The temperature is between -3 and  7 degrees celsius.

#Use "," to add a comma as a thousand separator:
txt = "The universe is {:,} years old."
print(txt.format(13800000000))# saida The universe is 13,800,000,000 years old.

#Use "_" to add a underscore character as a thousand separator:
txt = "The universe is {:_} years old."
print(txt.format(13800000000))# saida The universe is 13_800_000_000 years old.

#Use "b" to convert the number into binary format:
txt = "The binary version of {0} is {0:b}"
print(txt.format(5)) # saida The binary version of 5 is 101

#Use "d" to convert a number, in this case a binary number, into decimal number format:
txt = "We have {:d} chickens."
print(txt.format(0b101))# saida We have 5 chickens.

#Use "e" to convert a number into scientific number format (with a lower-case e):
txt = "We have {:e} chickens."
print(txt.format(5)) # saida We have 5.000000e+00 chickens.

#Use "E" to convert a number into scientific number format (with an upper-case E):
txt = "We have {:E} chickens."
print(txt.format(5))#We have 5.000000E+00.

#Use "f" to convert a number into a fixed point number, default with 6 decimals,
#but use a period followed by a number to specify the number of decimals:
txt = "The price is {:.2f} dollars."
print(txt.format(45))# saida The price is 45.00 dollars.
#without the ".2" inside the placeholder, this number will be displayed like this:
txt = "The price is {:f} dollars."
print(txt.format(45))# saida The price is 45.000000 dollars.

#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:
x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x)) # saida The price is INF dollars.
#same example, but with a lower case f:
txt = "The price is {:f} dollars."
print(txt.format(x))# saida The price is inf dollars.

#Use "o" to convert the number into octal format:
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))# saida The octal version of 10 is 12

#Use "x" to convert the number into Hex format:
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))# saida The Hexadecimal version of 255 is ff

#Use "X" to convert the number into upper-case Hex format:
txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255)) # saida The Hexadecimal version of 255 is FF

#Use "%" to convert the number into a percentage format:
txt = "You scored {:%}"
print(txt.format(0.25))# saida You scored 25.000000%
#Or, without any decimals:
txt = "You scored {:.0%}"
print(txt.format(0.25))# saida You scored 25%

#--------------------------------------------------------------------------------
#O index()método encontra a primeira ocorrência do valor especificado.
#O index()método gera uma exceção se o valor não for encontrado.
#O index()método é quase o mesmo que o find() método, a única diferença é que o find()
#método retorna -1 se o valor não for encontrado. (Veja exemplo abaixo)

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)# saida 7

txt = "Hello, welcome to my world."
x = txt.index("e")
print(x)# saida 1

txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)# saida 8

txt = "Hello, welcome to my world."
print(txt.find("q"))# saida -1
print(txt.index("q")) # saida
#Traceback (most recent call last):
 # File "demo_ref_string_find_vs_index.py", line 4 in <module>
#    print(txt.index("q"))
#ValueError: substring not found

#-----------------------------------------------------------------------------------
#O isalnum()método retornará True se todos os caracteres forem alfanuméricos, ou seja,
#letra do alfabeto (az) e números (0-9).
#Exemplo de caracteres que não são alfanuméricos: (espaço)!#%&? etc.

txt = "Company12"
x = txt.isalnum()
print(x)# saida true

txt = "Company 12"
x = txt.isalnum()
print(x)# saida false
#------------------------------------------------------------------------------
#O isalpha()método retornará True se todos os caracteres forem letras do alfabeto (az).
#Exemplo de caracteres que não são letras do alfabeto: (espaço)!#%&? etc.

txt = "CompanyX"
x = txt.isalpha()
print(x)#saida true

txt = "Company10"
x = txt.isalpha()
print(x)# saida false
#-------------------------------------------------------------------------------
#O isdecimal()método retornará True se todos os caracteres forem decimais (0-9).
#Este método é usado em objetos unicode.

txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)# saida True

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal()) #saida true
print(b.isdecimal())# saida False
#-------------------------------------------------------------------------------
#O isdigit()método retorna True se todos os caracteres forem dígitos, caso contrário, False.
#Expoentes, como ², também são considerados um dígito.
txt = "50800"
x = txt.isdigit()
print(x)# saida True

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
print(a.isdigit())# saida True
print(b.isdigit())# saida True
#-------------------------------------------------------------------------------
#O isidentifier()método retorna True se a string for um identificador válido, caso contrário, False.
#Uma string é considerada um identificador válido se contiver apenas letras alfanuméricas (az) e (0-9)
#ou sublinhados (_). Um identificador válido não pode começar com um número nem conter espaços.
txt = "Demo"
x = txt.isidentifier()
print(x)# saida true

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier())# saida true
print(b.isidentifier())# saida true
print(c.isidentifier())# saida false
print(d.isidentifier())# saida false
#----------------------------------------------------------------------------------
#O islower()método retorna True se todos os caracteres estiverem em minúsculas, caso contrário, False.
#Números, símbolos e espaços não são verificados, apenas caracteres alfabéticos.
txt = "hello world!"
x = txt.islower()
print(x)# saida true

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"
print(a.islower())# saida false
print(b.islower())# saida true
print(c.islower())# saida false
#---------------------------------------------------------------------------------
#O isnumeric()método retorna True se todos os caracteres forem numéricos (0-9), caso contrário, False.
#Expoentes, como ² e ¾ também são considerados valores numéricos.
#"-1"e "1.5"NÃO são considerados valores numéricos, pois todos os caracteres na string devem ser numéricos,
#e the -e the .não são.
txt = "565543"
x = txt.isnumeric()
print(x)# saida True

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = "10km2"
d = "-1"
e = "1.5"
print(a.isnumeric())# saida True
print(b.isnumeric())# saida True
print(c.isnumeric())# saida false
print(d.isnumeric())# saida false
print(e.isnumeric())# saida false
#------------------------------------------------------------------------------
#O isprintable()método retorna True se todos os caracteres forem imprimíveis, caso contrário, False.
#Exemplo de nenhum caractere imprimível pode ser retorno de carro e alimentação de linha.
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)# saida True

txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)# saida false
#------------------------------------------------------------------------------
#O isspace()método retorna True se todos os caracteres em uma string forem espaços em branco, caso contrário, False.
txt = "   "
x = txt.isspace()
print(x)# saida True

txt = "   s   "
x = txt.isspace()
print(x)# saida False
#------------------------------------------------------------------------------
#The istitle() method returns True if all words in a text start with a upper case letter,
#AND the rest of the word are lower case letters, otherwise False.
#Symbols and numbers are ignored.
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)# saida True

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"
print(a.istitle())# saida false
print(b.istitle())# saida True
print(c.istitle())# saida True
print(d.istitle())# saida True
#-------------------------------------------------------------------------------
#The isupper() method returns True if all the characters are in upper case, otherwise False.
#Numbers, symbols and spaces are not checked, only alphabet characters.
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)# saida True

a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"
print(a.isupper()) # saida False
print(b.isupper())# saida False
print(c.isupper())# saida True
#---------------------------------------------------------------------------------
#O join()método pega todos os itens em um iterável e os une em uma string.
#Uma string deve ser especificada como separador.
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)# saida John#Peter#Vicky

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)# saida nameTESTcountry
#-------------------------------------------------------------------------------
#O ljust()método alinhará a string à esquerda, usando um caractere especificado
#(o espaço é o padrão) como o caractere de preenchimento.
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")#saida banana              is my favorite fruit.

txt = "banana"
x = txt.ljust(20, "O")
print(x)#saida bananaOOOOOOOOOOOOOO
#-------------------------------------------------------------------------------
#O lower()método retorna uma string onde todos os caracteres são minúsculos.
#Símbolos e números são ignorados.
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)# saida hello my friends
#-------------------------------------------------------------------------------
#O lstrip()método remove quaisquer caracteres iniciais (espaço é o caractere inicial padrão a ser removido)

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")# saida of all fruits banana     is my favorite

txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)# saida banana
#-------------------------------------------------------------------------------
#O maketrans()método retorna uma tabela de mapeamento que pode ser usada com o
#método para substituir caracteres especificados. translate()
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))#saida Hello Pam!

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))# saida Hi Joe!

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))# saida G i Joe!

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(txt.maketrans(x, y, z)) # saida {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
#-------------------------------------------------------------------------------
#O partition()método procura uma string especificada e divide a string em uma tupla contendo três elementos.
#O primeiro elemento contém a parte antes da string especificada.
#O segundo elemento contém a string especificada.
#O terceiro elemento contém a parte após a string.
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)# saida ('I could eat ', 'bananas', ' all day')

txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x)# saida ('I could eat bananas all day', '', '')
#-------------------------------------------------------------------------------
#O replace()método substitui uma frase especificada por outra frase especificada.
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)#saida I like apples

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)# saida three three was a race horse, two two was three too."

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)#saida three three was a race horse, two two was one too."
#--------------------------------------------------------------------------------
#O rfind()método encontra a última ocorrência do valor especificado.
#O rfind()método retorna -1 se o valor não for encontrado.
#O rfind()método é quase o mesmo que o rindex() método. Veja exemplo abaixo.
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)# saida 12

txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(x)# saida 13

txt = "Hello, welcome to my world."
x = txt.rfind("e", 5, 10)
print(x)#saida 8

txt = "Hello, welcome to my world."
print(txt.rfind("q"))# saida -1
print(txt.rindex("q"))# saida Traceback (most recent call last):
  #File "demo_ref_string_rfind_vs_rindex.py", line 4 in <module>
    #print(txt.rindex("q"))
#ValueError: substring not found
#-------------------------------------------------------------------------------
#O rindex()método encontra a última ocorrência do valor especificado.
#O rindex()método gera uma exceção se o valor não for encontrado.
#O rindex()método é quase o mesmo que o rfind() método. Veja exemplo abaixo.
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)# saida 12

txt = "Hello, welcome to my world."
x = txt.rindex("e")
print(x)#saida 13

txt = "Hello, welcome to my world."
x = txt.rindex("e", 5, 10)
print(x)#saida 8

txt = "Hello, welcome to my world."
print(txt.rfind("q"))# saida -1
print(txt.rindex("q"))# saida Traceback (most recent call last):
  #File "demo_ref_string_rfind_vs_rindex.py", line 4 in <module>
    #print(txt.rindex("q"))
#ValueError: substring not found
#-------------------------------------------------------------------------------
#O rjust()método alinhará a string à direita, usando um caractere especificado
#(o espaço é o padrão) como o caractere de preenchimento.
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")# saida               banana is my favorite fruit.

txt = "banana"
x = txt.rjust(20, "O")
print(x)# saida OOOOOOOOOOOOOObanana
#-------------------------------------------------------------------------------
#O rpartition()método procura a última ocorrência de uma string especificada e divide
#a string em uma tupla contendo três elementos.
#O primeiro elemento contém a parte antes da string especificada.
#O segundo elemento contém a string especificada.
#O terceiro elemento contém a parte após a string.
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)# saida ('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("apples")
print(x)# saida ('', '', 'I could eat bananas all day, bananas are my favorite fruit')

#-------------------------------------------------------------------------------
#O rsplit()método divide uma string em uma lista, começando pela direita.
#Se nenhum "max" for especificado, este método retornará o mesmo que o split() método.

txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)#saida ['apple', 'banana', 'cherry']

txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x)# saida ['apple, banana', 'cherry']
# note that the result has only 2 elements "apple, banana" is the first element, and "cherry" is the last.
#--------------------------------------------------------------------------------
#O rstrip()método remove quaisquer caracteres finais (caracteres no final de uma string),
# espaço é o caractere final padrão a ser removido.
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")# saida of all fruits     banana is my favorite

txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)# saida banana
#-------------------------------------------------------------------------------
#O split()método divide uma string em uma lista.
#Você pode especificar o separador, o separador padrão é qualquer espaço em branco.
txt = "welcome to the jungle"
x = txt.split()
print(x)# saida ['welcome', 'to', 'the', 'jungle']

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)# saida ['hello', 'my name is Peter', 'I am 26 years old']

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)# saida ['apple', 'banana', 'cherry', 'orange']

txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)# saida ['apple', 'banana#cherry#orange']
#-------------------------------------------------------------------------------
#O splitlines()método divide uma string em uma lista. A divisão é feita em quebras de linha.
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)# saida ['Thank you for the music', 'Welcome to the jungle']

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines(True)
print(x)# saida ['Thank you for the music\n', 'Welcome to the jungle']
#-------------------------------------------------------------------------------
#O startswith()método retorna True se a string começar com o valor especificado, caso contrário, False.
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)# saida True

txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)# saida true
#-------------------------------------------------------------------------------
#O strip()método remove quaisquer caracteres iniciais (espaços no início) e finais
#(espaços no final) (o espaço é o caractere inicial padrão a ser removido)
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")# saida of all fruits banana is my favorite

txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)# saida banana
#-------------------------------------------------------------------------------
#O swapcase()método retorna uma string onde todas as letras maiúsculas são minúsculas e vice-versa.
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)#saida hELLO mY nAME iS peter
#-------------------------------------------------------------------------------
#O title()método retorna uma string onde o primeiro caractere em cada palavra é maiúsculo.
#Como um cabeçalho, ou um título.
#Se a palavra contiver um número ou um símbolo, a primeira letra a seguir será convertida em maiúscula.
txt = "Welcome to my world"
x = txt.title()
print(x)# saida Welcome To My World

txt = "Welcome to my 2nd world"
x = txt.title()
print(x)# saida Welcome To My 2Nd World

txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x)# saida Hello B2B2B2 And 3G3G3G
#-------------------------------------------------------------------------------
#O translate()método retorna uma string onde alguns caracteres especificados são
#substituídos pelo caractere descrito em um dicionário ou em uma tabela de mapeamento.
#Use o maketrans()método para criar uma tabela de mapeamento.
#Se um caractere não for especificado no dicionário/tabela, o caractere não será substituído.
#Se você usar um dicionário, deverá usar códigos ASCII em vez de caracteres.

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))# saida  Hello Pam!

txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))# saida Hello Pam!

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))# saida Hi Joe!

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))# saida  G i Joe!

txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))# saida G i Joe!
#-------------------------------------------------------------------------------
#O upper()método retorna uma string onde todos os caracteres estão em maiúsculas.
#Símbolos e números são ignorados.

txt = "Hello my friends"
x = txt.upper()
print(x)# saida HELLO MY FRIENDS
#-------------------------------------------------------------------------------
#O zfill()método adiciona zeros (0) no início da string, até atingir o comprimento especificado.
#Se o valor do parâmetro len for menor que o comprimento da string, nenhum preenchimento será feito.

txt = "50"
x = txt.zfill(10)
print(x)# saida 0000000050

a = "hello"
b = "welcome to the jungle"
c = "10.000"
print(a.zfill(10))#saida 00000hello
print(b.zfill(10))# saida welcome to the jungle
print(c.zfill(10))# saida 000010.000
