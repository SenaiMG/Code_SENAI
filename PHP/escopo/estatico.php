<?php

    // Exemplo 0 

    function myTest(){
        static $x = 0;        
        echo $x;
        $x++; 
    }
        
    myTest(); //exibe 0
    myTest(); //exibe 1
    myTest(); //exibe 2

?>