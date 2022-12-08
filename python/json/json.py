#JSON é uma sintaxe para armazenar e trocar dados.

#JSON é texto, escrito com notação de objeto JavaScript.

#JSON em Python
#O Python possui um pacote interno chamado json, 
#que pode ser usado para trabalhar com dados JSON.

#Exemplo
#Importe o módulo json: import json


#Analisar JSON - Converter de JSON para Python
#Se você tiver uma string JSON, poderá analisá-la usando o json.loads() método.

#OBS:  O resultado será um dicionário Python .


import json

x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["age"])#saida 30 


#---------------------------------------------------------------------------------------------------
#Converter de Python para JSON
#Se você tiver um objeto Python, poderá convertê-lo em uma string JSON usando o json.dumps()método.


x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)#saida {"name": "John", "age": 30, "city": "New York"}

#---------------------------------------------------------------------------------------------------
#Você pode converter objetos Python dos seguintes tipos em strings JSON:

#ditado
#Lista
#tupla
#corda
#int
#flutuador
#Verdadeiro
#Falso
#Nenhum

print(json.dumps({"name": "John", "age": 30}))#saida  {"name": "John", "age": 30}
print(json.dumps(["apple", "bananas"]))#saida  ["apple", "bananas"]
print(json.dumps(("apple", "bananas")))#saida  ["apple", "bananas"]
print(json.dumps("hello"))#saida  "hello"
print(json.dumps(42))#saida  42
print(json.dumps(31.76))#saida 31.76 
print(json.dumps(True))#saida  true
print(json.dumps(False))#saida  false
print(json.dumps(None))#saida  null

#---------------------------------------------------------------------------------------------------
#Quando você converte de Python para JSON, os objetos Python são 
# convertidos no equivalente JSON (JavaScript):

#Python	 = JSON
#dict	= Object
#list	= Array
#tuple	= Array
#str	= String
#int	= Number
#float	= Number
#True	= true
#False	= false
#None	= null

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
#saida {"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann","Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}

#---------------------------------------------------------------------------------------------------
#Formatar o resultado
#O exemplo acima imprime uma string JSON, mas não é muito fácil de ler, sem recuos e quebras de linha.

#O json.dumps()método possui parâmetros para facilitar a leitura do resultado:
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# Use o indent parâmetro para definir os números de recuos:
print(json.dumps(x, indent=4))
#saida {
#    "name": "John",
#    "age": 30,
#    "married": true,
#    "divorced": false,
#    "children": [
#        "Ann",
#        "Billy"
#    ],
#    "pets": null,
#    "cars": [
#        {
#            "model": "BMW 230",
#            "mpg": 27.5
#        },
#        {
#            "model": "Ford Edge",
#           "mpg": 24.1
#        }
#    ]
#}


#---------------------------------------------------------------------------------------------------
#Você também pode definir os separadores, o valor padrão é (", ", ": "), 
# o que significa usar uma vírgula e um espaço para separar cada objeto, 
# e dois pontos e um espaço para separar as chaves dos valores:


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))
#saida {
#    "name" = "John".
#   "age" = 30.
#    "married" = true.
#    "divorced" = false.
#    "children" = [
#        "Ann".
#        "Billy"
#    ].
#    "pets" = null.
#    "cars" = [
#        {
#            "model" = "BMW 230".
#            "mpg" = 27.5
#        }.
#        {
#            "model" = "Ford Edge".
#            "mpg" = 24.1
#        }
#    ]
#}

#---------------------------------------------------------------------------------------------------
#Ordene o resultado
#O json.dumps()método possui parâmetros para ordenar as chaves no resultado:
#Use o sort_keysparâmetro para especificar se o resultado deve ser classificado ou não:

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))

#saida {
#    "age": 30,
#    "cars": [
#        {
#           "model": "BMW 230",
#            "mpg": 27.5
#        },
#        {
#           "model": "Ford Edge",
#           "mpg": 24.1
#        }
#    ],
#    "children": [
#        "Ann",
#        "Billy"
#    ],
#    "divorced": false,
#    "married": true,
#    "name": "John",
#    "pets": null
#}

#---------------------------------------------------------------------------------------------------
