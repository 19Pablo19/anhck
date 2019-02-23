<html>
<head>
  <title>Nombre aplicacion</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.4/css/bulma.min.css">
  <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
  <style>
 .centrar
	{
		position: absolute;
		top:50%;
		left:50%;
		width:400px;
		margin-left:-200px;
		height:300px;
		margin-top:-150px;
		padding:5px;
	}
  </style>
  </head>
  <body>
    <div class="centrar">
    <form action="{{ url_for('report') }}" method="POST">
  <label for="respuesta1">Respuesta 1</label><p>Respuesta</p>
  <label for="respuesta2">Respuesta 2</label><p>Respuesta</p>
  <label for="respuesta3">Respuesta 3</label><p>Respuesta</p>
  <label for="respuesta4">Respuesta 4</label><p>Respuesta</p>
  <label for="respuesta5">Respuesta 5</label><p>Respuesta</p>
  <label for="respuesta6">Respuesta 6</label><p>Respuesta</p>



<input type="submit" value="Echo" class="button is-primary" id="button">
</form>
</div>
  </body>
</html>
