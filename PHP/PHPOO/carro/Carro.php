<?php
    // classe Pai / Mãe
    class Carro {

        // propriedades
        public $marca;
        public $modelo;
        public $ano;
        public $cor;
        public $preco;
        public $taxa;

        // métodos
        public function __construct()
        {
            $this->marca = "indefinida";
            $this->modelo = "indefinido";
            $this->ano = 0;
            $this->cor = "indefinida";
            $this->preco = 40000;
        }

        // gets e sets das propriedades
        // get = atualiza a informação
        // set = lê a informação
        public function getMarca()
        {
            return $this->marca;
        }

        public function setMarca($marca)
        {
            $this->marca = $marca;
        }

        public function getModelo()
        {
            return $this->modelo;
        }

        public function setModelo($modelo)
        {
            $this->modelo = $modelo;
        }

        public function getAno()
        {
            return $this->ano;
        }

        public function setAno($ano)
        {
            $this->ano = $ano;
        }

        // método para calcular o preço do carro
        public function calculaPreco()
        {
            return($this->preco + ($this->preco * $this->taxa / 100));
        }
        // método para completar todas as propriedades do carro
        public function cadastrarCarro($marca,$modelo,$ano,$cor,$preco,$taxa)
        {
            $this->marca = $marca;
            $this->modelo = $modelo;
            $this->ano = $ano;
            $this->cor = $cor;
            $this->preco = $preco;
            $this->taxa = $taxa;
        }
        // método para apresentar todas as características do carro
        public function apresentarCarro($fonte)
        {
            echo "<pre style=\"color:$fonte;\">";
            echo '<br>=====================<br>';
            echo '    DADOS DO CARRO DO MAURÍCIO   <br>';
            echo 'Marca: ', $this->marca , '<br>';
            echo 'Modelo: ', $this->modelo , '<br>';
            echo 'Ano: ', $this->ano , '<br>';
            echo 'Cor: ', $this->cor , '<br>';
            echo 'Preco: ', $this->preco , '<br>';
            echo 'Taxa: ', $this->taxa , '<br>';
            echo "</pre>";
        }
    }

?>