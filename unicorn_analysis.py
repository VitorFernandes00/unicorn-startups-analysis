#importar as libs
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

#Ler os dados
Base_Dados = pd.read_csv('Startups+in+2021+end.csv')

#Verificar Dimensão
Base_Dados.shape

#Visualizando Primeiros Registros
Base_Dados.head()

#Visualizando Colunas
Base_Dados.columns

#Renomeando Colunas
Base_Dados.rename(columns={
    'Unnamed: 0': 'Id',
    'Company':'Empresa',
    'Valuation ($B)':'Valor',
    'Date Joined': 'Data de Adesão',
    'Country':'País',
    'City':'Cidade',
    'Industry':'Setor',
    'Select Investors':'Investidores',
}, inplace=True )

#Verificar Tipo de Informação
Base_Dados.info()

#Campos Nulos
Base_Dados.isnull().sum()

#Visão Grafica
plt.figure( figsize=(15,6))
plt.title ('Analisando Campos Nulos')
sns.heatmap(Base_Dados.isnull(), cbar=False);

#Visualizando Campos Unicos
Base_Dados.nunique()

#Visualizando Valores unicos
Base_Dados['Setor'].unique()

#Valores Unicos em Ranking
Base_Dados['Setor'].value_counts()

#Valores Unicos em Ranking Porcentagem
Base_Dados['Setor'].value_counts(normalize=True)

plt.figure(figsize=(15,6))
plt.title('Analise de Setores')
plt.bar( Base_Dados['Setor'].value_counts().index, Base_Dados['Setor'].value_counts())
plt.xticks( rotation=45, ha='right');

Base_Dados['País'].value_counts()

Analise = round(Base_Dados['País'].value_counts(normalize=True)*100,1)

#Grafico Pizza Países Top 5
plt.figure(figsize=(15,6))
plt.title('Analise dos países gerador de unicornios')
plt.pie(
    Analise.head(5),
    labels= Analise.index[0:5],
    shadow=True,
    startangle=90,
    autopct='%1.1f%%');


#Convertendo para o tipo data
Base_Dados['Data de Adesão'] = pd.to_datetime(Base_Dados['Data de Adesão'])
Base_Dados['Data de Adesão'].head()

#Extrair Ano e Mês
Base_Dados['Mes'] = pd.DatetimeIndex(Base_Dados['Data de Adesão']).month
Base_Dados['Ano'] = pd.DatetimeIndex(Base_Dados['Data de Adesão']).year
Base_Dados.head()

Analise_Agrupada = Base_Dados.groupby( by=['País', 'Ano', 'Mes', 'Empresa'] ).count()['Id'].reset_index()

Analise_Agrupada.loc[
    Analise_Agrupada['País'] == 'Brazil'
]

#Transformando a coluna valor
Base_Dados['Valor'] = pd.to_numeric(Base_Dados['Valor'].apply(lambda Linha: Linha.replace('$', '')))

#Tabela Analitica
Analise_Pais = Base_Dados.groupby(by='País', as_index=False)['Valor'].sum()


Analise_Valor = Analise_Pais.sort_values('Valor', ascending=False)
Analise_Valor.head()

#Grafico de Valores
plt.figure( figsize=(15,6) )
plt.title('Analise dos maiores valores de unicornios')
plt.plot ( Analise_Valor['País'], Analise_Valor['Valor'] )
plt.xticks( rotation=45, ha= 'right');
plt.show()
