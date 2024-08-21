import customtkinter
import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import requests
import json

def dolar_API():
    response = requests.get('https://backend.selfspaces.com.br/cotacao-dia')
    data = response.json()
    dolar = data[0].get('valor_final')
    return str(dolar)

dolar_API()

