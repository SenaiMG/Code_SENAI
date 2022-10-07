<?php
    // definição e criação da Classe
    class MinhaClasse{
      // propriedade da Classe criação de uma variavel publica
        public $message = "Olá Mundo! Estou programando em O.O.!";
    }

    $obj = new MinhaClasse; // instanciação de um objeto da Classe MinhaClasse

    var_dump($obj); // mostra que foi criado um objeto

    echo $obj->message; // chama a variavel publica da classe

?>
