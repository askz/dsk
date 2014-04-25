<?php
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