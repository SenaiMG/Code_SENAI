<?php

    class Volks extends Carro {

        public function __construct($modelo)
        {
            parent::__construct();

            $this->setMarca("Ford");
            $this->setModelo($modelo);
            $this->taxa = 15;
        }

        // falta __destruct()
    }

?>