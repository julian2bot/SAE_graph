""" 
0695412699
marquesjulian26@gmail.com


Alternance concepteur devellopeur d'application
0671854583
elodie Bossier

"""
# # import json
# # import networkx as nx
# # import itertools
# # import re
# # import matplotlib.pyplot as plt
# # def json_to_nx(chemin_vers_le_fichier_json):
# #     G=nx.Graph()
# #     with open(chemin_vers_le_fichier_json,"r") as f:
# #         data=json.loads(f)#liste de dictionnaire
# #     for dico in data:
# #         liste_acteurs=dico["cast"]
# #         taille=len(liste_acteurs)
# #         for i in range(taille):
# #             for j in range(taille-i):
# #                 G.add_edge(liste_acteurs[i],liste_acteurs[i+j])
# #     options = {
# #     'with_labels': True,
# #     'node_size': 1500,
# #     'node_color': "skyblue",
# #     'node_shape': "s", 
# #     'alpha': 0.5, 
# #     'linewidths': 10
# #     }
# #     pos = nx.spring_layout(G)
# #     fig = plt.figure()
# #     nx.draw(G, pos, with_labels=True, node_size=30)
# #     # fig.savefig("G12.png")
# #     plt.show()


# # json_to_nx("dataTests.txt")

# # # def affichage_graph(G):
   
# # """ 
# # 0695412699
# # marquesjulian26@gmail.com


# # Alternance concepteur devellopeur d'application
# # 0671854583
# # elodie Bossier

# # """
# # import json
# # import networkx as nx
# # import itertools
# # import re
# # import matplotlib.pyplot as plt

# # def json_to_nx(chemin_vers_le_fichier_json):
# #     G=nx.Graph()
# #     with open(chemin_vers_le_fichier_json,"r") as f:
        
# #         for dico in f:
# #             data=json.loads(dico)#liste de dictionnaire

# #             liste_acteurs=data["cast"]
# #             taille=len(liste_acteurs)
# #             for i in range(taille):
# #                 for j in range(taille-i):
# #                     G.add_edge(liste_acteurs[i],liste_acteurs[i+j])
# #     options = {
# #     'with_labels': True,
# #     'node_size': 1500,
# #     'node_color': "skyblue",
# #     'node_shape': "s", 
# #     'alpha': 0.5, 
# #     'linewidths': 10
# #     }
# #     pos = nx.spring_layout(G)
# #     fig = plt.figure()
# #     nx.draw(G, pos, with_labels=True, node_size=30)
# #     # fig.savefig("G12.png")
# #     plt.show()


# # json_to_nx("dataTests.txt")
# from pyspark.sql import SparkSession
# from graphframes import GraphFrame

# # # Initialize SparkSession
# # spark = SparkSession.builder \
# #     .appName("graph_analysis") \
# #     .getOrCreate()

# # # Create DataFrame from JSON data
# # json_data = spark.read.json("dataTests.txt")

# # # Convert DataFrame to GraphFrame
# # graph = GraphFrame.fromEdges(json_data)

# # # Use GraphX parallel operations to analyze the graph
# # # For example, to compute the graph diameter
# # diameter = graph.shortestPaths().groupBy().max()

# # # Display the result
# # print("Graph Diameter:", diameter)
# # from pyspark.sql import SparkSession

# # # Initialisation de la session Spark
# # spark = SparkSession.builder \
# #     .appName("Lecture JSON") \
# #     .getOrCreate()

# # # Lecture du fichier JSON dans un DataFrame
# # data_df = spark.read.json("dataTests.txt")

# # # Affichage du schéma pour vérifier la structure des données
# # data_df.printSchema()

# # # Affichage des premières lignes du DataFrame
# # data_df.show()


# from pyspark.sql import SparkSession
# from graphframes import GraphFrame

# # Initialisez la session Spark
# spark = SparkSession.builder \
#     .appName("Analyse de graphe") \
#     .getOrCreate()

# # Définition de la fonction pour lire le fichier JSON et créer le GraphFrame
# def create_graph_frame(file_path):
#     # Lecture du fichier JSON dans un DataFrame Spark
#     data_df = spark.read.json(file_path)

#     # Convertissez le DataFrame en un GraphFrame
#     graph_frame = GraphFrame.fromEdges(data_df)

#     return graph_frame

# # Utilisez la fonction pour créer le GraphFrame à partir de votre fichier JSON
# graph = create_graph_frame("dataTests.txt")

# # Utilisez les fonctionnalités de GraphFrames pour analyser le graphe, par exemple :
# # Calculer le nombre de nœuds dans le graphe
# num_vertices = graph.vertices.count()
# print("Nombre de nœuds dans le graphe:", num_vertices)

# # Calculer le nombre d'arêtes dans le graphe
# num_edges = graph.edges.count()
# print("Nombre d'arêtes dans le graphe:", num_edges)

