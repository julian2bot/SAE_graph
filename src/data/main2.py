# # # # # import json
# # # # # import networkx as nx
# # # # # import itertools
# # # # # import matplotlib.pyplot as plt
# # # # # from multiprocessing import Pool

# # # # # def txt_to_json_batch(entre, batch_size=1000):
# # # # #     with open(entre, 'r', encoding='utf-8') as f:
# # # # #         while True:
# # # # #             batch = []
# # # # #             for _ in range(batch_size):
# # # # #                 line = f.readline()
# # # # #                 if not line:
# # # # #                     break
# # # # #                 try:
# # # # #                     data = json.loads(line)
# # # # #                     batch.append(data)
# # # # #                 except json.JSONDecodeError as e:
# # # # #                     print(f"Erreur de décodage JSON: {e}")
# # # # #             if not batch:
# # # # #                 break
# # # # #             yield batch

# # # # # def json_to_list(data_list):
# # # # #     liste_films = []
# # # # #     for film in data_list:
# # # # #         dict_film = {
# # # # #             "title": film.get("title", ""),
# # # # #             "cast": film.get("cast", []),
# # # # #             "directors": film.get("directors", []),
# # # # #             "producers": film.get("producers", []),
# # # # #             "companies": film.get("companies", []),
# # # # #             "year": film.get("year", "")
# # # # #         }
# # # # #         liste_films.append(dict_film)
# # # # #     return liste_films

# # # # # def create_graph_from_batch(batch):
# # # # #     G = nx.Graph()
# # # # #     for film in batch:
# # # # #         cast = film["cast"]
# # # # #         actor_combinations = list(itertools.combinations(cast, 2))
# # # # #         for actor_pair in actor_combinations:
# # # # #             actor1, actor2 = actor_pair
# # # # #             G.add_edge(actor1, actor2, film=film["title"])
# # # # #     return G

# # # # # def merge_graphs(graphs):
# # # # #     G = nx.Graph()
# # # # #     for G_temp in graphs:
# # # # #         G.add_edges_from(G_temp.edges(data=True))
# # # # #     return G

# # # # # # Chemin vers le fichier JSON contenant les données des films
# # # # # fichier = 'test.txt'

# # # # # # Créer le graphe à partir des données des films en utilisant le traitement par lots
# # # # # graphs = []
# # # # # with Pool() as pool:
# # # # #     for batch in txt_to_json_batch(fichier):
# # # # #         graph = pool.apply(create_graph_from_batch, args=(batch,))
# # # # #         graphs.append(graph)
# # # # # graph_films = merge_graphs(graphs)

# # # # # # Afficher quelques informations sur le graphe
# # # # # print("Nombre de nœuds (personnes) :", graph_films.number_of_nodes())
# # # # # print("Nombre d'arêtes (relations) :", graph_films.number_of_edges())

# # # # # # Afficher le graphe
# # # # # pos = nx.spring_layout(graph_films)
# # # # # nx.draw(graph_films, pos, with_labels=True, node_size=30)
# # # # # plt.show()



# # # # import json
# # # # import networkx as nx
# # # # import itertools

# # # # def txt_to_json(entre):
# # # #     with open(entre, 'r', encoding='utf-8') as f:
# # # #         data_list = []
# # # #         for line in f:
# # # #             data = json.loads(line)
# # # #             data_list.append(data)
# # # #     return data_list

# # # # def create_graph_from_films(file_path):
# # # #     # Créer un graphe non orienté
# # # #     G = nx.Graph()

# # # #     # Charger les données des films depuis le fichier texte
# # # #     data_list = txt_to_json(file_path)

# # # #     # Parcourir chaque film
# # # #     for film in data_list:
# # # #         cast = film["cast"]
        
# # # #         # Créer toutes les combinaisons possibles de deux acteurs dans le cast
# # # #         actor_combinations = list(itertools.combinations(cast, 2))
        
# # # #         # Ajouter une arête pour chaque paire d'acteurs dans le cast
# # # #         for actor_pair in actor_combinations:
# # # #             actor1, actor2 = actor_pair
# # # #             # Ajouter une arête entre les deux acteurs
# # # #             G.add_edge(actor1, actor2, film=film["title"])
    
# # # #     return G

# # # # # Chemin vers le fichier JSON contenant les données des films
# # # # fichier = 'data.txt'

# # # # # Créer le graphe à partir des données des films
# # # # graph_films = create_graph_from_films(fichier)

