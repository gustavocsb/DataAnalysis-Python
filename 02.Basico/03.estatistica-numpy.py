import numpy as np

arr1 = np.array([14,23,64,59,78])
print(f'Array: {arr1}')


# Média
'''
Em estatística, a média é uma medida de tendência central que representa o valor central de um conjunto de dados. É calculada somando-se todos os valores do conjunto
de dados e dividindo-se pelo número de elementos. A média é uma medida de tendência central que é afetada por valores extremos, ou seja, valores muito altos ou muito
baixos podem distorcer o valor da média. 
'''
print(f'Média: {np.mean(arr1)}')


# Desvio Padrão
'''
O desvio padrão é uma medida de dispersão que indica o quanto os valores de um conjunto de dados se afastam da média. Ele é calculado como a RAIZ QUADRADA da VARIÂNCIA,
que é a média dos quadrados das diferenças entre cada valor e a média.

Ele é útil porque permite avaliar a variabilidade dos dados em torno da média. Se os valores estiverem próximo da média, o desvio padrão será baixo, indicando que os
dados têm pouca variabilidade. Se os valores estiverem muito distantes da média, o desvio padrão será alto, indicando que os dados têm muita variabilidade.

A fórmula do desvio padrão é dada por: √Σ(xi - μ)² / n, onde xi é o valor de cada elemento, μ é a média dos valores e n é o número de elementos.

IMPORTANTE: Nota-se que o desvio padrão pode ser influenciado por valores extremos (outliers) e pode ser afetado por diferentes distribuições de dados.
'''
print(f'Desvio Padrão: {np.std(arr1)}')

# Variância
'''
A variância é uma medida que quantifica a dispersão dos valores em um conjunto de dados em relação à média. Ela é calculada como a média dos quadrados das diferenças
entre cada valor e a média.

A fórmula da variância é dada por: Σ(xi - μ)² / n, onde xi é o valor de cada elemento, μ é a média dos valores e n é o número de elementos.

IMPORTANTE: Nota-se que a variância pode ser influenciada por valores extremos (outliers) e pode ser afetada por diferentes distribuições de dados.
'''
print(f'Variância: {np.var(arr1)}\n')