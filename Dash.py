import csv
import pandas as pd

# Dados para serem escritos no CSV
dados = [
    ['Nome', 'Idade', 'Cidade', 'Data'],
    ['João', '25', 'São Paulo', '01-10-1990'],
    ['Maria', '30', 'Rio de Janeiro', '01-10-1998'],
    ['Carlos', '35', 'Belo Horizonte', '01-10-1995'], 
]

# Criar e escrever no arquivo CSV
with open('dados.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    for linha in dados:
        escritor.writerow(linha)

# Ler o arquivo CSV e carregar em um DataFrame
df = pd.read_csv('dados.csv')

# Converter a coluna 'Data' para o formato datetime
df['Data'] = pd.to_datetime(df['Data'], format='%d-%m-%Y')

# Converter a coluna 'Data' para o formato MM/DD/YYYY
df['Data'] = df['Data'].dt.strftime('%m/%d/%Y')

print(df)
