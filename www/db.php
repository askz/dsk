<?php
<<<<<<< HEAD
ini_set('display_errors', '1');
=======

error_reporting(E_ALL);

$m = new Mongo('localhost');

$collection = $m->accidents;

$cursor = $collection->find();

 foreach ($cursor as $obj)
 {
 	var_dump($obj);
=======
>>>>>>> 4c592bc6bd76f2bac944e8241e566e97a555b4e6
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
 }