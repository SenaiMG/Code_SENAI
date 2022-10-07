<?php

    class Ford extends Carro {

        public function __construct($modelo)
        {
            parent::__construct();

            $this->setMarca("Ford");
            $this->setModelo($modelo);
            $this->taxa = 20;
        }

        // falta __destruct()

    }

?>