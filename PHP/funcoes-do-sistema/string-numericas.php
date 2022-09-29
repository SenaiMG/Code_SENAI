<?php
$x = 5985;
var_dump(is_numeric($x));//Exibe bool(true)

echo"<br/>";

$x = "5985";
var_dump(is_numeric($x));//Exibe bool(true)

echo"<br/>";

$x = "5985" + 100;
var_dump(is_numeric($x));//Exibe bool(true)

echo"<br/>";

$x = "Hello";
var_dump(is_numeric($x));//Exibe bool(false)

echo"<br/>";

//Cast float para int
$x = 23465.768;
$int_cast = (int)$x;
echo $int_cast; //Exibe 23456

echo"<br/>";

$x = "23465.768";
$int_cast = (int)$x;
echo $int_cast; //Exibe 23456
?>