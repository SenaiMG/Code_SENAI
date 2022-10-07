<?php
    class MinhaClasse
    {
        public $message = "Sou uma propriedade de classe!";

        public function setMessage($msg) // método para adicionar e atualizar a propriedade
        {
            $this->message = $msg;
        }

        public function getMessage() // método para pegar o valor da propriedade
        {
            return $this->message . "<br />";
        }
    }
    $obj = new MinhaClasse; // cria novo objeto
    echo $obj->message; // mostra o conteúdo da propriedade do objeto
?>
