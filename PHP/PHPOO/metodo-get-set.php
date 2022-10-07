<?php
    class MinhaClasse
    {
        private $message = "Sou uma propriedade de classe!";

        public function setMessage($msg)
        {
            $this->message = $msg;
        }

        public function getMessage()
        {
            return $this->message;
        }
    }
    $obj = new MinhaClasse;
    echo $obj->getMessage(); // Lê o valor da propriedade
    echo "<br />";
    $obj->setMessage("Estou alterando parametros por get e set!"); // Atribui um novo valor
    echo "<br />";
    echo $obj->getMessage(); // Lê o valor novamente para mostrar a mudança
?>
