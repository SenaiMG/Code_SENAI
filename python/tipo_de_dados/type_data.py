#Na programação, o tipo de dados é um conceito importante.
#Variáveis ​​podem armazenar dados de diferentes tipos, e diferentes tipos podem fazer coisas diferentes.
#O Python tem os seguintes tipos de dados integrados por padrão, nestas categorias:
#exemplo de tipos de dados
#Tipo de texto:	str
#Tipos Numéricos:	int, float, complex
#Tipos de sequência:	list, tuple, range
#Tipo de mapeamento:	dict
#Tipos de conjunto:	set,frozenset
#Tipo booleano:	bool
#Tipos binários:	bytes, bytearray, memoryview
#Nenhum Tipo:	NoneType

#para você saber qualquer tipo de dado utilize a função Type()
x = 5
print(type(x))#saida <class 'int'>

#configurando tipos de dados

#tipo str
x = "Hello World"
#display x:
print(x)
#display the data type of x:
print(type(x)) #saida <class 'str'>
#---------------------------------------------------------------------
#tipo int
x = 20
#display x:
print(x)
#display the data type of x:
print(type(x)) #saida <class 'int'>
#------------------------------------------------------------------------
#tipo float
x = 20.5
#display x:
print(x)
#display the data type of x:
print(type(x)) #saida <class 'float'>
#----------------------------------------------------------------------
#tipo complex
x = 1j
#display x:
print(x)
#display the data type of x:
print(type(x)) #saida <class 'complex'>
#-----------------------------------------------------------------------
#tipo lista
x = ["apple", "banana", "cherry"]
#display x:
print(x)
#display the data type of x:
print(type(x)) #saida <class 'list'>
#-----------------------------------------------------------------------
#tipo tupla
x = ("apple", "banana", "cherry")
#display x:
print(x)
#display the data type of x:
print(type(x)) #saida <class 'tuple'>
#-----------------------------------------------------------------------
#tipo range
x = range(6)
#display x:
print(x)# saida range(0, 6)
#display the data type of x:
print(type(x)) #saida <class 'range'>
#----------------------------------------------------------------------
#tipo dict
x = {"name" : "John", "age" : 36}
#display x:
print(x){'name': 'John', 'age': 36}# saida {'name': 'John', 'age': 36}
#display the data type of x:
print(type(x))  #saida <class 'dict'>
#----------------------------------------------------------------------------
#tipo frozenset
x = frozenset({"apple", "banana", "cherry"})
#display x:
print(x) #saida frozenset({'apple', 'banana', 'cherry'})
#display the data type of x:
print(type(x)) #saida <class 'frozenset'>
#-----------------------------------------------------------------------------
#tipo set
x = {"apple", "banana", "cherry"}
#display x:
print(x)
#display the data type of x:
print(type(x)) #saida <class 'set'>
#-----------------------------------------------------------------------------
#tipo booleano
x = True
#display x:
print(x)
#display the data type of x:
print(type(x)) # saida <class 'bool'>
#----------------------------------------------------------------------------
#tipos bytes
x = b"Hello"
#display x:
print(x)
#display the data type of x:
print(type(x)) # saida <class 'bytes'>
#----------------------------------------------------------------------------
#tipo bytearray
x = bytearray(5)
#display x:
print(x) #saida bytearray(b'\x00\x00\x00\x00\x00')
#display the data type of x:
print(type(x)) #saida <class 'bytearray'>
#----------------------------------------------------------------------------
#tipo memoryview
x = memoryview(bytes(5))
#display x:
print(x)# saida <memory at 0x00D58FA0>
#display the data type of x:
print(type(x)) # saida <class 'memoryview'>
#----------------------------------------------------------------------------
# tipo NoneType
x = None
#display x:
print(x)# saida None
#display the data type of x:
print(type(x)) # saida <class 'NoneType'>
#-----------------------------------------------------------------------------
#forçando dados para tipos especificos
#forçando tipo string
#tipo str
x = str("Hello World")
#-------------------------------------------------------------------
#tipo int
x = int(20)
#--------------------------------------------------------------------------
# tipo float
x = float(20.5)
#--------------------------------------------------------------------------
#tipo complex
x = complex(1j)
#----------------------------------------------------------------------------
#tipo list
x = list(("apple", "banana", "cherry"))
#----------------------------------------------------------------------------
#tipo tupla
x = tuple(("apple", "banana", "cherry"))
#----------------------------------------------------------------------------
#tipo range
x = range(6)
#----------------------------------------------------------------------------
#tipo dict
x = dict(name="John", age=36)
#----------------------------------------------------------------------------
#tipo set
x = set(("apple", "banana", "cherry"))
#----------------------------------------------------------------------------
#tipo frozenset
x = frozenset(("apple", "banana", "cherry"))
#----------------------------------------------------------------------------
#tipo booleano
x = bool(5)
#----------------------------------------------------------------------------
#tipo bytes
x = bytes(5)
#----------------------------------------------------------------------------
#tipo bytearray
x = bytearray(5)
#----------------------------------------------------------------------------
#tipo memoryview
x = memoryview(bytes(5))
