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
    """Transforme un fichier en graphe

    Parametres:
        file_path2 (str): chemin vers le document à transformer en graphe
        affiche (bool, optionel): Demande si il faut affiche le graphe False par défaut.

    Resultat:
        nx.Graph: le graphe obtenu
    """
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
        return G


# affichage du graphe :
def affichage_graph(graph_films, label = False):
    """Affiche le graphe avec ou sans les labels des sommets.

    Parametres:
        graph_films (nx.Graph): le graphe
        label (bool, optionel): Demande si il faut afficher les labels. False par defaut.
    """

    pos = nx.spring_layout(graph_films)
    fig = plt.figure()
    nx.draw(graph_films, pos, with_labels=True)
    # fig.savefig("G12.png")
    plt.show()
    # nx.draw(graph_films, with_labels=True)
    # nx.draw(graph_films)
    # plt.show()
    # nx.draw(graph_films, with_labels=label)
    # plt.show()

def save_graph(graph_films, cheminnameimg= None):
    """Affiche le graphique passé en paramètre grâce à matplotlib et le sauvegarde sous forme d'image.

    Parametres:
        graph_films (nx.Graph): Le graphique à afficher
        chemin_name_img (str):Le nom sous lequel sera enregistré le graphe. Par défaut, graph.png
    Resultat:
        str: Le chemin absolu de l'image enregistrée
    """
    if cheminnameimg is None:
        nameimg = "graph.png"
    else:
        nameimg = cheminnameimg
        
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
    """Fonction qui trouve tous les sommets possédants un chemin vers les sommets u et v

    Parametres:
        G (nx.Graph): le graphe
        u (Any): un premier sommet
        v (Any): un deuxième sommet

    Resultat:
        set: l'ensemble des sommets possédants un chemin entre les deux sommets
    """
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
    
    Resultat:
        set: l'ensemble des sommets se situants à une distance au plus k du sommet u    
    """

    collaborateurs = set()
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return collaborateurs
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
    """Vérifie si le sommet v se situe à une distance au plus k du sommet u

    Parametres:
        G (nx.Graph): le graphe
        u (Any): le premier sommet
        v (Any): le deuxieme sommet
        k (int, optional): _description_. Defaults to 1.

    Resultat:
        bool: _description_
    """
    # if u not in G or v not in G or k<=-1:
    #     return None
    return v in collaborateurs_proches(G,u,k) 

def distance_naive(G, u, v):
    """Fonction qui peut retourner la distance entre u et v

    Parametres:
        G (nx.Graph): le graphe
        u (Any): premier sommet
        v (Any): deuxieme sommet

    Resultat:
        int: distance potentiel entre les deux sommets. -1 si l'un des sommets ne fait pas parti du graphe ou queles sommets se situe à une distance supérieur à 100 ou que les sommets ne sont pas dans la meme composante connexe
    """    
    if u not in G.nodes or v not in G.nodes:
        return -1
    distance = 0
    
    while distance <100:
        if est_proche(G, u, v, k=distance):
            return distance
        distance += 1
    return -1

def distance(G, u, v):
    """Fonction qui retourne la distance la plus petite entre les sommets u et v

    Parametres:
        G (nx.Graph): le graphe
        u (Any): premier sommet
        v (Any): deuxième sommet

    Resultat:
        int: la distance entre u et v, -1 si il n'existe pas de chemin.
    """
    try:
        return nx.shortest_path_length(G,u, v)
    except: 
        return -1



# Q4

 

def centralite_bis(G,u):
    """Calcule la centralite du sommet u

    Parametres:
        G (nx.Graph): le  graphe
        u (Any): un sommet

    Resultat:
        int: la centralite du sommet u
    """    
    try: 
    
        def val(elem):
            return len(elem[1])
        truc = max(nx.single_source_dijkstra_path(G,u).items(), key=val)
        # print(truc)
        return truc[1][0],truc[1][-1],len(truc[1])-1
        # return V max, u, len btw u => v
    except:
        return None

def centralite(G,u):
    """Calcule la centralite du sommet u

    Parametres:
        G (nx.Graph): le  graphe
        u (Any): un sommet

    Resultat:
        int: la centralite du sommet u
    """ 
    return centralite_bis(G,u)[2]

def centre_hollywood(G):
    """Fonction qui trouve le centre du graphe

    Parametres:
        G (nx.Graph): le graphe

    Resultat:
        str : le sommet au centre du graphe
    """    
    # ch = nx.single_source_dijkstra_path(G,centralite(G, centralite(G, list(G.nodes)[0])[0])[0])
    def val(elem):
        return len(elem[1])
    ch = max(nx.single_source_dijkstra_path(G,centralite_bis(G, list(G.nodes)[0])[0]).items(), key=val)

    # print("ch>>>>>",ch)
    return ch[1][len(ch[1]) // 2] # -> centraliter(centraliter()) 

# Q5
def eloignement_max(G):
    """Fonction qui retourne la longueur de la chaine la plus longue du graphe

    Parametres:
        G (nx.Graph): le graphe

    Resultat:
        int: la longueur de la chaine la plus longue du graphe
    """
    return centralite_bis(G, centralite_bis(G, list(G.nodes)[0])[0])[2]

# BONUS
def centralite_groupe(G,S):
    """Fonction renvoyant le sommet au centre du groupe 

    Parametres:
        G (nx.Graph): le graphe
        S (set): ensemble de sommets

    Resultat:
        Any: le sommet au centre du groupe
    """
    # return max([centralite(G,u) for u in S]) # mais la version de dessous est mieux car si un acteur de S n'existe pas ca crash donc:
    return min([centralite_bis(G, u) for u in S if centralite_bis(G, u) is not None], default=None)[0]


# BONUS collab proche to graph
def collaborateurs_proches_Graph(G,u,k):
    """Fonction renvoyant un sous-graphe des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G(nx.Graph): le graphe
        u(Any): le sommet de départ
        k(int): la distance depuis u
    
    Resultat:
        nx.Graph: un sous graphe de G
    """
    Graph = nx.Graph()

    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return Graph
    
    Graph.add_node(u)
    visiter= set()
    for i in range(k):
        for node in Graph.copy():
            if node not in visiter:
                visiter.add(node)
                Graph.add_edges_from([(node,x) for x in G.adj[node]])
    print( Graph)
    return Graph
# list(map(lambda x : (1, x), ['he',"fe","dfsf"]))
#   
