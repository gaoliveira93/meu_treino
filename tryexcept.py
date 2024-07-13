import tkinter as tk
from tkinter import ttk
import pandas as pd
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

index = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','30','40','50']
columns = ['Espaço TB', 'ANUAL(U$)', 'MENSAL(U$)', 'ANUAL(R$)', 'MENSAL(R$)', 'Taxa % Cyclopay', 'IOF %', 'Taxa fixa Cyclopay', 'Impostos', 'Custo servidor', 'Custo NF', 'Margem', 'VALOR VENDA MENSAL (R$)', 'VALOR MENSAL câmbio cartão', 'VALOR VENDA (Dólar)']

class CustomWidgets:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.create_widgets()
        self.create_table()
        
    def create_widgets(self):
        self.entries = {}

        row_positions = [
            ('Cyclopay_Tax', 'Taxa Cyclopay :', 0),
            ('Initial_Tax', 'Imposto :', 1),
            ('Cost_Tera', 'Custo por Terabyte :', 2),
            ('Cost_Invoice', 'Custo Nota Fiscal :', 3),
            ('Server_Cost', 'Custo Servidor :', 4),
            ('Dolar_Price', 'Câmbio do dólar :', 5),
            ('Margim', 'Margem de Lucro :', 6),
            ('IOF', 'IOF :', 7),
            ('Fix_Tax_Cyclopay', 'Taxa Fixa Cyclopay :', 8)
        ]

        for key, label_text, row in row_positions:
            label = customtkinter.CTkLabel(master=self.parent_frame, width=15, height=2, text=label_text, fg_color='#292929', corner_radius=0)
            label.grid(row=row, column=0, padx=10, pady=10)
            self.entries[key] = customtkinter.CTkEntry(master=self.parent_frame, width=150, height=40, border_width=2, justify='c')
            self.entries[key].grid(row=row, column=1, padx=10, pady=10)

    def create_table(self):
        self.data = pd.DataFrame(columns=columns, index=index)

        self.treeview = ttk.Treeview(self.parent_frame, columns=columns, show="headings")

        for col in columns:
            self.treeview.heading(col, text=col)

        self.treeview.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

    def generate_table(self):
        data_dict = {}
        for key in self.entries:
            data_dict[key] = self.entries[key].get()

        self.data.loc[len(self.data)] = data_dict

        # Limpa a tabela antes de adicionar os novos dados
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Insere os novos dados na tabela
        for i, row_data in self.data.iterrows():
            self.treeview.insert("", "end", values=list(row_data))

    def clear_entries(self):
        for key in self.entries:
            self.entries[key].delete(0, tk.END)

# Interface principal
app = customtkinter.CTk()
app.title('Calculadora de Custo')
app.geometry('1200x600')

# Abas
my_tab = customtkinter.CTkTabview(app, height=800, width=800)
my_tab.pack(side="top", fill="x", pady=10)

tab1 = my_tab.add('Assinatura')
tab2 = my_tab.add('Por uso')

# Frames para as tabelas
table_frame1 = customtkinter.CTkFrame(master=tab1, width=1500, height=400)
table_frame1.pack(fill='both', expand=True, pady=10)

table_frame2 = customtkinter.CTkFrame(master=tab2, width=1500, height=400)
table_frame2.pack(fill='both', expand=True, pady=10)

# Instancia os widgets personalizados nas abas
custom_widgets1 = CustomWidgets(table_frame1)
custom_widgets2 = CustomWidgets(table_frame2)

# Botões de Gravar
record_button1 = customtkinter.CTkButton(master=tab1, width=150, height=40, border_width=2, text='Gravar', compound='bottom', command=custom_widgets1.generate_table)
record_button1.place(x=950, y=100)

record_button2 = customtkinter.CTkButton(master=tab2, width=150, height=40, border_width=2, text='Gravar', compound='bottom', command=custom_widgets2.generate_table)
record_button2.place(x=950, y=100)

# Botões de Limpar
clear_button1 = customtkinter.CTkButton(master=tab1, width=150, height=40, border_width=2, text='Limpar', compound='bottom', fg_color='#9C0908', command=custom_widgets1.clear_entries)
clear_button1.place(x=950, y=30)

clear_button2 = customtkinter.CTkButton(master=tab2, width=150, height=40, border_width=2, text='Limpar', compound='bottom', fg_color='#9C0908', command=custom_widgets2.clear_entries)
clear_button2.place(x=950, y=30)

app.mainloop()
