<?php
$age = array("Peter"=>"35","Ben"=>"37","Joe"=>"43");

echo json_encode($age);
//Exibe{"Peter":"35","Bem":"37","Joe":"43"}

echo"<br/>";
echo"<br/>";
echo"<br/>";

var_dump($age);

echo"<br/>";
echo"<br/>";
echo"<br/>";

$jsonobj ='{"Peter":"35","Ben":"37","Joe":"43"}';
var_dump(json_decode($jsonobj));
//object(stdClass)#1 (3) { ["Peter"]=> string(2) "35" ["Bem"]=> string(2) "37" ["Joe"]=> string(2) "43" }

















?>