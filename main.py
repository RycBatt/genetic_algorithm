from ga import GeneticAlgorithm as GA
from agents import Agent
import numpy
from matplotlib import pyplot as plt


alfabeto = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"
in_str = None
in_str_len = None
populacao = 50
geracoes = 1000



## Plotagem
def bar_plot(ax, data, colors=None, total_width=0.8, single_width=1, legend=True):
    if colors is None:
        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    n_bars = len(data)
    bar_width = total_width / n_bars
    bars = []
    for i, (name, values) in enumerate(data.items()):
        x_offset = (i - n_bars / 2) * bar_width + bar_width / 2
        for x, y in enumerate(values):
            bar = ax.bar(x + x_offset, y, width=bar_width * single_width, color=colors[i % len(colors)])
        bars.append(bar[0])
    if legend:
        ax.legend(bars, data.keys())


## Principal

if __name__ == '__main__':
    
    frases = {
      "AI is changing the game",
      "Smart machines shape AI",
      "AI leads the way forward",
      "Data empowers AI systems",
      "Machine learning drives AI",
      "AI unlocks new potential",
      "AI transforms industries",
      "Ethics guide responsible AI",
      "AI fuels technological progress",
      "AI revolutionizes our world",
    }

    final = {
        "E1" : numpy.zeros(10),
        "E2" : numpy.zeros(10),
    }
    phase_result = []
    index = 0
    for frase in frases:
      in_str = frase
      in_str_len = len(in_str)
      results = {
        "E1" : numpy.zeros(10),
        "E2" : numpy.zeros(10),
      }
      print(frase)


      results_lst = []
      mutation_max = 1.0
      selection_max = 1.0
      split_max = in_str_len

      mutation_lst = []
      selection_lst = []  
      for mutation in numpy.arange(0.1, mutation_max, (mutation_max-0.1)/10):
        mutation_lst.append(mutation)
        for selection in numpy.arange(0.1, selection_max, (selection_max-0.1)/10):
            print("Taxa de mutação: " + str(mutation) + " e taxa de seleçao " + str(selection))
            selection_lst.append(selection)
            ga1 = GA(alfabeto, populacao, geracoes, frase, mutation, selection)
            results_lst.append(numpy.mean(ga1.execute()))
            phase_result.append([mutation_lst, selection_lst, results_lst])

    for i in range(len(frases)):
      
      # Dados das variáveis e resultados
      variavel1 = phase_result[i][0]
      variavel2 = phase_result[i][1]
      resultado = phase_result[i][2]

      # Criando uma matriz de valores
      valores = numpy.zeros((len(variavel1), len(variavel2)))
      for i in range(len(variavel1)):
          for j in range(len(variavel2)):
              valores[i][j] = resultado[i]

    # Plotando o mapa de calor
    fig, ax = plt.subplots()
    heatmap = ax.imshow(valores, cmap='hot')

    # Configurando os eixos
    ax.set_xticks(numpy.arange(len(variavel2)))
    ax.set_yticks(numpy.arange(len(variavel1)))
    ax.set_xticklabels(variavel2)
    ax.set_yticklabels(variavel1)

    # Adicionando os valores nas células
    for i in range(len(variavel1)):
        for j in range(len(variavel2)):
            text = ax.text(j, i, valores[i][j], ha='center', va='center', color='b')

    # Configurando a barra de cores
    cbar = ax.figure.colorbar(heatmap)

    plt.show()

    fig, ax = plt.subplots()
    bar_plot(ax, results, total_width=.8, single_width=.9)
    plt.show()
    
    final["E1"][index] = numpy.mean(results["E1"])
    index = index + 1
