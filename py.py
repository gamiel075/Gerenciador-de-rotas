import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Função para carregar os dados e calcular os KPIs
def carregar_dados():
    global df
    df = pd.read_excel('Rotas.xlsx')

    # Calcular KPIs
    Valor_Total_Carga = df['Valor_Carga'].sum()
    Media_Carga = Valor_Total_Carga / 30
    Lucro_media_carga = Media_Carga * 0.30

    # Atualizar os KPIs na interface
    label_kpi_total.config(text=f'Valor Total da Carga: R$ {Valor_Total_Carga:.2f}')
    label_kpi_media.config(text=f'Média da Carga: R$ {Media_Carga:.2f}')
    label_kpi_lucro.config(text=f'Lucro Médio da Carga: R$ {Lucro_media_carga:.2f}')


# Função para abrir o gráfico de pizza
def abrir_grafico_pizza():
    Destino_Valor = df[['Destino', 'Valor_Carga']].groupby('Destino').sum()
    plt.figure(figsize=(8, 6))
    plt.pie(Destino_Valor['Valor_Carga'], labels=Destino_Valor.index, autopct='%1.1f%%', startangle=140)
    plt.title('Carga por Destino')
    plt.axis('equal')  # Para garantir que o gráfico de pizza seja um círculo
    plt.show()


# Função para abrir o gráfico de barras
def abrir_grafico_barras():
    Status_valor = df[['Status', 'Valor_Carga']].groupby('Status').sum()
    plt.figure(figsize=(8, 6))
    cor = ['red', 'blue', 'green']
    plt.bar(Status_valor.index, Status_valor['Valor_Carga'], color=cor)
    plt.xlabel('Status')
    plt.ylabel('Valor Final')
    plt.title('Faturamento por Status')
    plt.show()


# Função para abrir o gráfico de linha
def abrir_grafico_linha():
    Valor_Data = df[['Cadastro', 'Valor_Carga']].groupby('Cadastro').sum()
    Valor_Data = Valor_Data.reset_index()
    plt.figure(figsize=(8, 6))
    plt.plot(Valor_Data['Cadastro'], Valor_Data['Valor_Carga'], marker='o', linestyle='-', color='blue')
    plt.xlabel('Data')
    plt.ylabel('Valor da Carga')
    plt.title('Valor da Carga por Data')
    plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x para melhor legibilidade
    plt.grid(axis='y')  # Adiciona uma grade ao gráfico
    plt.tight_layout()  # Ajusta o layout para não cortar rótulos
    plt.show()


# Criar a janela principal
root = tk.Tk()
root.title("Gerenciador de Rotas")
root.geometry("500x400")
root.configure(bg='lightblue')

# Estilo
style = ttk.Style()
style.configure("TButton", background="orange", font=("Arial", 12))
style.configure("TLabel", background="lightblue", font=("Arial", 14))

# Criar um frame para os KPIs
frame_kpis = tk.Frame(root, bg='lightblue')
frame_kpis.pack(pady=20)

label_kpi_total = ttk.Label(frame_kpis, text='Valor Total da Carga: R$ 0.00')
label_kpi_total.pack(pady=5)

label_kpi_media = ttk.Label(frame_kpis, text='Média da Carga: R$ 0.00')
label_kpi_media.pack(pady=5)

label_kpi_lucro = ttk.Label(frame_kpis, text='Lucro Médio da Carga: R$ 0.00')
label_kpi_lucro.pack(pady=5)

# Botões para abrir os gráficos
frame_botoes = tk.Frame(root, bg='lightblue')
frame_botoes.pack(pady=20)

botao_grafico_pizza = ttk.Button(frame_botoes, text="Gráfico de Pizza", command=abrir_grafico_pizza)
botao_grafico_pizza.pack(side=tk.LEFT, padx=10)

botao_grafico_barras = ttk.Button(frame_botoes, text="Gráfico de Barras", command=abrir_grafico_barras)
botao_grafico_barras.pack(side=tk.LEFT, padx=10)

botao_grafico_linha = ttk.Button(frame_botoes, text="Gráfico de Linha", command=abrir_grafico_linha)
botao_grafico_linha.pack(side=tk.LEFT, padx=10)

# Carregar dados e atualizar KPIs
carregar_dados()

# Iniciar a interface
root.mainloop()
