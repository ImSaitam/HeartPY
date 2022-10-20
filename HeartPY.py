from cProfile import label
import tkinter as tk
from tkinter import ttk
from tkinter import *
import serial

arduino = serial.Serial('COM4', 9600)

class Proyecto(tk.Tk):#Contains the methods of the window
    def __init__(self, window) : #Initializes the state of an object
        self.wind = window #Store the window as a parameter
        self.wind.title('Proyecto')#Title of the windows
        self.wind.geometry('600x400+375+50') #Window dimensions
        self.wind.resizable(False, False) #Remove the maximize option
        self.windtext = Label(self.wind, text='Calculadora de salud', font="Century_Gothic")#Title
        self.windtext.pack(ipady= 30)#Position
        
        #A container is created
        frame = LabelFrame(self.wind, text ='Ingrese sus datos', font="Century_Gothic") #Name of the container
        frame.pack(ipady= 20, ipadx = 40, anchor= tk.N) #Position of the container
        
        #Input age
        self.labeledad = Label(frame, text= 'Edad')#Text that appears in front of the input
        self.labeledad.pack(ipady=15, ipadx = 0)#Position text
        self.edad = ttk.Combobox(frame, state='readonly') #Declare combobox
        self.edad.pack(ipady=0.5, ipadx= 2)#Position of the combobox
        self.edad['values'] = ('10 a 19', '20 a 29',  '29 a 39', '39 a 49', '+50')#Values of the combobox
        self.edad.current(0) #Default value
        self.edad.pack(ipady=  0, ipadx= 0) #Position input
        
        #Combobox Gender   
        self.labelgenero = Label(frame, text = 'Genero')  #Text that appears in front of the input
        self.labelgenero.pack(ipady=  15, ipadx= 0) #Position text
        self.genero = ttk.Combobox(frame, state='readonly') #Declare combobox
        self.genero.pack(ipady=0.5, ipadx= 2)#Position of the combobox
        self.genero['values'] = ('Masculino',  'Femenino') #Values of the combobox
        self.genero.current(0) #Default value
        
        #Send data button function
        def obtener_info():
                genero = self.genero.get()#Save the variables of the gender field
                edad = self.edad.get()#Save the variables of the age field
                bpm = int(arduino.readline().decode('utf-8')) #Comunication with arduino monitor serial
                NewWind = Toplevel(window) #Open a new window
                NewWind.geometry('500x500')#New window dimensions
                NewWind.title('Coso')#Title new window
                self.wind.withdraw()
                NewWind.update()
                while True:
                        bpm = int(arduino.readline().decode('utf-8')) #Comunication with arduino monitor serial
                        Label(NewWind, text=bpm, font="Century_Gothic").place(x=0, y=0) #BPM in tkinter window
                        Label(NewWind, text="Fuente: https://mejorconsalud.as.com/frecuencia-cardiaca-normal-edad-calcularla/").place(x=0, y=475)
                        print(bpm)
                        NewWind.update() #Window update
                        if genero == "femenino":
                                label_estado = Label(NewWind, text="Su estado de salud es ", font="system")
                                label_estado.place(x=100, y=100)
                                if edad == "10 a 19":
                                        if bpm >= 60 and bpm <= 100:
                                               label_estado.configure(text="Su estado de salud es optimo      ")
                                        elif bpm < 60 and bpm > 100:
                                                label_estado.configure(text="Su estado de salud es no optimo")
                                if edad == "20 a 29":
                                        if bpm >= 78 and bpm <= 94:
                                                label_estado.configure(text="Su estado de salud es optimo      ")
                                        elif bpm < 78 or bpm > 94:
                                                label_estado.configure(text="Su estado de salud es no optimo")              
                                if edad == "29 a 39":
                                        if bpm >= 80 and bpm <= 96:
                                            label_estado.configure(text="Su estado de salud es optimo      ")
                                        elif bpm < 80 and bpm > 96:
                                                label_estado.configure(text="Su estado de salud es no optimo") 
                                if edad == "39 a 49":
                                        if bpm >= 80 and bpm <= 98:
                                               label_estado.configure(text="Su estado de salud es optimo      ")    
                                        elif bpm > 80 and bpm < 98:  
                                                label_estado.configure(text="Su estado de salud es no optimo")          
                                if edad == "+50":
                                        if bpm >= 84 and bpm <= 102:
                                               label_estado.configure(text="Su estado de salud es optimo      ")
                                        elif bpm > 84 and bpm < 102:
                                                label_estado.configure(text="Su estado de salud es no optimo")    
                        if genero == "masculino":
                                label_estado = Label(NewWind, text="Su estado de salud es ", font="Century_Gothic")
                                if edad == "10 a 19":
                                        if bpm >= 60 and bpm <= 100:
                                               label_estado.configure(text="Su estado de salud es optimo      ")
                                        elif bpm < 60 and bpm > 100:
                                                label_estado.configure(text="Su estado de salud es no optimo")
                                if edad == "20 a 29":
                                        if bpm >= 70 and bpm <= 84:
                                                label_estado.configure(text="Su estado de salud es optimo      ")
                                        elif bpm < 74 or bpm > 84:
                                                label_estado.configure(text="Su estado de salud es no optimo")          
                                if edad == "29 a 39":
                                        if bpm >= 74 and bpm <= 84:
                                            label_estado.configure(text="Su estado de salud es optimo      ") 
                                        elif bpm < 74 and bpm > 84:
                                                label_estado.configure(text="Su estado de salud es no optimo")    
                                if edad == "39 a 49":
                                        if bpm >= 74 and bpm <= 88:
                                               label_estado.configure(text="Su estado de salud es optimo      ")  
                                        elif bpm > 74 and bpm < 88:  
                                                label_estado.configure(text="Su estado de salud es no optimo")          
                                if edad == "+50":
                                        if bpm >= 76 and bpm <= 88:
                                               label_estado.configure(text="Su estado de salud es optimo      ")
                                        elif bpm > 76 and bpm < 88:
                                                label_estado.configure(text="Su estado de salud es no optimo")   
                        
                
                                   
                                        
        self.boton = Button(frame, text = 'Enviar Datos', command=obtener_info).pack(ipady =0, ipadx= 36, pady=30) #Create the button that sends the data
                


if __name__  == '__main__' or 'NewWind':
    window = Tk() 
    aplication = Proyecto(window) 
    window.mainloop() 
