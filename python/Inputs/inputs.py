#Entrada do usuário
#Python permite a entrada do usuário.

#Isso significa que podemos solicitar entrada do usuário.

#O método é um pouco diferente no Python 3.6 do que no Python 2.7.

#O Python 3.6 usa o input()método.

#O Python 2.7 usa o raw_input()método.

#O exemplo a seguir solicita o nome de usuário e, quando você digita o nome de usuário,
# ele é impresso na tela:


#python 3.6
sername = input("Enter username:")
print("Username is: " + username)

#python 2.7
username = raw_input("Enter username:")
print("Username is: " + username)

#OBS: O Python para de executar quando se trata da input()função e 
# continua quando o usuário fornece alguma entrada.