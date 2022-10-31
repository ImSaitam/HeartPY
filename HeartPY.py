from cProfile import label
import tkinter as tk
from tkinter import ttk, font
from tkinter import *
import webbrowser as wb#libreria hipervinculo
import serial#libreria python


arduino = serial.Serial('COM4', 9600) #Conexión con arduino

class Proyecto(tk.Tk):#Contiene los metodos de las ventanas
    def __init__(self, window) : #Inicializa el estado de un objeto
        self.wind = window #Almacena la vetana como parametro
        self.wind.title('HeartPY')#Titulo de la ventana
        self.wind.geometry('600x400+375+50') #Cambia el tamaño de la ventana
        self.wind.resizable(False, False) #Elimina la opcion de maximzar la ventana
        self.wind['bg'] ='#b2e2f2'#Cambia el color de la ventana
        self.wind.defaultfont = font.nametofont("TkDefaultFont") #Cambia la fuente default
        self.wind.iconbitmap('C:/Users/every/Desktop/HeartPY/HeartPY/icon.ico') #Cambiar icono de la ventana (cambiar ruta a donde haya sido descargado)
        self.wind.defaultfont.configure(family= "Bahnschrift SemiLight", size=12) #Se elige la fuente default
#Se crea un contenedor en la ventana self.wind
        frame = LabelFrame(self.wind) #Definimos contenedor
        frame.pack(ipady= 20, ipadx = 60, pady=40, anchor= tk.N) #Posicion del contenedor
        frame.config(borderwidth=1, relief='solid')
        frame['bg'] = '#97b8db'#Cambia el color del contenedor
        frame.defaultfont = font.nametofont("TkDefaultFont") #Cambia la fuente default
        frame.defaultfont.configure(family= "Bahnschrift SemiLight", size=12) #Se elige la fuente default
#Se crea un input edad
        self.labeledad = Label(frame, text= 'Edad')#Texto que acompaña al input
        self.labeledad['bg'] = '#97b8db'#Cambia el color del texto
        self.labeledad.pack(ipady=15, ipadx = 0)#Posicion del texto
        self.edad = ttk.Combobox(frame, state='readonly') #Declara combobox
        self.edad.pack(ipady=0.5, ipadx= 2)#Posicion del combobox
        self.edad['values'] = ('20 a 29', '29 a 39', '39 a 49','+50')#Valores del combobox
        self.edad.current(0) #Valores predeterminados
        self.edad.pack(ipady=  0, ipadx= 0) #Posicion del input
#Selector de genero con combobox        
        self.labelgenero = Label(frame, text = 'Genero')  #Texto que aparece en el input
        self.labelgenero['bg'] = '#97b8db'#cambia el color del texto
        self.labelgenero.pack(ipady=  15, ipadx= 0) #Posicion del texto
        self.genero = ttk.Combobox(frame, state='readonly') #Declarar combobox
        self.genero.pack(ipady=0.5, ipadx= 2)#Posicion del combobox
        self.genero['values'] = ('masculino',  'femenino')#Valores del combobox de genero
        self.genero.current(0) #Default value

        
        def redirect_to_folleto():
                fol_Wind = Toplevel(window) #Abre una nueva ventana
                fol_Wind.geometry('500x500')#Dimensiones de la nueva ventana
                fol_Wind.title('Cuida tu salud')#Titulo de la nueva ventana
                fol_Wind['bg'] ='#b2e2f2'#Cambia el color de la ventana
                self.wind.withdraw()#Cierra la ventana padre(self.wind)
                fol_Wind.titulo = Label(fol_Wind, text='Algunos consejos utiles', font=('Bahnschrift SemiLight', 18)).place(x=120, y=20)#escribimos titulo

                fol_Wind.frame = LabelFrame(fol_Wind)#se crea un contenedor adentro de la ventana fol_Wind
                fol_Wind.frame.pack(ipadx='180', ipady='180', expand=True)#cambiamos el tamaño del contenedor
#usamos la etiqueta label para agregar consejos
                frame.consejo1 = Label(fol_Wind.frame, text="❤Haga actividad fisica").place(x=0, y=25)
                frame.consejo2 = Label(fol_Wind.frame, text="❤Evite el sedentarismo").place(x=0, y=50)
                frame.consejo3 = Label(fol_Wind.frame, text="❤Controle su presión arterial").place(x=0, y=75)
                frame.consejo4 = Label(fol_Wind.frame, text="❤Controle su colesterol").place(x=0, y=100)
                frame.consejo5 = Label(fol_Wind.frame, text="❤Mantenga un peso saludable").place(x=0, y=125)
                frame.consejo6 = Label(fol_Wind.frame, text="❤Mantenga una dieta saludable").place(x=0, y=150)
                frame.consejo7 = Label(fol_Wind.frame, text="❤Limite el consumo de alcohol").place(x=0, y=175)
                frame.consejo8 = Label(fol_Wind.frame, text="❤No fume").place(x=0, y=200)
                frame.consejo9 = Label(fol_Wind.frame, text="❤Controle su estrés").place(x=0, y=225)
                frame.consejo10 = Label(fol_Wind.frame, text="❤Mantenga habitos de sueño saludables").place(x=0, y=250)
                frame.consejo11 = Label(fol_Wind.frame, text="❤Presentece a examenes medicos diarios").place(x=0, y=275)
                frame.consejo12 = Label(fol_Wind.frame, text="❤Controle enfermedades preexistentes").place(x=0, y=300)
        self.boton1 = Button(window, text = 'Cuida tu salud', command = redirect_to_folleto).place(x=240, y=350)#creamos boton que redirecciona a una nueva ventana
