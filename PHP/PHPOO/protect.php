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
        public function __toString()
        {
            echo "Usando o método toString: ";
            return $this->getProperty();
        }
        public function setProperty($novoValor)
        {
            $this->prop1 = $novoValor;
        }
        protected function getProperty()
        {
            return $this->prop1 . "<br />";
        }
    }

    class MinhaOutraClasse extends MinhaClasse
    {
        public function __construct()
        {
            parent::__construct();
            echo "Um novo construtor em " . __CLASS__ . ".<br />";
        }

        public function newMethod()
        {
            echo "De um novo método na classe " . __CLASS__ . ".<br />";
        }
    }

    // Cria um novo objeto
    $newobj = new MinhaOutraClasse;

    // Tentativa de invocar um método protegido fora da classe
    echo $newobj->getProperty();

?>
