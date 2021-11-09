from tkinter import ttk
from tkinter import *

import sqlite3

class Product:

    db_name = 'matricula.db'

    def __init__(self, box):
        self.box=box
        self.box.title('Registro De Estudiante')
       
        frame = LabelFrame(self.box, text='Datos del estudiante')
        frame.grid(row = 0, column = 0, columnspan= 3, pady= 20)
        
        #Espacio nombres

        Label(frame, text= 'Nombres y apellidos: ').grid(row = 1, column = 0)
        self.nombre = Entry (frame)
        self.nombre.focus()
        self.nombre.grid(row = 1, column = 1)

        #Espacio edad
        Label(frame, text='NuCedula: ').grid(row=2,column=0)
        self.edad=Entry (frame)
        self.edad.grid(row=2,column=1)
        
        #Espacio Cedula
        Label(frame, text='Direccion: ').grid(row=3, column= 0)
        self.cedula = Entry(frame)
        self.cedula.grid(row=3, column=1)

        #Espacio Celular
        Label(frame, text='NuTelular: ').grid(row=4, column=0)
        self.celular = Entry(frame)
        self.celular.grid(row=4, column=1)
        
        #Boton agregar
        ttk.Button(frame,text='Registrar').grid(row = 5,column = 0, columnspan=3, sticky = W+E)    
        #mensaje

        self.menssage = Label(text='',fg='red')
        self.menssage.grid(row=3,column=0,columnspan=2,sticky=W+E)
        
        #Tabla
        self.tree = ttk.Treeview(height = 10,column= ('#1', '#2', '#3'))
        self.tree.grid(row= 4, column= 0, columnspan=3)
        self.tree.heading("#0", text = 'Nombre y Apellido', anchor = CENTER)
        self.tree.heading("#1", text= 'NUmero de Cedula', anchor= CENTER)
        self.tree.heading("#2", text= 'Direccion', anchor= CENTER)
        self.tree.heading("#3", text= 'Numero de Telefono', anchor= CENTER)
        #botones
        ttk.Button(text='Eliminar').grid(row=5,column=0,sticky=W+E)
        ttk.Button(text='Editar').grid(row=5, column=2,sticky=W+E)

        self.get_Estudiante()

    #conecto la base de datos
    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    #Metodo Onbtner estudiante
    def get_estudiante(self):
        #limpiar
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        
        #consultar datos
        query = 'SELC * FROM Estudiante ORDER BY name DESC'
        db_rows = self.run_query(query)
        #Rellenar datos
        for row in db_rows:
            self.tree.insert('',0,txt= row[1], values= row[3])

        




if __name__ == '__main__':
    box = Tk()
    sistema = Product(box)
    box.mainloop()