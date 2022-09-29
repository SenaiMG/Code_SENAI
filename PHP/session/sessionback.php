<?php
 ob_start(); //função que os dados devem ser guardados em memoria 
    $login = 'Igor'; //armazem o usuario dentro da variavel $login
    $senha = 1234;// armazena  a senha detro da variavel $senha
    
    //se o usuario e asenha conferirem com os valores registrados
    if($login == $_POST['usuario'] && $senha == $_POST['password'])
    //entao execute isto
    {
        //antes de redirecionarmos 
        //vamos salvar  algumas informaçoes para utilizar depos
        //primeiro a variavel $validacao recebe o valor 1
        // usarmos esse  variavel para verificar se ele esta
        //logado, se o  usuario nao tiver o valor  1 nesse variavel ele nao eata
        //logado !
        $validacao = "1";

        $usuario = $_POST['usuario'];

        session_start();

        $_SESSION['usuario'] = $usuario;
        $_SESSION['validacao'] = $validacao;

        header ("Location: sessionrestrict.php");
    }else {
        header ("Location: senssionnegado.php");
    }
?>