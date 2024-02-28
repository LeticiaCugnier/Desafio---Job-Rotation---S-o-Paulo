import json  # Importação do módulo json para trabalhar com arquivos JSON

# Abrir o arquivo JSON e carregar os dados
with open('faturamento_diario.json') as file:
    data = json.load(file)  # Carrega os dados do arquivo JSON para a variável 'data'

# Inicializar uma lista para armazenar os valores de faturamento diário
faturamento_diario = []

# Iterar sobre os dados do arquivo JSON e extrair os valores de faturamento diário
for entry in data['faturamento_mensal']:
    if entry['dia_util']:  # Verifica se o dia é útil
        faturamento_diario.append(entry['faturamento'])  # Adiciona o valor de faturamento à lista

# Calcular o menor valor de faturamento diário
menor = min(faturamento_diario)

# Calcular o maior valor de faturamento diário
maior = max(faturamento_diario)

# Calcular a média de faturamento diário
media = sum(faturamento_diario) / len(faturamento_diario)

# Contar os dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media)

# Exibir os resultados
print("Menor valor de faturamento diário:", menor)  # Imprime o menor valor de faturamento diário
print("Maior valor de faturamento diário:", maior)  # Imprime o maior valor de faturamento diário
print("Número de dias com faturamento acima da média:", dias_acima_da_media)  # Imprime o número de dias com faturamento acima da média
