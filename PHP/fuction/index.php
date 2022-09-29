<?php
declare(strict_types=1);

/*
    SINTAX BASICA:

    function functionName(Declarar uma variavel){
        code to be executed
        2 tipo de retorno de função: 
        - RETORNO
        - EXIBIÇÃO
    }
*/
function writeMsg(){
    echo "Hello world!";
}
writeMsg();//chama a função
//Exibe Hello world!

echo "<br/>";
echo "<br/>";



function familyName($fname){
    echo "$fname Refsnes.<br/>";
}
familyName("Jani");
familyName("Hege");
familyName("Stale");
familyName("Kai Jim");
familyName("Borge");

$x = "Diogo";
familyName($x);

echo "<br/>";
echo "<br/>";

function aluno($nome,$materia){
    echo"Meu nome é:" . $nome . "<br/>";
    echo"Eu amo:" . $materia . "<br/>";
}


$n ="saulo";
$p ="faca";
aluno($n,$p);

echo "<br/>";

aluno(" Diogo"," HTML é CSS");



echo "<br/>";
echo "<br/>";

//-------------------------------------
function addNunbers(int $a, int $b){
    return $a + $b;
}
//echo addNunbers(5,"5 days");

echo addNunbers(5,5);
//como strict NÃO está habilitado "5 dias" é alterado para int(5) e retornará 10
//Exibe 10

//Já que a strict está habilitado "5 days" não é um numero inteiro , um erro será gerado 

/*Fatal error: Uncaught TypeError: addNunbers(): Argument #2 ($b) must be of type 
int, string given, called in C:\xampp\htdocs\programacao\diogo-php\fuction\index.php 
on line 57 and defined in C:\xampp\htdocs\programacao\diogo-php\fuction\index.php:54 
Stack trace: #0 C:\xampp\htdocs\programacao\diogo-php\fuction\index.php(57): addNunbers(5, '5 days') 
#1 {main} thrown in C:\xampp\htdocs\programacao\diogo-php\fuction\index.php on line 54 */

echo "<br/>";
echo "<br/>";


function setHeight(int $minheigight = 50){
    echo "The height is: $minheigight <br/>";
}
setHeight(350);//Exibe The height is: 350
setHeight();//Exibe The height is: 50
setHeight(135);//Exibe The height is: 135 
setHeight(80);//Exibe The height is: 80

echo "<br/>";
echo "<br/>";

function sum(int $x, int $y){
    $z = $x + $y;
    return $z;
}
echo "5 + 10 =" . sum(5,10) . "<br/>";
echo "7 + 13 =" . sum(7,13) . "<br/>";
echo "2 + 4  =" . sum(2,4) . "<br/>";

function addNunbers2(float $a,float $b ):float{
    return $a+$b; 
}
echo addNunbers2(1.2,5.2);

echo "<br/>";
echo "<br/>";

//function addNunbers3(float $h,float $c):int{
 //   return ($h+$c); 
//}
//echo addNunbers3(1.2,1.4);

echo "<br/>";
echo "<br/>";

function add_five(&$value){
    $value += 5;
}
$num = 2;
add_five($num);
echo $num;

echo "<br/>";
echo "<br/>";





































?>