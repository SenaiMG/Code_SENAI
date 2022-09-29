<?php
//Verifica se exite o cookies
if (isset($_COOKIE['count'])) {
    //ajusta para expirar em uma hora;
    //Calcula 60 segundos * 60 minutos - 3600
   setcookie("count", "" , time() - 3600);
   $msg = "Cookie deletado com susseso !!!!!!";
}else{
    $msg = "Cookie não encotrado";
}
?>
<!DOCTYPE html>
<html lang = "pt-br">
    <head>
        <meta charset = "utf-8">
        <title>PHP - Cookiens - Deletar </title>
    </head>
    <body>
        <h1><?php echo "$msg" ?></h1>
        <ul>
            <li>Clique aqui <a href="cookies.php">para voltar a pagina inicial</a></li>
        </ul>
    </body>
</html>
