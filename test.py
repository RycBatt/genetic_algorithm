import numpy as np
import matplotlib.pyplot as plt

# Dados das variáveis e resultados
variavel1 = [1, 2, 3, 4, 5]
variavel2 = [2, 4, 6, 8, 10]
resultado = [7, 4, 3, 20, 6]

# Criando uma matriz de valores
valores = np.zeros((len(variavel1), len(variavel2)))
for i in range(len(variavel1)):
    for j in range(len(variavel2)):
        valores[i][j] = resultado[i]

# Plotando o mapa de calor
fig, ax = plt.subplots()
heatmap = ax.imshow(valores, cmap='hot')

# Configurando os eixos
ax.set_xticks(np.arange(len(variavel2)))
ax.set_yticks(np.arange(len(variavel1)))
ax.set_xticklabels(variavel2)
ax.set_yticklabels(variavel1)

# Adicionando os valores nas células
for i in range(len(variavel1)):
    for j in range(len(variavel2)):
        text = ax.text(j, i, valores[i][j], ha='center', va='center', color='b')

# Configurando a barra de cores
cbar = ax.figure.colorbar(heatmap)

plt.show()