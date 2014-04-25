<?php
error_reporting(E_ALL);

$m = new Mongo('localhost');

$collection = $m->accidents;

$cursor = $collection->find();

 foreach ($cursor as $obj)
 {
 	var_dump($obj);
 }