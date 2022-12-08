#Datas do Python
#Uma data em Python não é um tipo de dados próprio,
#mas podemos importar um módulo nomeado datetimepara trabalhar com datas como objetos de data.


import datetime

x = datetime.datetime.now()

print(x)#saida 2022-12-08 14:40:42.785520

#Saída de Data
#Ao executarmos o código do exemplo acima o resultado será:

#2022-12-08 14:38:49.832069
#A data contém ano, mês, dia, hora, minuto, segundo e microssegundo.

#O datetimemódulo possui vários métodos para retornar informações sobre o objeto de data.

#Aqui estão alguns exemplos, você aprenderá mais sobre eles mais adiante neste capítulo:


x = datetime.datetime.now()

print(x.year)#saida 2022
print(x.strftime("%A"))#saida Thursday



#--------------------------------------------------------------------------------------
#Criando Objetos de Data
#Para criar uma data, podemos usar a datetime()classe (construtor) do datetimemódulo.

#A datetime()classe requer três parâmetros para criar uma data: ano, mês, dia.

x = datetime.datetime(2020, 5, 17)

print(x)#saida 2020-05-17 00:00:00

#A datetime()classe também aceita parâmetros de hora e fuso horário 
# (hora, minuto, segundo, microssegundo, tzone), mas eles são opcionais e 
# têm um valor padrão de 0, ( Nonepara fuso horário).



#--------------------------------------------------------------------------------------
#O método strftime()
#O datetimeobjeto tem um método para formatar objetos de data em strings legíveis.

#O método é chamado strftime()e recebe um parâmetro, format, 
#para especificar o formato da string retornada:
x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))#saida june

#--------------------------------------------------------------------------------------
#Uma referência de todos os códigos de formato legal:

x = datetime.datetime.now()

print(x.strftime("%a"))
#saida Thu


#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%A"))
#saida Thursday

#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%w"))#saida 4

#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%d"))#saida 08

#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%b"))#saida Dec

#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%B"))#saida December

#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%m"))#saida 12

#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%y"))#saida 22

#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%Y"))#saida 2022

#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%H"))#saida 14

#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%I"))#saida 02
#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%p"))#saida PM
#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%M"))#saida 46
#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%S"))#saida 15
#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%f"))#saida 055763
#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%j"))#saida 342
#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%U"))#saida 21
#--------------------------------------------------------------------------------------
x = datetime.datetime(2018, 5, 31)

print(x.strftime("%W"))#saida 22
#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%c"))#saida Thu Dec 08 14:46:27 2022
#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%C"))#saida 20
#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%X"))#saida 14:46:35
#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%%"))#saida %
#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%G"))#saida 2022
#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%u"))#saida 4
#--------------------------------------------------------------------------------------
x = datetime.datetime.now()

print(x.strftime("%V"))#saida 49
#--------------------------------------------------------------------------------------

