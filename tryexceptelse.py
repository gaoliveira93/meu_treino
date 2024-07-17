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
        dados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # Coleta dos valores das entradas
        Anual_USD = float(self.entries['Cost_Tera'].get()) * 0.85
        Value_dolar = float(self.entries['Dolar_Price'].get())
        Month_USD = Anual_USD / 12
        Anual_Brl = Anual_USD * Value_dolar
        Cyclopay_Tax = float(self.entries['Cyclopay_Tax'].get())
        IOFF = float(self.entries['IOF %'].get())

        # Multiplicação dos dados pelos valores das entradas
        result_array = np.array([d * Anual_USD for d in dados] +
                                [d * Value_dolar for d in dados] +
                                [d * Month_USD for d in dados] +
                                [d * Anual_Brl for d in dados] +
                                [d * Cyclopay_Tax for d in dados] +
                                [d * IOFF for d in dados])

        print(result_array)

root = tk.Tk()
app = App(root)
root.mainloop()