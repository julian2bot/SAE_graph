import json
import networkx as nx
import itertools
import re
import matplotlib.pyplot as plt
import time
import cProfile
t_start = time.perf_counter()



def json_vers_nx(file_path, affiche=False):
    G = nx.Graph()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line:
                continue
            film = json.loads(line)
            cast = [actor.strip("[[").strip("]]") for actor in film["cast"]]
            for i, actor1 in enumerate(cast):
                for actor2 in cast[i+1:]:
                    G.add_edge(actor1, actor2, film=film["title"])
    return G


# affichage du graphe :
def affichage_graph(graph_films):
    pos = nx.spring_layout(graph_films)
    fig = plt.figure()
    nx.draw(graph_films, pos, with_labels=True, node_size=30)
    fig.savefig("G12.png")
    plt.show()


def collaborateurs_communs(G, u, v):
    voisins_u = set(G.neighbors(u))
    voisins_v = set(G.neighbors(v))
    return voisins_u.intersection(voisins_v)


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
        return nx.algorithms.shortest_paths.unweighted(G, u,v)# a TEST => 1.15
    except: return -1



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



from collections import deque

def bfs_max_distance(G, source):
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

def parcours_largeur(graphe, depart):
    sommet_a_explorer = [depart]
    deja_vu = {depart}

    while (len(sommet_a_explorer)>0):
        noeud_courant = sommet_a_explorer.pop(0)
        print(noeud_courant)
        for noeud in graphe[noeud_courant]:
            if noeud not in deja_vu:
                deja_vu.add(noeud_courant)
                sommet_a_explorer.append(noeud)


def arthus_sauce(G):
    # networkx.algorithms.shortest_paths.generic.shortest_path RAISE
    graphe = G
    start = list(G.nodes.keys())[0]
    depart = list(G[start].keys())[0]
    sommet_a_explorer = [depart]
    deja_vu = {depart , start}
    teh_end = [0,depart]
    while (len(sommet_a_explorer)>0):
        noeud_courant = sommet_a_explorer.pop(0)
        dist = distance(G,depart,noeud_courant)
        if dist > teh_end[0]:
            teh_end = [dist,noeud_courant]
        # print(noeud_courant)
        for noeud in graphe[noeud_courant]:
            if noeud not in deja_vu:
                deja_vu.add(noeud_courant)
                sommet_a_explorer.append(noeud)

    print("1er/2 DFS")
    # DFS depart OK
    depart = teh_end[1]
    sommet_a_explorer = [depart]
    deja_vu = {depart}
    teh_end = [0,depart]
    while (len(sommet_a_explorer)>0):
        noeud_courant = sommet_a_explorer.pop(0)
        if distance(G,depart,noeud_courant) > teh_end[0]:
            teh_end = [distance(G,depart,noeud_courant),noeud_courant]
        # print(noeud_courant)
        for noeud in graphe[noeud_courant]:
            if noeud not in deja_vu:
                deja_vu.add(noeud_courant)
                sommet_a_explorer.append(noeud)
    return (depart,teh_end[1], distance(G,depart,teh_end[1]))




def cheminer(G,u,v):
    """
    On suppose que l'algorithme de DFS a été effectué sur G depuis un sommet quelconque r
    """
    import heapq
    # si il y a pas de chemin ba va te fiare
    distances = {}
    previous_nodes = {}
    heap = [(0, u)]  # (distance jusqu'au nœud, nœud)

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        # print(current_distance,current_node)
        
        # Vérifier si le nœud actuel est le nœud d'arrivée
        if current_node == v:
            path = []
            # print("entrain de faire chemin back")
            previous_nodes[u] = None
            while current_node is not None:
                path.append(current_node)
                print(path)
                current_node = previous_nodes.get(current_node)
            # print("END",path)
            return path[::-1]  # Retourne le chemin dans l'ordre correct
        # print("not end")
        
        # Parcourir les voisins du nœud actuel
        for neighbor in G[current_node]:
            distance = current_distance + 1
            # Mettre à jour la distance si elle est plus courte que la précédente
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))

def centre_hollywood(G,sauce):
    depart , end , distance = sauce
    print(" depart ",depart,  " end ",end,  " distance ",distance)
    
    ch = cheminer(G,depart,end)
    # print("ch>>>>>",ch)
    return ch[len(ch) // 2]



def centralite_groupe(G,S):
    return max([centralite(G,u) for u in S])

def lesprints():
    # fichier = 'hgsifs.txt'
    # fichier = 'arthur_med.txt'
    # fichier = 'dataTests.txt'

    # fichier = 'datatest.txt'
    # fichier = 'data.txt'
    # fichier = 'test.txt'
    fichier = 'data_100.txt'
    # fichier = 'data_1000.txt'
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
    arthus_sauce1 = arthus_sauce(graph_films)
    print("centre_hollywood:", centre_hollywood(graph_films,arthus_sauce1) ) 

    # print("eloignement_max:", eloignement_max(graph_films) )
    print("eloignement_max:", arthus_sauce1 )
    liste = ["Carol Kane","Paul Reubens"]
    print("centralite_groupe:", centralite_groupe(graph_films,liste) )

    print("time taken",time.perf_counter()-t_start,"s")

# cProfile.run("lesprints()")
lesprints()
print("time taken",time.perf_counter()-t_start,"s")




















