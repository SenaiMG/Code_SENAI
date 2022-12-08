#O Python possui um conjunto de funções matemáticas integradas, 
# incluindo um extenso módulo matemático, que permite realizar
# tarefas matemáticas com números.

#Funções matemáticas integradas
#As funções min()e max()podem ser usadas para encontrar 
# o valor mais baixo ou mais alto em um iterável:

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)#saida 5
print(y)#saida 25

#----------------------------------------------------------------------------------------------------
#A abs()função retorna o valor absoluto (positivo) do número especificado:
x = abs(-7.25)

print(x)#saida 7.25
#----------------------------------------------------------------------------------------------------
#A função retorna o valor de x à potência de y (x y ).pow(x, y)

x = pow(4, 3)

print(x)#saida 64

#----------------------------------------------------------------------------------------------------
#O módulo de matemática
#O Python também possui um módulo embutido chamado math, que estende 
# a lista de funções matemáticas.

#Para usá-lo, você deve importar o math módulo:

#Depois de importar o mathmódulo, você pode começar a usar métodos e constantes do módulo.

#O math.sqrt()método por exemplo, retorna a raiz quadrada de um número:
import math

x = math.sqrt(64)

print(x)#saida 8.0

#----------------------------------------------------------------------------------------------------
#O math.ceil()método arredonda um número para cima até o inteiro mais próximo, e 
# o math.floor() método arredonda um número para baixo até o inteiro mais 
# próximo e retorna o resultado:

#Arredondar um número para cima até o inteiro mais próximo
x = math.ceil(1.4)

#Arredondar um número para baixo até o inteiro mais próximo
y = math.floor(1.4)

print(x)#saida 2
print(y)#saida 1
#----------------------------------------------------------------------------------------------------
#A math.piconstante, retorna o valor de PI (3.14...):

x = math.pi

print(x)#saida 3.141592653589793
#----------------------------------------------------------------------------------------------------
#Metodos do modulo math

#Definição e Uso
#O math.acos()método retorna o valor do arco cosseno de um número.

#Nota: O parâmetro passado math.acos()deve estar entre -1 e 1.

#Dica: math.acos(-1) retornará o valor do PI.

#Sintaxe
#math.acos(x)

print(math.acos(0.55))#saida 0.9884320889261531
print(math.acos(-0.55))#saida 2.15316056466364
print(math.acos(0))#saida 1.5707963267948966
print(math.acos(1))#saida 0.0
print(math.acos(-1))#saida 3.141592653589793

#----------------------------------------------------------------------------------------------------
#O math.acosh()método retorna o cosseno hiperbólico inverso de um número.

#Obs: O parâmetro passado em acosh() deve ser maior ou igual a 1.

#Sintaxe
#math.acosh(x)

print(math.acosh(7))#saida 2.6339157938496336
print(math.acosh(56))#saida 4.718419142372879
print(math.acosh(2.45))#saida 1.5447131178707394
print(math.acosh(1))#saida 0

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.asin()método retorna o arco seno de um número.

#Nota: O parâmetro passado math.asin()deve estar entre -1 e 1.

#Dica: math.asin(1) retornará o valor de PI/2 e math.asin(-1)retornará o valor de -PI/2.

#Sintaxe
#math.asin(x)

print(math.asin(0.55))#saida 0.5823642378687435
print(math.asin(-0.55))#saida -0.5823642378687435
print(math.asin(0))#saida 0.0
print(math.asin(1))#saida 1.5707963267948966
print(math.asin(-1))#saida -1.5707963267948966
#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.asinh()método retorna o seno hiperbólico inverso de um número.

#Sintaxe
#math.asinh(x)

print(math.asinh(7))#saida 2.644120761058629
print(math.asinh(56))#saida 4.718578581151767
print(math.asinh(2.45))#saida 1.6284998192841909
print(math.asinh(1))#saida 0.881373587019543
print(math.asinh(0.5))#saida 0.48121182505960347
print(math.asinh(-10))#saida -2.99822295029797

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.atan()método retorna o arco tangente de um número ( x ) 
#como um valor numérico entre -PI/2 e PI/2 radianos.

