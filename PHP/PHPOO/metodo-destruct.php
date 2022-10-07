<?php
    class MinhaClasse
    {
        public $property = "Sou uma propriedade de classe!";
        public function __construct()
        {
            echo 'A classe "', __CLASS__, '" foi instanciada!<br />';
        }
        public function __destruct()
        {
            echo 'A classe "', __CLASS__, '" foi destruída.<br />';
        }
        public function __clone()
        {
            echo "O objeto foi clonado! <br />";
        }
        public function setProperty($newval)
        {
            $this->property = $newval;
        }
        public function getProperty()
        {
            return $this->property . "<br />";
        }
    }
    // Cria um novo objeto
    $obj = new MinhaClasse;
    // Mostra o valor de $property
    echo $obj->getProperty();
    // Mostra uma mensagem ao final do arquivo
    $clone = clone $obj;
    echo "<br>====== Arquivo carregado ====== <br>";
    echo "Arquivo carregado nesta página: ", __FILE__,"<br>";
    echo "Diretório desta página........: ", __DIR__,"<br>";
    echo "Método desta página: ", __METHOD__,"<br>";
    echo "<br>====== Objetos Criados ====== <br>";
    echo "Objeto 01: ". var_dump($obj) . "<br>";
    echo "Objeto 02: ". var_dump($clone) . "<br>";
    echo "Fim do arquivo.<br />";
    /*
        Quando o fim do arquivo é alcançado, o PHP libera, automaticamente, todos os recursos.
    */
?>
