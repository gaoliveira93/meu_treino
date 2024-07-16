import customtkinter
import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

index = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','30','40','50']
columns = ['Espaço TB', 'ANUAL(U$)', 'MENSAL(U$)', 'ANUAL(R$)', 'MENSAL(R$)', 'Taxa % Cyclopay', 'IOF %', 'Taxa fixa Cyclopay', 'Impostos', 'Custo servidor', 'Custo NF', 'Margem', 'VENDA MENSAL (R$)', 'MENSAL câmbio cartão', 'VALOR (Dólar)']

class CustomWidgets:
    def __init__(self, master, exclude_widgets=[]):
        self.master = master
        self.exclude_widgets = exclude_widgets
        self.entries = {}
        self.create_widgets()
        
    def create_widgets(self):
        widget_params = [
            ('Cyclopay_Tax', 'Taxa Cyclopay :', 750, 170, 620, 180),
            ('Initial_Tax', 'Imposto :', 450, 30, 310, 40),
            ('Cost_Tera', 'Custo por Terabyte :', 750, 30, 620, 40),
            ('Cost_Invoice', 'Custo Nota Fiscal :', 750, 100, 620, 110),
            ('Server_Cost', 'Custo Servidor :', 130, 30, 20, 40),
            ('Dolar_Price', 'Câmbio do dólar :', 130, 100, 15, 110),
            ('Margim', 'Margem de Lucro :', 130, 170, 15, 180),
            ('IOF', 'IOF :', 450, 100, 310, 110),
            ('Fix_Tax_Cyclopay', 'Taxa Fixa Cyclopay :', 450, 170, 310, 180)
        ]

        for key, label, x_entry, y_entry, x_label, y_label in widget_params:
            if key not in self.exclude_widgets:
                self.entries[key] = customtkinter.CTkEntry(master=self.master, width=150, height=40, border_width=2, justify='c')
                self.entries[key].place(x=x_entry, y=y_entry)
                label_widget = customtkinter.CTkLabel(master=self.master, width=10, height=10, text=label, fg_color='#292929', corner_radius=0)
                label_widget.place(x=x_label, y=y_label)
        
        # Calculate Button
        if 'Calculate_Button' not in self.exclude_widgets:
            self.Record_Button = customtkinter.CTkButton(master=self.master, width=150, height=40, border_width=2, text='Calcular', command=self.generate_table)
            self.Record_Button.place(x=950, y=100)
        
        # Clean Button
        if 'Clean_Button' not in self.exclude_widgets:
            self.Clean_Button = customtkinter.CTkButton(master=self.master, width=150, height=40, border_width=2, text='Limpar', compound='bottom', fg_color='#9C0908')
            self.Clean_Button.place(x=950, y=30)

        # Record Button
        if 'Record_Button' not in self.exclude_widgets:
            self.Record_Button = customtkinter.CTkButton(master=self.master, width=150, height=40, border_width=2, text='Gravar', compound='bottom')
            self.Record_Button.place(x=950, y=170)

    def generate_table(self):
        data_dict = {key: self.entries[key].get() for key in self.entries}
        self.data.loc[len(self.data)] = data_dict
        self.update_table()

    def update_table(self):
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        for index, row in self.data.iterrows():
            self.treeview.insert('', 'end', values=row.tolist())

    def create_table(self):
        self.data = pd.DataFrame(columns=columns, index=index)
        self.treeview = ttk.Treeview(self.master, columns=columns, show="headings")

        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=98, stretch=tk.NO, minwidth=50, anchor='center')
        
        self.treeview.place(x=10, y=350, width=2000, height=400)

    def create_array(self):
        Anual_USD = float((self.entries['Cost_Tera'].get()) * 0.85)
        Value_dolar = float(self.entries['Dolar_Price'].get())
        Month_USD = float(Anual_USD/12)
        Anual_Brl = float(Anual_USD * Value_dolar)
        Cyclopay_Tax = float((self.entries['Cyclopay_Tax'].get()) * Month_Brl)
        IOFF = float((self.entries['IOF %'].get()) * Month_USD)
        Fix_Tax_Cyclopay = float(self.entries['Fix_Tax_Cyclopay'].get())
        Initial_Tax = float((self.entries['Initial_Tax'].get()) * Month_Brl)
        Server_Cost = float(self.entries['Server_Cost'].get())
        Cost_Invoice = float(self.entries['Cost_Invoice'].get())
        Margim = float(((Month_Brl + Cyclopay_Tax + IOFF + Fix_Tax_Cyclopay + Initial_Tax + Server_Cost + Cost_Invoice)/1-self.entries['Margim'].get()) / (Month_Brl + Cyclopay_Tax + IOFF + Fix_Tax_Cyclopay + Initial_Tax + Server_Cost + Cost_Invoice))
        Month_Brl = float(Month_USD * Anual_USD)
        Month_Brl_CC = float(Month_Brl * 1.065)
        Month_USD_CC = float(Month_Brl_CC * Value_dolar)
        TreeView_array = np.array([])





# Exemplo de uso:
app = customtkinter.CTk()
app.title('Calculadora de Custo')
app.geometry('1200x600')

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
custom_widgets1.create_table()

# Instancia os widgets personalizados no frame2, excluindo alguns widgets
custom_widgets2 = CustomWidgets(frame2, exclude_widgets=['Cyclopay_Tax', 'Cost_Invoice'])
custom_widgets2.create_table()

app.mainloop()
