<?php
$cars = array("Volvo","BMW","Toyota");
var_dump($cars);

echo"<br/>";
echo"<br/>";

$cars = array("Volvo","BMW","Toyota");
echo "I like" . $cars[0] . "," . $cars[1] . "and" . $cars[2] . ".";

echo"<br/>";
echo"<br/>";

$cars = array("Volvo","BMW","Toyota");
echo count($cars);

echo"<br/>";
echo"<br/>";

$cars = array("Volvo","BMW","Toyota");
$arrlength = count($cars);

for($x = 0 ; $x < $arrlength ; $x++){
    echo $cars[$x];
    echo"<br/>";
    /*Exibe
    Volvo
    BMW
    Toyota*/
}

echo"<br/>";
echo"<br/>";


$age = array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
echo "Peter is " . $age['Peter'] . " years old.";
//Exibe Peter is35years old.

echo"<br/>";
echo"<br/>";

//Array assciativo
$age = array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
foreach($age as $x=> $x_value){
    echo "Key = " . $x . ", Value = " . $x_value;
    echo"<br/>";
}

echo"<br/>";
echo"<br/>";

$cars = array(
array("Volvo",22,18),
array("BMW",15,13),
array("Saab",5,2),
array("Land Rover",17,15)
);
echo $cars[0][0] . ": In stock: " . $cars[0][1] . " sold: " . $cars[0][2] . "<br/>";
echo $cars[1][0] . ": In stock: " . $cars[1][1] . " sold: " . $cars[1][2] . "<br/>";
echo $cars[2][0] . ": In stock: " . $cars[2][1] . " sold: " . $cars[2][2] . "<br/>";
echo $cars[3][0] . ": In stock: " . $cars[3][1] . " sold: " . $cars[3][2] . "<br/>";

echo"<br/>";
echo"<br/>";

$cars = array(
    array("Volvo",22,18),
    array("BMW",15,13),
    array("Saab",5,2),
    array("Land Rover",17,15)
);

for($row = 0; $row < 4; $row++){
    echo "<p><b>Row number $row</b></p>";
    echo"<ul>";
    for($col = 0; $col < 3; $col++){
        echo "<li>" . $cars[$row][$col] . "</li>";
    }
    echo"</ul>";
}
echo"<br/>";
echo"<br/>";
echo"<br/>";
echo"<br/>";
echo"<br/>";
echo"<br/>";

//forma de percorre dinamicamente

$c = count($cars);

for($row = 0; $row < $c; $row++){
    echo "<p><b>Row number $row</b></p>";
    echo"<ul>";
        $r  = count($cars[$row]);
        for($col = 0; $col < $r; $col++){
            echo "<li>" . $cars[$row][$col] . "</li>";
        }
    echo"</ul>";
}

//classificação para arrays:

//sort()
$cars = array("Volvo","BMW","Toyota");
sort($cars);
$clength = count($cars);
for($x = 0; $x < $clength ; $x++){
    echo $cars[$x];
    echo"<br/>";
}

echo"<br/>";

//rsort
$cars = array("Volvo","BMW","Toyota");
rsort($cars);
$clength = count($cars);
for($x = 0; $x < $clength ; $x++){
    echo $cars[$x];
    echo"<br/>";
}

echo"<br/>";

//asort

$age = array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
asort($age);

foreach($age as $x=> $x_value){
    echo "Key = " . $x . ", Value = " . $x_value;
    echo"<br/>";
}

echo"<br/>";

//ksort
$age = array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
ksort($age);

foreach($age as $x=> $x_value){
    echo "Key = " . $x . ", Value = " . $x_value;
    echo"<br/>";
}

echo"<br/>";

//arsort

$age = array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
arsort($age);
foreach($age as $x=> $x_value){
    echo "Key = " . $x . ", Value = " . $x_value;
    echo"<br/>";
}

echo"<br/>";

//krsort
$age = array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
krsort($age);

foreach($age as $x=> $x_value){
    echo "Key = " . $x . ", Value = " . $x_value;
    echo"<br/>";
}





















?>