# # Vous pouvez poursuivre avec d'autres analyses sur le graphe...

        # import json
        # import os
        # import networkx as nx
        # import itertools
        # import re
        # import matplotlib.pyplot as plt
        # import time
        # import cProfile
        # t_start = time.perf_counter()

        # # liste = ["[[Carol Kane]]","[[Julian Marques]]", "fesf"]


        # # def txt_to_json(entre):
        # #     with open(entre, 'r', encoding='utf-8') as f:
        # #         data_list = []
        # #         for line in f:
        # #             data = json.loads(line)
        # #             data_list.append(data)
        # #     return data_list

        # # def json_to_list(data_list):
        # #     liste_films = []
        # #     for film in data_list:
        # #         dict_film = {
        # #             "title": film.get("title", ""),
        # #             "cast": film.get("cast", []),
        # #             "directors": film.get("directors", []),
        # #             "producers": film.get("producers", []),
        # #             "companies": film.get("companies", []),
        # #             "year": film.get("year", "")
        # #         }
        # #         liste_films.append(dict_film)
        # #     return liste_films

        # # # def extract_actor_name(actor_string):
        # # #     pattern = r'\[\[(.*?)\]\]'
        # # #     match = re.search(pattern, actor_string)
        # # #     if match:
        # # #         return match.group(1) 
        # # #     else:
        # # #         return actor_string
            
        # # def json_vers_nx(file_path):
        # #     G = nx.Graph()
        # #     data_list = txt_to_json(file_path)
        # #     liste_films = json_to_list(data_list)
        # #     for film in liste_films:
        # #         cast = film["cast"]
        # #         # Créer toutes les combinaisons possibles de deux acteurs dans le cast
        #         # actor_combinations = list(itertools.combinations(cast, 2))
        # #         # ajout dans un ensembe tout les tuples:
        # #         #  Ajout arête pour chaque paire d'acteurs dans le cast
        # #         for actor_pair in actor_combinations:
        # #             actor1, actor2 = actor_pair
        # #             # print(actor1, actor2)
        # #             actor1 = actor1.strip("[[").strip("]]")
        # #             actor2 = actor2.strip("[[").strip("]]") 
        # #             # actor1 = extract_actor_name(actor1) 
        # #             # actor2 = extract_actor_name(actor2)
        # #             # print(actor1, actor2)

        # #             G.add_edge(actor1, actor2, film=film["title"])
        # #     return G

        # # LE BON
        # def json_vers_nx(file_path, affiche=False):
        #     G = nx.Graph()
        #     with open(file_path, 'r', encoding='utf-8') as f:
        #         for line in f:
        #             if not line:
        #                 continue
        #             film = json.loads(line)
        #             cast = [actor.strip("[[").strip("]]") for actor in film["cast"]]
        #             for i, actor1 in enumerate(cast):
        #                 for actor2 in cast[i+1:]:
        #                     G.add_edge(actor1, actor2, film=film["title"])
        #     return G


        
        # # def json_vers_nx(chemin_vers_le_fichier_json, affiche= False):
        # #     G=nx.Graph()
        # #     with open(chemin_vers_le_fichier_json,"r", encoding='utf-8') as f:
        # #         data=json.load(f)#liste de dictionnaire
        # #     ens_acteur_parcouru=set()
        # #     for dico in data:
        # #         # print(len(ens_acteur_parcouru))
        # #         liste_acteurs=dico["cast"]
        # #         taille=len(liste_acteurs)
        # #         for i in range(taille):
        # #             if liste_acteurs[i]not in ens_acteur_parcouru:
        # #                 ens_acteur_parcouru.add(liste_acteurs[i])
        # #                 for j in range(taille-i):
        # #                     G.add_edge(liste_acteurs[i],liste_acteurs[i+j])
        # #     # print("Il y a "+str(len(ens_acteur_parcouru))+" acteurs.")
        # #     # affichage_graph(G)
        # #     return G


        # # def json_vers_nx(file_path, affiche=False):
        # #     G = nx.Graph()
        # #     with open(file_path, 'r', encoding='utf-8') as f:
        # #         for line in f:
        # #             film = json.loads(line)
        # #             cast = [actor.strip("[[").strip("]]") for actor in film["cast"]]
        # #             for actors in cast:
        # #                 G.add_edges_from(list(itertools.combinations(actors,2)))

        # #     return G



        # # Pour afficher le graph et le sauvegardé en .png

        # # Créer le graphe à partir des données des films
        # # graph_films = json_vers_nx(fichier)

        # # Vous pouvez visualiser le graphe si vous avez Matplotlib installé
        # # Voici un exemple de code pour le visualiser

        # # affichage du graphe :
        # def affichage_graph(graph_films):
        #     pos = nx.spring_layout(graph_films)
        #     fig = plt.figure()
        #     nx.draw(graph_films, pos, with_labels=True, node_size=30)
        #     fig.savefig("G12.png")
        #     plt.show()
        # # def save_graph(graph_films):
        # #     """affiche le graph qu'on lui rentre en parametre grace a plotlib

        # #     Args:
        # #         graph_films (nx.Graph): le graphique à afficher
        # #     """
        # #     nameimg = "graph.png"
        # #     pos = nx.spring_layout(graph_films)
        # #     fig = plt.figure()
        # #     nx.draw(graph_films, pos, with_labels=True, node_size=30)
        # #     fig.savefig(nameimg)
        # #     # plt.show()
        # #     print(nameimg)
        # #     print(os.path.abspath(nameimg))
        # #     return os.path.abspath(nameimg)


        # def save_graph(graph_films):
        #     """Affiche le graphique passé en paramètre grâce à matplotlib et le sauvegarde sous forme d'image.

        #     Args:
        #         graph_films (nx.Graph): Le graphique à afficher
        #     Returns:
        #         str: Le chemin absolu de l'image enregistrée
        #     """
        #     nameimg = "graph.png"
        #     pos = nx.spring_layout(graph_films)
        #     fig = plt.figure()
        #     nx.draw(graph_films, pos, with_labels=True, node_size=30)
        #     fig.savefig(nameimg)
        #     # Renvoyer le chemin absolu de l'image enregistrée
        #     print(nameimg)
        #     print("img!!!!!",os.path.abspath(nameimg))
        #     return str(os.path.abspath(nameimg))


        # def collaborateurs_communs(G, u, v):
        #     if u not in G or v not in G:
        #         return None

        #     voisins_u = set(G.neighbors(u))
        #     voisins_v = set(G.neighbors(v))
        #     return voisins_u.intersection(voisins_v)


        # def collaborateurs_proches(G,u,k):
        #     """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
            
        #     Parametres:
        #         G: le graphe
        #         u: le sommet de départ
        #         k: la distance depuis u
        #     """
        #     if u not in G.nodes:
        #         print(u,"est un illustre inconnu")
        #         return None
        #     collaborateurs = set()
        #     collaborateurs.add(u)
        #     # print(collaborateurs)
        #     for i in range(k):
        #         collaborateurs_directs = set()
        #         for c in collaborateurs:
        #             for voisin in G.adj[c]:
        #                 if voisin not in collaborateurs:
        #                     collaborateurs_directs.add(voisin)
        #         collaborateurs = collaborateurs.union(collaborateurs_directs)
        #     return collaborateurs


        # def est_proche(G,u,v,k=1):
        #     return v in collaborateurs_proches(G,u,k) 


        # def distance_naive(G, u, v):
        #     if u not in G.nodes or v not in G.nodes:
        #         return -1
        #     distance = 0
            
        #     while distance <100:
        #         if est_proche(G, u, v, k=distance):
        #             return distance
        #         distance += 1
        #     return -1


        # # Cette fonction distance utilise BFS pour trouver la distance entre deux acteurs u et v dans un graphe G. Sa complexité est O(V + E), ce qui est plus efficace que l'approche naïve précédente.
        # def distance(G, u, v):
        #     # retorune distance dsitra 
        #     try:
        #         return nx.shortest_path_length(G,u, v) # a TEST oui => 0.10
        #         # return nx.dijkstra_path_length(G,u, v) # ok mais peut mieux faire
        #         # return nx.single_source_dijkstra_path_length(G, u,v) # non 
        #         # return nx.floyd_warshall_numpy(G, u,v) # mais non
        #         # return nx.algorithms.shortest_paths.astar(G, u,v)# a TEST => 0.09 mais non
        #         # return nx.algorithms.shortest_paths.dense (G, u,v)# a TEST => 1.32 mais non
        #         # return nx.algorithms.shortest_paths.generic (G, u,v)# a TEST => 1.16 mais non
        #         # return nx.algorithms.shortest_paths.unweighted(G, u,v)# a TEST => 1.26 mais non
        #         # return nx.algorithms.shortest_paths.unweighted(G, u,v)# a TEST => 1.15 mais non
        #         # return nx.algorithms.shortest_paths.unweighted.single_source_shortest_path_length(G, u,v)# a TEST => 0.09 mais non 

        #         # return int(nx.all_shortest_paths(G, source=u, target=v))
        #     except: return -1
        #     # visited = set()
        #     # queue = [(u, 0)]
        #     # while queue:
        #     #     node, dist = queue.pop(0)
        #     #     if node == v:
        #     #         return dist
        #     #     visited.add(node)
        #     #     for neighbor in G.neighbors(node):
        #     #         if neighbor not in visited:
        #     #             queue.append((neighbor, dist + 1))
        #     # return -1 

        # # def centralite(G,u):
        #     # shortest_paths = nx.shortest_path_length(G, source=u)
        # #     centralite_u = max(shortest_paths.values())
        # #     return centralite_u


        # # def centre_hollywood(G):
        # #     centralites = {acteur: centralite(G, acteur) for acteur in G.nodes()}
        # #     acteur_central = min(centralites, key=centralites.get)
        # #     return acteur_central, centralites[acteur_central]

        # # def centralite(G, u):
        # #     shortest_paths = nx.single_source_dijkstra_path_length(G, u)
        # #     centralite_u = max(shortest_paths.values())
        # #     return centralite_u



        # def centralite(G, u):
        #     """ renvoie une distance entre u et le bord du graph

        #     Args:
        #         G: le graphe
        #         u: le sommet de départ de l'acteur
        #     Returns:
        #         int : la centralité depuis u vers v
        #     """
        #     shortest_paths = nx.single_source_dijkstra_path_length(G, u)
        #     centralite_u = max(shortest_paths.values())
        #     return centralite_u
        #     # or
        #     # return max(nx.single_source_dijkstra_path_length(G, u).values())


        # # def centralite(G, u):
            
        # #     return max(nx.single_source_dijkstra_path_length(G, u).values())

        # # def centre_hollywood(G):
        # #     centralites = {acteur: centralite(G, acteur) for acteur in G.nodes()}
        # #     acteur_central = min(centralites, key=centralites.get)
        # #     return acteur_central, centralites[acteur_central]
        # # import random
        # # def centralite(G, u, sample_size=100):
        # #     # Convertir l'ensemble de nœuds en une liste
        # #     nodes_list = list(G.nodes())
            
        # #     # Échantillonner un sous-ensemble aléatoire de nœuds du graphe
        # #     sampled_nodes = random.sample(nodes_list, min(sample_size, len(nodes_list)))
            
        # #     # Calculer la centralité à partir des nœuds échantillonnés
        # #     centralities = nx.single_source_dijkstra_path_length(G.subgraph(sampled_nodes), u)
            
        # #     # Renvoyer la valeur maximale de la centralité parmi les nœuds échantillonnés
        # #     return max(centralities.values())

        #             # import random

        #             # def centralite(G, u, sample_size=100):
        #             #     # Vérifier si le nœud u existe dans le graphe
        #             #     if not G.has_node(u):
        #             #         return None

        #             #     # Convertir l'ensemble de nœuds en une liste
        #             #     nodes_list = list(G.nodes())
                        
        #             #     # Vérifier si le nœud u est dans la liste des nœuds
        #             #     if u not in nodes_list:
        #             #         return None
                        
        #             #     # Échantillonner un sous-ensemble aléatoire de nœuds du graphe
        #             #     sampled_nodes = random.sample(nodes_list, min(sample_size, len(nodes_list)))
                        
        #             #     # Calculer la centralité à partir des nœuds échantillonnés
        #             #     centralities = nx.single_source_dijkstra_path_length(G.subgraph(sampled_nodes), u)
                        
        #             #     # Renvoyer la valeur maximale de la centralité parmi les nœuds échantillonnés
        #             #     return max(centralities.values())

        #             # def centre_hollywood(G, sample_size=100):
        #             #     # Vérifier si le graphe est vide
        #             #     if not G:
        #             #         return None, None
                        
        #             #     # Convertir l'ensemble de nœuds en une liste
        #             #     nodes_list = list(G.nodes())
                        
        #             #     # Vérifier si la liste des nœuds est vide
        #             #     if not nodes_list:
        #             #         return None, None
                        
        #             #     # Calculer la centralité pour chaque acteur dans un sous-ensemble aléatoire
        #             #     centralities = {acteur: centralite(G, acteur, sample_size) for acteur in nodes_list}
                        
        #             #     # Exclure les acteurs avec une centralité nulle
        #             #     centralities = {acteur: centrality for acteur, centrality in centralities.items() if centrality is not None}
                        
        #             #     # Vérifier si la liste des centralités est vide
        #             #     if not centralities:
        #             #         return None, None
                        
        #             #     # Trouver l'acteur avec la centralité maximale
        #             #     acteur_central = max(centralities, key=centralities.get)
                        
        #             #     return acteur_central, centralities[acteur_central]

        # # def centre_hollywood(G, sample_size=100):
        # #     # Convertir l'ensemble de nœuds en une liste
        # #     nodes_list = list(G.nodes())
            
        # #     # Vérifier si la taille de l'échantillon est supérieure au nombre total de nœuds
        # #     if sample_size >= len(nodes_list):
        # #         print("La taille de l'échantillon est supérieure au nombre total de nœuds. Utilisation de tous les nœuds.")
        # #         sampled_nodes = nodes_list
        # #     else:
        # #         # Échantillonner un sous-ensemble aléatoire de nœuds du graphe
        # #         sampled_nodes = random.sample(nodes_list, sample_size)
            
        # #     # Calculer la centralité pour chaque acteur dans l'échantillon
        # #     centralities = {acteur: centralite(G, acteur, sample_size) for acteur in sampled_nodes}
            
        # #     # Trouver l'acteur avec la centralité minimale parmi les échantillons
        # #     acteur_central = min(centralities, key=centralities.get)
            
        # #     return acteur_central, centralities[acteur_central]


        # # def dfs_max_distance(G, u, visited=None, distance=0):
        # #     if visited is None:
        # #         visited = set()
        # #     visited.add(u)
        # #     max_distance = distance
        # #     for v in G.neighbors(u):
        # #         if v not in visited:
        # #             max_distance = max(max_distance, dfs_max_distance(G, v, visited, distance + 1))
        # #     return max_distance

        # # def centralite(G, u):
        # #     return dfs_max_distance(G, u)

        # # def centre_hollywood(G):
        # #     centralites = {acteur: centralite(G, acteur) for acteur in G.nodes()}
        # #     acteur_central = min(centralites, key=centralites.get)
        # #     return acteur_central, centralites[acteur_central]


        # # def dfs_max_distance(G, u):
        # #     visited = set()
        # #     stack = [(u, 0)]  # Pile de nœuds à explorer avec leur distance
        # #     max_distance = 0

        # #     while stack:
        # #         node, distance = stack.pop()
        # #         visited.add(node)
        # #         max_distance = max(max_distance, distance)

        # #         for neighbor in G.neighbors(node):
        # #             if neighbor not in visited:
        # #                 stack.append((neighbor, distance + 1))

        # #     return max_distance

        # # def centralite(G, u):
        # #     return dfs_max_distance(G, u)

        # # def centre_hollywood(G):
        # #     centralites = {acteur: centralite(G, acteur) for acteur in G.nodes()}
        # #     acteur_central = min(centralites, key=centralites.get)
        # #     return acteur_central, centralites[acteur_central]


        # # def eloignement_max(G: nx.Graph):
        # #     # Calcul des distances minimales entre toutes les paires de nœuds
        # #     distances = nx.floyd_warshall(G)
            
        # #     # Recherche de la distance maximale dans la matrice des distances
        # #     max_distance = 0
        # #     for u, distances_from_u in distances.items():
        # #         max_distance = max(max_distance, max(distances_from_u.values()))
            
        # #     return max_distance

        # import networkx as nx

        # # def eloignement_max(G: nx.Graph):
        # #     # Créer un dictionnaire pour stocker les distances maximales entre les films
        # #     distances_max = {}
            
        # #     # Parcourir toutes les paires de nœuds (acteurs)
        # #     for actor1 in G.nodes():
        # #         for actor2 in G.nodes():
        # #             # Ignorer les paires identiques
        # #             if actor1 == actor2:
        # #                 continue
                    
        # #             # Récupérer tous les chemins possibles entre les acteurs
        # #             paths = nx.all_shortest_paths(G, source=actor1, target=actor2)
                    
        # #             # Parcourir tous les chemins et trouver la distance maximale entre les films
        # #             max_distance = float('-inf')
        # #             for path in paths:
        # #                 # Trouver la distance entre les films sur ce chemin
        # #                 distance = 0
        # #                 for i in range(len(path) - 1):
        # #                     film = G[path[i]][path[i+1]]['film']
        # #                     distance += 1  # On suppose que chaque lien a une distance de 1
        # #                 # Mettre à jour la distance maximale si nécessaire
        # #                 if distance > max_distance:
        # #                     max_distance = distance
                    
        # #             # Mettre à jour le dictionnaire des distances maximales
        # #             if max_distance != float('-inf'):
        # #                 if max_distance not in distances_max:
        # #                     distances_max[max_distance] = [(actor1, actor2)]
        # #                 else:
        # #                     distances_max[max_distance].append((actor1, actor2))
            
        # #     return distances_max

        # # import networkx as nx

        # # def eloignement_max(G: nx.Graph):
        # #     # Créer un dictionnaire pour stocker les distances maximales entre les films
        # #     distances_max = {}
            
        # #     # Parcourir tous les nœuds du graphe
        # #     for actor in G.nodes():
        # #         # Calculer les distances les plus courtes à partir de l'acteur actuel
        # #         shortest_distances = nx.single_source_dijkstra_path_length(G, source=actor)
                
        # #         # Parcourir les distances les plus courtes et mettre à jour les distances maximales
        # #         for target_actor, distance in shortest_distances.items():
        # #             # Ignorer le cas où l'acteur actuel est le même que la cible
        # #             if actor != target_actor:
        # #                 # Mettre à jour la distance maximale si nécessaire
        # #                 max_distance = distances_max.get(distance, 0)
        # #                 if max_distance < distance:
        # #                     distances_max[distance] = max_distance
            
        # #     return distances_max



        # # def eloignement_max(G: nx.Graph):
        # #     # Calcul des distances minimales entre toutes les paires de nœuds
        # #     distances = nx.floyd_warshall(G)
            
        # #     # Recherche de la distance maximale dans la matrice des distances
        # #     max_distance = 0
        # #     for u, distances_from_u in distances.items():
        # #         max_distance_from_u = max(dist for v, dist in distances_from_u.items() if dist != float('inf'))
        # #         max_distance = max(max_distance, max_distance_from_u)
            
        # #     return max_distance

        # # import numpy as np

        # # def eloignement_max(G):
        # #     # Convertir le graphe en matrice d'adjacence
        # #     adj_matrix = nx.to_numpy_array(G)

        # #     # Remplacer les valeurs nulles (pas de connexion) par l'infini
        # #     adj_matrix[adj_matrix == 0] = np.inf

        # #     # Utiliser l'algorithme de Floyd-Warshall pour calculer toutes les distances minimales
        # #     distances = np.array(nx.floyd_warshall_numpy(G))

        # #     # Trouver la distance maximale
        # #     max_distance = np.max(distances[~np.isinf(distances)])

        # #     return max_distance

        # from collections import deque

        # def bfs_max_distance(G, source):
        #     visited = set()
        #     queue = deque([(source, 0)])  # Queue pour BFS, avec la distance de départ 0
        #     max_distance = 0

        #     while queue:
        #         node, distance = queue.popleft()
        #         visited.add(node)
        #         max_distance = max(max_distance, distance)

        #         for neighbor in G.neighbors(node):
        #             if neighbor not in visited:
        #                 queue.append((neighbor, distance + 1))

        #     return max_distance

        # def eloignement_max(G):
        #     max_distance = 0
        #     for node in G.nodes():
        #         distance_from_node = bfs_max_distance(G, node)
        #         max_distance = max(max_distance, distance_from_node)
            
        #     return max_distance

        # def parcours_largeur(graphe, depart):
        #     sommet_a_explorer = [depart]
        #     deja_vu = {depart}

        #     while (len(sommet_a_explorer)>0):
        #         noeud_courant = sommet_a_explorer.pop(0)
        #         print(noeud_courant)
        #         for noeud in graphe[noeud_courant]:
        #             if noeud not in deja_vu:
        #                 deja_vu.add(noeud_courant)
        #                 sommet_a_explorer.append(noeud)


        # def arthus_sauce(G):
        #     # networkx.algorithms.shortest_paths.generic.shortest_path RAISE
        #     graphe = G
        #     start = list(G.nodes.keys())[0]
        #     depart = list(G[start].keys())[0]
        #     sommet_a_explorer = [depart]
        #     deja_vu = {depart , start}
        #     teh_end = [0,depart]
        #     while (len(sommet_a_explorer)>0):
        #         noeud_courant = sommet_a_explorer.pop(0)
        #         dist = distance(G,depart,noeud_courant)
        #         if dist > teh_end[0]:
        #             teh_end = [dist,noeud_courant]
        #         # print(noeud_courant)
        #         for noeud in graphe[noeud_courant]:
        #             if noeud not in deja_vu:
        #                 deja_vu.add(noeud_courant)
        #                 sommet_a_explorer.append(noeud)

        #     print("1er/2 DFS")
        #     # DFS depart OK
        #     depart = teh_end[1]
        #     sommet_a_explorer = [depart]
        #     deja_vu = {depart}
        #     teh_end = [0,depart]
        #     while (len(sommet_a_explorer)>0):
        #         noeud_courant = sommet_a_explorer.pop(0)
        #         if distance(G,depart,noeud_courant) > teh_end[0]:
        #             teh_end = [distance(G,depart,noeud_courant),noeud_courant]
        #         # print(noeud_courant)
        #         for noeud in graphe[noeud_courant]:
        #             if noeud not in deja_vu:
        #                 deja_vu.add(noeud_courant)
        #                 sommet_a_explorer.append(noeud)
        #     return (depart,teh_end[1], distance(G,depart,teh_end[1]))

        # # def cheminer(G,u,v):
        # #     """
        # #     On suppose que l'algorithme de DFS a été effectué sur G depuis un sommet quelconque r
        # #     """
        # #     # si il y a pas de chemin ba va te fiare
        # #     chemin = []
        # #     sommet_courant = u
        # #     no_no = set()
        # #     while sommet_courant != None and sommet_courant != v:
        # #         chemin.append(sommet_courant)
        # #         # neightbors
        # #         for neibords in G[sommet_courant]:
        # #             if neibords not in no_no and neibords not in chemin:
        # #                 sommet_courant = neibords
        # #                 no_no.add(sommet_courant)
        # #                 break
        # #         else:
        # #             chemin.pop()
        # #             sommet_courant = chemin.pop()
        # #     chemin.append(sommet_courant)
        # #     return chemin

        # def cheminer(G,u,v):
        #     return nx.dag_longest_path(G,u,v)
        #     # """
        #     # On suppose que l'algorithme de DFS a été effectué sur G depuis un sommet quelconque r
        #     # """
        #     # import heapq
        #     # # si il y a pas de chemin ba va te fiare
        #     # distances = {}
        #     # previous_nodes = {}
        #     # heap = [(0, u)]  # (distance jusqu'au nœud, nœud)

        #     # while heap:
        #     #     current_distance, current_node = heapq.heappop(heap)
        #     #     # print(current_distance,current_node)
                
        #     #     # Vérifier si le nœud actuel est le nœud d'arrivée
        #     #     if current_node == v:
        #     #         path = []
        #     #         # print("entrain de faire chemin back")
        #     #         previous_nodes[u] = None
        #     #         while current_node is not None:
        #     #             path.append(current_node)
        #     #             print(path)
        #     #             current_node = previous_nodes.get(current_node)
        #     #         # print("END",path)
        #     #         return path[::-1]  # Retourne le chemin dans l'ordre correct
        #     #     # print("not end")
                
        #     #     # Parcourir les voisins du nœud actuel
        #     #     for neighbor in G[current_node]:
        #     #         distance = current_distance + 1
        #     #         # Mettre à jour la distance si elle est plus courte que la précédente
        #     #         if neighbor not in distances or distance < distances[neighbor]:
        #     #             distances[neighbor] = distance
        #     #             previous_nodes[neighbor] = current_node
        #     #             heapq.heappush(heap, (distance, neighbor))

        # def centre_hollywood(G,sauce):
        #     depart , end , distance = sauce
        #     # depart , end , distance = nx.algorithms.shortest_paths.generic.shortest_path(G,)

        #     print(" depart ",depart,  " end ",end,  " distance ",distance)
        #     # ch = nx.algorithms.shortest_paths.dense.reconstruct_path( depart, end,G)
        #     # ch =nx.algorithms.shortest_paths.generic.shortest_path(G,depart, end)
        #     ch = cheminer(G,depart,end)

        #     print("ch>>>>>",ch)
        #     return ch[len(ch) // 2]


        # # def cheminer(G,u,v):
        # #     """
        # #     On suppose que l'algorithme de DFS a été effectué sur G depuis un sommet quelconque r
        # #     """
        # #     # Initialisation de la file
        # #     file = [(u, [u])]
        # #     visited = set()

        # #     while file:
        # #         (sommet_courant, chemin) = file.pop()
        # #         if sommet_courant == v:
        # #             return chemin
        # #         if sommet_courant not in visited:
        # #             visited.add(sommet_courant)
        # #             for voisin in G[sommet_courant]:
        # #                 if voisin not in visited:
        # #                     file.append((voisin, chemin + [voisin]))
        # #     # Pas de chemin trouvé
        # #     return None




        # # def dfs_chercher_chemin(G, u, v, chemin=[]):
        # #     chemin = chemin + [u]
        # #     if u == v:
        # #         return chemin
        # #     plus_court_chemin = None
        # #     for voisin in G[u]:
        # #         if voisin not in chemin:
        # #             nouveau_chemin = dfs_chercher_chemin(G, voisin, v, chemin)
        # #             if nouveau_chemin:
        # #                 if not plus_court_chemin or len(nouveau_chemin) < len(plus_court_chemin):
        # #                     plus_court_chemin = nouveau_chemin
        # #     return plus_court_chemin

        # # def centre_hollywood(G):
        # #     depart, end, distance = arthus_sauce(G)
        # #     ch = dfs_chercher_chemin(G, depart, end)
        # #     print("ch>>>>>",ch)
        # #     return ch[len(ch) // 2]





        # def centralite_groupe(G,S):
        #     return max([centralite(G,u) for u in S])

        # def lesprints():
        #     # fichier = 'hgsifs.txt'
        #     # fichier = 'arthur_med.txt'
        #     fichier = 'dataTests.txt'

        #     # fichier = 'datatest.txt'
        #     # fichier = 'data.txt'
        #     # fichier = 'test.txt'
        #     # fichier = 'data_100.txt'
        #     # fichier = 'data_1000.txt'
        #     graph_films = json_vers_nx(fichier, True)
        # # print(graph_films)
        # # Afficher quelques informations sur le graphe
        # # print("Nombre de nœuds (personnes) :", graph_films.number_of_nodes())
        # # print("Nombre d'arêtes (relations) :", graph_films.number_of_edges())
        #     # affichage_graph(graph_films)
        #     print(save_graph(graph_films))
        #     print(graph_films)
        #     # print("colab: ", collaborateurs_communs(graph_films, "Paul Reubens", "Julian Marques"))  # Output: {'Carol Kane'}
        #     # print("colab proche: ", collaborateurs_proches(graph_films,"Julian Marques",1))
        #     # print("colab proche: ", collaborateurs_proches(graph_films,"Julian Marques",2))
        #     # print("EST proche: ", est_proche(graph_films,"Julian Marques", "Anthony Michael Hall",1) )
        #     # print("EST proche: ", est_proche(graph_films,"Julian Marques", "Carol Kane",1))
        #     # print("distance_naive:", distance_naive(graph_films,"Julian Marques","Carol Kane") )
        #     # print("distance_naive:", distance_naive(graph_films,"Julian Marques","Julian Marques") )
        #     # print("distance_naive:", distance_naive(graph_films,"Julian Marques","Anthony Michael Hall") )
        #     # print("distance_naive:", distance_naive(graph_films,"Julian Marques","Goldie Hawn") )
        #     # print("distance:", distance(graph_films,"Julian Marques","Carol Kane") )
        #     # print("distance:", distance(graph_films,"Julian Marques","Julian Marques") )
        #     # print("distance:", distance(graph_films,"Julian Marques","Anthony Michael Hall") )
        #     # print("distance:", distance(graph_films,"Julian Marques","Goldie Hawn") )
        #     # print("centralite:", centralite(graph_films,"Julian Marques") ) # 3
        #     # print("centralite:", centralite(graph_films,"Goldie Hawn") ) # 3
        #     # print("centralite:", centralite(graph_films,"Carol Kane") ) # 2
        #     # # #Gcentre= graph_films
        #     # arthus_sauce1 = arthus_sauce(graph_films)
        #     # print("centre_hollywood:", centre_hollywood(graph_films,arthus_sauce1) ) 

        #     # print("eloignement_max:", eloignement_max(graph_films) )
        #     # print("eloignement_max:", arthus_sauce1 )
        #     # liste = ["Carol Kane","Paul Reubens"]
        #     # print("centralite_groupe:", centralite_groupe(graph_films,liste) )

        #     print("time taken",time.perf_counter()-t_start,"s")

        # # cProfile.run("lesprints()")
        # lesprints()
        # print("time taken",time.perf_counter()-t_start,"s")

        # # # Q1
        # # def json_vers_nx(chemin):
        # #     ...
        # # # Q2
        # # def collaborateurs_communs(G,u,v):
        # #     ...
        # # # Q3
        # # def collaborateurs_proches(G,u,k):
        # #     ...
        # # def est_proche(G,u,v,k=1):
        # #     if v in list(G.adj[u]):
        # #         return True
        # #     return False
        # #     ...
        # # def distance_naive(G,u,v):
        # #     ...
        # # def distance(G,u,v):
        # #     ...
        # # # Q4
        # # def centralite(G,u):
        # #     ...
        # # def centre_hollywood(G):
        # #     ...
        # # # Q5

        # # def eloignement_max(G:nx.Graph):
        # #     ...
        # # # Bonus
        # # def centralite_groupe(G,S):
        # #     ...





        # # def create_set_from_films(file_path):
            
        # #     res = set()
        # #     # indezfbhifzehiqdfsnjo=0
        # #     data_list = txt_to_json(file_path)
        # #     liste_films = json_to_list(data_list)
        # #     for film in liste_films:
        # #         cast = film["cast"]
        # #         # Créer toutes les combinaisons possibles de deux acteurs dans le cast
        # #         actor_combinations = list(itertools.combinations(cast, 2))
        # #         for actor_pair in actor_combinations:
        # #             actor1, actor2 = actor_pair
        # #             # print(actor1, actor2)
        # #             actor1 = extract_actor_name(actor1) 
        # #             actor2 = extract_actor_name(actor2)
        # #             res.add((actor1,actor2))
                    
        # #     return res

        # # print(create_set_from_films(fichier))


        # # def list_to_txt(entre, ensemble):
        # #     with open(entre, 'w', encoding='utf-8') as f:
        # #         f.write(entre)



        # # import json

        # # import json

        # # def txt_to_json(entre, sortie):
        # #     with open(entre, 'r', encoding='utf-8') as f:
        # #         data_list = []
        # #         for line in f:
        # #             data = json.loads(line)
        # #             data_list.append(data)

        # #     with open(sortie, 'w') as f:
        # #         json.dump(data_list, f, indent=4)

        # #     print("Fichier modifié avec succès!")
            
        # #     return data_list

        # # def json_to_list(fichier):

        # #     with open(fichier, 'r', encoding='utf-8') as f:
        # #         data_list = json.load(f)
                
        # #     liste_films = []
        # #     for film in data_list:
        # #         dict_film = {
        # #             "title": film.get("title", ""),
        # #             "cast": film.get("cast", []),
        # #             "directors": film.get("directors", []),
        # #             "producers": film.get("producers", []),
        # #             "companies": film.get("companies", []),
        # #             "year": film.get("year", "")
        # #         }
        # #         liste_films.append(dict_film)
            
        # #     return liste_films

        # # # Utilisation de la fonction
        # # fichier = 'data.txt'
        # # retour = 'nouveau_fichier.json'

        # # # Convertir le fichier texte en JSON
        # # donnees = txt_to_json(fichier, retour)
        # # # Convertir le JSON en liste de dictionnaires
        # # liste_films = json_to_list(retour)
        # # print(liste_films)  # Afficher la liste de films











        # # def txt_to_json(entre, sortie):
        # #     with open(entre, 'r', encoding='utf-8') as f:
        # #         data_list = []
        # #         for line in f:
        # #             data = json.loads(line)
        # #             data_list.append(data)
        # # jsonString = '{ "id": 121, "name": "Naveen", "course": "MERN Stack"}'
        
        # # # Convert JSON String to Python
        # # student_details = json.loads(jsonString)
        
        # # # Print Dictionary
        # # print(student_details)
        
        # # # Print values using keys
        # # print(student_details['name'])
        # # print(student_details['course'])

        # # fichier = 'data.txt'
        # # fichier = 'data.txt'
        # # retour = 'nouveau_fichier.json'

        # # def txt_to_json(entre, sortie):
        # #     with open(entre, 'r', encoding='utf-8') as f:
        # #         data_list = []
        # #         for line in f:
        # #             data = json.loads(line)
        # #             data_list.append(data)

        # #     with open(sortie, 'w') as f:
        # #         json.dump(data_list, f, indent=4)

        # #     print("Fichier modifié avec succès!")

        # # # txt_to_json('./data/data.txt', 'nouveau_fichier.json')
        # # # txt_to_json(fichier, retour )


        # # def json_to_list(fichier, retour):
        # #     donnees = txt_to_json(fichier, retour)
        # #     liste_films = []
        # #     for film in donnees:
        # #         print(film["cast"])
        # #         dict_film = {
        # #             "title": film["title"],
        # #             "cast": film["cast"],
        # #             "directors": film["directors"],
        # #             "producers": film["producers"],
        # #             "companies": film["companies"],
        # #             "year": film["year"]

        # #         }
        # #         liste_films.append(dict_film)

        #     # Affichage de la liste de dictionnaires
        # #     print(liste_films)
        # # json_to_list(fichier, retour)


        # # def lectureJson(fichier):
        # #     res=0
        # #     with open(fichier, "r") as f:
        # #         # print("f"+f)
        # #         for line in f:
        # #             # ['title', 'cast', 'directors', 'producers', 'companies', 'year']
        # #             for i in line:
        # #                 print("line"+ line)
        # #                 print("i"+ i)
        # #                 res+=1
        # #     print(res)
        # #             # data = json.loads(line)
        # #             # data_list.append(data)data = json.load(f)
        # #             # print(data)

        # # lectureJson(retour)

        # # def txt_to_json(entre):
        # #     data = []
        # #     dicoCast = dict()
        # #     setCast = set()

        # #     with open(entre, 'r', encoding='utf-8') as f:
        # #         for line in f:
        # #             tmp = json.loads(line)
        # #             ret = {}
        # #             for k,v in tmp.items():

        # #                 if isinstance(v,list):
        # #                     ret[k] = [x.strip("[").strip("]") for x in v]
        # #                     print(ret)
        # #                 else:
        # #                      ret[k] = v
        # #                 print("VVV",k["cast"])
        # #                 # if v in dicoCast.items:
        # #                 #     pass
        # #                 # else:
        # #                 #     # dicoCast[v]
        # #                 #     dicoCast[v]
        # #             print(dicoCast)
        # #             data.append(ret)
                    
        # #     return data

        # # txt_to_json(fichier)
        # # import json
        # # import networkx

        # # fichier = "./data/test.txt"


        # # def txt_to_json(entre, sortie):
        # #     with open(entre, 'r', encoding='utf-8') as f:
        # #         data_list = []
        # #         for line in f:
        # #             data = json.loads(line)
        # #             print('data:' + data)
        # #             data_list.append(data)

        # #     with open(sortie, 'w') as f:
        # #         json.dump(data_list, f, indent=4)

        # #     print("Fichier modifié avec succès!")

        # # txt_to_json(fichier, 'nouveau_fichier.json')

        # # def txt_to_json(entre):
        # #     data = []
        # #     with open(entre, 'r', encoding='utf-8') as f:
        # #         for line in f:
        # #             tmp = json.loads(line)
        # #             ret = {}
        # #             for k,v in tmp.items():
        # #                 if isinstance(v,list):
        # #                     ret[k] = [x.strip("[").strip("]") for x in v]
        # #                 else:
        # #                      ret[k] = v
        # #             data.append(ret)
        # #     return data
        # # def   (data):
        # #     G = networkx.Graph()
        # #     # crée table
        # #     G.add_node("title")
        # #     G.add_node("cast")
        # #     G.add_node("directors")
        # #     G.add_node("producers")
        # #     G.add_node("companies")
        # #     G.add_node("year")
        # # #     # ['title', 'cast', 'directors', 'producers', 'companies', 'year']
        # #     res = []
        # #     for index,film in enumerate(data):
        # #         # print(film)
        # #         # res.append(film["title"])
        # #         G.add_edge("title",film["title"])
        # #         G.add_edge("cast",film["cast"])
        # #         G.add_edge("directors",film["directors"])
        # #         G.add_edge("producers",film["producers"])
        # #         G.add_edge("companies",film["companies"])
        # #         G.add_edge("year",film["year"])
        # #     # return res

        # # data = txt_to_json(fichier)
        # # print(list_json_vers_graph(data))

            
        # # def main():
        # #     print("loading data")
        # #     data = txt_to_json(fichier)
        # #     print("building graph")
        # #     G = list_json_vers_graph(data)

        # # if __name__ == "__main__":
        # #     main()
        # # else:
        # #     print("SAE imported")






        # # def distance_naive(G,u,v):
        # #     index = 0
        # #     while len(G.nodes) > index:
        # #         index+=1
        # #         if est_proche(G,u,v):
        # #             return index 
        # #     return False

import networkx as nx
import json
import random

def json_vers_nx(file_path):
    G = nx.Graph()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            film = json.loads(line)
            cast = [actor.strip("[[").strip("]]") for actor in film["cast"]]
            for i, actor1 in enumerate(cast):
                for actor2 in cast[i+1:]:
                    G.add_edge(actor1, actor2, film=film["title"])
    return G

def centralite(G, u):
    shortest_paths = nx.single_source_dijkstra_path_length(G, u)
    centralite_u = max(shortest_paths.values())
    return centralite_u

def centre_hollywood(G):
    centralites = {acteur: centralite(G, acteur) for acteur in G.nodes()}
    acteur_central = min(centralites, key=centralites.get)
    return acteur_central, centralites[acteur_central]

# Charger le graphe à partir du fichier JSON
graph_films = json_vers_nx("dataTests.txt")

# Afficher les centralités pour certains acteurs
print("centralite:", centralite(graph_films, "Julian Marques"))  # Output: 2
print("centralite:", centralite(graph_films, "Goldie Hawn"))    # Output: 3
print("centralite:", centralite(graph_films, "Carol Kane"))     # Output: 1
