class Nodo_reporte:
    def __init__(self, nombre,vacio,lleno,hora,fecha):
        self.nombre=nombre
        self.vacio=vacio
        self.lleno=lleno
        self.hora=hora
        self.fecha=fecha
        self.siguiente=None