import customtkinter
import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import requests
import time
import json

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

columns = ['Espaço TB', 'ANUAL(U$)', 'MENSAL(U$)', 'ANUAL(R$)', 'MENSAL(R$)', 'Taxa % Cyclopay', 'IOF %', 'Taxa fixa Cyclopay', 'Impostos', 'Custo servidor', 'Custo NF', 'Margem', 'VENDA MENSAL (R$)', 'MENSAL câmbio cartão', 'VALOR (Dólar)']

def dolar_API():
    response = requests.get('https://backend.selfspaces.com.br/cotacao-dia')
    data = response.json()
    dolar = data[0].get('valor_final')
    return dolar

def validate_decimal(P):
    if P in ("", ","):
        return True
    try:
        float(P.replace(",", "."))
        return True
    except ValueError:
        return False

class CustomWidgets:
    def __init__(self, master, exclude_widgets=[]):
        self.master = master
        self.exclude_widgets = exclude_widgets
        self.entries = {}
        self.create_widgets()
        
    def create_widgets(self):
        widget_params = [
            ('Fix_Tax_Cyclopay', 'Taxa Fixa Cyclopay :', 750, 170, 620, 180),
            ('Initial_Tax', 'Imposto :', 450, 30, 310, 40),
            ('Cost_Tera', 'Custo por Terabyte :', 750, 30, 620, 40),
            ('Cost_Invoice', 'Custo Nota Fiscal :', 750, 100, 620, 110),
            ('Server_Cost', 'Custo Servidor :', 130, 30, 20, 40),
            ('Dolar_Price', 'Câmbio do dólar :', 130, 100, 15, 110),
            ('Margim', 'Margem de Lucro :', 130, 170, 15, 180),
            ('IOF', 'IOF :', 450, 100, 310, 110),
            ('Cyclopay_Tax', 'Taxa Cyclopay :', 450, 170, 310, 180)
        ]

        vcmd = (self.master.register(validate_decimal), '%P')
        
        for key, label, x_entry, y_entry, x_label, y_label in widget_params:
            if key not in self.exclude_widgets:
                self.entries[key] = customtkinter.CTkEntry(master=self.master, width=150, height=40, border_width=2, justify='center', validate='key', validatecommand=vcmd)
                self.entries[key].place(x=x_entry, y=y_entry)
                label_widget = customtkinter.CTkLabel(master=self.master, width=10, height=10, text=label, fg_color='#292929', corner_radius=0)
                label_widget.place(x=x_label, y=y_label)
                if key == 'Dolar_Price':
                    self.entries[key].insert(0, dolar_API())
        
        # Calculate Button
        if 'Calculate_Button' not in self.exclude_widgets:
            self.Calculate_Button = customtkinter.CTkButton(master=self.master, width=150, height=40, border_width=2, text='Calcular', command=self.generate_table)
            self.Calculate_Button.place(x=950, y=100)
        
        # Clean Button
        if 'Clean_Button' not in self.exclude_widgets:
            self.Clean_Button = customtkinter.CTkButton(master=self.master, width=150, height=40, border_width=2, text='Limpar', compound='bottom', fg_color='#9C0908', command=self.clean_table)
            self.Clean_Button.place(x=950, y=30)

        # Record Button
        if 'Record_Button' not in self.exclude_widgets:
            self.Record_Button = customtkinter.CTkButton(master=self.master, width=150, height=40, border_width=2, text='Gravar', compound='bottom')
            self.Record_Button.place(x=950, y=170)

    def update_table(self):
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        for _, row in self.data.iterrows():
            self.treeview.insert('', 'end', values=row.tolist())

    def create_table(self):
        self.data = pd.DataFrame(columns=columns)

        # Excluindo colunas
        excluded_columns = set()
        if 'Fix_Tax_Cyclopay' in self.exclude_widgets:
            excluded_columns.add('Taxa fixa Cyclopay')
        if 'Initial_Tax' in self.exclude_widgets:
            excluded_columns.add('Impostos')
        if 'Cost_Tera' in self.exclude_widgets:
            excluded_columns.add('ANUAL(U$)')
            excluded_columns.add('MENSAL(U$)')
            excluded_columns.add('ANUAL(R$)')
            excluded_columns.add('MENSAL(R$)')
        if 'Cost_Invoice' in self.exclude_widgets:
            excluded_columns.add('Custo NF')
        if 'Server_Cost' in self.exclude_widgets:
            excluded_columns.add('Custo servidor')
        if 'Dolar_Price' in self.exclude_widgets:
            excluded_columns.add('MENSAL câmbio cartão')
            excluded_columns.add('VALOR (Dólar)')
        if 'Margim' in self.exclude_widgets:
            excluded_columns.add('Margem')
        if 'IOF' in self.exclude_widgets:
            excluded_columns.add('IOF %')
        if 'Cyclopay_Tax' in self.exclude_widgets:
            excluded_columns.add('Taxa % Cyclopay')

        filtered_columns = [col for col in columns if col not in excluded_columns]

        self.treeview = ttk.Treeview(self.master, columns=filtered_columns, show="headings")

        for col in filtered_columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=98, stretch=tk.NO, minwidth=50, anchor='center')
        
        self.treeview.place(x=10, y=280, width=1495, height=400)
        scrollbarY = tk.Scrollbar(self.master, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=scrollbarY.set)
        scrollbarY.place(x=1480, y=280, width=20, height=380)

    def clean_table(self):
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def generate_table(self):
        Teras = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 30.0, 40.0, 50.0]

        try:
            # Extrair valores apenas se os widgets não foram excluídos
            Anual_USD = round(float(self.entries['Cost_Tera'].get().replace(",", ".")), 2) if 'Cost_Tera' in self.entries else 0
            Value_dolar = round(float(self.entries['Dolar_Price'].get().replace(",", ".")), 2) if 'Dolar_Price' in self.entries else 0
            Cyclopay_Tax = round(float(self.entries['Cyclopay_Tax'].get().replace(",", ".")), 2) if 'Cyclopay_Tax' in self.entries else 0
            IOFF = round(float(self.entries['IOF'].get().replace(",", ".")), 2) if 'IOF' in self.entries else 0
            Fix_Tax_Cyclopay = round(float(self.entries['Fix_Tax_Cyclopay'].get().replace(",", ".")), 2) if 'Fix_Tax_Cyclopay' in self.entries else 0
            Initial_Tax = round(float(self.entries['Initial_Tax'].get().replace(",", ".")), 2) if 'Initial_Tax' in self.entries else 0
            Server_Cost = round(float(self.entries['Server_Cost'].get().replace(",", ".")), 2) if 'Server_Cost' in self.entries else 0
            Cost_Invoice = round(float(self.entries['Cost_Invoice'].get().replace(",", ".")), 2) if 'Cost_Invoice' in self.entries else 0

            Month_USD = round((Anual_USD / 12.00), 2)
            Anual_Brl = round((Anual_USD * Value_dolar), 2)
            Month_Brl = round((Month_USD * Value_dolar), 2)
            Month_Brl_CC = round((Month_Brl * 1.065), 2)
            Month_USD_CC = round((Month_Brl_CC / Value_dolar), 2)

            result_Anual_USD = np.round([t * (Anual_USD * 0.85) for t in Teras], 2)
            result_Value_dolar = np.round([t * Value_dolar for t in Teras])
            result_Month_USD = np.round([result_Anual_USD[i] / 12 for i in range(len(Teras))],2)
            result_Anual_Brl = np.round([t * Anual_Brl for t in Teras],2)
            result_Cyclopay_Tax = np.round([t * (Cyclopay_Tax * Month_Brl) for t in Teras],2)
            result_IOFF = np.round([t * (IOFF * Month_USD) for t in Teras],2)
            result_Fix_Tax_Cyclopay = np.round([Fix_Tax_Cyclopay] * len(Teras))
            result_Initial_Tax = np.round([t * (Initial_Tax * Month_Brl) for t in Teras],2)
            result_Server_Cost = np.round([t * Server_Cost for t in Teras],2)
            result_Cost_Invoice = np.round([Cost_Invoice] * len(Teras))
            result_Month_Brl = np.round([t * Month_Brl for t in Teras],2)
            result_Month_Brl_CC = np.round([t * Month_Brl_CC for t in Teras],2)
            result_Month_USD_CC = np.round([t * Month_USD_CC for t in Teras],2)

            data_dict = {
                'Espaço TB': Teras,
                'ANUAL(U$)': result_Anual_USD,
                'MENSAL(U$)': result_Month_USD,
                'ANUAL(R$)': result_Anual_Brl,
                'MENSAL(R$)': result_Month_Brl,
                'Taxa % Cyclopay': result_Cyclopay_Tax,
                'IOF %': result_IOFF,
                'Taxa fixa Cyclopay': result_Fix_Tax_Cyclopay,
                'Impostos': result_Initial_Tax,
                'Custo servidor': result_Server_Cost,
                'Custo NF': result_Cost_Invoice,
                'Margem': result_Month_Brl,
                'VENDA MENSAL (R$)': result_Month_Brl,
                'MENSAL câmbio cartão': result_Month_Brl_CC,
                'VALOR (Dólar)': result_Month_USD_CC,
            }

            # Excluir colunas baseadas nos widgets excluídos
            for key in self.exclude_widgets:
                if key == 'Fix_Tax_Cyclopay':
                    del data_dict['Taxa fixa Cyclopay']
                elif key == 'Initial_Tax':
                    del data_dict['Impostos']
                elif key == 'Cost_Tera':
                    del data_dict['ANUAL(U$)']
                    del data_dict['MENSAL(U$)']
                    del data_dict['ANUAL(R$)']
                    del data_dict['MENSAL(R$)']
                elif key == 'Cost_Invoice':
                    del data_dict['Custo NF']
                elif key == 'Server_Cost':
                    del data_dict['Custo servidor']
                elif key == 'Dolar_Price':
                    del data_dict['MENSAL câmbio cartão']
                    del data_dict['VALOR (Dólar)']
                elif key == 'Margim':
                    del data_dict['Margem']
                elif key == 'IOF':
                    del data_dict['IOF %']
                elif key == 'Cyclopay_Tax':
                    del data_dict['Taxa % Cyclopay']

            self.data = pd.DataFrame(data_dict)
            self.update_table()

        except Exception as e:
            print("Erro ao gerar a tabela:", e)

# Criar a janela principal
app = customtkinter.CTk()
app.title('Calculadora de Custo')
app.geometry('1500x700')

# Criar e posicionar os widgets no frame1 e frame2
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
custom_widgets2 = CustomWidgets(frame2, exclude_widgets=['Fix_Tax_Cyclopay','Cost_Invoice'])
custom_widgets2.create_table()

# Iniciar o loop principal do Tkinter
app.mainloop()
