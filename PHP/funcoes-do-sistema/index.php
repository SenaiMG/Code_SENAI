<?php
echo"_____________Funções de stings_____________";
echo"<br/>";
echo"<br/>";

echo strlen("Hello world!");
//Exibe 12 (conta caracteres e espaço)

echo"<br/>";

echo str_word_count("Hello world!");
//Exibe 2 (conta as palavras)

echo"<br/>";

echo strrev("Hello world!");
//Exibe !dlrow olleH (Exibe de traz pra frente)

echo"<br/>";

echo strpos("Hello world!", "world");
//Exibe 6 (conta o começo da palavra e o espaço)

echo"<br/>";

echo str_replace("world", "Dolly", "Hello world");
//Exibe Hello Dolly!

echo"<br/>";

$txt = "Diogo da ilva Oliveira";
$proc = "ilva";
$sub = "Silva";
echo str_replace($proc ,$sub ,$txt);


echo"<br/>";
echo"<br/>";
echo"_____________Funções Numerico INT_____________";
echo"<br/>";
echo"<br/>";

echo PHP_INT_MAX;


echo"<br/>";

//Verifica se o tipo da variavel é inteiro
$X = 5985;
var_dump(is_int($X)); //Exibe bool(true)

echo"<br/>";

$X = 59.85;
var_dump(is_int($X)); //Exibe bool(false)

echo"<br/>";
echo"<br/>";
echo"_____________Funções Numerico FLOAT_____________";
echo"<br/>";
echo"<br/>";

echo PHP_FLOAT_MAX;

echo"<br/>";

//Verifica se a variável é um ponto flutuante
$X = 10.365;
var_dump(is_float($X)); //Exibe bool(true)

echo"<br/>";

$X = 10365;
var_dump(is_float($X)); //Exibe bool(false)

echo"<br/>";
echo"<br/>";
echo"_____________Funções Numerico INFINITO_____________";
echo"<br/>";
echo"<br/>";

var_dump(is_finite(PHP_FLOAT_MAX)); //Exibe bool(true)

echo"<br/>";

$X = 1.79769313484E623645654654564566565465415645+308;
var_dump(is_infinite($X)); //Exibe bool(true)

echo"<br/>";
echo"<br/>";
echo"_____________Funções Numerico INFINITO_____________";
echo"<br/>";
echo"<br/>";
?>