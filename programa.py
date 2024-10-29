import pandas as pd
from openpyxl import load_workbook


df = pd.read_excel('Rotas.xlsx')

for index, row in df.iterrows():
    # Cada row é um objeto Series (uma linha do DataFrame)
    Row_Id = row['Row Id']
    Title = row['Title']
    Motorista_Id = row['Motorista_Id']
    Status =  row["Status"]
    Valor_Carga=  row["Valor_Carga"]
    Cadastro= row['Cadastro']


    # Criar um objeto personalizado com esses dados






