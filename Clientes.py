from ttk import *
from Tkinter import *
import tkMessageBox
import pyodbc



class clientes ():

    def formcliente(self):
        self.conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=DESKTOP-LOAFBH2\MSSQLSERVER01;'
                              'Database=AerolineaCarrillo;'
                              "Trusted_Connection=yes;")
        self.window = Tk()
        self.window.title("Clientes")
        self.window.geometry('730x400')
        self.window.config(cursor="trek",bg="DodgerBlue4")
        canvas = Canvas(self.window,width=805,height=505)
        canvas.place(x=-45,y=-30)
        img = PhotoImage(file="Aerolinea.gif") #FALTA EL ARCHIVO .gif
        canvas.create_image(405, 255, image=img)
        lbl = Label(self.window, text="Clientes "
                    ,font="Impact",relief="solid",height=2, width=80).pack()
        lbl2 = Label(self.window, text="Id cliente: "
                    , font="Impact", relief="solid",width=10)
        lbl2.place(x=10, y=70)
        self.txtid = Entry(self.window, width=20, font="Arial")#textvariable=self.id_cliente
        self.txtid.place(x=100, y=70)
        lbl3 = Label(self.window, text="Nombre: "
                     , font="Impact", relief="solid",width=10)
        lbl3.place(x=10, y=110)
        self.txtnombre = Entry(self.window, width=20, font="Arial")
        self.txtnombre.place(x=100, y=112)
        lbl4 = Label(self.window, text="Edad: "
                     , font="Impact", relief="solid",width=10)
        lbl4.place(x=10, y=150)
        self.txtedad = Entry(self.window, width=20, font="Arial")
        self.txtedad.place(x=100, y=154)
        lbl5 = Label(self.window, text="Direccion: "
                     , font="Impact", relief="solid",width=10)
        lbl5.place(x=10, y=190)
        self.txtdir = Entry(self.window, width=20, font="Arial")
        self.txtdir.place(x=100, y=192)
        lbl6 = Label(self.window, text="Telefono: "
                     , font="Impact", relief="solid",width=10)
        lbl6.place(x=10, y=230)
        self.txttel = Entry(self.window, width=20, font="Arial")
        self.txttel.place(x=100, y=232)
        self.botones()
        self.window.mainloop()


    def botones(self):
        self.button1 = Button(self.window, font="Arial", text=" NUEVO ",width=15, command=self.create)
        self.button1.place(x=450, y=60)
        self.button2 = Button(self.window, font="Arial", text=" ACTUALIZAR ", width=15,command=self.update)
        self.button2.place(x=450, y=120)
        self.button3 = Button(self.window, font="Arial", text=" BUSCAR ",width=15, command=self.busca)
        self.button3.place(x=450, y=180)
        self.button4 = Button(self.window, font="Arial", text=" ELIMINAR ",width=15, command=self.elim)
        self.button4.place(x=450, y=240)

    def elim(self):
        self.windowelim = Tk()
        self.windowelim.title("Clientes")
        self.windowelim.geometry('500x300')
        self.windowelim.config(cursor="trek", bg="Gray50")
        lbl = Label(self.windowelim, text=" Clientes "
                    , font="Impact", relief="solid", height=2, width=80).pack()
        lbl2 = Label(self.windowelim, text="Eliminar cliente "
                     , font="Impact", relief="solid", width=30).pack()
        T = Text(self.windowelim, height=1, width=13)
        T.place(x=30, y=130)
        T.insert(END, " ID Cliente: ")
        T.configure(state='disabled')
        self.txtelim = Entry(self.windowelim, width=30, font="Arial")
        self.txtelim.place(x=170, y=129)
        self.buttonbusca = Button(self.windowelim, font="Arial", text=" ELIMINAR ", width=15, command=self.delete)
        self.buttonbusca.place(x=175, y=190)

    def busca(self):
        self.windowb = Tk()
        self.windowb.title("Clientes")
        self.windowb.geometry('500x300')
        self.windowb.config(cursor="trek", bg="Gray50")
        lbl = Label(self.windowb, text="Clientes "
                    , font="Impact", relief="solid", height=2, width=80).pack()
        lbl2 = Label(self.windowb, text="Buscar Cliente "
                     , font="Impact", relief="solid", width=30).pack()
        T = Text(self.windowb, height=1, width=13)
        T.place(x=30, y=130)
        T.insert(END, " ID Cliente: ")
        T.configure(state='disabled')
        self.txtbusca = Entry(self.windowb, width=30, font="Arial")
        self.txtbusca.place(x=170, y=129)
        self.buttonbusca = Button(self.windowb, font="Arial", text=" BUSCAR ", width=15, command=self.read)
        self.buttonbusca.place(x=175, y=190)


    def read(self):
        try:
            x=self.txtbusca.get()
            cursor = self.conn.cursor()
            cursor.execute("select * from clientes where id_cliente = ? ",
                       (x))
            self.buscado = cursor.fetchone()
            try:
                self.windowb.destroy()
            except:
                pass
            self.mostrar()
        except:
            pass

    def create(self):
        try:
            x = tkMessageBox.askyesno(message="Crear nuevo?", title="Nuevo cliente")
            if x == True:
                cursor = self.conn.cursor()
                cursor.execute("insert into clientes(id_cliente,nombre,edad,direccion,telefono) values(?,?,?,?,?);",
                           (self.txtid.get(), self.txtnombre.get(), self.txtedad.get(), self.txtdir.get(),
                            self.txttel.get())
                           )
                self.conn.commit()
                tkMessageBox.showinfo(message="Nuevo cliente agregado")
                self.txtid.delete(0, END)
                self.txtnombre.delete(0, END)
                self.txtedad.delete(0, END)
                self.txtdir.delete(0, END)
                self.txttel.delete(0, END)
        except:
            pass

    def update(self):
        x=tkMessageBox.askyesno(message="Actualizar?", title="Atualizar")
        if x == True:
            cursor = self.conn.cursor()
            cursor.execute("update clientes set nombre=?,edad=?,direccion=?,telefono=? where id_cliente = ?;",
                           (self.txtnombre.get(), self.txtedad.get(), self.txtdir.get(), self.txttel.get(),
                            self.txtid.get())
                           )
            self.conn.commit()
            tkMessageBox.showinfo(message="  Actualizado  ")
            self.txtid.delete(0, END)
            self.txtnombre.delete(0, END)
            self.txtedad.delete(0, END)
            self.txtdir.delete(0, END)
            self.txttel.delete(0, END)

    def delete(self):
        x = tkMessageBox.askyesno(message="Eliminar?", title="Eliminar")
        if x == True:
            cursor = self.conn.cursor()
            cursor.execute("delete from clientes where id_cliente = ?;",
                           (self.txtelim.get())
                           )
            self.conn.commit()
        try:
            self.windowelim.destroy()
        except:
            pass

    def mostrar(self):
        self.txtid.delete(0, END)
        self.txtnombre.delete(0,END)
        self.txtedad.delete(0, END)
        self.txtdir.delete(0, END)
        self.txttel.delete(0, END)
        self.txtid.insert(0,self.buscado[0])
        self.txtnombre.insert(0,self.buscado[1])
        self.txtedad.insert(0, self.buscado[2])
        self.txtdir.insert(0, self.buscado[3])
        self.txttel.insert(0, self.buscado[4])










obj=clientes()
obj.formcliente()