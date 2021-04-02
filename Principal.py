import xml.etree.ElementTree as et
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as MessageBox
from Listas_matriz import Lista_matrix
from Lista_ortogonal import Lista_orto
from datetime import datetime
import Reporte
now=datetime.now()
lista=Lista_matrix()
raiz=""

def Cargar_Archivo():
    file=askopenfilename(filetypes=[("archivos","*.xml")])#Aperrtura ventana emergente
    if file != "":
        file=et.parse(file)#generar parseo de ruta para leer archivo .xml
        global raiz
        raiz=file.getroot()#Sirve para dar la raiz del archivo ElementTree
        Leer_archivo(raiz)
    else:
        MessageBox.showinfo("Error", "No se selecciono ningun archivo")

def Leer_archivo(raiz):
    for matriz in raiz:
        for dato in matriz:
            if dato.tag=="nombre":
                nombre=dato.text
            elif dato.tag == "filas":
                filas=dato.text
            elif dato.tag == "columnas":
                columnas=dato.text
            elif dato.tag=="imagen":
                imagen=dato.text
        lista.AgregarMatriz(nombre,filas,columnas,imagen)

def Rotacion_horizontal(original):
    fecha = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    hora = str(now.hour) + ":" + str(now.minute)
    list=Lista_orto()
    fila=int(original.filas)
    aux = 0
    while fila!=0:
        aux += 1
        for a in range(1,int(original.columnas)+1):
            dato=original.lista.Buscar(fila,a)
            list.Ingresar_datos(dato,aux,a)
        fila=fila-1
    Reporte.operaciones.Ingresar_datos(fecha,hora,original.nombre,"Rotacion Horizontal","")
    return list.Mostrar_matriz()

def Rotacion_vertical(original):
    fecha = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    hora = str(now.hour) + ":" + str(now.minute)
    list=Lista_orto()
    for a in range(1, int(original.filas) + 1):
        aux = 0
        columna = int(original.columnas)
        while columna != 0:
            aux += 1
            dato=original.lista.Buscar(a,columna)
            list.Ingresar_datos(dato,a,aux)
            columna = columna - 1
    Reporte.operaciones.Ingresar_datos(fecha, hora, original.nombre, "Rotacion Vertical", "")
    return list.Mostrar_matriz()

def Transpuesta(original):
    fecha = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    hora = str(now.hour) + ":" + str(now.minute)
    list = Lista_orto()
    aux=0
    for a in range(1, int(original.columnas) + 1):
        aux += 1
        for b in range(1,int(original.filas)+1):
            dato = original.lista.Buscar(b, a)
            list.Ingresar_datos(dato,aux, b)
    Reporte.operaciones.Ingresar_datos(fecha, hora, original.nombre, "Transpuesta", "")
    return list.Mostrar_matriz()

def Limpiar_zona(original,inicialx,inicialy,finalx,finaly):
    fecha = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    hora = str(now.hour) + ":" + str(now.minute)
    list=Lista_orto()
    for a in range(1,int(original.filas)+1):
        for b in range(1, int(original.columnas)+1):
            if (a>=int(inicialx)) and (a<=int(finalx)):
                if (b>=int(inicialy)) and (b<=int(finaly)):
                    list.Ingresar_datos("#",a,b)
                else:
                    dato = original.lista.Buscar(a, b)
                    list.Ingresar_datos(dato, a, b)
            else:
                dato=original.lista.Buscar(a,b)
                list.Ingresar_datos(dato,a,b)
    Reporte.operaciones.Ingresar_datos(fecha, hora, original.nombre, "Limpiar Zona", "")
    return list.Mostrar_matriz()

def Linea_Horizontal(original,inicialx,inicialy,finalx):
    fecha = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    hora = str(now.hour) + ":" + str(now.minute)
    list=Lista_orto()
    for a in range(1, int(original.filas) + 1):
        for b in range(1, int(original.columnas) + 1):
            if (b>=int(inicialx)) and (b<=int(inicialx)+int(finalx)-1) and (a==int(inicialy)):
                list.Ingresar_datos("#",a,b)
            else:
                dato=original.lista.Buscar(a,b)
                list.Ingresar_datos(dato,a,b)
    Reporte.operaciones.Ingresar_datos(fecha, hora, original.nombre, "Linea Horizontal", "")
    return list.Mostrar_matriz()

