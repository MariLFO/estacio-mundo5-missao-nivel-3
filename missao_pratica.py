import pandas as pd
import numpy as np

# Variável para armazenar os dados
dados = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')

# Verificação dos dados
print("Informações gerais sobre o conjunto de dados:")
print(dados.info())

# Exibe as N primeiras e as N últimas linhas do arquivo
N = 5
print("\nPrimeiras 5 linhas do arquivo:")
print(dados.head(N))
print("\nÚltimas 5 linhas do arquivo:")
print(dados.tail(N))

# Cópia do conjunto de dados original
dados_copia = dados.copy()

# Substituição de todos os valores nulos da coluna ‘Calories’ por 0
dados_copia['Calories'].fillna(0, inplace=True)
print("\nConjunto de dados após substituir valores nulos em 'Calories' por 0:")
print(dados_copia)

# Substituição de todos os valores nulos da coluna ‘Date’ por ‘1900/01/01’
dados_copia['Date'].fillna('1900/01/01', inplace=True)
print("\nConjunto de dados após substituir valores nulos em 'Date' por '1900/01/01':")
print(dados_copia)

# Transformação de todos os dados da coluna ‘Date’ em datetime usando o método ‘to_datetime’
try:
    dados_copia['Date'] = pd.to_datetime(dados_copia['Date'], format='%Y/%m/%d')
except ValueError as e:
    print(f"Erro ao converter 'Date': {e}")

# Substituição, na coluna ‘Date’, valor ‘1900/01/01’ por ‘NaN’
dados_copia['Date'].replace('1900/01/01', np.nan, inplace=True)

# Repitindo a transformação dos dados da coluna ‘Date’ para datetime
dados_copia['Date'] = pd.to_datetime(dados_copia['Date'], format='%Y/%m/%d', errors='coerce')
print("\nConjunto de dados após transformar 'Date' para datetime:")
print(dados_copia)

# Transformar especificamente o valor "20201226" para o formato datetime
dados_copia['Date'] = dados_copia['Date'].replace('20201226', '2020/12/26')

# Repitindo novamente a transformação dos dados da coluna ‘Date’ para datetime
dados_copia['Date'] = pd.to_datetime(dados_copia['Date'], format='%Y/%m/%d', errors='coerce')
print("\nConjunto de dados após corrigir o valor '20201226' e transformar 'Date' para datetime:")
print(dados_copia)

# Remoção de todos os registros contendo valores nulos
dados_copia.dropna(subset=['Date'], inplace=True)
print("\nConjunto de dados após remover registros com valores nulos em 'Date':")
print(dados_copia)
