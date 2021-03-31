from Lista_ortogonal import Lista_orto
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
        for a in self.ruta:
            if (a != "\n") and (a !="\t"):
                if cont<= aux:
                    self.lista.Ingresar_datos(a,val,cont)
                    cont=cont+1
                else:
                    cont=1
                    val+=1
                    self.lista.Ingresar_datos(a, val, cont)
                    cont+=1