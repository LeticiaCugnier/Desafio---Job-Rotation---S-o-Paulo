faturamento_mensal_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_mensal = sum(faturamento_mensal_por_estado.values())

percentuais = {estado: (faturamento / total_mensal) * 100 for estado, faturamento in faturamento_mensal_por_estado.items()}

for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')
