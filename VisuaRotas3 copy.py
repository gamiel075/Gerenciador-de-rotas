import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# Carregar os dados do Excel
df = pd.read_excel('Rotas.xlsx')

# Função para criar o gráfico de pizza
def criar_grafico_pizza():
    Destino_Valor = df[['Destino', 'Valor_Carga']].groupby('Destino').sum()
    fig, ax = plt.subplots()
    ax.pie(Destino_Valor['Valor_Carga'], labels=Destino_Valor.index, autopct='%1.1f%%', startangle=140)
    ax.set_title('Carga por Destino')
    return fig

# Função para criar o gráfico de barras
def criar_grafico_barras():
    Status_valor = df[['Status', 'Valor_Carga']].groupby('Status').sum()
    fig, ax = plt.subplots()
    cor = ['red', 'blue', 'green']
    ax.bar(Status_valor.index, Status_valor['Valor_Carga'], color=cor)
    ax.set_xlabel('Status')
    ax.set_ylabel('Valor Final')
    ax.set_title('Faturamento por Status')
    return fig

# Função para criar o gráfico de linha
def criar_grafico_linha():
    Valor_Data = df[['Cadastro', 'Valor_Carga']].groupby('Cadastro').sum()
    Valor_Data = Valor_Data.reset_index()
    fig, ax = plt.subplots()
    ax.plot(Valor_Data['Cadastro'], Valor_Data['Valor_Carga'], marker='o', linestyle='-', color='blue')
    ax.set_xlabel('Data')
    ax.set_ylabel('Valor da Carga')
    ax.set_title('Valor da Carga por Data')
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y')
    return fig

# Função para adicionar um gráfico em um frame
def adicionar_grafico(frame, fig):
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Criar a janela principal
root = tk.Tk()
root.title("VisualRotas")
root.geometry("800x600")
root.configure(bg='lightblue')

# Título do programa
titulo = tk.Label(root, text="VisualRotas", font=("Helvetica", 20), bg='lightblue', fg='orange')
titulo.pack(pady=10)

# Frame para os gráficos
frame_grafico_pizza = ttk.Frame(root)
frame_grafico_pizza.pack(fill=tk.BOTH, expand=True)
adicionar_grafico(frame_grafico_pizza, criar_grafico_pizza())

frame_grafico_barras = ttk.Frame(root)
frame_grafico_barras.pack(fill=tk.BOTH, expand=True)
adicionar_grafico(frame_grafico_barras, criar_grafico_barras())

frame_grafico_linha = ttk.Frame(root)
frame_grafico_linha.pack(fill=tk.BOTH, expand=True)
adicionar_grafico(frame_grafico_linha, criar_grafico_linha())

# Mostrar a janela
root.mainloop()



