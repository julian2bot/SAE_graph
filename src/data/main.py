import json
import networkx as nx
import itertools
import re
import matplotlib.pyplot as plt


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

# def extract_actor_name(actor_string):
#     pattern = r'\[\[(.*?)\]\]'
#     match = re.search(pattern, actor_string)
#     if match:
#         return match.group(1) 
#     else:
#         return actor_string
    
def json_vers_nx(file_path):
    G = nx.Graph()
    data_list = txt_to_json(file_path)
    liste_films = json_to_list(data_list)
    for film in liste_films:
        cast = film["cast"]
        # Créer toutes les combinaisons possibles de deux acteurs dans le cast
        actor_combinations = list(itertools.combinations(cast, 2))
        # ajout dans un ensembe tout les tuples:
        #  Ajout arête pour chaque paire d'acteurs dans le cast
        for actor_pair in actor_combinations:
            actor1, actor2 = actor_pair
            # print(actor1, actor2)
            actor1 = actor1.strip("[[").strip("]]")
            actor2 = actor2.strip("[[").strip("]]") 
            # actor1 = extract_actor_name(actor1) 
            # actor2 = extract_actor_name(actor2)
            # print(actor1, actor2)

            G.add_edge(actor1, actor2, film=film["title"])
    return G



# Pour afficher le graph et le sauvegardé en .png

# Créer le graphe à partir des données des films
# graph_films = json_vers_nx(fichier)

# Vous pouvez visualiser le graphe si vous avez Matplotlib installé
# Voici un exemple de code pour le visualiser

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


# Cette fonction distance utilise BFS pour trouver la distance entre deux acteurs u et v dans un graphe G. Sa complexité est O(V + E), ce qui est plus efficace que l'approche naïve précédente.
def distance(G, u, v):
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

def centralite(G,u):
    shortest_paths = nx.shortest_path_length(G, source=u)
    centralite_u = max(shortest_paths.values())
    return centralite_u


def centre_hollywood(G):
    centralites = {acteur: centralite(G, acteur) for acteur in G.nodes()}
    acteur_central = min(centralites, key=centralites.get)
    return acteur_central, centralites[acteur_central]



# def eloignement_max(G: nx.Graph):
#     # Calcul des distances minimales entre toutes les paires de nœuds
#     distances = nx.floyd_warshall(G)
    
#     # Recherche de la distance maximale dans la matrice des distances
#     max_distance = 0
#     for u, distances_from_u in distances.items():
#         max_distance = max(max_distance, max(distances_from_u.values()))
    
#     return max_distance



def eloignement_max(G: nx.Graph):
    # Calcul des distances minimales entre toutes les paires de nœuds
    distances = nx.floyd_warshall(G)
    
    # Recherche de la distance maximale dans la matrice des distances
    max_distance = 0
    for u, distances_from_u in distances.items():
        max_distance_from_u = max(dist for v, dist in distances_from_u.items() if dist != float('inf'))
        max_distance = max(max_distance, max_distance_from_u)
    
    return max_distance



def lesprints():
    fichier = 'dataTests.txt'

    # fichier = 'datatest.txt'
    # fichier = 'data.txt'
    graph_films = json_vers_nx(fichier)
# print(graph_films)
# Afficher quelques informations sur le graphe
# print("Nombre de nœuds (personnes) :", graph_films.number_of_nodes())
# print("Nombre d'arêtes (relations) :", graph_films.number_of_edges())

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
    # Gcentre= graph_films
    print("centre_hollywood:", centre_hollywood(graph_films) ) 

    print("eloignement_max:", eloignement_max(graph_films) )

lesprints()
# # Q1
# def json_vers_nx(chemin):
#     ...
# # Q2
# def collaborateurs_communs(G,u,v):
#     ...
# # Q3
# def collaborateurs_proches(G,u,k):
#     ...
# def est_proche(G,u,v,k=1):
#     if v in list(G.adj[u]):
#         return True
#     return False
#     ...
# def distance_naive(G,u,v):
#     ...
# def distance(G,u,v):
#     ...
# # Q4
# def centralite(G,u):
#     ...
# def centre_hollywood(G):
#     ...
# # Q5

# def eloignement_max(G:nx.Graph):
#     ...
# # Bonus
# def centralite_groupe(G,S):
#     ...





# def create_set_from_films(file_path):
    
#     res = set()
#     # indezfbhifzehiqdfsnjo=0
#     data_list = txt_to_json(file_path)
#     liste_films = json_to_list(data_list)
#     for film in liste_films:
#         cast = film["cast"]
#         # Créer toutes les combinaisons possibles de deux acteurs dans le cast
#         actor_combinations = list(itertools.combinations(cast, 2))
#         for actor_pair in actor_combinations:
#             actor1, actor2 = actor_pair
#             # print(actor1, actor2)
#             actor1 = extract_actor_name(actor1) 
#             actor2 = extract_actor_name(actor2)
#             res.add((actor1,actor2))
            
#     return res

# print(create_set_from_films(fichier))


# def list_to_txt(entre, ensemble):
#     with open(entre, 'w', encoding='utf-8') as f:
#         f.write(entre)



# import json

# import json

# def txt_to_json(entre, sortie):
#     with open(entre, 'r', encoding='utf-8') as f:
#         data_list = []
#         for line in f:
#             data = json.loads(line)
#             data_list.append(data)

#     with open(sortie, 'w') as f:
#         json.dump(data_list, f, indent=4)

#     print("Fichier modifié avec succès!")
    
#     return data_list

# def json_to_list(fichier):

#     with open(fichier, 'r', encoding='utf-8') as f:
#         data_list = json.load(f)
        
