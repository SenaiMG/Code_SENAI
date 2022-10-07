<?php
    class MinhaClasse
    {
        public $prop1 = "Sou uma propriedade de classe!";
        public static $count = 0;
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
        public function setProperty($newval)
        {
            $this->prop1 = $newval;
        }
        private function getProperty()
        {
            return $this->prop1 . "<br />";
        }
        public static function plusOne()
        {
            return "O valor é " . ++self::$count . ".<br />";
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

        public function callProtected()
        {
            return $this->getProperty();
        }
    }
    do
    {
        // Invoca o método plusOne sem instanciar a classe MinhaClasse
        echo MinhaClasse::plusOne();
    } while ( MinhaClasse::$count < 10 );

?>
