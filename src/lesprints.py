import requetes as API
import networkx as nx
graph_films = API.json_vers_nx("./data/data.txt")

# # Q1
def e():
    # API.affichage_graph(graph_films)
    ...
# # Q2
    print( API.collaborateurs_communs(graph_films, "Jill Whitlow", "Kevin Nealon") )


# # Q3
    print( API.collaborateurs_proches(graph_films,"Adam West",2))

    print( API.est_proche(graph_films,"robert", "Carol Kane",2))
    


    print( API.distance_naive(graph_films,"robert","Goldie Hawn"))



    print( API.distance(graph_films,"robert","Goldie Hawn"))

# # Q4

    print( API.centralite(graph_films,"Goldie Hawn") ,3)
    print( API.centralite(graph_films,"Carol Kane") ,2)



    print( API.centre_hollywood(graph_films))
    # print( API.centre_hollywood(nx.Graph(), API.eloignement_max(graph_films)) ==  ,   ) # print( API.centre_hollywood(graph_films, None) ==  ,   ) 
# # Q5

    print( API.eloignement_max(graph_films ))

# Bonus
    print( API.collaborateurs_proches_Graph(graph_films,"Adam West",2))



e()