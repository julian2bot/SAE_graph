import json
import os

import networkx as nx

import matplotlib.pyplot as plt


def json_vers_nx(file_path, affiche=False):

    G = nx.Graph()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if not line:
                    continue
                film = json.loads(line)
                cast = [actor.strip("[[").strip("]]") for actor in film["cast"]]
                for i, actor1 in enumerate(cast):
                    for actor2 in cast[i+1:]:
                        G.add_edge(actor1, actor2, film=film["title"])
        if affiche :
            affichage_graph(G)
        return G
    except:

        return G

# affichage du graphe :
def affichage_graph(graph_films):
    pos = nx.spring_layout(graph_films)
    fig = plt.figure()
    nx.draw(graph_films, pos, with_labels=True)
    fig.savefig("G12.png")
    plt.show()


def save_graph(graph_films):
    """Affiche le graphique passé en paramètre grâce à matplotlib et le sauvegarde sous forme d'image.

    Args:
        graph_films (nx.Graph): Le graphique à afficher
    Returns:
        str: Le chemin absolu de l'image enregistrée
    """
    nameimg = "graph.png"
    pos = nx.spring_layout(graph_films)
    fig = plt.figure()
    nx.draw(graph_films, pos, with_labels=True, node_size=30,font_size=8, font_color='black' )
    fig.savefig(nameimg)
    # Renvoyer le chemin absolu de l'image enregistrée
    print(nameimg)
    print("img!!!!!",os.path.abspath(nameimg))
    return str(os.path.abspath(nameimg))




























