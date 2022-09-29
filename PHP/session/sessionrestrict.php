<?php
    session_start();
    $validacao = $_SESSION['validacao'];
    $usuario   = $_SESSION['usuario'];
    if ($validacao == "1") 
    {
?>
<html>
    <head>
        <title>Pagina restrita</title>
    </head>
    <body>
        Seja bem vindo(a) <b><?php echo $usuario; ?></b> a pagina testita
        <a href="sessiondestroyer.php">>>> Fazer Logout <<<</a>
    </body>
</html>
<?php
    }
    else
    {
        echo "<a href=sessionnegado.php>Voltar</a>";

    }
?>