#Boton que envia datos
        def obtener_info():
                genero = self.genero.get()#Guarda los valores del campo genero
                edad = self.edad.get()#Guarda los valores del campo edad
                bpm = arduino.readline().decode('utf-8') #Se comunica con el monitor serial de arduino
                NewWind = Toplevel(window) #Abre una nueva ventana
                NewWind.geometry('500x500')#Dimensiones de la nueva ventana
                NewWind.title('HeartPY')#Titulo de la nueva ventana
                self.wind.withdraw()#Cierra la ventana padre(self.wind)
                NewWind.update()#Actualiza la ventana
#Se usan condicionales para comparar edad y genero con datos optimos para la salud
                def comparacionFem():
                        label_estado = Label(NewWind, text="Su estado de salud es ", font=('Bahnschrift SemiLight', 20))
                        label_estado.place(x=50, y=410) 
                        if edad == "20 a 29":
                                if bpm >= 78 and bpm <= 94:
                                        label_estado.configure(text="Su estado de salud es optimo        ")
                                elif bpm < 78 or bpm > 94:
                                        label_estado.configure(text="Su estado de salud es no optimo")              
                        if edad == "29 a 39":
                                if bpm >= 80 and bpm <= 96:
                                        label_estado.configure(text="Su estado de salud es optimo        ")
                                elif bpm < 80 or bpm > 96:
                                        label_estado.configure(text="Su estado de salud es no optimo") 
                        if edad == "39 a 49":
                                if bpm >= 80 and bpm <= 98:
                                        label_estado.configure(text="Su estado de salud es optimo        ")    
                                elif bpm > 80 or bpm < 98:  
                                        label_estado.configure(text="Su estado de salud es no optimo")          
                        if edad == "+50":
                                if bpm >= 84 and bpm <= 102:
                                        label_estado.configure(text="Su estado de salud es optimo        ")
                                elif bpm > 84 or bpm < 102:
                                        label_estado.configure(text="Su estado de salud es no optimo") 
                                        
                def comparacionMasc():
                        label_estado = Label(NewWind, text="Su estado de salud es ", font=('Bahnschrift SemiLight', 20))
                        label_estado.place(x=50, y=410)
                        if edad == "20 a 29":
                                if bpm >= 70 and bpm <= 84:
                                        label_estado.configure(text="Su estado de salud es optimo        ")
                                elif bpm < 74 or bpm > 84:
                                        label_estado.configure(text="Su estado de salud es no optimo")          
                        if edad == "29 a 39":
                                if bpm >= 74 and bpm <= 84:
                                        label_estado.configure(text="Su estado de salud es optimo        ") 
                                elif bpm < 74 or bpm > 84:
                                        label_estado.configure(text="Su estado de salud es no optimo")    
                        if edad == "39 a 49":
                                if bpm >= 74 and bpm <= 88:
                                        label_estado.configure(text="Su estado de salud es optimo        ")  
                                elif bpm > 74 or bpm < 88:  
                                        label_estado.configure(text="Su estado de salud es no optimo")          
                        if edad == "+50":
                                if bpm >= 76 and bpm <= 88:
                                        label_estado.configure(text="Su estado de salud es optimo        ")
                                elif bpm > 76 or bpm < 88:
                                        label_estado.configure(text="Su estado de salud es no optimo")
                                        
                def mas_info():
                        wb.open("https://www.argentina.gob.ar/salud/glosario/enfermedadcardiovascular") #Abrir pagina en el navegador                   
                
                                                
                while True:
                        bpm = int(arduino.readline().decode('utf-8')) #Comunicacion con arduino monitor serial
                        Label(NewWind, text=bpm, font=('Bahnschrift SemiLight', 43)).place(x=180, y=200) #BPM en ventana tkinter
                        label_corazon = Label(NewWind, text="❤", fg="red", font=('Calibri', 40))
                        label_corazon.place(x=275, y=205)
                        boton_mas_info = Button(NewWind, text="Mas Info", command=mas_info).place(x=200, y=460) #Boton para redireccionar al navegador
                        NewWind.update() #window update
                        if genero == "femenino":
                                comparacionFem()    
                        if genero == "masculino":
                                comparacionMasc()
                                                                                             
        self.boton2 = Button(frame, text = 'Enviar Datos', command=obtener_info).pack(ipady =0, ipadx= 36, pady=30) #Crear boton que manda los datos
                

if __name__  == '__main__' or 'NewWind':#Comprueba si es el archivo main
    window = Tk() 
    aplication = Proyecto(window) 
    window.mainloop() 
