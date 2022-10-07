<?php
    class MinhaClasse
    {
        public $prop1 = "Sou uma propriedade de classe!";
        public $prop2 = "===> outra propriedade de classe!";
        public function __construct()
        {
            echo 'A classe "', __CLASS__, '" foi instanciada!<br />';
        }
        public function __destruct()
        {
            echo 'A classe "', __CLASS__, '" foi destruída.<br />';
        }
        public function __toString()
        {
            echo "Usando o método __toString: ";
            return $this->getProperty();
        }
        public function setProperty($novoValor)
        {
            $this->prop1 = $novoValor;
        }
        public function getProperty()
        {
            return $this->prop1 . "<br />" . $this->prop2 . "<br />";
        }
    }
    // Cria um novo objeto
    $obj = new MinhaClasse;
    // Mostra o objeto como uma string vai automaticamente chamar o metodo toString
    echo $obj;
    // Destrói o objeto
    unset($obj);
    // Mostra uma mensagem ao final do arquivo
    echo "Fim do arquivo.<br />";
?>