#A tangente do arco também é definida como uma função tangente inversa de x ,
#onde x é o valor da tangente do arco a ser calculada.

#Sintaxe
#math.atan(x)
print (math.atan(0.39))#saida 0.37185607384858127
print (math.atan(67))#saida 1.5558720618048116
print (math.atan(-21))#saida -1.5232132235179132

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.atan2()método retorna o arco tangente de y/x, em radianos. 
# Onde xey são as coordenadas de um ponto (x,y).

#O valor retornado está entre PI e -PI.

#Sintaxe
#math.atan2(y, x)

print(math.atan2(8, 5))#saida 1.0121970114513341
print(math.atan2(20, 10))#saida 1.1071487177940904
print(math.atan2(34, -7))#saida 1.7738415440483617
print(math.atan2(-340, -120))#saida -1.9100889412489412

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.atanh()método retorna a tangente hiperbólica inversa de um número.

#Observação: O parâmetro passado math.atanh()deve estar entre -0,99 e 0,99.

#Sintaxe
#math.atanh(x)

print (math.atanh(0.59))#saida 0.6776660677579618
print (math.atanh(-0.12))#saida -0.12058102840844404
print (math.atanh(0.99))#saida 2.6466524123622457

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.ceil()método arredonda um número PARA CIMA para o inteiro mais próximo,
# se necessário, e retorna o resultado.

#Dica: Para arredondar um número PARA BAIXO para o inteiro mais próximo,
# veja o math.floor()método.

#Sintaxe
#math.ceil(x)

print(math.ceil(1.4))#saida 2
print(math.ceil(5.3))#saida 6
print(math.ceil(-5.3))#saida -5
print(math.ceil(22.6))#saida 23
print(math.ceil(10.0))#saida 10

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.comb()método retorna o número de maneiras de selecionar k 
# resultados não ordenados de n possibilidades, sem repetição, também conhecidas como combinações.

#Obs.: Os parâmetros passados ​​neste método devem ser inteiros positivos.

#Sintaxe
#math.comb(n, k)

# Initialize the number of items to choose from
n = 7

# Initialize the number of possibilities to choose
k = 5

# Print total number of possible combinations
print (math.comb(n, k))#saida 21

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.copysign()método retorna um float que consiste no valor do primeiro 
# parâmetro e o sinal (+/-) do segundo parâmetro.

#Sintaxe
#math.copysign(x, y)

print(math.copysign(4, -1))#saida -4.0
print(math.copysign(-8, 97.21))#saida 8.0
print(math.copysign(-43, -76))#saida -43.0

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.cos()método retorna o cosseno de um número.

#Sintaxe
#math.cos(x)

print (math.cos(0.00))#saida 1.0
print (math.cos(-1.23))#saida 0.3342377271245026
print (math.cos(10))#saida -0.8390715290764524
print (math.cos(3.14159265359))#saida -1.0

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.cosh()método retorna o cosseno hiperbólico de um
# número (equivalente a (exp(número) + exp(-número)) / 2).

#Sintaxe
#math.cosh(x)

print (math.cosh(1))#saida 1.5430806348152437
print (math.cosh(8.90))#saida 3665.986837772461
print (math.cosh(0))#saida 1.0
print (math.cosh(1.52))#saida 2.3954685410471868

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O mmath.degrees()método converte um ângulo de radianos para graus.

#Dica: PI (3.14..) radianos são iguais a 180 graus, o que significa que 1 radiano 
# é igual a 57,2957795 graus.

#Dica: Consulte também math.radians()para converter um valor de grau em radianos.

#Sintaxe
#math.degrees(x)

