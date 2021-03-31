class nodo_ortogonal:
    def __init__(self,dato, fila, columna):
        self.dato=dato
        self.columna=columna
        self.fila=fila
        self.siguiente=None
        self.anterior=None
        self.arriba=None
        self.abajo=None