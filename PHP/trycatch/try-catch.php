<?php
//SEM try...catch
function divide($dividend, $divisor){
    if($divisor == 0){
        throw new Exception("Divisor by zero");
    }
    return $dividend/$divisor;
}
//echo divide(5,0);
/*Exibe:
Fatal error: Uncaught Exception: Divisor by zero in C:\xampp\htdocs\programacao\diogo-php\execucao\try-catch
.php:4 Stack trace: #0 C:\xampp\htdocs\programacao\diogo-php\execucao\try-catch.php(8): divide(5, 0) #1 {main}
thrown in C:\xampp\htdocs\programacao\diogo-php\execucao\try-catch.php on line 4*/

echo"<br/>";
echo"<br/>";

//COM try...catch
function divide2($dividend, $divisor){
    if($divisor == 0){
        throw new Exception("Divisor by zero");
    }
    return $dividend/$divisor;
}
try{
    echo divide2(5,0);
}catch(Exception $e){
    echo"Unable to divide.";
}


echo"<br/>";
echo"<br/>";

//COM try...catch...finally
function divide3($dividend, $divisor){
    if($divisor == 0){
        throw new Exception("Divisor by zero");
    }
    return $dividend/$divisor;
}
try{
    echo divide3(5,0);
}catch(Exception $e){
    echo"Unable to divide.";
}finally{
    echo"Process complete.";
}

echo"<br/>";
echo"<br/>";

function divide4($dividend, $divisor){
    if($divisor == 0){
        throw new Exception("Divisor by zero",1);
    }
    return $dividend/$divisor;
}
try{
    echo divide4(5,0);
}catch(Exception $ex){
    $code = $ex ->getCode();
    $message = $ex ->getMessage();
    $file = $ex ->getFile();
    $line = $ex ->getLine();
    echo "Exception trown in $file online $line: [Code $code]
    $message";
}
?>