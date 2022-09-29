<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
    <input type="text" name="fname">
    <input type="submit" value="submit">
</form>
<?php
    if($_SERVER["REQUEST_METHOD"]=="POST"){

        $name =$_POST['fname'];
        if(empty($name)){
            echo "Name is empty";
        }else{
            echo $name;
        }
    }
?>
</body>
</html>