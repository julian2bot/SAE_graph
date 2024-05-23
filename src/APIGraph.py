import json
import os
import networkx as nx
import itertools
import re
import matplotlib.pyplot as plt
import time
import cProfile
from collections import deque



t_start = time.perf_counter()
   
# LE BON
def json_vers_nx(file_path2, affiche=False):
    # print("hfe")
    print('file', file_path2)
    file_path = file_path2.strip("{").strip("}")
    # for eleme in file_path:
    #     filepath = eleme
    #     break
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


def collaborateurs_communs(G, sommet, autre_sommet):
    if sommet not in G or autre_sommet not in G:
        return None

    voisins_u = set(G.neighbors(sommet))
    voisins_v = set(G.neighbors(autre_sommet))
    return voisins_u.intersection(voisins_v)


def collaborateurs_proches(G,sommet,distance):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur sommet dans le graphe G. La fonction renvoie None si sommet est absent du graphe.
    
    Parametres:
        G: le graphe
        sommet: le sommet de départ
        distance: la distance depuis sommet
    """
    if sommet not in G.nodes:
        print(sommet,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(sommet)
    # print(collaborateurs)
    for i in range(distance):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs


def est_proche(G,sommet,autre_sommet,distance=1):
    if sommet not in G or autre_sommet not in G or distance<=-1:
        return None
    return autre_sommet in collaborateurs_proches(G,sommet,distance) 


def distance_naive(G, sommet, autre_sommet):
    if sommet not in G.nodes or autre_sommet not in G.nodes:
        return -1
    distance = 0
    
    while distance <100:
        if est_proche(G, sommet, autre_sommet, k=distance):
            return distance
        distance += 1
    return -1


# Cette fonction distance utilise BFS pour trouver la distance entre deux acteurs sommet et autre_sommet dans un graphe G. Sa complexité est O(V + E), ce qui est plus efficace que l'approche naïve précédente.
def distance(G, sommet, autre_sommet):
    # retorune distance dsitra 
    try:
        return nx.shortest_path_length(G,sommet, autre_sommet) # a TEST oui => 0.10
    except: return -1

        # return nx.dijkstra_path_length(G,sommet, autre_sommet) # ok mais peut mieux faire
        # return nx.single_source_dijkstra_path_length(G,sommet, autre_sommet)# non 
        # return nx.floyd_warshall_numpy(G,sommet, autre_sommet) # mais non
        # return nx.algorithms.shortest_paths.astar(G,sommet, autre_sommet)# a TEST => 0.09 mais non
        # return nx.algorithms.shortest_paths.dense (G,sommet, autre_sommet)# a TEST => 1.32 mais non
        # return nx.algorithms.shortest_paths.generic (G,sommet, autre_sommet)# a TEST => 1.16 mais non
        # return nx.algorithms.shortest_paths.unweighted(G,sommet, autre_sommet)# a TEST => 1.26 mais non
        # return nx.algorithms.shortest_paths.unweighted(G,sommet, autre_sommet)# a TEST => 1.15 mais non
        # return nx.algorithms.shortest_paths.unweighted.single_source_shortest_path_length(G,sommet, autre_sommet)# a TEST => 0.09 mais non 

        # return int(nx.all_shortest_paths(G, source=u, target=v))

    # visited = set()
    # queue = [(u, 0)]
    # while queue:
    #     node, dist = queue.pop(0)
    #     if node == v:
    #         return dist
    #     visited.add(node)
    #     for neighbor in G.neighbors(node):
    #         if neighbor not in visited:
    #             queue.append((neighbor, dist + 1))
    # return -1 



def centralite(G, sommet):
    """ renvoie une distance entre sommet et le bord du graph

    Args:
        G: le graphe
        sommet: le sommet de départ de l'acteur
    Returns:
        int : la centralité depuis sommet vers v
    """
    if sommet not in G:
        return None
    shortest_paths = nx.single_source_dijkstra_path_length(G, sommet)
    centralite_u = max(shortest_paths.values())
    return centralite_u
    # or
    # return max(nx.single_source_dijkstra_path_length(G, u).values())



def bfs_max_distance(G, source):
    if source not in G:
        return None
    visited = set()
    queue = deque([(source, 0)])  # Queue pour BFS, avec la distance de départ 0
    max_distance = 0

    while queue:
        node, distance = queue.popleft()
        visited.add(node)
        max_distance = max(max_distance, distance)

        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))

    return max_distance

def eloignement_max(G):
    max_distance = 0
    for node in G.nodes():
        distance_from_node = bfs_max_distance(G, node)
        max_distance = max(max_distance, distance_from_node)
    
    return max_distance

# def parcours_largeur(graphe, depart):
#     if depart not in graphe:
#         return None
    
#     sommet_a_explorer = [depart]
#     deja_vu = {depart}

#     while (len(sommet_a_explorer)>0):
#         noeud_courant = sommet_a_explorer.pop(0)
#         print(noeud_courant)
#         for noeud in graphe[noeud_courant]:
#             if noeud not in deja_vu:
#                 deja_vu.add(noeud_courant)
#                 sommet_a_explorer.append(noeud)


def arthus_sauce(G):
    # networkx.algorithms.shortest_paths.generic.shortest_path RAISE
    # if G.number_of_nodes() == 0:
    #     return None

    graphe = G
    start = list(G.nodes.keys())[0]
    depart = list(G[start].keys())[0]
    sommet_a_explorer = [depart]
    deja_vu = {depart , start}
    fin = [0,depart]
    while (len(sommet_a_explorer)>0):
        noeud_courant = sommet_a_explorer.pop(0)
        dist = distance(G,depart,noeud_courant)
        if dist > fin[0]:
            fin = [dist,noeud_courant]
        # print(noeud_courant)
        for noeud in graphe[noeud_courant]:
            if noeud not in deja_vu:
                deja_vu.add(noeud_courant)
                sommet_a_explorer.append(noeud)

    print("1er/2 DFS")
    # DFS depart OK
    depart = fin[1]
    sommet_a_explorer = [depart]
    deja_vu = {depart}
    fin = [0,depart]
    while (len(sommet_a_explorer)>0):
        noeud_courant = sommet_a_explorer.pop(0)
        if distance(G,depart,noeud_courant) > fin[0]:
            fin = [distance(G,depart,noeud_courant),noeud_courant]
        # print(noeud_courant)
        for noeud in graphe[noeud_courant]:
            if noeud not in deja_vu:
                deja_vu.add(noeud_courant)
                sommet_a_explorer.append(noeud)
    return (depart,fin[1], distance(G,depart,fin[1]))


def eloignement_max(G):
    return arthus_sauce(G)

def cheminer(G,sommet,autre_sommet):
    # return nx.dag_longest_path(G,u,v)
    """
    On suppose que l'algorithme de DFS a été effectué sur G depuis un sommet quelconque r
    """
    import heapq
    if sommet not in G or autre_sommet not in G:
        return None

    # si il y a pas de chemin ba va te fiare
    distances = {}
    previous_nodes = {}
    heap = [(0, sommet)]  # (distance jusqu'au nœud, nœud)

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        # print(current_distance,current_node)
    
        # Vérifier si le nœud actuel est le nœud d'arrivée
        if current_node == autre_sommet:
            path = []
            # print("entrain de faire chemin back")
            previous_nodes[sommet] = None
            while current_node is not None:
                path.append(current_node)
                print(path)
                current_node = previous_nodes.get(current_node)
            # print("END",path)
            return path[::-1]  # Retourne le chemin dans l'ordre correct
        print("not end")
        # Parcourir les voisins du nœud actuel
        for neighbor in G[current_node]:
            distance = current_distance + 1
            # Mettre à jour la distance si elle est plus courte que la précédente
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))
    

def centre_hollywood(G,sauce):
    # if sauce == None or G.number_of_nodes():
    #     return None

    depart , end , distance = sauce
    # depart , end , distance = nx.algorithms.shortest_paths.generic.shortest_path(G,)

    print(" depart ",depart,  " end ",end,  " distance ",distance)
    # ch = nx.algorithms.shortest_paths.dense.reconstruct_path( depart, end,G)
    # ch =nx.algorithms.shor    test_paths.generic.shortest_path(G,depart, end)
    ch = cheminer(G,depart)

    print("ch>>>>>",ch)
    return ch[len(ch) // 2]


def centralite_groupe(G,Sommets):
    if Sommets not in G:
        return None
    return max([centralite(G,sommet) for sommet in Sommets])

import gzip

def lesprints():
    fichier = './data/dataTests.txt'
    # fichier ="./data/data.txt"
    graph_films = json_vers_nx(fichier, False)
# print(graph_films)
# Afficher quelques informations sur le graphe
# print("Nombre de nœuds (personnes) :", graph_films.number_of_nodes())
# print("Nombre d'arêtes (relations) :", graph_films.number_of_edges())
    affichage_graph(graph_films)
    # print(save_graph(graph_films))
    print(graph_films)
    
    # print(centre_hollywood(graph_films,eloignement_max(graph_films))) 
    
    # print("colab: ", collaborateurs_communs(graph_films, "Paul Reubens", "Julian Marques"))  # Output: {'Carol Kane'}
    # print("colab proche: ", collaborateurs_proches(graph_films,"Julian Marques",1))
    # print("colab proche: ", collaborateurs_proches(graph_films,"Julian Marques",2))
    # print("EST proche: ", est_proche(graph_films,"Julian Marques", "Anthony Michael Hall",1) )
    # print("EST proche: ", est_proche(graph_films,"Julian Marques", "Carol Kane",1))
    # print("distance_naive:", distance_naive(graph_films,"Julian Marques","Carol Kane") )
    # print("distance_naive:", distance_naive(graph_films,"Julian Marques","Julian Marques") )
    # print("distance_naive:", distance_naive(graph_films,"Julian Marques","Anthony Michael Hall") )
    # print("distance_naive:", distance_naive(graph_films,"Julian Marques","Goldie Hawn") )
    # print("distance:", distance(graph_films,"Julian Marques","Carol Kane") )
    # print("distance:", distance(graph_films,"Julian Marques","Julian Marques") )
    # print("distance:", distance(graph_films,"Julian Marques","Anthony Michael Hall") )
    # print("distance:", distance(graph_films,"Julian Marques","Goldie Hawn") )
    # print("centralite:", centralite(graph_films,"Julian Marques") ) # 3
    # print("centralite:", centralite(graph_films,"Goldie Hawn") ) # 3
    # print("centralite:", centralite(graph_films,"Carol Kane") ) # 2
    # # #Gcentre= graph_films
    # arthus_sauce1 = arthus_sauce(graph_films)
    # print("centre_hollywood:", centre_hollywood(graph_films,arthus_sauce1) ) 

#     print("eloignement_max:", eloignement_max(graph_films) )
#     print("eloignement_max:", arthus_sauce1 )
#     liste = ["Carol Kane","Paul Reubens"]
#     print("centralite_groupe:", centralite_groupe(graph_films,liste) )

#     print("time taken",time.perf_counter()-t_start,"s")

# cProfile.run("lesprints()")
lesprints()
print("time taken",time.perf_counter()-t_start,"s")
