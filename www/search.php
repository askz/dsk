<!DOCTYPE html>
<html>

	<head>
		<title>Driving Safety Keeper</title>
		<link rel="stylesheet" href="search.css" />
		<meta charset="utf-8" />
	</head>

	<body>
		<div id="global">
			<?php include("header.php");?>
			<div id="contenu">
				
					<section>
					 	<form method="post" action="./search.php">
					 		<h3>Faire une recherche en fonction du nom de ville, du nombre d'accidents...</h3>
					   		<label for="search">Rechercher :</label>
					   		<input id="search" name="search" type="search" placeholder="Recherche"/>
					   		<button type="submit">Recherche</button>
					   		<br />
					   		<input type="checkbox" name="nb_acc" value="nb_acc">Nombre d'accidents</input>
					   		<input type="checkbox" name="nb_ble" value="">Nombre de bléssés</input>
					   		<input type="checkbox" name="test" value="">test</input>

					   </form>
					</section>					
			</div>
		</div>
		<?php include("footer.php");?>
	</body>
</html>
