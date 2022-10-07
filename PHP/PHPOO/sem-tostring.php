<?php
     class MinhaClasse
    {
        public $prop1 = "Sou uma propriedade de classe!";
        public function __construct()
        {
            echo 'A classe "', __CLASS__, '" foi instanciada!<br />';
        }
        public function __destruct()
        {
            echo 'A classe "', __CLASS__, '" foi destruída.<br />';
        }
        public function setProperty($novoValor)
        {
            $this->prop1 = $novoValor;
        }
        public function getProperty()
        {
            return $this->prop1 . "<br />";
        }
    }
    // Cria um novo objeto
    $obj = new MinhaClasse;
    // Mostra o objeto como uma string e vai da um erro pois é um objeto não uma string
    echo $obj;
    // Destrói o objeto
    unset($obj);
    // Mostra uma mensagem ao final do arquivo
    echo "Fim do arquivo.<br />";
    // Sem o método __toString(), tentar mostrar um objeto como uma string resulta em um erro fatal.
    // Tente mostrar um objeto, usando echo, sem o método mágico
?>
