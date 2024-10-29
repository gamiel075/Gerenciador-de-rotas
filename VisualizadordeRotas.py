import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

# Função para processar dados e mostrar resultados
def processar_dados():
    try:
        # Lê os dados do Excel
        df = pd.read_excel('Rotas.xlsx')
        
        # Cálculos
        Valor_Total_Carga = df['Valor_Carga'].sum()
        Media_Carga = Valor_Total_Carga / 30
        Lucro_media_carga = Media_Carga * 0.30
        
        carga_rota = df[['Title', 'Valor_Carga']].groupby('Title').sum()
        df_ranking = df.sort_values(by='Valor_Carga', ascending=False)
        Destino_Valor = df[['Destino', 'Valor_Carga']].groupby('Destino').sum()
        Status_valor = df[['Status', 'Valor_Carga']].groupby('Status').sum()
        Valor_Data = df[['Cadastro', 'Valor_Carga']].groupby('Cadastro').sum().reset_index()
        media_valor_carga = Valor_Data['Valor_Carga'].mean()

        # Monta o resultado em uma string
        resultado = f"Valor Total Carga: {Valor_Total_Carga}\n"
        resultado += f"Média de Carga: {Media_Carga}\n"
        resultado += f"Lucro Médio da Carga: {Lucro_media_carga}\n\n"
        resultado += "Carga por Rota:\n" + carga_rota.to_string() + "\n\n"
        resultado += "Ranking:\n" + df_ranking.to_string() + "\n\n"
        resultado += "Valor da Carga por Destino:\n" + Destino_Valor.to_string() + "\n\n"
        resultado += "Valor da Carga por Status:\n" + Status_valor.to_string() + "\n\n"
        resultado += "Valor Carga por Dia:\n" + Valor_Data.to_string() + "\n"
        resultado += f"Média Valor Carga: {media_valor_carga}\n"

        # Atualiza a caixa de texto com os resultados
        text_area.delete(1.0, tk.END)  # Limpa o texto anterior
        text_area.insert(tk.END, resultado)  # Insere o novo resultado

        # Gráficos
        gerar_graficos(Destino_Valor, Status_valor, Valor_Data)

    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Função para gerar gráficos
def gerar_graficos(Destino_Valor, Status_valor, Valor_Data):
    # Gráfico de Pizza
    plt.figure(figsize=(16, 10))
    plt.pie(Destino_Valor['Valor_Carga'], labels=Destino_Valor.index, autopct='%1.1f%%', startangle=140)
    plt.title('Carga por Destino')
    plt.axis('equal')  # Para garantir que o gráfico de pizza seja um círculo
    plt.show()

    # Gráfico de Barras
    cor = ['red', 'blue', 'green']
    plt.bar(Status_valor.index, Status_valor['Valor_Carga'], color=cor)
    plt.xlabel('Status')
    plt.ylabel('Valor Final')
    plt.title('Faturamento por Status')
    plt.show()

    # Gráfico de Linhas
    plt.figure(figsize=(10, 5))
    plt.plot(Valor_Data['Cadastro'], Valor_Data['Valor_Carga'], marker='o', linestyle='-', color='blue')
    plt.xlabel('Data')
    plt.ylabel('Valor da Carga')
    plt.title('Valor da Carga por Data')
    plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x para melhor legibilidade
    plt.grid(axis='y')  # Adiciona uma grade ao gráfico
    plt.tight_layout()  # Ajusta o layout para não cortar rótulos
    plt.show()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Análise de Rotas")
janela.geometry("600x600")

# Botão para processar dados
botao_processar = tk.Button(janela, text="Processar Dados", command=processar_dados)
botao_processar.pack(pady=10)

# Área de texto para exibir resultados
text_area = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=70, height=20)
text_area.pack(pady=10)

# Executa a aplicação
janela.mainloop()
