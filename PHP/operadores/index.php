<?php
$x = 10;
$y = 6;

echo $x + $y;//Soma
//Exibe 16

echo"<br/>"; 

echo $x - $y;//Subitração
//Exibe 4

echo"<br/>"; 

echo $x * $y;//Mutiplicação
//Exibe 60

echo"<br/>"; 

echo $x / $y;//Divisão
//Exibe 1.6666666666667

echo"<br/>"; 

echo $x % $y;//Mudulo
//Exibe 4

echo"<br/>"; 

echo $x ** $y;//Esponencial
//Exibe 1000000

echo"<br/>"; 

echo $x;
//Exibe 10

echo"<br/>"; 

$x = 20;
$x += 100; 
echo $x;//Atribuição com soma

echo"<br/>"; 

$x = 20;
$x -= 100;
echo $x;//Atribuição com subitração

echo"<br/>"; 

$x = 20;
$x *= 100;
echo $x;//Atribuição com Mutipllicação

echo"<br/>"; 

$x = 20;
$x /= 100;
echo $x;//Atribuição com Divisão

echo"<br/>"; 

$x = 20;
$x %= 100;
echo $x;//Atribuição com Modulo

echo"<br/>"; 

$x = 100;
$x = "100";

var_dump($x==$y);//igual

echo"<br/>";

var_dump($x===$y);//identico

echo"<br/>";

var_dump($x!==$y);//retorma falso se os valores forem igual

echo"<br/>";

$x = 100;
$y = "900";
var_dump($x<>$y);//Outra forma de comparar se a variavel e diferete

echo"<br/>";

$x = 100;
$y = "100";
var_dump($x!==$y);//returns true because types are not equal

echo"<br/>";

$x = 100;
$y = "50";
var_dump($x>$y);//(Maior)retorns true se $x for maior que $y

echo"<br/>";

$x = 10;
$y = 50;
var_dump($x<$y);//(Menor)etorns true se $x for menor que $y

echo"<br/>";

$x = 50;
$y = 50;
var_dump($x>=$y);//(Igual ou maior)retorna true se $x for maior que $y

echo"<br/>";

$x = 5;
$y = 10;
echo($x<=>$y);//Spaceship 01

echo"<br/>";

$x = 10;
$y = 10;
echo($x<=>$y);//Spaceship 02

echo"<br/>";

$x = 15;
$y = 10;
echo($x<=>$y);//Spaceship 03

echo"<br/>";

$x = 10;
echo ++$x;//Pre-incremento

echo"<br/>";

$x = 10;
echo $x++;//Pre-incremento
echo"<br/>";
echo $x;//Pre-incremento

echo"<br/>";

$x = 10;
echo --$x;//Pre-incremento

echo"<br/>";

$x = 10;
echo $x--;//Pre-incremento
echo"<br/>";
echo $x;//Pre-incremento
?>