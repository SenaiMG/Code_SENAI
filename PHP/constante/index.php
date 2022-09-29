<?php
    //case-sensitive nome da constante
    //se eu digitar cost não irá chamar a constante
    define("COST","Professor Igor");
    echo COST;
    // Exibe Professor Igor

    echo"<br/>";

    //case-sensitive nome da constante
    define("cost","Professor Igor");
    echo cost;
    // Exibe Professor Igor
    
    echo"<br/>";

    define("cars", [
        "Alfa Romano",
        "BMW",
        "Toyota"
    ]);
    echo cars[0];
    //Exibe Alfa Romano

    echo"<br/>";

    //define("CONST","Diogo");
    //echo CONST;  !!!ERRADO!!!

    CONST x = 1;
    echo x;

    echo"<br/>";

    define("OI","Progrmador PHP!");

    function myTest(){
        echo OI;
    }

    myTest();
    //Exibe Progrmador PHP!
    
?>