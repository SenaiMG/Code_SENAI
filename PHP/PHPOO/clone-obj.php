<?php
    class MinhaClasse
    {
        public $property = "Sou uma propriedade de classe!";

        // metodo construtor
        public function __construct(){
            echo 'A classe "', __CLASS__, '" foi instanciada!<br />';
        }
        public function __clone()
        {
            echo "O objeto foi clonado! <br />";
        }
        public function setProperty($newValue)
        {
            $this->property = $newValue;
        }
        public function getProperty()
        {
            return $this->property;
        }
    }
    // Cria um novo objeto
    $obj = new MinhaClasse;
    // Mostra o valor de $property
    echo $obj->getProperty();
    // clone o objeto criado
    $clone = clone $obj;
    echo "<br>====== Objetos Criados ====== <br>";
    echo "Objeto 01: ". var_dump($obj) . "<br>";
    echo "Objeto 02: ". var_dump($clone) . "<br>";
    // Mostra uma mensagem ao final do arquivo
    echo "Fim do arquivo.<br />";
?>
