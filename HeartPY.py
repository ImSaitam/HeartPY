import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import serial

arduino = serial.Serial('COM4', 9600)

class Proyecto(tk.Tk):#contiene los metodos de la ventanas
    def __init__(self, window) : #inicializa el estado de un objeto
        self.wind = window #almacena la vetana como parametro
        self.wind.title('Proyecto')#titulo de la ventana
        self.wind.geometry('600x400+375+50') #dimensiones de la ventana
        self.wind.resizable(False, False) #elimina la opcion de maximizar
        self.windtext = Label(self.wind, text='Calculadora de salud', font="Century_Gothic")#titulo
        self.windtext.pack(ipady= 30)#posicion
#se crea un contenedor
        frame = LabelFrame(self.wind, text ='Ingrese sus datos', font="Century_Gothic") #nombre del contenedor
        frame.pack(ipady= 20, ipadx = 40, anchor= tk.N) #posicion del contenedor
#input edad
        self.labeledad = Label(frame, text= 'Edad')#texto que aparece adelante del input 
        self.labeledad.pack(ipady=15, ipadx = 0)#posicion del texto
        self.edad = ttk.Combobox(frame, state='readonly') #declaramos combobo  
        self.edad.pack(ipady=0.5, ipadx= 2)#posicion del combobox
        self.edad['values'] = ('20 a 29',  '29 a 39', '39 a 49', '+50')#valores del combobox
        self.edad.current(0) #valor predeterminado
        self.edad.pack(ipady=  0, ipadx= 0) #posicion del input
        self.edad.focus()
#Combobox Genero
        
        self.labelgenero = Label(frame, text = 'Genero')  #texto que aparece en frente del combobox
        self.labelgenero.pack(ipady=  15, ipadx= 0) #posicion del texto
        self.genero = ttk.Combobox(frame, state='readonly') #declaramos combobo  
        self.genero.pack(ipady=0.5, ipadx= 2)#posicion del combobox
        self.genero['values'] = ('masculino',  'femenino')#valores del combobox
        self.genero.current(0) #valor predeterminado
#boton envio de datos
        def obtener_info():
                genero = self.genero.get()#guarda las variables del campo genero
                edad = self.edad.get()#guarda las variables del campo edad
                bpm = int(arduino.readline().decode('utf-8')) #Comunicacion con Monitor serial
                NewWind = Toplevel(window) #abre una ventana hija
                NewWind.geometry('500x500')#configuracion de la ventana hija
                NewWind.title('Coso')#titulo de la ventana hija
                self.wind.withdraw()
                NewWind.update()
                while True:
                        bpm = int(arduino.readline().decode('utf-8')) #Comunicacion con Monitor serial
                        Label(NewWind, text=bpm, font="Century_Gothic").place(x=0, y=0) #BPM en ventana Tkinter
                        print(bpm)
                        NewWind.update() #Actualización de la ventana
                        if genero == "femenino":
                                Label(NewWind, text="Su estado de salud es", font="Century_Gothic").place(x=100, y=100)
                                if edad == "20 a 29":
                                        if bpm >= 78 and bpm <= 94:
                                                Label(NewWind, text="optima", font="Century_Gothic").place(x=100, y=200)
                                        elif bpm < 78 or bpm > 94:
                                                Label(NewWind, text="no optima", font="Century_Gothic").place(x=100, y=300)               
                                elif edad == "29 a 39":
                                        if bpm >= 80 and bpm <= 96:
                                            Label(NewWind, text="optima", font="Century_Gothic").place(x=100, y=200)  
                                        elif bpm < 80 and bpm > 96:
                                                Label(NewWind, text="no optima", font="Century_Gothic").place(x=100, y=300)  
                                elif edad == "39 a 49":
                                        if bpm >= 80 and bpm <= 98:
                                               Label(NewWind, text="optima", font="Century_Gothic").place(x=100, y=200)     
                                        elif bpm > 80 and bpm < 98:  
                                                Label(NewWind, text="no optima", font="Century_Gothic").place(x=100, y=300)          
                                elif edad == "+50":
                                        if bpm >= 84 and bpm <= 102:
                                               Label(NewWind, text="optima", font="Century_Gothic").place(x=100, y=200) 
                                        elif bpm > 84 and bpm < 102:
                                                Label(NewWind, text="no optima", font="Century_Gothic").place(x=100, y=300)    
                                
                        if genero == "masculino":
                                Label(NewWind, text="Su estado de salud es", font="Century_Gothic").place(x=100, y=100)
                                if edad == "20 a 29":
                                        if bpm >= 70 and bpm <= 84:
                                                        Label(NewWind, text="optima", font="Century_Gothic").place(x=100, y=200)
                                        elif bpm < 74 or bpm > 84:
                                                Label(NewWind, text="no optima", font="Century_Gothic").place(x=100, y=300)               
                                elif edad == "29 a 39":
                                        if bpm >= 74 and bpm <= 84:
                                            Label(NewWind, text="optima", font="Century_Gothic").place(x=100, y=200)  
                                        elif bpm < 74 and bpm > 84:
                                                Label(NewWind, text="no optima", font="Century_Gothic").place(x=100, y=300)  
                                elif edad == "39 a 49":
                                        if bpm >= 74 and bpm <= 88:
                                               Label(NewWind, text="optima", font="Century_Gothic").place(x=100, y=200)     
                                        elif bpm > 74 and bpm < 88:  
                                                Label(NewWind, text="no optima", font="Century_Gothic").place(x=100, y=300)          
                                elif edad == "+50":
                                        if bpm >= 76 and bpm <= 88:
                                               Label(NewWind, text="optima", font="Century_Gothic").place(x=100, y=200) 
                                        elif bpm > 76 and bpm < 88:
                                                Label(NewWind, text="no optima", font="Century_Gothic").place(x=100, y=300) 
                        
                
                                   
                                        
        self.boton = Button(frame, text = 'Enviar Datos', command=obtener_info).pack(ipady =0, ipadx= 36, pady=30) #creamos el botón que envia los datos
                


if __name__  == '__main__' or 'NewWind':#comprueba si es el archivo main
    window = Tk() #ventana principal
    aplication = Proyecto(window) #se guarda la clase en una variable
    window.mainloop() #inicializa la ventana
