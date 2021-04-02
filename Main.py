from tkinter import *
import Principal
import Reporte
p=Principal
original=None
original2=None

def Rot_horizontal():
    impresion=p.Rotacion_horizontal(original)
    Nueva_ventana(impresion)

def Rot_vertical():
    impresion=p.Rotacion_vertical(original)
    Nueva_ventana(impresion)

def Trans():
    impresion=p.Transpuesta(original)
    Nueva_ventana(impresion)

def segunda(texto1,caja2,comando,ok):
    global original2
    nombre = caja2.get()
    original2 = p.lista.Buscar_matriz(nombre)
    if original2 == "a":
        p.MessageBox.showinfo("Error", "Matriz no encontrada")
    else:
        im = original2.lista.Mostrar_matriz()
        matriz=Label(form,text=im)
        matriz.place(x="30",y="280")
        if comando==1:
            impresion=p.Union(original,original2)
        elif comando==2:
            impresion=p.Interseccion(original,original2)
        elif comando==3:
            impresion=p.Diferencia(original,original2)
        else:
            impresion=p.Diferencia_Simetrica(original,original2)
        Nueva_ventana(impresion)
        limpiar = Button(form, text="Limpiar",command=lambda :eliminar(texto1,caja2,ok,matriz,limpiar))
        limpiar.place(x="200", y="255")

def eliminar(texto1,caja2,ok,matriz,limpiar):
    texto1.destroy()
    caja2.destroy()
    ok.destroy()
    matriz.destroy()
    limpiar.destroy()

def Rec(caja2,caja3,caja4,caja5,texto1,texto2,texto3,texto4,aceptar,comando):
    if comando == 1:
        impresion=p.Rectangulo(original,caja2.get(),caja3.get(),caja4.get(),caja5.get())
    else:
        impresion=p.Triangulo_Rectangulo(original,caja2.get(),caja3.get(),caja4.get(),caja5.get())
    Nueva_ventana(impresion)
    caja2.destroy()
    caja3.destroy()
    caja4.destroy()
    caja5.destroy()
    texto1.destroy()
    texto2.destroy()
    texto3.destroy()
    texto4.destroy()
    aceptar.destroy()

def Zona(caja2,caja3,caja4,caja5,texto1,texto2,texto3,texto4,aceptar):
    impresion=p.Limpiar_zona(original,caja2.get(),caja3.get(),caja4.get(),caja5.get())
    Nueva_ventana(impresion)
    caja2.destroy()
    caja3.destroy()
    caja4.destroy()
    caja5.destroy()
    texto1.destroy()
    texto2.destroy()
    texto3.destroy()
    texto4.destroy()
    aceptar.destroy()

def Insertar(posicionx,posiciony,longitud,aceptar,condicion,texto1,texto2,texto3):
    if condicion==1:
        impresion=p.Linea_Horizontal(original,posicionx.get(),posiciony.get(),longitud.get())
    else:
        impresion=p.Linea_Vertical(original,posicionx.get(),posiciony.get(),longitud.get())
    Nueva_ventana(impresion)
    posicionx.destroy()
    posiciony.destroy()
    longitud.destroy()
    aceptar.destroy()
    texto1.destroy()
    texto2.destroy()
    texto3.destroy()

def horizontal():
    global original
    nombre=caja1.get()
    original=p.lista.Buscar_matriz(nombre)
    if original == "a":
        p.MessageBox.showinfo("Error","Matriz no encontrada")
    elif original == "b":
        p.MessageBox.showinfo("Error", "No ha cargado ningun documento")
    else:
        im = original.lista.Mostrar_matriz()
        matriz=Label(form,text=im)
        matriz.place(x="40",y="50")
        limpiar = Button(form, text="Limpiar",command=matriz.destroy)
        limpiar.place(x="240", y="15")

def Nueva_ventana(accion):
    form2=Tk()
    form2.title("Operaciones")
    form2.iconbitmap("icono.ico")
    Label(form2, text=accion).place(x="40",y="50")

def Limpiar():
    texto1=Label(form,text="Posicion x Inicial")
    texto1.place(x="30",y="300")
    caja2=Entry(form)
    caja2.place(x="30",y="320")
    texto2=Label(form,text="Posicion y Inicial")
    texto2.place(x="180",y="300")
    caja3=Entry(form)
    caja3.place(x="180",y="320")
    texto3=Label(form,text="Posicion x Final")
    texto3.place(x="30",y="340")
    caja4=Entry(form)
    caja4.place(x="30",y="360")
    texto4=Label(form,text="Posicion y Final")
    texto4.place(x="180",y="340")
    caja5=Entry(form)
    caja5.place(x="180",y="360")
    aceptar=Button(form, text="Aceptar",command=lambda:Zona(caja2,caja3,caja4,caja5,texto1,texto2,texto3,texto4,aceptar))
    aceptar.place(x="330",y="335")