def Linea_Vertical(original,inicialx,inicialy,longitud):
    fecha = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    hora = str(now.hour) + ":" + str(now.minute)
    list = Lista_orto()
    for a in range(1, int(original.filas) + 1):
        for b in range(1, int(original.columnas) + 1):
            if (a >= int(inicialx)) and (a <= int(inicialx) + int(longitud) - 1) and (b == int(inicialy)):
                list.Ingresar_datos("#", a, b)
            else:
                dato = original.lista.Buscar(a, b)
                list.Ingresar_datos(dato, a, b)
    Reporte.operaciones.Ingresar_datos(fecha, hora, original.nombre, "Linea Vertical", "")
    return list.Mostrar_matriz()

def Rectangulo(original,inicialx,inicialy,longitudx,longitudy):
    fecha = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    hora = str(now.hour) + ":" + str(now.minute)
    list=Lista_orto()
    val=0
    cont=0
    for a in range(1, int(original.filas) + 1):
        for b in range(1, int(original.columnas) + 1):
            if (b==int(inicialx)) and (a==int(inicialy)):
                list.Ingresar_datos("#",a,b)
                val+=1
            elif val==1 and (cont<(int(longitudx)-1)):
                list.Ingresar_datos("#",a,b)
                cont+=1
            elif (b==int(inicialx) and (a>=int(inicialy)) and (a<(int(inicialy)+int(longitudy)-1))):
                list.Ingresar_datos("#",a,b)
            elif(b==(int(inicialx)+int(longitudx)-1) and (a>=int(inicialy)) and (a<(int(inicialy)+int(longitudy)-1))):
                list.Ingresar_datos("#",a,b)
            elif(a==(int(inicialy)+int(longitudy)-1) and (b<(int(inicialx)+int(longitudx)))) and (b>=int(inicialx)):
                list.Ingresar_datos("#",a,b)
            else:
                dato=original.lista.Buscar(a,b)
                list.Ingresar_datos(dato,a,b)
    Reporte.operaciones.Ingresar_datos(fecha, hora, original.nombre, "Rectangulo", "")
    return list.Mostrar_matriz()

def Triangulo_Rectangulo(original,inicialx,inicialy,longitudx,longitudy):
    fecha = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    hora = str(now.hour) + ":" + str(now.minute)
    list=Lista_orto()
    cont=0
    for a in range(1, int(original.filas) + 1):
        for b in range(1, int(original.columnas) + 1):
            if (b==int(inicialx) and (a>=int(inicialy)) and (a<(int(inicialy)+int(longitudy)-1))):
                list.Ingresar_datos("#", a, b)
                cont+=1
            elif (a == (int(inicialy) + int(longitudy) - 1) and (b < (int(inicialx) + int(longitudx)))) and (b >= int(inicialx)):
                list.Ingresar_datos("#", a, b)
                cont=b
            elif (b==(int(inicialx)+cont-1) and (b>int(inicialx)) and (a<(int(inicialy)+int(longitudy)-1))):
                list.Ingresar_datos("#",a,b)
            else:
                dato=original.lista.Buscar(a,b)
                list.Ingresar_datos(dato,a,b)
    Reporte.operaciones.Ingresar_datos(fecha, hora, original.nombre, "Triangulo Rectangulo", "")
    return list.Mostrar_matriz()

