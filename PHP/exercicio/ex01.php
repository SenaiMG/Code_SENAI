<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="<?php echo $_SERVER['PHP_SELF'];?>" method="post">
        <input type="number" name="altura">
        <input type="number" name="base">    
        <input type="submit" value="Calcular">
    </form>
    <?php
        function Calcular(){
            if($_SERVER["REQUEST_METHOD"]=="POST"){
                $a = $_POST['altura'];
                $p = $_POST['base'];
    
                $a = $b * $h;
                $p = 2*($b + $h);
            }   
        }
        try{
            echo Calcular($a,$p);
        }catch(Exception $e){
            echo $a;
        }finally{
            echo"Process complete.";
        }
    ?>
</body>
</html>
