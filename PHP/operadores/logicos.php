<?php
//Operador AND "e"
$x = 100;
$y = 50;
if($x == 100 and $y == 50){ //outra forma de declarar e com &&
    echo"Hello world";
    //Exibe Hello world
}

echo"<br/>";

//Operador OR "ou"
$x = 100;
$y = 50;
if($x == 100 or $y == 50){ //outra forma de declarar e com ||
    echo"Hello world";
    //Exibe Hello world
}

echo"<br/>";

//Operador XOR "ou"
$x = 100;
$y = 50;
if($x == 100 xor $y == 80){
    echo"Hello world";
    //Exibe Hello world
}

echo"<br/>";

//Operador ! "diferente"
$x = 100;
if($x !== 90){
    echo"Hello world";
    //Exibe Hello world
}

?>