#     liste_films = []
#     for film in data_list:
#         dict_film = {
#             "title": film.get("title", ""),
#             "cast": film.get("cast", []),
#             "directors": film.get("directors", []),
#             "producers": film.get("producers", []),
#             "companies": film.get("companies", []),
#             "year": film.get("year", "")
#         }
#         liste_films.append(dict_film)
    
#     return liste_films

# # Utilisation de la fonction
# fichier = 'data.txt'
# retour = 'nouveau_fichier.json'

# # Convertir le fichier texte en JSON
# donnees = txt_to_json(fichier, retour)
# # Convertir le JSON en liste de dictionnaires
# liste_films = json_to_list(retour)
# print(liste_films)  # Afficher la liste de films











# def txt_to_json(entre, sortie):
#     with open(entre, 'r', encoding='utf-8') as f:
#         data_list = []
#         for line in f:
#             data = json.loads(line)
#             data_list.append(data)
# jsonString = '{ "id": 121, "name": "Naveen", "course": "MERN Stack"}'
 
# # Convert JSON String to Python
# student_details = json.loads(jsonString)
 
# # Print Dictionary
# print(student_details)
 
# # Print values using keys
# print(student_details['name'])
# print(student_details['course'])

# fichier = 'data.txt'
# fichier = 'data.txt'
# retour = 'nouveau_fichier.json'

# def txt_to_json(entre, sortie):
#     with open(entre, 'r', encoding='utf-8') as f:
#         data_list = []
#         for line in f:
#             data = json.loads(line)
#             data_list.append(data)

#     with open(sortie, 'w') as f:
#         json.dump(data_list, f, indent=4)

#     print("Fichier modifié avec succès!")

# # txt_to_json('./data/data.txt', 'nouveau_fichier.json')
# # txt_to_json(fichier, retour )


# def json_to_list(fichier, retour):
#     donnees = txt_to_json(fichier, retour)
#     liste_films = []
#     for film in donnees:
#         print(film["cast"])
#         dict_film = {
#             "title": film["title"],
#             "cast": film["cast"],
#             "directors": film["directors"],
#             "producers": film["producers"],
#             "companies": film["companies"],
#             "year": film["year"]

#         }
#         liste_films.append(dict_film)

    # Affichage de la liste de dictionnaires
#     print(liste_films)
# json_to_list(fichier, retour)


# def lectureJson(fichier):
#     res=0
#     with open(fichier, "r") as f:
#         # print("f"+f)
#         for line in f:
#             # ['title', 'cast', 'directors', 'producers', 'companies', 'year']
#             for i in line:
#                 print("line"+ line)
#                 print("i"+ i)
#                 res+=1
#     print(res)
#             # data = json.loads(line)
#             # data_list.append(data)data = json.load(f)
#             # print(data)

# lectureJson(retour)

# def txt_to_json(entre):
#     data = []
#     dicoCast = dict()
#     setCast = set()

#     with open(entre, 'r', encoding='utf-8') as f:
#         for line in f:
#             tmp = json.loads(line)
#             ret = {}
#             for k,v in tmp.items():

#                 if isinstance(v,list):
#                     ret[k] = [x.strip("[").strip("]") for x in v]
#                     print(ret)
#                 else:
#                      ret[k] = v
#                 print("VVV",k["cast"])
#                 # if v in dicoCast.items:
#                 #     pass
#                 # else:
#                 #     # dicoCast[v]
#                 #     dicoCast[v]
#             print(dicoCast)
#             data.append(ret)
            
#     return data

# txt_to_json(fichier)
# import json
# import networkx

# fichier = "./data/test.txt"


# def txt_to_json(entre, sortie):
#     with open(entre, 'r', encoding='utf-8') as f:
#         data_list = []
#         for line in f:
#             data = json.loads(line)
#             print('data:' + data)
#             data_list.append(data)

#     with open(sortie, 'w') as f:
#         json.dump(data_list, f, indent=4)

#     print("Fichier modifié avec succès!")

# txt_to_json(fichier, 'nouveau_fichier.json')

# def txt_to_json(entre):
#     data = []
#     with open(entre, 'r', encoding='utf-8') as f:
#         for line in f:
#             tmp = json.loads(line)
#             ret = {}
#             for k,v in tmp.items():
#                 if isinstance(v,list):
#                     ret[k] = [x.strip("[").strip("]") for x in v]
#                 else:
#                      ret[k] = v
#             data.append(ret)
#     return data
# def   (data):
#     G = networkx.Graph()
#     # crée table
#     G.add_node("title")
#     G.add_node("cast")
#     G.add_node("directors")
#     G.add_node("producers")
#     G.add_node("companies")
#     G.add_node("year")
# #     # ['title', 'cast', 'directors', 'producers', 'companies', 'year']
#     res = []
#     for index,film in enumerate(data):
#         # print(film)
#         # res.append(film["title"])
#         G.add_edge("title",film["title"])
#         G.add_edge("cast",film["cast"])
#         G.add_edge("directors",film["directors"])
#         G.add_edge("producers",film["producers"])
#         G.add_edge("companies",film["companies"])
#         G.add_edge("year",film["year"])
#     # return res

# data = txt_to_json(fichier)
# print(list_json_vers_graph(data))

    
# def main():
#     print("loading data")
#     data = txt_to_json(fichier)
#     print("building graph")
#     G = list_json_vers_graph(data)

# if __name__ == "__main__":
#     main()
# else:
#     print("SAE imported")






# def distance_naive(G,u,v):
#     index = 0
#     while len(G.nodes) > index:
#         index+=1
#         if est_proche(G,u,v):
#             return index 
#     return False
