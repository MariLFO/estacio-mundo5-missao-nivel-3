import pandas as pd

# Variável para armazenar os dados
dados = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')

# Nova variável contendo subconjunto de dados com apenas três colunas
subconjunto_dados = dados[['ID', 'Date', 'Calories']]

# Salva as alterações em um novo arquivo CSV
subconjunto_dados.to_csv('dados_gerados_microatividade2.csv', index=False)

# Exibe os dados da nova variável
print(subconjunto_dados)
