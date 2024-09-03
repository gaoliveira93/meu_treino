import pandas as pd
import pyautogui

data = pd.read_excel('Teste_Email.xlsx')

pyautogui.write(data['Assunto'][1])