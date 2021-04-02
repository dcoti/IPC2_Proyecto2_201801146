class Nodo_reporte:
    def __init__(self,fecha, hora,nombre ,lleno,vacio):
        self.nombre=nombre
        self.vacio=vacio
        self.lleno=lleno
        self.hora=hora
        self.fecha=fecha
        self.siguiente=None