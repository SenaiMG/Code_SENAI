<?php
$x = array("a"=>"red", "b"=>"green");
$y = array("c"=>"blue", "d"=>"yellow");
print_r($x + $y);//Uniao "+"

echo"<br/>";

$x = array("a"=>"red", "b"=>"green");
$y = array("c"=>"blue", "d"=>"yellow");
var_dump($x == $y);//Igual "=="

echo"<br/>";

$x = array("a"=>"red", "b"=>"green");
$y = array("c"=>"blue", "d"=>"yellow");
var_dump($x === $y);//idêntico "==="

echo"<br/>";

$x = array("a"=>"red", "b"=>"green");
$y = array("c"=>"blue", "d"=>"yellow");
var_dump($x != $y);//Diferente "!= ou <>"
echo"<br/>";
var_dump($x <> $y);

echo"<br/>";

$x = array("a"=>"red", "b"=>"green");
$y = array("c"=>"blue", "d"=>"yellow");
var_dump($x !== $y);//Não identico "!=="
?>
