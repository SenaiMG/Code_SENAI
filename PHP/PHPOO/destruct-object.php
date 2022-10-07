<?php
     class MiCl
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
        public function setProperty($nv)
        {
            $this->property = $nv;
        }
        public function getProperty()
        {
            return $this->property . "<br />";
        }
    }
    // Cria um novo objeto
    $obj = new MiCl;
    // Mostra o valor de $property
    echo $obj->getProperty();
    // Destrói o objeto
    unset($obj);
    // Mostra uma mensagem ao final do arquivo
    echo "Fim do arquivo.<br />";
    // Para executar, explicitamente, o método destruidor, você pode destruir o objeto usando a função unset()
?>
