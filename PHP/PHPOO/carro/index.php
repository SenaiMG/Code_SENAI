<?php
    // inclusão das classes
    include_once("Carro.php");
    include_once("Fiat.php");
    include_once("Ford.php");
    include_once("Volks.php");
    // tag HTML
    echo("<pre>");
    // instanciação dos objetos
    $fiat  = new Fiat("Siena");
    $ford  = new Ford("Fusion");
    $volks = new Volks("Virtus");
    // apresentação das propriedades dos objetos
    var_dump($fiat);
    var_dump($ford);
    var_dump($volks);
    // cálculo dos valores dos objetos
    var_dump($fiat->calculaPreco());
    var_dump($ford->calculaPreco());
    var_dump($volks->calculaPreco());
    // fechamento da tag HTML
    echo("</pre><br><br>");
    // instanciação de objetos utilizando novos métodos
    $Celta = new Carro("Celta");
    $Celta->cadastrarCarro("Chevrolet","Celta","2011","Prata","25000","12");
    $Celta->apresentarCarro("red");
    $Prisma = new Carro("Prisma");
    $Prisma->cadastrarCarro("Chevrolet","Prisma","2015","Vermelho","40000","15");
    $Prisma->apresentarCarro("gray");
?>