#A manipulação de arquivos é uma parte importante de qualquer aplicativo da web.

#Python tem várias funções para criar, ler, atualizar e deletar arquivos.

#Manipulação de arquivos
#A função chave para trabalhar com arquivos em Python é a open()função.

#A open()função recebe dois parâmetros; nome do arquivo e modo .

#Existem quatro métodos diferentes (modos) para abrir um arquivo:

#"r"- Leitura - Valor padrão. Abre um arquivo para leitura, erro se o arquivo não existir

#"a"- Anexar - Abre um arquivo para anexar, cria o arquivo se ele não existir

#"w"- Write - Abre um arquivo para escrita, cria o arquivo se ele não existir

#"x"- Criar - Cria o arquivo especificado, retorna um erro se o arquivo existir

#Além disso, você pode especificar se o arquivo deve ser tratado como modo binário ou texto

#"t"- Texto - Valor padrão. modo de texto

#"b"- Binário - modo binário (por exemplo, imagens)

#Sintaxe
#Para abrir um arquivo para leitura basta especificar o nome do arquivo:

#f = open("demofile.txt")
#O código acima é o mesmo que:

#f = open("demofile.txt", "rt")
#Como "r"para leitura e "t"para texto são os valores padrão, você não precisa especificá-los.

#Nota: Certifique-se de que o arquivo existe, caso contrário, você receberá um erro.

#Abra um arquivo no servidor
#Suponha que temos o seguinte arquivo, localizado na mesma pasta do Python:

#demofile.txt

#Hello! Welcome to demofile.txt
#This file is for testing purposes.
#Good Luck!
#Para abrir o arquivo, use a open()função interna.

#A open()função retorna um objeto de arquivo, que possui um read()método 
# para ler o conteúdo do arquivo:
f = open("demofile.txt", "r")

print(f.read())
#saida Hello! Welcome to demofile.txt
#This file is for testing purposes.
#Good Luck!


#-------------------------------------------------------------------------------------------
#Se o arquivo estiver em um local diferente, você terá que 
# especificar o caminho do arquivo, assim:

f = open(r"c:\Users\N Armament\Desktop\SENAI\python\manipulacaoArquivos\demofile.txt", "r")

print(f.read())
#saida Hello! Welcome to demofile.txt
#This file is for testing purposes.
#Good Luck!

#-------------------------------------------------------------------------------------------
#Somente leitura de partes do arquivo
#Por padrão, o read()método retorna o texto inteiro, mas você também pode 
#especificar quantos caracteres deseja retornar:

f = open("demofile.txt", "r")

print(f.read(5))
#saida Hello
#-------------------------------------------------------------------------------------------
#Ler Linhas
#Você pode retornar uma linha usando o readline()método:

f = open("demofile.txt", "r")

print(f.readline())
#saida Hello! Welcome to demofile.txt

#Chamando readline()duas vezes, você pode ler as duas primeiras linhas:

f = open("demofile.txt", "r")

print(f.readline())#saida Hello! Welcome to demofile.txt
print(f.readline())#saida This file is for testing purposes.
#-------------------------------------------------------------------------------------------
#Ao percorrer as linhas do arquivo, você pode ler o arquivo inteiro, linha por linha:
f = open("demofile.txt", "r")
for x in f:
  print(x)
#saida Hello! Welcome to demofile.txt
#This file is for testing purposes.
#Good Luck!

#-------------------------------------------------------------------------------------------
#Fechar arquivos
#É uma boa prática sempre fechar o arquivo quando terminar de usá-lo.

f = open("demofile.txt", "r")

print(f.readline())#saida Hello! Welcome to demofile.txt

f.close()

#OBS: Você deve sempre fechar seus arquivos, em alguns casos, 
# devido ao buffer, as alterações feitas em um arquivo podem não
# aparecer até que você feche o arquivo.
#-------------------------------------------------------------------------------------------
#Gravar em um arquivo existente
#Para gravar em um arquivo existente, você deve adicionar um parâmetro à open()função:

#"a"- Anexar - será anexado ao final do arquivo

#"w"- Escrever - substituirá qualquer conteúdo existente

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
#saida Hello! Welcome to demofile2.txt
#This file is for testing purposes.
#Good Luck!Now the file has more content!

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
#saida Woops! I have deleted the content!

#OBS: o método "w" substituirá o arquivo inteiro.

#-------------------------------------------------------------------------------------------
#Criar um novo arquivo
#Para criar um novo arquivo em Python, utilize o open()método, com um dos seguintes parâmetros:

#"x"- Criar - criará um arquivo, retornará um erro se o arquivo existir

#"a"- Anexar - criará um arquivo se o arquivo especificado não existir

#"w"- Write - criará um arquivo se o arquivo especificado não existir

f = open("myfile.txt", "x")

#Crie um novo arquivo se ele não existir:
f = open("myfile.txt", "w")

#-------------------------------------------------------------------------------------------
#Excluir um arquivo
#Para excluir um arquivo, você deve importar o módulo OS e 
# executar sua os.remove() função:


#Verifique se o arquivo existe:
#Para evitar erros, verifique se o arquivo existe antes de tentar excluí-lo:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#-------------------------------------------------------------------------------------------
#Excluir pasta
#Para excluir uma pasta inteira, use o os.rmdir() método:

os.rmdir("myfolder")
#Observação: você só pode remover pastas vazias .

#-------------------------------------------------------------------------------------------
