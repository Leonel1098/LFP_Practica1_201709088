from tkinter import *
from tkinter import Tk
from tkinter import filedialog
import tkinter.font as tkFont


def ventana_carga():
    #Abre Ventana para Buscar el archivo .lfp 
    archivo =  filedialog.askopenfilename(initialdir = "/") 
    #Abre el achivo 
    archivo = open(archivo ,'r')
    read = archivo.read()
    print(read)
    archivo.close()
    print("===================================================")
    

ventana = Tk()
ventana.title("Pensum de Estudios")
ventana.geometry("%dx%d+%d+%d" % (600,450,450,150))
ventana.resizable(0,0)


panel_Frame = Frame(ventana)
panel_Frame.pack(side = "top")
panel_Frame.place(width = "600", height = "450")
panel_Frame.config(background = "Black")

label = Label(text = "Nombre del curso: Laboratorio Lenguajes Formales y de Programación B+" , foreground = "White", bg = "black", font = "Modern" )
label.pack()
label.place(x = 45, y = 50,width = 450, height= 30)

label2 = Label(text = "Nombre del Estudiante: Leonel Antonio González García", foreground = "White", bg = "black", font = "Modern")
label2.pack()
label2.place(x = 45, y = 100,width = 340, height= 30)

label3 = Label(text = "Carnet del Estudiante: 201709088", foreground = "White", bg = "black", font = "Modern" )
label3.pack()
label3.place(x = 45, y = 150,width = 220, height= 30)

button = Button(panel_Frame, text="Cargar", command = ventana_carga,  foreground = "white")
button.pack()
button.config(bg = "black")
button.place(x = 50,y = 220,width= 150, height  = 40)

button = Button(panel_Frame, text="Gestionar Cursos",  foreground = "white")
button.pack()
button.config(bg = "black")
button.place(x = 210,y = 220,width= 150, height  = 40)

buttonabrir = Button(panel_Frame, text="Conteo de Créditos", foreground = "white")
buttonabrir.pack()
buttonabrir.config(bg = "black")
buttonabrir.place(x= 370, y= 220, width = 150, height = 40)

buttonabrir = Button(panel_Frame, text="Salir", command = ventana.destroy, foreground = "white")
buttonabrir.pack()
buttonabrir.config(bg = "black")
buttonabrir.place(x= 485, y= 400, width = 100, height = 40)
ventana.mainloop()
