import numpy as np
import tkinter as tk

class App:
    def __init__(self, root):
        self.entries = {}
        self.create_widgets(root)

    def create_widgets(self, root):
        # Criação dos campos de entrada
        labels = ['Cost_Tera', 'Dolar_Price', 'Cyclopay_Tax', 'IOF %']
        for label in labels:
            tk.Label(root, text=label + ":").pack()
            self.entries[label] = tk.Entry(root)
            self.entries[label].pack()
        
        # Botão para criar o array
        tk.Button(root, text="Calcular", command=self.create_array).pack()

    def create_array(self):
        # Lista de dados
        dados = [1, 2, 3, 4, 5]

        # Coleta dos valores das entradas
        Anual_USD = float(self.entries['Cost_Tera'].get()) * 0.85
        Value_dolar = float(self.entries['Dolar_Price'].get())
        Month_USD = Anual_USD / 12
        Anual_Brl = Anual_USD * Value_dolar
        Cyclopay_Tax = float(self.entries['Cyclopay_Tax'].get())
        IOFF = float(self.entries['IOF %'].get())

        # Multiplicação dos dados pelos valores das entradas e print dos resultados
        result_Anual_USD = np.array([d * Anual_USD for d in dados])
        result_Value_dolar = np.array([d * Value_dolar for d in dados])
        result_Month_USD = np.array([d * Month_USD for d in dados])
        result_Anual_Brl = np.array([d * Anual_Brl for d in dados])
        result_Cyclopay_Tax = np.array([d * Cyclopay_Tax for d in dados])
        result_IOFF = np.array([d * IOFF for d in dados])

        print("Result Anual_USD:", result_Anual_USD)
        print("Result Value_dolar:", result_Value_dolar)
        print("Result Month_USD:", result_Month_USD)
        print("Result Anual_Brl:", result_Anual_Brl)
        print("Result Cyclopay_Tax:", result_Cyclopay_Tax)
        print("Result IOFF:", result_IOFF)

        # Concatenando todos os resultados em um único array
        result_array = np.concatenate([result_Anual_USD, result_Value_dolar, result_Month_USD, result_Anual_Brl, result_Cyclopay_Tax, result_IOFF])

        print("Final Result Array:", result_array)

root = tk.Tk()
app = App(root)
root.mainloop()
