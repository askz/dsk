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
					 	<form>
					 		<h3>Faire une recherche en fonction du nom de ville, du nombre d'accidents...</h3>
					   		<label for="search">Rechercher :</label>
					   		<input id="search" type="search" placeholder="Recherche"/>
					   		<input type="button" name="button" value="GO !"/>
					   		<br />
					   		<input type="checkbox" name="choix1" value="nb_acc">Nombre d'accidents</input>
					   		<input type="checkbox" name="choix2" value="">Nombre de bléssés</input>
					   		<input type="checkbox" name="choix3" value="">test</input>
					   </form>
					</section>					
			</div>
		</div>
		<?php include("footer.php");?>
	</body>
</html>
