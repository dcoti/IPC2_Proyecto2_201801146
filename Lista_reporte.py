from Nodo_reporte import Nodo_reporte
r=Nodo_reporte

class Lista_reporte:
    def __init__(self):
        self.cabeza=None

    def vacio(self):
        if self.cabeza == None:
            return True
        else:
            return False

    def Ingresar_datos(self,fecha,hora,nombre,lleno,vacio):
        nuevo = r(fecha,hora,nombre,lleno,vacio)
        if self.vacio():
            self.cabeza = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo