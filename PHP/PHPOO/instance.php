<?php
    class MinhaClasse{
    private $message = "Estou programando em O.O. e vamos ver instâncias!";
    public function setMessage($value)
    {
        $this->message = $value;
    }
    public function getMessage()
    {
        return $this->message;
    }
    }
    // Cria dois Objetos
    $obj = new MinhaClasse;
    $obj2 = new MinhaClasse;
    // Mostra o valor de $prop1 de ambos os objetos
    echo "Mostra os conteudos instanciados nas variaveis <br/>";
    echo $obj->getMessage();
    echo "<br />";
    echo $obj2->getMessage();
    echo "<br /><br /><br />";
    echo "Fazemos alterações nas intâncias diferentes<br />";
    // Atribui novos valores para ambos os objetos
    $obj->setMessage("Sou da primeira intancia do objeto chamado OBJ!");
    $obj2->setMessage("Pertenço à segunda instância do objeto chamado OBJ2!");
    // Mostra o valor de $prop1 de ambos os objetos
    echo $obj->getMessage();
    echo "<br />";
    echo $obj2->getMessage();
?>
