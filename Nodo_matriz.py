from Lista_ortogonal import Lista_orto
import Reporte
from datetime import datetime
now=datetime.now()
class nodo_matrix:
    def __init__(self,nombre, filas, columnas, ruta):
        self.nombre=nombre
        self.columnas=columnas
        self.filas=filas
        self.ruta=ruta
        self.siguiente=None
        self.lista=Lista_orto()
        aux=int(self.columnas)
        cont=1
        val=1
        vacio=0
        lleno=0
        fecha = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
        hora = str(now.hour) + ":" + str(now.minute)
        for a in self.ruta:
            if (a != "\n") and (a !="\t"):
                if a=="*":
                    lleno+=1
                else:
                    vacio+=1
                if cont<= aux:
                    self.lista.Ingresar_datos(a,val,cont)
                    cont=cont+1
                else:
                    cont=1
                    val+=1
                    self.lista.Ingresar_datos(a, val, cont)
                    cont+=1
        Reporte.matriz.Ingresar_datos(fecha,hora,self.nombre,lleno,vacio)