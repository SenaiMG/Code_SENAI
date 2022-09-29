<?php
    $count = 0;
    setcookie("count", $count, time()+600);
?>
<!DOCTYPE html>
<html lang = "pt-br">
    <head>
        <meta charset = "utf-8">
        <title>PHP - Cookiens </title>
    </head>
    <body>
        <h1>Contador de Cookies inicializando com<?php echo " $count" ?></h1>
        <ul>
            <li>Clique aqui: <a href="cookiesincremento.php">Incrementar o contador</a></li>
            <li>Clique aqui: <a href="cookiesdecremento.php">Para destruir o cookie</a></li>
        </ul>
    </body>
</html>
