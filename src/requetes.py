import json
import os
import networkx as nx
import itertools
import re
import matplotlib.pyplot as plt
import time
import cProfile
from collections import deque

# Q1
def json_vers_nx(file_path2, affiche=False):
    print('file', file_path2)
    file_path = file_path2.strip("{").strip("}")

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
        print("nsdfjd")
        return G

# affichage du graphe :
def affichage_graph(graph_films):
    # pos = nx.spring_layout(graph_films)
    # fig = plt.figure()
    # nx.draw(graph_films, pos, with_labels=True)
    # fig.savefig("G12.png")
    # plt.show()
    nx.draw(graph_films, with_labels=True)
    # nx.draw(graph_films)
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


# Q2
def collaborateurs_communs(G, u, v):
    if u not in G or v not in G:
        return None

    voisins_u = set(G.neighbors(u))
    voisins_v = set(G.neighbors(v))
    return voisins_u.intersection(voisins_v)


# Q3
def collaborateurs_proches(G,u,k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    # print(collaborateurs)
    for i in range(k):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs


def est_proche(G,u,v,k=1):
    if u not in G or v not in G or k<=-1:
        return None
    return v in collaborateurs_proches(G,u,k) 

def distance_naive(G, u, v):
    if u not in G.nodes or v not in G.nodes:
        return -1
    distance = 0
    
    while distance <100:
        if est_proche(G, u, v, k=distance):
            return distance
        distance += 1
    return -1

def distance(G, u, v):
    try:
        return nx.shortest_path_length(G,u, v)
    except: 
        return -1



# Q4
def centralite(G,u):
    def val(elem):
        return len(elem[1])
    truc = max(nx.single_source_dijkstra_path(G,u).items(), key=val)
    print(truc)
    return truc[1][0],truc[1][-1],len(truc[1])-1
    # return V max, u, len btw u => v


def centre_hollywood(G):
    
    # ch = nx.single_source_dijkstra_path(G,centralite(G, centralite(G, list(G.nodes)[0])[0])[0])
    def val(elem):
        return len(elem[1])
    ch = max(nx.single_source_dijkstra_path(G,centralite(G, list(G.nodes)[0])[0]).items(), key=val)

    print("ch>>>>>",ch)
    return ch[1][len(ch[1]) // 2] # -> centraliter(centraliter()) 

Gr = json_vers_nx("data/data.txt")
print(centre_hollywood(Gr))

# Q5
def eloignement_max(G):
    return centralite(G, centralite(G, list(G.nodes)[0])[0])

# BONUS
def centralite_groupe(G,S):
    if S not in G:
        return None
    return max([centralite(G,u) for u in S])


# BONUS collab proche to graph
def collaborateurs_proches_Graph(G,u,k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    Graph = nx.Graph()

    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    
    Graph.add_node(u)
    visiter= set()
    for i in range(k):
        for node in Graph.copy():
            if node not in visiter:
                visiter.add(node)
                Graph.add_edges_from([(node,x) for x in G.adj[node]])
    return Graph

