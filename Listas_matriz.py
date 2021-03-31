from Nodo_matriz import nodo_matrix
nodo=nodo_matrix

class Lista_matrix:
    def __init__(self):
        self.cabeza=None

    def vacio(self):
        if self.cabeza==None:
            return True
        else:
            return False

    def AgregarMatriz(self,nombre,filas,columnas,ruta):
        nuevo=nodo(nombre,filas,columnas,ruta)
        if self.vacio():
            self.cabeza = nuevo
        else:
            nuevo.siguiente=self.cabeza
            self.cabeza=nuevo

    def Buscar_matriz(self,nombre):
        nuevo=self.cabeza
        if nuevo!=None:
            while nuevo.nombre!=nombre:
                if nuevo.siguiente !=None:
                    nuevo = nuevo.siguiente
                else:
                    return "a"
            return nuevo
        else:
            return "b"