<?php
    function myTest(){
    $x = 5; //local scope

        echo"<p>Variavel x dentro da função: $x</p>";

    }
    myTest();
    //usar x fora da função irá gerar um erro
    echo"<p>Variavel x fora da função: $x</p>";

?>
