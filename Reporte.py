import os  #sirve para hacer operaciones en el sistema operativo
from Lista_reporte import Lista_reporte
matriz=Lista_reporte()
operaciones=Lista_reporte()
combinadas=Lista_reporte()

def Generar_reporte():
    file=open("Reporte.html","w")
    file.write("<html>\n")
    file.write("""<!DOCTYPE html>
<!-- saved from url=(0069)https://www.w3schools.com/w3css/tryw3css_templates_photo3.htm#contact -->
<!-- saved from url=(0059)https://www.w3schools.com/w3css/tryw3css_templates_teal.htm -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><title>PROYECTO 2</title>

<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="./W3.CSS Template_files/w3.css">

<link rel="stylesheet" href="./W3.CSS Template_files/w3.css">
<link rel="stylesheet" href="./W3.CSS Template_files/w3-theme-teal.css">
<link rel="stylesheet" href="./W3.CSS Template_files/font-awesome.min.css">
</head><body>

<!-- Header -->
<header class="w3-display-container w3-content w3-center" style="max-width:1500px">
  <img class="w3-image" src="./W3.CSS Template_files/photographer.jpg" alt="Me" width="1500" height="600">
  <div class="w3-display-middle w3-padding-large w3-border w3-wide w3-text-light-grey w3-center">
    <h1 class="w3-hide-medium w3-hide-small w3-xxxlarge">REPORTE</h1>
    <h3 class="w3-hide-medium w3-hide-small">PROYECTO 2</h3>
  </div>
</header>
<br>
<br>

<div class="w3-center">
<h2>TABLA DE MATRICES</h2>
</div>

<!-- TABLA -->
<div class="w3-responsive w3-card-4">
<table class="w3-table w3-striped w3-bordered">
<thead>
<tr class="w3-theme">
<th>FECHA</th>
<th>HORA</th>
<th>NOMBRE MATRIZ</th>
<th>CASILLAS LLENAS</th>
<th>CASILLAS VACIAS</th>
</tr> </thead> <tbody>""")
    ope=matriz.cabeza
    while ope!=None:
        file.write("<tr>")
        file.write("<td>" + ope.fecha+ "</td>")
        file.write("<td>" + ope.hora + "</td>")
        file.write("<td>" + ope.nombre + "</td>")
        file.write("<td>" + str(ope.lleno)+ "</td>")
        file.write("<td>" + str(ope.vacio) + "</td>")
        file.write("</tr>")
        ope=ope.siguiente
    file.write("""</tbody></table></div><br><br>

<div class="w3-center">
<h2>TABLA DE OPERACIONES</h2>
</div>

<!-- TABLA -->
<div class="w3-responsive w3-card-4">
<table class="w3-table w3-striped w3-bordered">
<thead>
<tr class="w3-theme">
<th>FECHA</th>
<th>HORA</th>
<th>NOMBRE MATRIZ</th>
<th>OPERACION</th>
</tr> </thead> <tbody>""")
    global operaciones
    ope = operaciones.cabeza
    while ope != None:
        file.write("<tr>")
        file.write("<td>" + ope.fecha + "</td>")
        file.write("<td>" + ope.hora + "</td>")
        file.write("<td>" + ope.nombre + "</td>")
        file.write("<td>" + str(ope.lleno) + "</td>")
        file.write("</tr>")
        ope = ope.siguiente
    file.write("""</tbody></table></div><br><br>
<div class="w3-center">
<h2>OPERACIONES COMBINADAS</h2>
</div>

<!-- TABLA -->
<div class="w3-responsive w3-card-4">
<table class="w3-table w3-striped w3-bordered">
<thead>
<tr class="w3-theme">
<th>FECHA</th>
<th>HORA</th>
<th>PRIMERA MATRIZ</th>
<th>SEGUNDA MATRIZ</th>
<th>OPERACION</th>
</tr> </thead> <tbody>""")
    ope= combinadas.cabeza
    while ope != None:
        file.write("<tr>")
        file.write("<td>" + ope.fecha + "</td>")
        file.write("<td>" + ope.hora + "</td>")
        file.write("<td>" + ope.nombre + "</td>")
        file.write("<td>" + str(ope.lleno) + "</td>")
        file.write("<td>" + str(ope.vacio) + "</td>")
        file.write("</tr>")
        ope = ope.siguiente
    file.write("""</tbody></table></div><br><br>
<!-- End page content -->
</body></html>""")
    file.close()
    os.startfile("Reporte.html")
