<?php

//$_GLOBAL
$x = 75;
$y = 25;

function addition(){
    $GLOBALS['z'] = $GLOBALS['x'] + $GLOBALS['y'];
}
addition();
echo $z;//Exibe 100

echo"<br/>";
echo"<br/>";
echo"<br/>";

//$_SERVER
echo $_SERVER['PHP_SELF'];
echo"<br/>";
echo $_SERVER['SERVER_NAME'];
echo"<br/>";
echo $_SERVER['HTTP_HOST'];
echo"<br/>";
echo $_SERVER['REMOTE_ADDR'];
echo"<br/>";
echo $_SERVER['HTTP_USER_AGENT'];
echo"<br/>";
echo $_SERVER['SCRIPT_NAME'];



?>