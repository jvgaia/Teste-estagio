import json

# Carregando os dados de faturamento diário a partir de um arquivo JSON
with open('faturamento.json') as f:
    faturamento_diario = json.load(f)

# Calculando o menor e o maior valor de faturamento diário
menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

# Calculando a média mensal de faturamento diário (ignorando os dias sem faturamento)
dias_com_faturamento = [valor for valor in faturamento_diario if valor > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Calculando o número de dias em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = sum([1 for valor in faturamento_diario if valor > media_mensal])

# Exibindo os resultados
print(f"Menor valor de faturamento diário: R${menor_valor:.2f}")
print(f"Maior valor de faturamento diário: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
