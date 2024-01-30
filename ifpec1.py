import pandas as pd

arquivo= 'Pagamentos Em aberto.xlsx'
data= pd.read_excel(arquivo, 'Plan1')
data['Pag']= data['Pag'].fillna(0)
data['Ano']= data['Data'].dt.year
data['Mes']= data['Data'].dt.month
data0= data[data['Ano']<= 2023]
data1= data0[data0['Mes']<= 8]
data2 =data1.sort_values('Mes', ascending= True)
devendo= []
for indice, linha in data2.iterrows():
    devendo.append('Pag em Aberto' if linha['Pag'] == 0 else 'Pag Efetuado')
data2['Situação'] = devendo

#data3 = data2[data2['Situação'] == 'Pag em Aberto']
#data4= data2[data2['Situação']== 'Pag Efetuado']
df= data2.groupby(['Nomes','Situação'])['Mes'].value_counts()
df2= df.drop_duplicates()
df2.to_excel('Planilha Atualizada3.xlsx')