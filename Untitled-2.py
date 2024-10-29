import pandas as pd
import matplotlib.pyplot as plt




df = pd.read_excel('Rotas.xlsx')
print(df)



print("----------")



Valor_Total_Carga = df['Valor_Carga'].sum()
print(Valor_Total_Carga)
print('-----------')
Media_Carga = Valor_Total_Carga / 30
print(Media_Carga)
Lucro_media_carga = Media_Carga * 0.30
print(Lucro_media_carga)







carga_rota = df[['Title','Valor_Carga']].groupby('Title').sum()
print(carga_rota)  #cargaPorId
df_ranking = df.sort_values(by='Valor_Carga', ascending=False)
print(df_ranking) #ranlingPorValor




Destino_Valor = df[['Destino','Valor_Carga']].groupby('Destino').sum()
print(Destino_Valor) #valorda carga por destino
plt.figure(figsize=(16, 10))
plt.pie(Destino_Valor['Valor_Carga'], labels=Destino_Valor.index, autopct='%1.1f%%', startangle=140)
plt.title(' Carga por Destino')
plt.axis('equal')  # Para garantir que o gráfico de pizza seja um círculo
plt.show()





Status_valor = df[['Status','Valor_Carga']].groupby('Status').sum()
print(Status_valor) #valor da carga por status
cor = ['red','blue','green']
plt.bar(Status_valor.index, Status_valor['Valor_Carga'],color = cor)
plt.xlabel('Status')
plt.ylabel('Valor_Final')
plt.title('Faturamento por Status')
plt.show()




Valor_Data= df[['Cadastro','Valor_Carga']].groupby('Cadastro').sum()
Valor_Data = Valor_Data.reset_index()
print(Valor_Data) #valor carga por dia
media_valor_carga = Valor_Data['Valor_Carga'].mean()
print(media_valor_carga)
plt.figure(figsize=(10, 5))
plt.plot(Valor_Data['Cadastro'], Valor_Data['Valor_Carga'], marker='o', linestyle='-', color='blue')
plt.xlabel('Data')
plt.ylabel('Valor da Carga')
plt.title('Valor da Carga por Data')
plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.grid(axis='y')  # Adiciona uma grade ao gráfico
plt.tight_layout()  # Ajusta o layout para não cortar rótulos
plt.show()














