import json
import networkx as nx
import itertools
import re
import matplotlib.pyplot as plt


def json_vers_nx(file_path, affiche=False):
    """cree un graph avce netWorkX par rapport au donnée du fichier qu'on lui entre et l'affiche (ou pas)

    Args:
        file_path (str): nom d'un fichier .txt contenant les données des films
        affiche (bool): booleen pour savoir si on veut affiché le graph ou pas

    Returns:
        _type_: _description_
    """
    G = nx.Graph()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            film = json.loads(line)
            cast = [actor.strip("[[").strip("]]") for actor in film["cast"]]
            for i, actor1 in enumerate(cast):
                for actor2 in cast[i+1:]:
                    G.add_edge(actor1, actor2, film=film["title"])
    if affiche:
        affichage_graph(G)
    return G

line = ["[[MON GROS CUL ca mere]]","[[Julian Marques]]"]

# affichage du graphe :
def affichage_graph(graph_films):
    """affiche le graph qu'on lui rentre en parametre grace a plotlib

    Args:
        graph_films (nx.Graph): le graphique à afficher
    """
    pos = nx.spring_layout(graph_films)
    fig = plt.figure()
    nx.draw(graph_films, pos, with_labels=True, node_size=30)
    fig.savefig("G12.png")
    plt.show()

    # affichage du graphe :



def collaborateurs_communs(G, u, v):
    """retourn l'ensemble des acteurs en commun entre acteur u et l'acteur v 

    Args:
        G (nx.Graph): graph
        u (str): nom d'acteur
        v (str): nom d'acteur

    Returns:
        set :ensemble d'acteurs 
    """
    voisins_u = set(G.neighbors(u))
    voisins_v = set(G.neighbors(v))
    return voisins_u.intersection(voisins_v)


def collaborateurs_proches(G,u,k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Args:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    Returns:
        set : ensemble d'acteurs 
    """
    if u not in G.nodes:
        print(u,"n'est pas connu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    # print(collaborateurs)
    for _ in range(k):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs


def est_proche(G,u,v,k=1):
    """ renvoie True si u est proche de v False sinon  

    Args:
        G: le graphe
        u: le sommet de départ de l'acteur
        u: le sommet du deuxieme acteur
        k: la distance depuis u
    Returns:
        bool :booleen
    """
    return v in collaborateurs_proches(G,u,k) 


def distance_naive(G, u, v):
    """ renvoie une distance entre u et v ou -1 s'ils ne sont pas lié 

    Args:
        G: le graphe
        u: le sommet de départ de l'acteur
    Returns:
        int : la distance depuis u vers v ou -1
    """
    if u not in G.nodes or v not in G.nodes:
        return -1
    distance = 0
    
    while distance <100:
        if est_proche(G, u, v, k=distance):
            return distance
        distance += 1
    return -1


# Cette fonction distance utilise BFS pour trouver la distance entre deux acteurs u et v dans un graphe G. Sa complexité est O(V + E), ce qui est plus efficace que l'approche naïve.
def distance(G, u, v):
    """ renvoie une distance entre u et v ou -1 s'ils ne sont pas lié 

    Args:
        G: le graphe
        u: le sommet de départ de l'acteur
    Returns:
        int : la distance depuis u vers v ou -1
    """
    if u == v:
        return 0
    visited = set()
    queue = [(u, 0)]

    while queue:
        node, dist = queue.pop(0)
        if node == v:
            return dist
        visited.add(node)
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                queue.append((neighbor, dist + 1))

    return -1 

# def centralite(G,u):
#     shortest_paths = nx.shortest_path_length(G, source=u)
#     centralite_u = max(shortest_paths.values())
#     return centralite_u

def centralite(G, u):
    """ renvoie une distance entre u et le bord du graph

    Args:
        G: le graphe
        u: le sommet de départ de l'acteur
    Returns:
        int : la centralité depuis u vers v
    """
    shortest_paths = nx.single_source_dijkstra_path_length(G, u)
    centralite_u = max(shortest_paths.values())
    return centralite_u
    # or
    # return max(nx.single_source_dijkstra_path_length(G, u).values())


def centre_hollywood(G):
    centralites = {acteur: centralite(G, acteur) for acteur in G.nodes()}
    acteur_central = min(centralites, key=centralites.get)
    return acteur_central, centralites[acteur_central]



def lesprints():
    # fichier = 'dataTests.txt'

    # fichier = 'datatest.txt'
    fichier = 'data.txt'
    # fichier = 'test.txt'
    graph_films = json_vers_nx(fichier, True)
# print(graph_films)
# Afficher quelques informations sur le graphe
# print("Nombre de nœuds (personnes) :", graph_films.number_of_nodes())
# print("Nombre d'arêtes (relations) :", graph_films.number_of_edges())
    # affichage_graph(graph_films)
    print(graph_films)
    print("colab: ", collaborateurs_communs(graph_films, "Paul Reubens", "Julian Marques"))  # Output: {'Carol Kane'}
    print("colab proche: ", collaborateurs_proches(graph_films,"Julian Marques",1))
    print("colab proche: ", collaborateurs_proches(graph_films,"Julian Marques",2))
    print("EST proche: ", est_proche(graph_films,"Julian Marques", "Anthony Michael Hall",1) )
    print("EST proche: ", est_proche(graph_films,"Julian Marques", "Carol Kane",1))
    print("distance_naive:", distance_naive(graph_films,"Julian Marques","Carol Kane") )
    print("distance_naive:", distance_naive(graph_films,"Julian Marques","Julian Marques") )
    print("distance_naive:", distance_naive(graph_films,"Julian Marques","Anthony Michael Hall") )
    print("distance_naive:", distance_naive(graph_films,"Julian Marques","Goldie Hawn") )
    print("distance:", distance(graph_films,"Julian Marques","Carol Kane") )
    print("distance:", distance(graph_films,"Julian Marques","Julian Marques") )
    print("distance:", distance(graph_films,"Julian Marques","Anthony Michael Hall") )
    print("distance:", distance(graph_films,"Julian Marques","Goldie Hawn") )
    print("centralite:", centralite(graph_films,"Julian Marques") ) # 3
    print("centralite:", centralite(graph_films,"Goldie Hawn") ) # 3
    print("centralite:", centralite(graph_films,"Carol Kane") ) # 2
    # # #Gcentre= graph_films
    print("centre_hollywood:", centre_hollywood(graph_films) ) 

    # print("eloignement_max:", eloignement_max(graph_films) )

lesprints()