print (math.degrees(8.90))#saida 509.9324376664327
print (math.degrees(-20))#saida -1145.9155902616465
print (math.degrees(1))#saida 57.29577951308232
print (math.degrees(90))#saida 5156.620156177409

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.dist()método retorna a distância euclidiana entre dois pontos (p e q), 
# onde p e q são as coordenadas desse ponto.

#Nota: Os dois pontos (p e q) devem ter as mesmas dimensões.

#Sintaxe
#math.dist(p, q)

p = [3] 
q = [1] 

# Calculate Euclidean distance
print (math.dist(p, q))#saida 2.0

p = [3, 3] 
q = [6, 12] 

# Calculate Euclidean distance
print (math.dist(p, q))#saida 9.486832980505138

#----------------------------------------------------------------------------------------------------
#Definition and Usage
#The math.erf() method returns the error function of a number.

#This method accepts a value between - inf and + inf, and returns a value between - 1 to + 1.

#Syntax
#math.erf(x)
print (math.erf(0.67))#saida 0.6566277023003051
print (math.erf(1.34))#saida 0.9419137152583653
print (math.erf(-6))#saida -1.0

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.erfc()método retorna a função de erro complementar de um número.

#Este método aceita um valor entre - inf e + inf e retorna um valor entre 0 e 2.

#Sintaxe
#math.erfc(x)

print (math.erfc(0.67))#saida 0.3433722976996949
print (math.erfc(1.34))#saida 0.058086284741634665
print (math.erfc(-6))#saida 2.0

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.exp()método retorna E elevado à potência de x (E x ).

#'E' é a base do sistema natural de logaritmos (aproximadamente 2,718282) e
# x é o número passado para ele.

#Sintaxe
#math.exp(x)

print(math.exp(65))#saida 1.6948892444103338e+28
print(math.exp(-6.89))#saida 0.0010179138409954387

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.expm1()método retorna E x - 1.

#'E' é a base do sistema natural de logaritmos (aproximadamente 2,718282) e x é o número passado para ele.

#Esta função é mais precisa do que chamar e subtrair 1. math.exp()

#Sintaxe
#math.expm1(x)

print(math.expm1(32))#saida 78962960182679.69
print(math.expm1(-10.89))#saida -0.9999813562576685

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.fabs()método retorna o valor absoluto de um número, como um float.

#Absoluto denota um número não negativo. Isso remove o sinal negativo do valor, se houver algum.

#Ao contrário do Python abs() , esse método sempre converte o valor em um valor flutuante.

#Sintaxe
#math.fabs(x)

print(math.fabs(-66.43))#saida 66.43 
print(math.fabs(-7))#saida 7.0

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.factorial()método retorna o fatorial de um número.

#Nota: Este método aceita apenas números inteiros positivos.

#O fatorial de um número é a soma da multiplicação, de todos os números inteiros, 
# de nosso número especificado até 1. Por exemplo, 
# o fatorial de 6 seria 6 x 5 x 4 x 3 x 2 x 1 = 720

#Sintaxe
#math.factorial(x)

print(math.factorial(9))#saida 362880
print(math.factorial(6))#saida 720
print(math.factorial(12))#saida 479001600

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.floor()método arredonda um número PARA BAIXO para o inteiro mais próximo,
# se necessário, e retorna o resultado.

#Dica: Para arredondar um número PARA CIMA para o inteiro mais próximo,
# veja o método. math.ceil()

#Sintaxe
#math.floor(x)

print(math.floor(0.6))#saida 0
print(math.floor(1.4))#saida 1
print(math.floor(5.3))#saida 5
print(math.floor(-5.3))#saida -6
print(math.floor(22.6))#saida 22
print(math.floor(10.0))#saida 10

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.fmod()método retorna o restante (módulo) de x/y.

#Sintaxe
#math.fmod(x, y)
print(math.fmod(20, 4))#saida 0.0
print(math.fmod(20, 3))#saida 2.0
print(math.fmod(15, 6))#saida 3.0
print(math.fmod(-10, 3))#saida -1.0
print(math.fmod(0, 0))
#saida Traceback (most recent call last):
#  File "./prog.py", line 5, in <module>
#ValueError: math domain error

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.frexp()método retorna a mantissa e o expoente de um número
# especificado, como um par ( m , e ).

