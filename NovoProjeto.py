import customtkinter
import tkinter as tk
from tkinter import ttk

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

class CustomWidgets:
    def __init__(self, master, exclude_widgets=[]):
        self.master = master
        self.exclude_widgets = exclude_widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Cyclopay_Tax Entry and Label
        if 'Cyclopay_Tax' not in self.exclude_widgets:
            self.Cyclopay_Tax = customtkinter.CTkEntry(master=self.master,
                                                       width=150,
                                                       height=40,
                                                       border_width=2,
                                                       justify='c')
            self.Cyclopay_Tax.place(x=750, y=170)
            
            self.Cyclopay_Tax_Label = customtkinter.CTkLabel(master=self.master,
                                                             width=10,
                                                             height=10,
                                                             text='Taxa Cyclopay :',
                                                             fg_color='#292929',
                                                             corner_radius=0)
            self.Cyclopay_Tax_Label.place(x=620, y=180)
        
        # Initial_Tax Entry and Label
        if 'Initial_Tax' not in self.exclude_widgets:
            self.Initial_Tax = customtkinter.CTkEntry(master=self.master,
                                                      width=150,
                                                      height=40,
                                                      border_width=2,
                                                      corner_radius=10,
                                                      justify='c')
            self.Initial_Tax.place(x=450, y=30)
            
            self.Initial_Tax_Label = customtkinter.CTkLabel(master=self.master,
                                                            width=10,
                                                            height=10,
                                                            text='Imposto :',
                                                            fg_color='#292929',
                                                            corner_radius=0)
            self.Initial_Tax_Label.place(x=310, y=40)
        
        # Cost_Tera Entry and Label
        if 'Cost_Tera' not in self.exclude_widgets:
            self.Cost_Tera = customtkinter.CTkEntry(master=self.master,
                                                    width=150,
                                                    height=40,
                                                    border_width=2,
                                                    justify='c')
            self.Cost_Tera.place(x=750, y=30)
            
            self.Cost_Tera_Label = customtkinter.CTkLabel(master=self.master,
                                                          width=10,
                                                          height=10,
                                                          text='Custo por Terabyte :',
                                                          fg_color='#292929',
                                                          corner_radius=0)
            self.Cost_Tera_Label.place(x=620, y=40)
        
        # Cost_Invoice Entry and Label
        if 'Cost_Invoice' not in self.exclude_widgets:
            self.Cost_Invoice = customtkinter.CTkEntry(master=self.master,
                                                       width=150,
                                                       height=40,
                                                       border_width=2,
                                                       justify='c')
            self.Cost_Invoice.place(x=750, y=100)
            
            self.Cost_Invoice_Label = customtkinter.CTkLabel(master=self.master,
                                                             width=10,
                                                             height=10,
                                                             text='Custo Nota Fiscal :',
                                                             fg_color='#292929',
                                                             corner_radius=0)
            self.Cost_Invoice_Label.place(x=620, y=110)
        
        # Server_Cost Entry and Label
        if 'Server_Cost' not in self.exclude_widgets:
            self.Server_Cost = customtkinter.CTkEntry(master=self.master,
                                                      width=150,
                                                      height=40,
                                                      border_width=2,
                                                      justify='c')
            self.Server_Cost.place(x=130, y=30)
            
            self.Server_Cost_Label = customtkinter.CTkLabel(master=self.master,
                                                            width=10,
                                                            height=10,
                                                            text='Custo Servidor :',
                                                            fg_color='#292929',
                                                            corner_radius=0)
            self.Server_Cost_Label.place(x=20, y=40)
        
        # Dolar_Price Entry and Label
        if 'Dolar_Price' not in self.exclude_widgets:
            self.Dolar_Price = customtkinter.CTkEntry(master=self.master,
                                                      width=150,
                                                      height=40,
                                                      border_width=2,
                                                      justify='c')
            self.Dolar_Price.place(x=130, y=100)
            
            self.Dolar_Price_Label = customtkinter.CTkLabel(master=self.master,
                                                            width=10,
                                                            height=10,
                                                            text='Câmbio do dólar :',
                                                            fg_color='#292929',
                                                            corner_radius=0)
            self.Dolar_Price_Label.place(x=15, y=110)
        
        # Margim Entry and Label
        if 'Margim' not in self.exclude_widgets:
            self.Margim = customtkinter.CTkEntry(master=self.master,
                                                 width=150,
                                                 height=40,
                                                 border_width=2,
                                                 justify='c')
            self.Margim.place(x=130, y=170)
            
            self.Margim_Label = customtkinter.CTkLabel(master=self.master,
                                                       width=10,
                                                       height=10,
                                                       text='Margem de Lucro :',
                                                       fg_color='#292929',
                                                       corner_radius=0)
            self.Margim_Label.place(x=15, y=180)
        
        # IOF Entry and Label
        if 'IOF' not in self.exclude_widgets:
            self.IOF = customtkinter.CTkEntry(master=self.master,
                                              width=150,
                                              height=40,
                                              border_width=2,
                                              corner_radius=10,
                                              justify='c')
            self.IOF.place(x=450, y=100)
            
            self.IOF_Label = customtkinter.CTkLabel(master=self.master,
                                                    width=10,
                                                    height=10,
                                                    text='IOF :',
                                                    fg_color='#292929',
                                                    corner_radius=0)
            self.IOF_Label.place(x=310, y=110)
        
        # Fix_Tax_Cyclopay Entry and Label
        if 'Fix_Tax_Cyclopay' not in self.exclude_widgets:
            self.Fix_Tax_Cyclopay = customtkinter.CTkEntry(master=self.master,
                                                           width=150,
                                                           height=40,
                                                           border_width=2,
                                                           corner_radius=10,
                                                           justify='c')
            self.Fix_Tax_Cyclopay.place(x=450, y=170)
            
            self.Fix_Tax_Cyclopay_Label = customtkinter.CTkLabel(master=self.master,
                                                                 width=10,
                                                                 height=10,
                                                                 text='Taxa Fixa Cyclopay :',
                                                                 fg_color='#292929',
                                                                 corner_radius=0)
            self.Fix_Tax_Cyclopay_Label.place(x=310, y=180)
        
        # Record Button
        if 'Record_Button' not in self.exclude_widgets:
            self.Record_Button = customtkinter.CTkButton(master=self.master,
                                                         width=150,
                                                         height=40,
                                                         border_width=2,
                                                         text='Gravar',
                                                         compound='bottom')
            self.Record_Button.place(x=950, y=100)
        
        # Clean Button
        if 'Clean_Button' not in self.exclude_widgets:
            self.Clean_Button = customtkinter.CTkButton(master=self.master,
                                                        width=150,
                                                        height=40,
                                                        border_width=2,
                                                        text='Limpar',
                                                        compound='bottom',
                                                        fg_color='#9C0908')
            self.Clean_Button.place(x=950, y=30)

# Exemplo de uso:
app = customtkinter.CTk()
app.title('Calculadora de Custo')
app.geometry('1200x600')
app.state('zoomed')

my_tab = customtkinter.CTkTabview(app, height=800, width=800)
my_tab.pack(side="top", fill="x", pady=10)

# Abas
tab1 = my_tab.add('Assinatura')
tab2 = my_tab.add('Por uso')

# Frames
frame1 = customtkinter.CTkFrame(master=tab1, width=1500, height=1200)
frame1.pack(fill='both', expand=True)

frame2 = customtkinter.CTkFrame(master=tab2, width=1500, height=1200)
frame2.pack(fill='both', expand=True)

# Instancia os widgets personalizados no frame1
custom_widgets1 = CustomWidgets(frame1)

# Instancia os widgets personalizados no frame2, excluindo alguns widgets
custom_widgets2 = CustomWidgets(frame2, exclude_widgets=['Cyclopay_Tax', 'Cost_Invoice'])
#CustomWidgets(frame2, 'frame2', widget_positions={'Server_Cost': (130, 30), 'Server_Cost_Label: (20, 40)})

app.mainloop()
