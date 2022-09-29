<?php

//if empty($user) = TRUE, set$status ="anonymous"
echo $status = empty($user) ?"anonymous" : "logged in";

echo"<br/>";

$user = "John Doe";
//if empty($user) = FALSE, set$status ="anonymous"
echo $status = empty($user) ? "anonymous" : "logged in";

echo"<br/>";

//variavel $user se tiver valor em $_Get['user']
//e 'anonymous' se não existir
echo $user = $_GET["user"] ?? "anonymous";
echo"<br/>";
//variavel $color com "red" se $color não existir atribua null
echo $color = $color ?? "red";

?>