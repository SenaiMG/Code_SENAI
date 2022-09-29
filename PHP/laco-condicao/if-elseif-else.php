<?php
$t = date("H");

echo"<p>The hour(of the server)is ".$t;
echo" ,and will give the fllowing message;</p>";

if($t > "20"){
    echo "Heve a good Morning";
} elseif($t > "20"){
    echo "Heve a good day";
} else{
    echo "Heve a good night";
}
//Exibe Heve a good night
?>