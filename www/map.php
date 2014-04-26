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
				<div id="canvas_labels">
 					<p>Accidents de la route en france depuis 6 ans. (2005-2011)</p>
 				</div>
				<div id="canvas_france" >
  					<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/mootools/1.2.4/mootools-yui-compressed.js"></script>
  					<script src="csvToArray.v2.1.min.js" charset="utf-8" ></script>
  					<script src="raphael-min.js" charset="utf-8" ></script>
  					<script src="map.js" charset="utf-8" ></script>
  					<script type="text/javascript"></script>
 				</div>
			</div>
		</div>
		<?php include("footer.php");?>
	</body>
</html>
