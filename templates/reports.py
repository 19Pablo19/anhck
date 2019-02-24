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
		margin-top:-190px;
		padding:5px;
        text-align:center;
        background-color: #e6fff7;
        padding-top:15px;
	}
  </style>
  </head>
  <body>
    <div class="centrar">
    <form action="{{ url_for('allreports') }}" method="POST">
  <label for="respuesta1">¿Dónde ha sucedido?</label><p>Recinto escolar y/o alrededores</p><br>
  <label for="respuesta2">Suceso:</label><p>Pelea</p><br>
  <label for="respuesta3">¿Quiénes han participado?</label><p>Varios alumnos (=2)</p><br>
  <label for="respuesta4">Resultado:</label><p>Arañazos</p><br>
  <label for="respuesta5">¿Ha sido necesaria asistencia médica?</label><p>Sí</p><br>
  <label for="respuesta6">Esa asistencia ha sido</label><p>Interna del propio centro</p><br>



<input type="submit" value="Enviar" class="button is-primary" id="button" style="margin-top: 10px;">
</form>
</div>
  </body>
</html>
