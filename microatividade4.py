import pandas as pd

# Configura a propriedade max_rows para 9999
pd.set_option('display.max_rows', 9999)

# Variável para armazenar os dados
dados = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')

# Subconjunto de dados com apenas três colunas
subconjunto_dados = dados[['ID', 'Date', 'Calories']]

# Salva as alterações no arquivo CSV
dados.to_csv('dados_gerados_microatividade4.csv', index=False)

# Exibe os dados da variável usando o método to_string()
print("\nDados original utilizando to_string():")
print(dados.to_string())

# Exibe as primeiras 10 linhas do conjunto de dados original
print("\nPrimeiras 10 linhas do conjunto de dados original:")
print(dados.head(10))

# Exibe as últimas 10 linhas do conjunto de dados original
print("\nÚltimas 10 linhas do conjunto de dados original:")
print(dados.tail(10))
