import graphdocpython as graphdocpython
import networkx as nx
graph_films = graphdocpython.json_vers_nx("./data/dataTests.txt")

# # Q1
def test_json_vers_nx():
    graphdocpython.affichage_graph(graph_films)
# # Q2
def test_collaborateurs_communs():
    assert graphdocpython.collaborateurs_communs(graph_films, "Paul Reubens", "Julian Marques") == {'Carol Kane'}
    assert graphdocpython.collaborateurs_communs(graph_films, "Jill Whitlow", "Kevin Nealon") == {'Wallace Langham'}
    assert graphdocpython.collaborateurs_communs(graph_films, "robert", "Julian Marques") == None
    assert graphdocpython.collaborateurs_communs(graph_films, "Paul Reubens", "robert") == None


# # Q3
def test_collaborateurs_proches():
    assert graphdocpython.collaborateurs_proches(graph_films,"Julian Marques",1) == {'Carol Kane', 'Julian Marques'}
    assert graphdocpython.collaborateurs_proches(graph_films,"Julian Marques",2) == {'Judge Reinhold', 'Candice Azzara', 'Kaye Ballard', 'Paul Reubens', 'Eileen Brennan', 'Teri Landrum', 'Eve Arden', 'Carol Kane', 'David L. Lander', "Donald O'Connor", 'Tab Hunter', 'Debralee Scott', 'Tom Smothers', 'Marc McClure', 'Julian Marques', 'Phil Hartman'}
    assert graphdocpython.collaborateurs_proches(graph_films,"rober",2) == None

def test_est_proche():
    assert graphdocpython.est_proche(graph_films,"Julian Marques", "Anthony Michael Hall",1) == False
    assert graphdocpython.est_proche(graph_films,"Julian Marques", "Carol Kane",2) == True
    assert graphdocpython.est_proche(graph_films,"robert", "Carol Kane",2) == None
    assert graphdocpython.est_proche(graph_films,"Julian Marques", "robert",2) == None
    assert graphdocpython.est_proche(graph_films,"Julian Marques", "Anthony Michael Hall",-1) == None
    assert graphdocpython.est_proche(graph_films,"Julian Marques", "Anthony Michael Hall",-101) == None
    
def test_distance_naive():


    assert graphdocpython.distance_naive(graph_films,"Julian Marques","Carol Kane")  == 1
    assert graphdocpython.distance_naive(graph_films,"Julian Marques","Julian Marques")  == 0
    assert graphdocpython.distance_naive(graph_films,"Julian Marques","Anthony Michael Hall" ) == -1 
    assert graphdocpython.distance_naive(graph_films,"Julian Marques","Goldie Hawn")  == 3
    assert graphdocpython.distance_naive(graph_films,"robert","Goldie Hawn")  == -1
    assert graphdocpython.distance_naive(graph_films,"Julian Marques","robert")  == -1


def test_distance():

    assert graphdocpython.distance(graph_films,"Julian Marques","Carol Kane")  == 1
    assert graphdocpython.distance(graph_films,"Julian Marques","Julian Marques")  == 0
    assert graphdocpython.distance(graph_films,"Julian Marques","Anthony Michael Hall" ) == -1 
    assert graphdocpython.distance(graph_films,"Julian Marques","Goldie Hawn")  == 3
    assert graphdocpython.distance(graph_films,"robert","Goldie Hawn")  == -1
    assert graphdocpython.distance(graph_films,"Julian Marques","robert")  == -1

# # Q4
def test_centralite():

    assert graphdocpython.centralite(graph_films,"Julian Marques") ==  3
    assert graphdocpython.centralite(graph_films,"Goldie Hawn") ==  3
    assert graphdocpython.centralite(graph_films,"Carol Kane") ==  2
    assert graphdocpython.centralite(graph_films,"robert") ==  None
    assert graphdocpython.centralite(nx.Graph(),"robert") ==  None

def test_centre_hollywood():

    assert graphdocpython.centre_hollywood(graph_films, graphdocpython.eloignement_max(graph_films)) ==  'Eileen Brennan'
    assert graphdocpython.centre_hollywood(nx.Graph(), graphdocpython.eloignement_max(graph_films)) ==  None
    assert graphdocpython.centre_hollywood(graph_films, None) ==  None
    
# # Q5
# def test_eloignement_max():
# 
#     assert main.eloignement_max(graph_films) == 

# # Bonus
# def centralite_groupe(G,S):
#     ...


