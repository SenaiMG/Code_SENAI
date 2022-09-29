<?php
for($x = 0; $x < 10; $x++){
    if($x==4){
        break;
    }
    echo "The number is: $x <br/>";
}

echo"<br/>"; 

for($x = 0; $x < 10; $x++){
    if($x==4){
        continue;
    }
    echo "The number is: $x <br/>";
}
?>