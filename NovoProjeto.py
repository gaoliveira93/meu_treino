import customtkinter
import tkinter as tk
from tkinter import ttk

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.title('Calculadora de Custo')


app_weight = 1200
app_height = 600
screen_weight = app.winfo_screenwidth()
screen_height = app.winfo_screenmmheight()

x = (screen_weight / 2 ) - (app_weight / 2)
y = (screen_height / 2 ) - (app_height / 2)

app.geometry(f'{app_weight} x {app_height}+{int(x)}+{int(y)}')


my_tab = customtkinter.CTkTabview(app,
                                  height=800,
                                  width=800)

my_tab.pack(side="top", fill="x", pady=10)

#Abas

tab1 = my_tab.add('Assinatura')
tab2 = my_tab.add('Por uso')


# Frames

frame1 = customtkinter.CTkFrame(master= tab1,
                                width=1500,
                                height=1200)
frame1.pack(fill='both', expand=True)

frame2 = customtkinter.CTkFrame(master= tab2,
                                width=1500,
                                height=1200)
frame2.pack(fill='both', expand=True)




Cyclopay_Tax = customtkinter.CTkEntry(master=tab1,
                                      width=150,
                                      height=40,
                                      border_width=2,
                                      justify='c').place(x=130, y=30)

customtkinter.CTkLabel(master=tab1,
                       width=10,
                       height=10,
                       text='Taxa Cyclopay :',
                       fg_color='#292929',
                       corner_radius=0
).place(x=20, y=40)

Initial_Tax = customtkinter.CTkEntry(master=tab1,
                                      width=150,
                                      height=40,
                                      border_width=2,
                                      corner_radius=10,
                                      justify='c').place(x=450, y=30)

customtkinter.CTkLabel(master=tab1,
                       width=10,
                       height=10,
                       text='Imposto :',
                       fg_color='#292929',
                       corner_radius=0
).place(x=310, y=40)

Cost_Tera = customtkinter.CTkEntry(master=tab1,
                                      width=150,
                                      height=40,
                                      border_width=2,
                                      justify='c').place(x=750, y=30)

customtkinter.CTkLabel(master=tab1,
                       width=10,
                       height=10,
                       text='Custo por Terabyte :',
                       fg_color='#292929',
                       corner_radius=0
).place(x=620, y=40)

Cost_Invoice = customtkinter.CTkEntry(master=tab1,
                                      width=150,
                                      height=40,
                                      border_width=2,
                                      justify='c').place(x=750, y=100)

customtkinter.CTkLabel(master=tab1,
                       width=10,
                       height=10,
                       text='Custo Nota Fiscal :',
                       fg_color='#292929',
                       corner_radius=0
).place(x=620, y=110)

Server_Cost = customtkinter.CTkEntry(master=tab1,
                                      width=150,
                                      height=40,
                                      border_width=2,
                                      justify='c').place(x=750, y=170)

customtkinter.CTkLabel(master=tab1,
                       width=10,
                       height=10,
                       text='Custo Servidor :',
                       fg_color='#292929',
                       corner_radius=0
).place(x=620, y=180)

Dolar_Price = customtkinter.CTkEntry(master=tab1,
                                      width=150,
                                      height=40,
                                      border_width=2,
                                      justify='c').place(x=130, y=100)

customtkinter.CTkLabel(master=tab1,
                       width=10,
                       height=10,
                       text='Câmbio do dólar :',
                       fg_color='#292929',
                       corner_radius=0
).place(x=15, y=110)

Margim = customtkinter.CTkEntry(master=tab1,
                                      width=150,
                                      height=40,
                                      border_width=2,
                                      justify='c').place(x=130, y=170)

customtkinter.CTkLabel(master=tab1,
                       width=10,
                       height=10,
                       text='Margem de Lucro :',
                       fg_color='#292929',
                       corner_radius=0
).place(x=15, y=180)

IOF = customtkinter.CTkEntry(master=tab1,
                                      width=150,
                                      height=40,
                                      border_width=2,
                                      corner_radius=10,
                                      justify='c').place(x=450, y=100)

customtkinter.CTkLabel(master=tab1,
                       width=10,
                       height=10,
                       text='IOF :',
                       fg_color='#292929',
                       corner_radius=0
).place(x=310, y=110)

Fix_Tax_Cyclopay = customtkinter.CTkEntry(master=tab1,
                                      width=150,
                                      height=40,
                                      border_width=2,
                                      corner_radius=10,
                                      justify='c').place(x=450, y=170)

customtkinter.CTkLabel(master=tab1,
                       width=10,
                       height=10,
                       text='Taxa Fixa Cyclopay :',
                       fg_color='#292929',
                       corner_radius=0
).place(x=310, y=180)

#Generate_Button = customtkinter.CTkButton(master=tab1,
#                                          width=150,
#                                          height=40,
#                                          border_width=2,
#                                          text='Gerar Cálculo',
#                                          compound='bottom').place(x=20, y=410)


app.mainloop()