#A fórmula matemática para este método é: número = m * 2 **e .

#Sintaxe
#math.frexp(x)

print(math.frexp(4))#saida (0.5, 3)
print(math.frexp(-4))#saida (-0.5, 3)
print(math.frexp(7))#saida (0.875, 3)
#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.fsum()método retorna a soma de todos os itens em 
#qualquer iterável (tuplas, arrays, listas, etc.).

#Sintaxe
#math.fsum(iterable)

print(math.fsum([1, 2, 3, 4, 5]))#saida 15.0
print(math.fsum([100, 400, 340, 500]))#saida 1340.0
print(math.fsum([1.7, 0.3, 1.5, 4.5]))#saida 8.0

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.gamma()método retorna a função gama em um número.

#Dica: Para encontrar o valor log gama de um número, use o math.lgamma()método.

#Sintaxe
#math.gamma(x)

print(math.gamma(-0.1))#saida -10.686287021193193
print(math.gamma(8))#saida 5040.0
print(math.gamma(1.2))#saida 0.9181687423997604
print(math.gamma(80))#saida 8.946182130782976e+116
print(math.gamma(-0.55))#saida  -3.578429819277059

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.gcd()método retorna o máximo divisor comum dos dois inteiros int1 e int2 .
#MDC é o maior divisor comum que divide os números sem deixar resto.
#GCD também é conhecido como o maior fator comum (HCF).
#Dica: gcd(0,0) retorna 0.

#Sintaxe
#math.gcd(int1, int2)

print (math.gcd(3, 6))#saida 3
print (math.gcd(6, 12))#saida 6
print (math.gcd(12, 36))#saida 12
print (math.gcd(-12, -36))#saida 12 
print (math.gcd(5, 12))#saida 1
print (math.gcd(10, 0))#saida 10
print (math.gcd(0, 34))#saida 34
print (math.gcd(0, 0))#saida 0

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.hypot()método retorna a norma euclidiana. 
# A norma euclidiana é a distância da origem às coordenadas dadas.

#Antes do Python 3.8, esse método era usado apenas para encontrar a 
# hipotenusa de um triângulo retângulo: sqrt(x*x + y*y).

#A partir do Python 3.8, esse método também é usado para calcular a norma euclidiana.
# Para casos n-dimensionais, as coordenadas passadas são assumidas como (x1, x2, x3, ..., xn).
# Portanto, o comprimento euclidiano a partir da origem 
# é calculado por sqrt(x1*x1 + x2*x2 +x3*x3 .... xn*xn).

#Sintaxe
#math.hypot(x1, x2, x3, ..., xn)

parendicular = 10
base = 5

print(math.hypot(parendicular, base))#saida 11.180339887498949

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.isclose()método verifica se dois valores estão próximos ou não. 
# Retorna True se os valores forem próximos, caso contrário, False.

#Este método usa uma tolerância relativa ou absoluta, para ver se os valores estão próximos.

#Dica: Use a seguinte fórmula para comparar os valores:
# abs(ab) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

#Sintaxe
#math.isclose(a, b, rel_tol, abs_tol)


print(math.isclose(1.233, 1.4566))#saida False
print(math.isclose(1.233, 1.233))#saida  True
print(math.isclose(1.233, 1.24))#saida False
print(math.isclose(1.233, 1.233000001))#saida True

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.isfinite()método verifica se um número é finito ou não.

#Este método retorna True se o número especificado for um número finito,
# caso contrário, retorna False.

#Sintaxe
#math.isfinite(x)

