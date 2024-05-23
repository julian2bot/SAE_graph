import main

graph_films = main.json_vers_nx("dataTests.txt")

# # Q1
def test_json_vers_nx():
    main.affichage_graph(graph_films)
# # Q2
def test_collaborateurs_communs():
    assert main.collaborateurs_communs(graph_films, "Paul Reubens", "Julian Marques") == {'Carol Kane'}


# # Q3
def test_collaborateurs_proches():
    assert main.collaborateurs_proches(graph_films,"Julian Marques",1) == {'Carol Kane', 'Julian Marques'}
    assert main.collaborateurs_proches(graph_films,"Julian Marques",2) == {'Judge Reinhold', 'Candice Azzara', 'Kaye Ballard', 'Paul Reubens', 'Eileen Brennan', 'Teri Landrum', 'Eve Arden', 'Carol Kane', 'David L. Lander', "Donald O'Connor", 'Tab Hunter', 'Debralee Scott', 'Tom Smothers', 'Marc McClure', 'Julian Marques', 'Phil Hartman'}

def test_est_proche():
    assert main.est_proche(graph_films,"Julian Marques", "Anthony Michael Hall",1) == False
    assert main.est_proche(graph_films,"Julian Marques", "Carol Kane",2) == True
    
def test_distance_naive():


    assert main.distance_naive(graph_films,"Julian Marques","Carol Kane")  == 1
    assert main.distance_naive(graph_films,"Julian Marques","Julian Marques")  == 0
    assert main.distance_naive(graph_films,"Julian Marques","Anthony Michael Hall" ) == -1 
    assert main.distance_naive(graph_films,"Julian Marques","Goldie Hawn")  == 3


def test_distance():

    assert main.distance(graph_films,"Julian Marques","Carol Kane")  == 1
    assert main.distance(graph_films,"Julian Marques","Julian Marques")  == 0
    assert main.distance(graph_films,"Julian Marques","Anthony Michael Hall" ) == -1 
    assert main.distance(graph_films,"Julian Marques","Goldie Hawn")  == 3

# # Q4
def test_centralite():

    assert main.centralite(graph_films,"Julian Marques") ==  3
    assert main.centralite(graph_films,"Goldie Hawn") ==  3
    assert main.0(graph_films,"Carol Kane") ==  2

def test_centre_hollywood():

    assert main.centre_hollywood(graph_films) ==  ('Gena Rowlands', 1)
    
# # Q5
# def test_eloignement_max():
# 
#     assert main.eloignement_max(graph_films) == 

# # Bonus
# def centralite_groupe(G,S):
#     ...


