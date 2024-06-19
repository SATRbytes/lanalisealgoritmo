import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from casas import  team_black, team_green, trono_de_ferro,neutros

casas_disponiveis = team_black + team_green + trono_de_ferro + neutros

G_Fb = nx.Graph()

def adicionar_conexao(familia_1, familia_2, relacao):
    if G_Fb.has_edge(familia_1, familia_2):
        return False
    G_Fb.add_node(familia_1)
    G_Fb.add_node(familia_2)
    if relacao == "INIMIGOS":
        G_Fb.add_edge(familia_1, familia_2, color="red", weight=2)
    elif relacao == "ALIADOS":
        G_Fb.add_edge(familia_1, familia_2, color="green", weight=2)
    elif relacao == "NEUTROS":
        G_Fb.add_edge(familia_1, familia_2, color="gray", weight=2)
    return True

def desenhar_grafo():
    plt.figure(figsize=(12, 9))
    plt.axis("off")
    np.random.seed(0)
    position = nx.spring_layout(G_Fb)
    edges = G_Fb.edges()
    colors = [G_Fb[u][v]['color'] for u, v in edges]

    node_colors = []
    for node in G_Fb.nodes():
        if node in team_black:
            node_colors.append('red')
        elif node in team_green:
            node_colors.append('green')
        elif node in trono_de_ferro:
            node_colors.append('gold')
        elif node in neutros:
            node_colors.append('blue')

    nx.draw_networkx(G_Fb, pos=position, node_color=node_colors, font_size=18, edge_color=colors)
    plt.show()