# # # # # Afficher quelques informations sur le graphe
# # # # print("Nombre de nœuds (personnes) :", graph_films.number_of_nodes())
# # # # print("Nombre d'arêtes (relations) :", graph_films.number_of_edges())

# # # # # Vous pouvez visualiser le graphe si vous avez Matplotlib installé
# # # # # Voici un exemple de code pour le visualiser
# # # # import matplotlib.pyplot as plt
# # # # options = {
# # # #     'with_labels': True,
# # # #     'node_size': 1500,
# # # #     'node_color': "skyblue",
# # # #     'node_shape': "s", 
# # # #     'alpha': 0.5, 
# # # #     'linewidths': 10
# # # # }
# # # # # Décommentez les lignes suivantes pour afficher le graphe
# # # # pos = nx.spring_layout(graph_films)
# # # # nx.draw(graph_films, pos, with_labels=True, node_size=30)
# # # # fig = plt.figure()
# # # # nx.draw(graph_films, **options)
# # # # fig.savefig("G12.png")

# # # # plt.show()


# # # import json
# # # import networkx as nx
# # # import itertools

# # # def txt_to_json(entre):
# # #     with open(entre, 'r', encoding='utf-8') as f:
# # #         data_list = [json.loads(line) for line in f]
# # #     return data_list

# # # def create_graph_from_films(file_path):
# # #     # Créer un graphe non orienté
# # #     G = nx.Graph()

# # #     # Charger les données des films depuis le fichier texte
# # #     data_list = txt_to_json(file_path)

# # #     # Parcourir chaque film
# # #     for film in data_list:
# # #         cast = film["cast"]
        
# # #         # Créer toutes les combinaisons possibles de deux acteurs dans le cast
# # #         actor_combinations = list(itertools.combinations(cast, 2))
        
# # #         # Ajouter une arête pour chaque paire d'acteurs dans le cast
# # #         for actor_pair in actor_combinations:
# # #             actor1, actor2 = actor_pair
# # #             # Ajouter une arête entre les deux acteurs
# # #             G.add_edge(actor1, actor2, film=film["title"])
    
# # #     return G

# # # # Chemin vers le fichier JSON contenant les données des films
# # # fichier = 'data.txt'

# # # # Créer le graphe global à partir des données de tous les films
# # # graph_global = create_graph_from_films(fichier)

# # # # Afficher quelques informations sur le graphe global
# # # print("Nombre de nœuds (personnes) dans le graphe global :", graph_global.number_of_nodes())
# # # print("Nombre d'arêtes (relations) dans le graphe global :", graph_global.number_of_edges())

# # # # Vous pouvez visualiser le graphe global si vous avez Matplotlib installé
# # # # Voici un exemple de code pour le visualiser
# # # import matplotlib.pyplot as plt
# # # options = {
# # #     'with_labels': True,
# # #     'node_size': 1500,
# # #     'node_color': "skyblue",
# # #     'node_shape': "s", 
# # #     'alpha': 0.5, 
# # #     'linewidths': 10
# # # }
# # # # Décommentez les lignes suivantes pour afficher le graphe
# # # pos = nx.spring_layout(graph_global)
# # # nx.draw(graph_global, pos, with_labels=True, node_size=30)
# # # fig = plt.figure()
# # # nx.draw(graph_global, **options)
# # # fig.savefig("graph_global.png")

# # # plt.show()



# # import json
# # import networkx as nx
# # import itertools
# # import matplotlib.pyplot as plt

# # def load_movies_from_file(file_path):
# #     with open(file_path, 'r', encoding='utf-8') as f:
# #         movies = [json.loads(line) for line in f]
# #     return movies

# # def create_actor_graph(movies):
# #     G = nx.Graph()
# #     for movie in movies:
# #         cast = movie["cast"]
# #         for actor_pair in itertools.combinations(cast, 2):
# #             G.add_edge(actor_pair[0], actor_pair[1])
# #     return G

# # # Chemin vers le fichier JSON contenant les données des films
# # fichier = 'nouveau_fichier.json'

# # # Charger les données des films depuis le fichier
# # movies = load_movies_from_file(fichier)

# # # Créer le graphe des relations entre les acteurs
# # actor_graph = create_actor_graph(movies)

# # # Afficher le nombre de nœuds et d'arêtes dans le graphe
# # print("Nombre de nœuds (acteurs) :", actor_graph.number_of_nodes())
# # print("Nombre d'arêtes (relations) :", actor_graph.number_of_edges())