print(math.isfinite(2000))#saida True
print(math.isfinite(-45.34))#saida True
print(math.isfinite(+45.34))#saida True
print(math.isfinite(math.inf))#saida False
print(math.isfinite(float("nan")))#saida False
print(math.isfinite(float("inf")))#saida False
print(math.isfinite(float("-inf")))#saida False
print(math.isfinite(-math.inf))#saida False
print(math.isfinite(0.0))#saida True

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.isinf()método verifica se um número é infinito ou não.

#Este método retorna True se o número especificado for um 
# infinito positivo ou negativo, caso contrário, retorna False.

#Sintaxe
#math.isinf(x)

print (math.isinf (56))#saida False
print (math.isinf (-45.34))#saida False
print (math.isinf (+45.34))#saida False
print (math.isinf (math.inf))#saida True
print (math.isinf (float("nan")))#saida False
print (math.isinf (float("inf")))#saida True
print (math.isinf (float("-inf")))#saida True
print (math.isinf (-math.inf))#saida True

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.isnan()método verifica se um valor é NaN (não é um número) ou não.

#Este método retorna True se o valor especificado for um NaN, caso contrário, retorna False.

#Sintaxe
#math.isnan(x)

print (math.isnan (56))#saida False
print (math.isnan (-45.34))#saida False
print (math.isnan (+45.34))#saida False
print (math.isnan (math.inf))#saida False
print (math.isnan (float("nan")))#saida True
print (math.isnan (float("inf")))#saida False
print (math.isnan (float("-inf")))#saida False
print (math.isnan (math.nan))#saida True

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.isqrt()método arredonda um número de raiz quadrada para 
# baixo até o inteiro mais próximo.

#Nota: O número deve ser maior ou igual a 0.

#Sintaxe
#math.isqrt(x)

print (math.sqrt(10))#saida 3.1622776601683795
print (math.sqrt (12))#saida 3.4641016151377544
print (math.sqrt (68))#saida 8.246211251235321
print (math.sqrt (100))#saida 10.0
print (math.isqrt(10))#saida 3
print (math.isqrt (12))#saida 3
print (math.isqrt (68))#saida 8
print (math.isqrt (100))#saida 10

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.ldexp()método retorna x * (2**i) dos números fornecidos x e i, 
# que é o inverso de math.freexp() .

#Sintaxe
#math.ldexp(x, i)

print(math.ldexp(9, 3))#saida 72.0
print(math.ldexp(-5, 2))#saida -20.0
print(math.ldexp(15, 2))#saida 60.0
#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.lgamma()método retorna o valor gama do logaritmo natural de um número.
#Dica: Também podemos encontrar o valor log gama usando o math.gamma()método para
# encontrar o valor gama e, em seguida, usar o math.log()método 
# para calcular o log desse valor.
#Dica: O valor gama é igual a fatorial(x-1).

#Sintaxe
#math.lgamma(x)

print (math.lgamma(7))#saida 6.579251212010102
print (math.lgamma(-4.2))#saida -1.8075166614192908

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.log()método retorna o logaritmo natural de um número ou 
# o logaritmo do número para a base.

#Sintaxe
#math.log(x, base)

print(math.log(2.7183))#saida  1.0000066849139877
print(math.log(2))#saida 0.6931471805599453
print(math.log(1))#saida 0.0

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.log10()método retorna o logaritmo de base 10 de um número.

#Sintaxe
#math.log10(x)

print(math.log10(2.7183))#saida 0.43429738512450866
print(math.log10(2))#saida 0.3010299956639812
print(math.log10(1))#saida 0.0

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.log1p()método retorna log(1+number), calculado de forma precisa mesmo 
# quando o valor de number está próximo de zero.

#Sintaxe
#math.log1p(x)

print(math.log1p(2.7183))#saida 1.3132665745863341
print(math.log1p(2))#saida 1.0986122886681096
print(math.log1p(1))#saida 0.6931471805599453
#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.log2()método retorna o logaritmo de base 2 de um número.

#Sintaxe
#math.log2(x)

print(math.log2(2.7183))#saida 1.4427046851812222
print(math.log2(2))#saida 1.0
print(math.log2(1))#saida 0.0 

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.perm()método retorna o número de maneiras de 
# escolher k itens de n itens com ordem e sem repetição.

