<?php
/*
O foreach loop funciona apenanas em uma arrays e é 
usado para percorrer cada par 
*/

$color = array("red","green","blue","yellow");
foreach($color as $value){
    echo "$value <br/>";
}
echo"<br/>";

$color = array("red","green","blue","yellow");
foreach($color as $value){
    echo " $value <br/>";
}

echo"<br/>";

$color = array("red","green","blue","yellow");
foreach($color as $key => $value){
    echo $key ." $value <br/>";
}

echo"<br/>";

$color = array("black"=>"red","pink"=>"green","Tim"=>"blue","homer"=>"yellow");
foreach($color as $key => $value){
    echo $key ." $value <br/>";//array associativo
}

echo $color["black"]
?>