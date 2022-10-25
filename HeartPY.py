import tkinter as tk
from tkinter import ttk, font
from tkinter import *
import serial


arduino = serial.Serial('COM5', 9600)

class Proyecto(tk.Tk):#Contiene los metodos de las ventanas
    def __init__(self, window) : #inicializa el estado de un objeto
        self.wind = window #almacena la vetana como parametro
        self.wind.title('HeartPY')#titulo de la ventana
        self.wind.geometry('600x400+375+50') #cambia el tamaño de la ventana
        self.wind.resizable(False, False) #elimina la opcion de maximzar la ventana
        self.windtext = Label(self.wind, text='Calculadora de salud')#Titulo a dentro de la ventana
        self.windtext.defaultfont = font.nametofont("TkDefaultFont") #Cambia la fuente default
        self.wind.defaultfont = font.nametofont("TkDefaultFont") #Cambia la fuente default
        self.wind.defaultfont.configure(family= "Bahnschrift SemiLight", size=12) #se elige la fuente default
        
#Se crea un contenedor
        frame = LabelFrame(self.wind, text ='Ingrese sus datos') #nombre del contenedor
        frame.pack(ipady= 20, ipadx = 40, anchor= tk.N) #posicion del contenedor
        frame.defaultfont = font.nametofont("TkDefaultFont") #Cambia la fuente default
        frame.defaultfont.configure(family= "Bahnschrift SemiLight", size=12) #se elige la fuente default
#se crea un input edad
        self.labeledad = Label(frame, text= 'Edad')#texto que acompaña al input
        self.labeledad.pack(ipady=15, ipadx = 0)#posicion del texto
        self.edad = ttk.Combobox(frame, state='readonly') #declara combobox
        self.edad.pack(ipady=0.5, ipadx= 2)#posicion del combobox
        self.edad['values'] = ('20 a 29', '29 a 39', '39 a 49','+50')#valores del combobox
        self.edad.current(0) #valores predeterminados
        self.edad.pack(ipady=  0, ipadx= 0) #posicion del input
#selector de genero con combobox        
        self.labelgenero = Label(frame, text = 'Genero')  #text that appears in front of the input
        self.labelgenero.pack(ipady=  15, ipadx= 0) #position text
        self.genero = ttk.Combobox(frame, state='readonly') #declare combobox
        self.genero.pack(ipady=0.5, ipadx= 2)#position of the combobox
        self.genero['values'] = ('masculino',  'femenino')#values of the combobox
        self.genero.current(0) #default value
#boton que envia datos
        def obtener_info():
                genero = self.genero.get()#guarda los valores del campo genero
                edad = self.edad.get()#guarda los valores del campo edad
                bpm = int(arduino.readline().decode('utf-8')) #se comunica con el monitor serial de arduino
                NewWind = Toplevel(window) #abre una nueva ventana
                NewWind.geometry('500x500')#dimensiones de la nueva ventana
                NewWind.title('HeartPY')#titulo de la nueva ventana
                self.wind.withdraw()#cierra la ventana padre(self.wind)
                NewWind.update()#actualiza la ventana

#se usan condicionales para comparar edad y genero con datos optimos para la salud
                def comparacionFem():
                        label_estado = Label(NewWind, text="Su estado de salud es ")
                        label_estado.place(x=100, y=100)
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
                        label_estado = Label(NewWind, text="Su estado de salud es ")
                        label_estado.place(x=100, y=100)
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
                                                
                while True:
                        bpm = int(arduino.readline().decode('utf-8')) #comunication with arduino monitor serial
                        Label(NewWind, text=bpm).place(x=0, y=0) #BPM in tkinter window
                        Label(NewWind, text="Fuente: https://mejorconsalud.as.com/frecuencia-cardiaca-normal-edad-calcularla/").place(x=0, y=475)
                        print(bpm)
                        NewWind.update() #window update
                        if genero == "femenino":
                                comparacionFem()    
                        if genero == "masculino":
                                comparacionMasc()
                                                                           
        self.boton = Button(frame, text = 'Enviar Datos', command=obtener_info).pack(ipady =0, ipadx= 36, pady=30) #create the button that sends the data
                


if __name__  == '__main__' or 'NewWind':#comprueba si es el archivo main
    window = Tk() 
    aplication = Proyecto(window) 
    window.mainloop() 
