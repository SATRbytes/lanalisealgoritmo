import matplotlib.pyplot as plt
import networkx as nx

from casas import casas, team_black, team_green, trono_de_ferro

G = nx.Graph()
G.add_nodes_from(casas)

arestas = [
    ("Casa Stark", "Casa Tully"),
    ("Casa Greyjoy", "Casa Lannister"),
    ("Casa Lannister", "Casa Tully"),
    ("Casa Tully", "Casa Tyrell"),
    ("Casa Tyrell", "Casa Hightower"),
    ("Casa Tyrell", "Casa Lannister"),
    ("Casa Tyrell", "Porto Real"),
    ("Casa Lannister", "Casa Tully"),
    ("Casa Tully", "Casa Strong"),
    ("Casa Strong", "Casa Arryn"),
    ("Casa Arryn", "Casa Tully"),
    ("Casa Tully", "Porto Real"),
    ("Porto Real", "Casa Targaryen"),
    ("Casa Targaryen", "Casa Baratheon"),
    ("Casa Targaryen", "Casa Tully"),
    ("Casa Baratheon", "Casa Velaryon"),
    ("Casa Tully", "Casa Baratheon"),
    ("Porto Real", "Casa Baratheon"),
]

G.add_edges_from(arestas)

def bfs_caminho(graph, start, goal):
    if start == goal:
        raise ValueError("A casa inicial e a casa final não podem ser a mesma.")

    jafoiexpl = []
    queue = [[start]]

    while queue:
        caminho = queue.pop(0)
        node = caminho[-1]

        if node not in jafoiexpl:
            vizinho = graph[node]

            for vizinho in vizinho:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                queue.append(novo_caminho)

                if vizinho == goal:
                    return novo_caminho

            jafoiexpl.append(node)

    return None

def desenhar_grafo(path):
    pos = {
        "Casa Stark": (0, 3),
        "Casa Arryn": (1, 2),
        "Casa Greyjoy": (-2, 2),
        "Casa Tully": (0, 1),
        "Casa Velaryon": (3, -1),
        "Casa Baratheon": (2, -1),
        "Casa Lannister": (-2, 0),
        "Casa Strong": (1, 1),
        "Casa Targaryen": (2, 0),
        "Porto Real": (1, -1),
        "Casa Tyrell": (-1, 0),
        "Casa Hightower": (-1, -2)
    }

    plt.figure(figsize=(12, 8))

    node_colors = []
    for node in G.nodes():
        if node in team_black:
            node_colors.append('red')
        elif node in team_green:
            node_colors.append('green')
        elif node in trono_de_ferro:
            node_colors.append('gold')
        else:
            node_colors.append('grey')

    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=2000, font_size=10, font_weight='bold', arrows=False)

    if path:
        edges_in_path = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='green', width=2)

    plt.title("ROTAS DE REGIÕES DOMINADAS PELAS FAMILIAS MAIS IMPORTANTES")
    plt.show()