# # # Afficher le graphe
# # pos = nx.spring_layout(actor_graph)
# # plt.figure(figsize=(10, 8))
# # nx.draw(actor_graph, pos, with_labels=True, node_size=50, font_size=8)
# # plt.title("Graphe des relations entre les acteurs")
# # plt.show()



# import json
# import networkx as nx
# import itertools
# import matplotlib.pyplot as plt

# def load_movies_from_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as f:
#         movies = [json.loads(line) for line in f]
#     return movies

# def clean_actor_names(actor):
#     # Supprime les crochets doubles des noms d'acteurs
#     return actor.strip("[]")

# def create_actor_graph(movies):
#     G = nx.Graph()
#     for movie in movies:
#         cast = [clean_actor_names(actor) for actor in movie["cast"]]
#         if cast:  # Vérifie si la liste des acteurs n'est pas vide
#             for actor_pair in itertools.combinations(cast, 2):
#                 G.add_edge(actor_pair[0], actor_pair[1])
#     return G

# # Chemin vers le fichier JSON contenant les données des films
# fichier = 'nouveau_fichier.json'

# # Charger les données des films depuis le fichier
# movies = load_movies_from_file(fichier)

# # Créer le graphe des relations entre les acteurs
# actor_graph = create_actor_graph(movies)

# # Afficher le nombre de nœuds et d'arêtes dans le graphe
# print("Nombre de nœuds (acteurs) :", actor_graph.number_of_nodes())
# print("Nombre d'arêtes (relations) :", actor_graph.number_of_edges())

# # Afficher le graphe
# pos = nx.spring_layout(actor_graph)
# plt.figure(figsize=(10, 8))
# nx.draw(actor_graph, pos, with_labels=True, node_size=50, font_size=8)
# plt.title("Graphe des relations entre les acteurs")
# plt.show()





import json
import networkx as nx
import itertools
import re

def txt_to_json(entre):
    with open(entre, 'r', encoding='utf-8') as f:
        data_list = []
        for line in f:
            data = json.loads(line)
            data_list.append(data)
    return data_list

def json_to_list(data_list):
    liste_films = []
    for film in data_list:
        dict_film = {
            "title": film.get("title", ""),
            "cast": film.get("cast", []),
            "directors": film.get("directors", []),
            "producers": film.get("producers", []),
            "companies": film.get("companies", []),
            "year": film.get("year", "")
        }
        liste_films.append(dict_film)
    return liste_films

def extract_actor_name(actor_string):
    pattern = r'\[\[(.*?)\]\]'
    match = re.search(pattern, actor_string)
    if match:
        return match.group(1) 
    else:
        return actor_string
    

def create_graph_from_films(file_path):
    # Créer un graphe non orienté
    G = nx.Graph()

    # Charger les données des films depuis le fichier texte
    data_list = txt_to_json(file_path)

    # Convertir les données en liste de dictionnaires
    liste_films = json_to_list(data_list)

    # Parcourir chaque film
    for film in liste_films:
        cast = film["cast"]
        
        # Créer toutes les combinaisons possibles de deux acteurs dans le cast
        actor_combinations = list(itertools.combinations(cast, 2))
        
        # Ajouter une arête pour chaque paire d'acteurs dans le cast
        for actor_pair in actor_combinations:
            actor1, actor2 = actor_pair
            print(actor1, actor2)
            actor1 = extract_actor_name(actor1) 
            actor2 = extract_actor_name(actor2)
            print(actor1, actor2)

            G.add_edge(actor1, actor2, film=film["title"])
    
    return G

# Chemin vers le fichier JSON contenant les données des films
# fichier = 'datatest.txt'
fichier = 'test.txt'

# Créer le graphe à partir des données des films
graph_films = create_graph_from_films(fichier)

# Afficher quelques informations sur le graphe
print("Nombre de nœuds (personnes) :", graph_films.number_of_nodes())
print("Nombre d'arêtes (relations) :", graph_films.number_of_edges())

# Vous pouvez visualiser le graphe si vous avez Matplotlib installé
# Voici un exemple de code pour le visualiser
import matplotlib.pyplot as plt
# options = {
#     'with_labels': True,
#     'node_size': 1500,
#     'node_color': "skyblue",
#     'node_shape': "s", 
#     'alpha': 0.5, 
#     'linewidths': 10
# }
# Décommentez les lignes suivantes pour afficher le graphe
pos = nx.spring_layout(graph_films)
# nx.draw(graph_films, pos, with_labels=True, node_size=30)
fig = plt.figure()
nx.draw(graph_films, pos, with_labels=False, node_size=30)
fig.savefig("G13.png")

plt.show()



