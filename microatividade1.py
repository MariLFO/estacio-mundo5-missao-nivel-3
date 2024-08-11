import pandas as pd

# Variável para armazenar os dados
dados = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')

# Salva as alterações no arquivo CSV
dados.to_csv('dados_gerados_microatividade1.csv', index=False)

# Exibe os dados da variável
print(dados)