#Nota: O parâmetro k é opcional. Se não fornecermos um, esse método 
# retornará n ! (por exemplo, math.perm(7) retornará 5040).

#Sintaxe
#math.perm(n, k)

n = 7

k = 5

print (math.perm(n, k))#saida 2520

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.pow()método retorna o valor de x elevado à potência y.
#Se x for negativo e y não for um número inteiro, ele retornará um ValueError.
#Este método converte ambos os argumentos em float.
#Dica: Se usarmos math.pow(1.0,x)ou math.pow(x,0.0), sempre retornará 1.0.
#Sintaxe
#math.pow(x, y)

print(math.pow(9, 3))#saida 729.0

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.prod()método retorna o produto dos elementos do iterável fornecido.

#Sintaxe
#math.prod(iterable, start)

sequence = (2, 2, 2)

print(math.prod(sequence))#saida 8

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.radians()método converte um valor de grau em radianos.

#Dica: Consulte também math.degrees()para converter um ângulo de radianos para graus.

#Sintaxe
#math.radians(x)
print(math.radians(180))#saida 3.141592653589793
print(math.radians(100.03))#saida 1.7458528507699278
print(math.radians(-20))#saida -0.3490658503988659

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.remainder()método retorna o restante de x em relação a y.

#Sintaxe
#math.remainder(x, y)

print (math.remainder(9, 2))#saida 1.0
print (math.remainder(9, 3))#saida 0.0
print (math.remainder(18, 4))#saida 2.0

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.sin()método retorna o seno de um número.

#Observação: Para encontrar o seno de graus, primeiro ele deve 
# ser convertido em radianos com o método (veja o exemplo abaixo). math.radians()

#Sintaxe
#math.sin(x)


print (math.sin(0.00))#saida 0.0
print (math.sin(-1.23))#saida -0.9424888019316975
print (math.sin(10))#saida -0.5440211108893698
print (math.sin(math.pi))#saida  1.2246467991473532e-16
print (math.sin(math.pi/2))#saida 1.0

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.sinh()método retorna o seno hiperbólico de um número.

#Sintaxe
#math.sinh(x)

print(math.sinh(0.00))#saida 0.0
print(math.sinh(-23.45))#saida -7641446994.979367
print(math.sinh(23))#saida 4872401723.124452
print(math.sinh(1.00))#saida 1.1752011936438014
print(math.sinh(math.pi))#saida 11.548739357257748

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.sqrt()método retorna a raiz quadrada de um número.

#Nota: O número deve ser maior ou igual a 0.

#Sintaxe
#math.sqrt(x)

print (math.sqrt(9))#saida 3.0
print (math.sqrt(25))#saida 5.0
print (math.sqrt(16))#saida 4.0

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.tan()método retorna a tangente de um número.

#Sintaxe
#math.tan(x)

print (math.tan(90))#saida -1.995200412208242
print (math.tan(-90))#saida 1.995200412208242
print (math.tan(45))#saida 1.6197751905438615
print (math.tan(60))#saida 0.320040389379563

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.tanh()método retorna a tangente hiperbólica de um número.

#Sintaxe
#math.tanh(x)

print(math.tanh(8))#saida 0.9999997749296758
print(math.tanh(1))#saida 0.7615941559557649
print(math.tanh(-6.2))#saida -0.9999917628565104

#----------------------------------------------------------------------------------------------------
#Definição e Uso
#O math.trunc()método retorna a parte inteira truncada de um número.

#Observação: este método NÃO arredondará o número para cima/para baixo para o
# inteiro mais próximo, mas simplesmente removerá os decimais.

#Sintaxe
#math.trunc(x)

print(math.trunc(2.77))#saida 2
print(math.trunc(8.32))#saida 8
print(math.trunc(-99.29))#saida -99
#----------------------------------------------------------------------------------------------------