def Agregar(condicion):
    texto1 = Label(form, text="Posicion x")
    texto1.place(x="30", y="300")
    caja2 = Entry(form)
    caja2.place(x="30", y="320")
    texto2 = Label(form, text="Posicion y")
    texto2.place(x="180", y="300")
    caja3 = Entry(form)
    caja3.place(x="180", y="320")
    texto3 = Label(form, text="Longitud")
    texto3.place(x="30", y="340")
    caja4 = Entry(form)
    caja4.place(x="30", y="360")
    aceptar = Button(form, text="Aceptar",command=lambda: Insertar(caja2, caja3, caja4,aceptar,condicion,texto1,texto2,texto3))
    aceptar.place(x="330", y="335")

def Rectangulo(comando):
    texto1 = Label(form, text="Posicion x")
    texto1.place(x="30", y="300")
    caja2 = Entry(form)
    caja2.place(x="30", y="320")
    texto2 = Label(form, text="Posicion y")
    texto2.place(x="180", y="300")
    caja3 = Entry(form)
    caja3.place(x="180", y="320")
    texto3 = Label(form, text="Longitud x")
    texto3.place(x="30", y="340")
    caja4 = Entry(form)
    caja4.place(x="30", y="360")
    texto4 = Label(form, text="Longitud y")
    texto4.place(x="180", y="340")
    caja5 = Entry(form)
    caja5.place(x="180", y="360")
    aceptar = Button(form, text="Aceptar",command=lambda: Rec(caja2, caja3, caja4,caja5,aceptar,texto1,texto2,texto3,texto4,comando))
    aceptar.place(x="330", y="335")

def Segunda_matriz(comando):
    texto1=Label(form,text="Segunda matriz")
    texto1.place(x="30",y="240")
    caja2=Entry(form)
    caja2.place(x="30",y="260")
    ok=Button(form,text="OK",command=lambda : segunda(texto1,caja2,comando,ok))
    ok.place(x="170",y="255")

form = Tk()#formulario
form.title("Proyecto 2")#Nombre al formulario
form.iconbitmap("icono.ico")#agregar icono
m=Menu(form)#barra de menu desplegable
form.config(menu=m,width="450",height="450")#agregar al formulario barra desplegable
archivo=Menu(m,tearoff=0)#submenu
archivo.add_command(label="Cargar archivo", command=p.Cargar_Archivo)#Opcion del menu
operaciones=Menu(m,tearoff=0)
operaciones.add_command(label="Rotación Horizontal", command=Rot_horizontal)
operaciones.add_command(label="Rotación Vertical",command=Rot_vertical)
operaciones.add_command(label="Transpuesta", command=Trans)
operaciones.add_command(label="Limpiar zona", command=Limpiar)
operaciones.add_command(label="Agregar linea horizontal",command=lambda: Agregar(1))
operaciones.add_command(label="Agregar linea vertical",command=lambda: Agregar(2))
operaciones.add_command(label="Agregar rectángulo",command=lambda: Rectangulo(1))
operaciones.add_command(label="Agregar triángulo rectángulo", command=lambda : Rectangulo(2))
reportes=Menu(m,tearoff=0)
reportes.add_command(label="Generar reporte",command=Reporte.Generar_reporte)
ayuda=Menu(m,tearoff=0)
ayuda.add_command(label="Datos del estudiante", command=lambda :p.MessageBox.showinfo("Datos Programador","Daniel Enrique Coti Peñate \n201801146"))
ayuda.add_command(label="Documentación del programa")
combinadas=Menu(m,tearoff=0)
combinadas.add_command(label="Unión",command=lambda : Segunda_matriz(1))
combinadas.add_command(label="Intersección",command=lambda : Segunda_matriz(2))
combinadas.add_command(label="Diferencia",command=lambda : Segunda_matriz(3))
combinadas.add_command(label="Diferencia Simetrica",command=lambda : Segunda_matriz(4))
caja1=Entry(form)#entry es una caja de texto
caja1.place(x="30",y="20")#Dimensiones
aceptar=Button(form,text="Aceptar",command=horizontal)
aceptar.place(x="180",y="15")
m.add_cascade(label="Cargar archivo",menu=archivo)
m.add_cascade(label="Operaciones", menu=operaciones)
m.add_cascade(label="Operaciones Combinadas", menu=combinadas)
m.add_cascade(label="Reporte", menu=reportes)
m.add_cascade(label="Ayuda", menu=ayuda)
form.mainloop()#abrir formulario, siempre va de ultimo