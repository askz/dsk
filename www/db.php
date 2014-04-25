<?php
$m = new MongoClient();
$db = $m->selectDB('test');

$collection = $db->test->accidents;
 $results = $collection->find();

 print_r($results);