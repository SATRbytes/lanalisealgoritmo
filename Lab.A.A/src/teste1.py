import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Dança dos dragões, análise de afiliações/aliados, inimigos, traições entre núcleos familiares??
# Entrada = família 1 e família 2 e pela percepção da família 1 a relação era qual, pela família 2 era qual? Atualmente é um grafo simétrico
# Se a relação for aliados é verde. Se for inimigos é vermelho. Traições é preto.
# É uma rede simétrica, mas o plano é deixar as arestas com cores diferentes.


#fazer tratamento de exceções, análise de fluxo, implementar dicionário com familias importantes pra seleção. pensar numa GUI.

G_Fb = nx.Graph()

while True:
    adtn = int(input("[1] Adicionar Conexão \n[2] Sair\n"))
    if adtn == 1:
        choice2 = int(input(" Familia 1: \n[1] Targaryen\n[2] Hightower\n[3] Outro (digitar)\n"))
        if choice2 == 1:
            familia_1 = "Targaryen"
        elif choice2 == 2:
            familia_1 = "Hightower"
        elif choice2 == 3:
            familia_1 = input("Digite a primeira família\n").lower().capitalize().strip()
        else:
            pass
        
        choice3 = int(input(" Familia 2: \n[1] Targaryen\n[2] Hightower\n[3] Outro (digitar)\n"))
        if choice3 == 1:
            familia_2 = "Targaryen"
        elif choice3 == 2:
            familia_2 = "Hightower"
        elif choice3 == 3:
            familia_2 = input("Digite a segunda família\n").lower().capitalize().strip()
        else:
            pass
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        relacao = int(input("Digite o que a primeira família acha da segunda:\n[1] ALIADOS \n[2] INIMIGOS \n[3] NEUTROS\n"))
        G_Fb.add_node(familia_1)
        G_Fb.add_node(familia_2)
        if relacao == 2:
            G_Fb.add_edge(familia_1, familia_2, color="red", weight=2)
        elif relacao == 1:
            G_Fb.add_edge(familia_1, familia_2, color="green", weight=2)
        elif relacao == 3:
            G_Fb.add_edge(familia_1, familia_2, color="gray", weight=2)
        else:
            print("Valor inválido, por favor insira um valor validoooo.")
    elif adtn == 2:
        break
    else:
        print("Valor inválido, por favor insira um valor validoooo.")
        pass

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
plt.figure(figsize=(12, 9))
plt.axis("off")
np.random.seed(0)
position = nx.spring_layout(G_Fb)
edges = G_Fb.edges()
colors = [G_Fb[u][v]['color'] for u, v in edges]

node_colors = []
for node in G_Fb.nodes():
    if node == "Hightower":
        node_colors.append('green')
    elif node == "Targaryen":
        node_colors.append('black')
    else:
        node_colors.append('blue')

nx.draw_networkx(G_Fb, pos=position, node_color=node_colors, font_size=18, edge_color=colors)
plt.show()
