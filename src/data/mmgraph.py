import json
import networkx as nx
import itertools
import re
import matplotlib.pyplot as plt



def affichage_graph(graph_films):
    pos = nx.spring_layout(graph_films)
    fig = plt.figure()
    nx.draw(graph_films, pos, with_labels=True, node_size=30)
    fig.savefig("G12.png")
    plt.show()
#txt_to_json('data/data.txt', 'nouveau_fichier.json')

#def json_to_nx(chemin_vers_le_fichier_json):
#    G=nx.Graph()
#    with open(chemin_vers_le_fichier_json,"r") as f:
#        data=json.load(f)#liste de dictionnaire
#    print(len(data))
#    for dico in data:
#        liste_acteurs=dico["cast"]
#        taille=len(liste_acteurs)
#        for i in range(taille):
#            for j in range(taille-i):
#                G.add_edge(liste_acteurs[i],liste_acteurs[i+j])
#    affichage_graph(G)
#    return G

def txt_to_json(entre, sortie):
    with open(entre, 'r', encoding='utf-8') as f:
        data_list = []
        for line in f:
            data = json.loads(line)
            data_list.append(data)

    with open(sortie, 'w') as f:
        json.dump(data_list, f, indent=4)

    print("Fichier modifié avec succès!")
    return sortie

def json_to_nx(chemin_vers_le_fichier_json):
    G=nx.Graph()
    with open(chemin_vers_le_fichier_json,"r") as f:
        data=json.load(f)#liste de dictionnaire
        # print(len(f))
    for x in range(10):
        dico=data[x]
        liste_acteurs=dico["cast"]
        taille=len(liste_acteurs)
        for i in range(taille):
            for j in range(taille-i):
                G.add_edge(liste_acteurs[i],liste_acteurs[i+j])
    affichage_graph(G)
    return G


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

        
# print(txt_to_json("dataTests.txt", "dataT.json"))
G=json_to_nx(txt_to_json("data.txt", "dataT.json"))
# G=json_vers_nx('dataTests.txt')
# G=json_vers_nx('data.txt')
print(G)


def collaborateurs_proches(G,acteur,k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    if acteur not in G.nodes():
        print(acteur,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(acteur)
    for i in range(k):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs



# print("colab proche: ", collaborateurs_proches(G,"[[Julian Marques]]",1)) # {'[[Carol Kane]]', '[[Julian Marques]]'}


# def centralite(graph,acteur):
#         taille_collabo=-1
#         ens_collabo=set()
#         distance=0
#         while taille_collabo<len(ens_collabo):
#             distance+=1
#             taille_collabo=len(ens_collabo)
#             ens_collabo=collaborateurs_proches(graph,acteur,distance)
#         return len(ens_collabo)

# print("centralite:", centralite(G,"[[Julian Marques]]") ) # 3
# print("centralite:", centralite(G,"[[Goldie Hawn]]") ) # 3
# print("centralite:", centralite(G,"[[Carol Kane]]") ) # 2

# def centre_hollywood(graph):
#     if len(G.nodes())==0:
#         print("Ce graph est vide")
#         return None
#     liste_acteurs=[]
#     for acteur in G.nodes():
#          liste_acteurs.append(acteur)
#     acteur_min=liste_acteurs[0]
#     taille_min=centralite(G,acteur_min)
#     for acteurs in liste_acteurs:
#          taille= centralite(G,acteurs)
#          if taille<taille_min:
#               taille=taille_min
#               acteur_min=acteurs
#     return acteur_min


# print(centre_hollywood(G)) # ('Gena Rowlands', 1)