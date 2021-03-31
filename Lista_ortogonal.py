from Nodo_ortogonal import nodo_ortogonal
n=nodo_ortogonal

class Lista_orto:
    def __init__(self):
        self.cont=0
        self.cabeza=None

    def vacio(self):
        if self.cabeza == None:
            return True
        else:
            return False

    def Ingresar_datos(self,dato,fila,columna):
        if self.vacio():
            nuevo=n(dato,fila,columna)
            self.cabeza = nuevo
            self.cont+=1
        else:
            aux=self.cabeza
            while(aux.abajo!=None):
                aux=aux.abajo
            if self.cont!=fila:
                self.cont+=1
                nuevo=n(dato,fila,columna)
                aux.abajo=nuevo
                nuevo.arriba=aux
            else:
                while(aux.siguiente!=None):
                    aux=aux.siguiente
                nuevo=n(dato,fila,columna)
                aux.siguiente=nuevo
                nuevo.anterior=aux
                if self.cont>1:
                    aux2=aux.arriba.siguiente
                    aux2.abajo=nuevo
                    nuevo.arriba=aux2

    def Mostrar_matriz(self):
        aux=self.cabeza
        data=""
        while (aux.abajo!=None) or (aux.siguiente!=None):
            data=data+aux.dato
            if aux.siguiente!=None:
                aux=aux.siguiente
            else:
                data=data+"\n"
                if aux.abajo!=None:
                    aux=aux.abajo
                    while aux.anterior!=None:
                        aux=aux.anterior
        data=data+aux.dato
        return  data

    def Buscar(self,fila,columna):
        aux=self.cabeza
        while (aux.abajo!=None) | (aux.siguiente!=None):
            if (aux.fila==int(fila)) and (aux.columna==int(columna)):
                return aux.dato
            elif (aux.fila==int(fila)) | (aux.columna==int(columna)):
                aux=aux.siguiente
                if aux==None:
                    return "_"
            else:
                if (aux.abajo!=None):
                    aux=aux.abajo
                    while aux.anterior!=None:
                        aux=aux.anterior
                else:
                    return "_"
        return aux.dato