def Union(original,original2):
    fecha = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    hora = str(now.hour) + ":" + str(now.minute)
    list=Lista_orto()
    if original.filas<original2.filas:
        filas=int(original.filas)
    else:
        filas=int(original2.filas)
    if original.columnas<original2.columnas:
        columnas=int(original.columnas)
    else:
        columnas=int(original2.columnas)
    for a in range(1,filas+1):
        for b in range(1,columnas+1):
            if (b<=int(original.columnas)and (a<=int(original.filas))):
                dato1=original.lista.Buscar(a,b)
            else:
                dato1="-"
            if (b<=int(original2.columnas)and (a<=int(original2.filas))):
                dato2=original2.lista.Buscar(a,b)
            else:
                dato2="-"
            if (str(dato1)=="*") or (str(dato2)=="*"):
                list.Ingresar_datos("*",a,b)
            else:
                list.Ingresar_datos("-",a,b)
    Reporte.combinadas.Ingresar_datos(fecha,hora,original.nombre,original2.nombre,"Union")
    return list.Mostrar_matriz()

def Interseccion(original,original2):
    fecha = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    hora = str(now.hour) + ":" + str(now.minute)
    list = Lista_orto()
    if original.filas < original2.filas:
        filas = int(original.filas)
    else:
        filas = int(original2.filas)
    if original.columnas < original2.columnas:
        columnas = int(original.columnas)
    else:
        columnas = int(original2.columnas)
    for a in range(1, filas + 1):
        for b in range(1, columnas + 1):
            if (b <= int(original.columnas)and (a<=int(original.filas))):
                dato1 = original.lista.Buscar(a, b)
            else:
                dato1 = "-"
            if (b <= int(original2.columnas)and (a<=int(original2.filas))):
                dato2 = original2.lista.Buscar(a, b)
            else:
                dato2 = "-"
            if (str(dato1) == "*") and (str(dato2) == "*"):
                list.Ingresar_datos("*", a, b)
            else:
                list.Ingresar_datos("-", a, b)
    Reporte.combinadas.Ingresar_datos(fecha, hora, original.nombre, original2.nombre, "Interseccion")
    return list.Mostrar_matriz()

def Diferencia(original,original2):
    fecha = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    hora = str(now.hour) + ":" + str(now.minute)
    list = Lista_orto()
    if original.filas < original2.filas:
        filas = int(original.filas)
    else:
        filas = int(original2.filas)
    if original.columnas < original2.columnas:
        columnas = int(original.columnas)
    else:
        columnas = int(original2.columnas)
    for a in range(1, filas + 1):
        for b in range(1, columnas + 1):
            if (b <= int(original.columnas) and (a<=int(original.filas))):
                dato1 = original.lista.Buscar(a, b)
            else:
                dato1 = "-"
            if (b <= int(original2.columnas) and (a<=int(original2.filas))):
                dato2 = original2.lista.Buscar(a, b)
            else:
                dato2 = "-"
            if (str(dato1) == "*") and (str(dato2) == "-"):
                list.Ingresar_datos("*", a, b)
            else:
                list.Ingresar_datos("-", a, b)
    Reporte.combinadas.Ingresar_datos(fecha, hora, original.nombre, original2.nombre, "Diferencia")
    return list.Mostrar_matriz()

def Diferencia_Simetrica(original,original2):
    fecha = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    hora = str(now.hour) + ":" + str(now.minute)
    list = Lista_orto()
    if original.filas < original2.filas:
        filas = int(original.filas)
    else:
        filas = int(original2.filas)
    if original.columnas < original2.columnas:
        columnas = int(original.columnas)
    else:
        columnas = int(original2.columnas)
    for a in range(1, filas + 1):
        for b in range(1, columnas + 1):
            if (b <= int(original.columnas) and (a <= int(original.filas))):
                dato1 = original.lista.Buscar(a, b)
            else:
                dato1 = "-"
            if (b <= int(original2.columnas) and (a <= int(original2.filas))):
                dato2 = original2.lista.Buscar(a, b)
            else:
                dato2 = "-"
            if str(dato1) != str(dato2):
                list.Ingresar_datos("*", a, b)
            else:
                list.Ingresar_datos("-", a, b)
    Reporte.combinadas.Ingresar_datos(fecha, hora, original.nombre, original2.nombre, "Diferencia Simétrica")
    return list.Mostrar_matriz()