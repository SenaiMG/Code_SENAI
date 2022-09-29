<?php

    $x = 5; //global scope
    function myTest(){
        //usa x dentro dessa função irá gerar um erro
        echo"<p>Variavel x dentro da função: $x</p>";
    }

    myTest();
    echo"<p>Variavel x fora da função: $x</p>";

    //Exemplo 01
    $x = 5;
    $y = 10;

    function myglobal(){
        global $x, $y;
        $y = $x + $y;
    }

    myGlobal();
    echo $y; //saida 15

    echo"<br>";

    //Exemplo 02
    $x = 5;
    $y = 10;

    function myWord(){
       $GLOBALS['y'] = $GLOBALS['x'] + $GLOBALS['y'];
    }

    myWord();
    echo $y; //saida 15

?>