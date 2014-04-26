<?php
<<<<<<< HEAD
error_reporting(E_ALL);

$m = new Mongo('localhost');

$collection = $m->accidents;

$cursor = $collection->find();

 foreach ($cursor as $obj)
 {
 	var_dump($obj);
=======
$m = new Mongo('localhost');


$collection = $m->test->accidents;

$cursor = $collection->find();
echo "lol";
 foreach ($cursor as $obj)
 {
 echo "<p>code : ". $obj['code_comm'];
 echo "</p>\n<p>commune : ". $obj['nom_comm'];
 echo "</p>\n<p>accidents : ". $obj['accidents'];
 echo "</p>";
>>>>>>> 42619df9f333cf12fe1847dd136561226aa7a894
 }