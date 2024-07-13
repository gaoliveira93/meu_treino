import tkinter as tk
from tkinter import ttk
import pandas as pd

class App(tk.Tk):
def create_table(self, app):
    
    num_rows = len(index)
    num_cols = len(columns) 

    cost_tera = float(self.custom_widgets.Cost_Tera.get())
    initial_tax = float(self.custom_widgets.Initial_Tax.get())
    cost_invoice = float(self.custom_widgets.Cost_Invoice.get())
    server_cost = float(self.custom_widgets.Server_Cost.get())
    cyclopay_tax = float(self.custom_widgets.Cyclopay_Tax.get()) 
    Dolar_Price = float(self.custom_widgets.Dolar_Price.get())
    IOF = float(self.custom_widgets.IOF.get())
    Fix_Tax_Cyclopay = float(self.custom.widgets.Fix_Tax_Cyclopay.get())
    Tax = month_RS * float(self.custom_widgets.initial_tax.get())
    server_cost = server_cost
    Margin = float(self.custom_widgets.Margim.get())

    anual_US = cost_tera * (1-0.15)
    month_US = anual_US/12
    anual_RS = anual_US * Dolar_Price
    month_RS = anual_RS * Dolar_Price
    cyclopay_taxx = month_RS * cyclopay_tax
    IOFF = month_RS * IOF
    month_selling_price = (month_RS + cyclopay_taxx + IOFF + Fix_Tax_Cyclopay + Tax + server_cost + cost_invoice + Margin)
    month_selling_price_credit = month_selling_price * 1.065
    selling_dolar_price = month_selling_price_credit * Dolar_Price
    

    self.df = pd.DataFrame(index=range(num_rows), columns=range(num_cols))
    for i in range(num_cols):
        for j in range(num_rows):
            if j == 1:
                self.df.iloc[i,j] = anual_US
            elif j == 2:
                self.df.iloc[i,j] = month_US
            elif j == 3:
                self.df.iloc[i,j] = anual_RS
            elif j == 4:
                self.df.iloc[i,j] = month_RS
            elif j == 5:
                self.df.iloc[i,j] = cyclopay_taxx
            elif j == 6:
                self.df.iloc[i,j] = IOFF
            elif j == 7:
                self.df.iloc[i,j] = Fix_Tax_Cyclopay
            elif j == 8:
                self.df.iloc[i,j] = Tax
            elif j == 9:
                self.df.iloc[i,j] = server_cost
            elif j == 10:
                self.df.iloc[i,j] = cost_invoice
            elif j == 11:
                self.df.iloc[i,j] = Margin
            elif j == 12:
                self.df.iloc[i,j] = month_selling_price
            elif j == 13:
                self.df.iloc[i,j] = month_selling_price_credit
            elif j == 14:
                self.df.iloc[i,j] = selling_dolar_price
