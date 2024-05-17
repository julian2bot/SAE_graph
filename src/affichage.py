
import json
import os
import tkinter as tk
from PIL import ImageTk, Image
from APIGraph import *
# import graphdocpython
from matplotlib import pyplot as plt
import networkx as nx
from tkinter import filedialog


#########################################
#########################################
## Vrai Code interface:
#########################################
#########################################
G = nx.Graph()

def on_closing():
    root.destroy()
    root.quit()  


def recuperer_cree_graph():
    filepath = filedialog.askopenfilename()
    global G
    try:
        G = json_vers_nx(filepath) 
        # result = collaborateurs_communs("grah", actor1_data, actor2_data)
        
        # le résultat dans le label
        result_label.config(text=G)
        return G
    except:
        return "Entrer un format valide" 
    
def ouvrir_fichier():
    global G
    G = recuperer_cree_graph()



def afficher_image(chemin=""):
    global G

    # FAIRE POP UP WARNING
    if chemin=="":
        graph = save_graph(G)
        chemin_image = fr"{graph}"
    else:
        G = json_vers_nx(chemin)
        chemin_image = save_graph(G)
        result_label.config(text=G)
    # chemin_image = r"""C:\Users\marqu\OneDrive\Images\2C8hCXfv2AAaO2S0CmsqmE.jpg""" # Appel de la fonction save_graph pour obtenir le chemin absolu de l'image

    # Charger l'image avec PIL
    image = Image.open(chemin_image)
    print(image)
    photo = ImageTk.PhotoImage(image)

    # Mettre à jour le label avec la nouvelle image
    image_label.configure(image=photo)
    image_label.image = photo  # Garder une référence à l'image pour éviter sa suppression par le garbage collector

def executer_collaborateurs_communs():
    # Récupérer les données des champs texte actor1 et actor2
    actor1_data = actor1_entry_commun.get()
    actor2_data = actor2_entry_commun.get()
    # Exécuter la fonction avec les données fournies
    result = collaborateurs_communs(G,actor1_data, actor2_data)
    # Afficher le résultat
    print("colab: ", collaborateurs_communs(G, "Paul Reubens", "Julian Marques"))  # Output: {'Carol Kane'}
    print("colab: ", collaborateurs_communs(G, str(actor1_data),str(actor2_data)))  # Output: {'Carol Kane'}

    res= f"Acteurs communs entre {actor1_data} et {actor2_data} est {result}"

    result_label.config(text=res)

def executer_collaborateurs_proche():
    # Récupérer les données des champs texte actor1 et actor2
    actor1_data = actor1_entryproche.get()
    k = int(distance_entryproche.get())
    # Exécuter la fonction avec les données fournies
    result = collaborateurs_proches(G,actor1_data, k)
    # Afficher le résultat
    # print("colab: ", collaborateurs_communs(G, "Paul Reubens", "Julian Marques"))  # Output: {'Carol Kane'}
    # print("colab: ", collaborateurs_communs(G, str(actor1_data),str(actor2_data)))  # Output: {'Carol Kane'}

    res= f"Acteurs proche de {actor1_data} a une distance de {k} est : {result}"


    result_label.config(text=res)

def executer_collaborateurs_estproche():
    # Récupérer les données des champs texte actor1 et actor2
    actor1_data = actor1_entry_estproche.get()
    actor2_data = actor2_entry_estproche.get()
    k = int(distance_entry_estproche.get())
    # Exécuter la fonction avec les données fournies
    result = est_proche(G,actor1_data,actor2_data, k)
    # Afficher le résultat
    # print("colab: ", collaborateurs_communs(G, "Paul Reubens", "Julian Marques"))  # Output: {'Carol Kane'}
    print("colab: ", est_proche(G, str(actor1_data),str(actor2_data),k))  # Output: {'Carol Kane'}
    
    
    # if none => connais pas cette acteur
    if result:
        res= f"l'acteur {actor1_data} est proche de{actor2_data} (distance: {k})"
    else:
        res= f"l'acteur {actor1_data} est pas proche de {actor2_data} à une  distance de {k}"


    result_label.config(text=res)

def executer_distance():
    # Récupérer les données des champs texte actor1 et actor2
    actor1_data = actor1_entry_distance.get()
    actor2_data = actor2_entry_distance.get()
    # Exécuter la fonction avec les données fournies
    result = distance(G,actor1_data, actor2_data)
    # Afficher le résultat
    if result == -1:
        res = f"Les acteurs {actor1_data} et {actor2_data} ne sont lié quelque soit la distance"
    res= f"Les acteurs {actor1_data} et {actor2_data} sont separé d'une distance de {result}"


    result_label.config(text=res)

def executer_centralite():
    global G
    # Récupérer les données des champs texte actor1 et actor2
    actor1_data = actor1_entry_centralite.get()
    # Exécuter la fonction avec les données fournies
    result = centralite(G,actor1_data)
    # Afficher le résultat
    res= f"la centralite de l'acteur {actor1_data} est de {result}"

    result_label.config(text=res)

def executer_centra_hollywood():
    global G
    # Exécuter la fonction avec les données fournies
    result = centre_hollywood(G, arthus_sauce(G))
    # Afficher le résultat
    res= f"la centralité d'hollywood est dessigné a l'acteur {result} !"

    result_label.config(text=res)


def executer_eloignement_max():
    global G
    # Exécuter la fonction avec les données fournies
    result = eloignement_max(G)
    # Afficher le résultat
    if result == None:
        res = f"veuillez importer un graph"
    else:
        res= f"L'éloignement maximun dans le graph est entre l'acteur {result[0]} et {result[1]} qui sont séparé d'une distande de {result[2]}"

    result_label.config(text=res)

from tkinterdnd2 import DND_FILES, TkinterDnD

# Creation de la fenetre principal avec le titre, et la barre du menu en haut
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Créer une fenêtre Tkinter
root = TkinterDnD.Tk()
# root.geometry("400x200")

root.title("Affichage d'une image dans un cadre")
# Création de la barre de menu
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Ouvrir",accelerator="Ctrl + O", command=recuperer_cree_graph)
file_menu.add_separator()
file_menu.add_command(label="Quitter",accelerator="Ctrl + Q", command=root.quit)
menubar.add_cascade(label="Fichier", menu=file_menu)
root.config(menu=menubar)


# Raccourcis clavier aux commandes
root.bind_all("<Control-o>", lambda event: recuperer_cree_graph())
root.bind_all("<Control-q>", lambda event: on_closing())
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



# Partie Frame Droite + Label resultat requette => frame afficher graph
"""---------------------------------------------------------------"""
# Créer le cadre pour afficher l'image en haut à droite
image_frame = tk.Frame(root, width=200, height=200, bg="white")
image_frame.grid(row=0, column=1, padx=10, pady=10)

# Créer le label pour afficher l'image dans le cadre
image_label = tk.Label(image_frame)
image_label.pack()

# Zone pour afficher les résultats en dessous de l'image
result_label = tk.Label(image_frame, text="", bg="white")
result_label.pack()



def drop(event):
    print('filepath')

    filepath = event.data
    # recuperer_cree_graph(filepath)
    print(f"filepath{filepath}")
    afficher_image(filepath)

# Activer le drop sur le cadre d'image
image_frame.drop_target_register(DND_FILES)
image_frame.dnd_bind('<<Drop>>', drop)
"""---------------------------------------------------------------"""





""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def on_mousewheel(event):
    canvas.yview_scroll(-1 * int(event.delta/120), "units")


# Création du Canvas pour contenir left_frame
canvas = tk.Canvas(root)
canvas.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Création du Scrollbar
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=0, sticky="ns")

# Configurer le Canvas pour utiliser le Scrollbar
canvas.config(yscrollcommand=scrollbar.set)

# Partie Frame Gauche
# Partie gauche avec les champs texte et le bouton
left_frame = tk.Frame(canvas)
left_frame.grid(row=0, column=0, padx=10, pady=10)


canvas.create_window((0, 0), window=left_frame, anchor="nw")

# Config scroll du Canvas
left_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.bind_all("<MouseWheel>", on_mousewheel)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Ou sans canva / scroll bar:
# left_frame = tk.Frame(root)
# left_frame.grid(row=0, column=0, padx=10, pady=10)





# Partie sur la frame de actor communs + bouton execution
"""---------------------------------------------------------------"""
# Titledpane pour les champs texte
actor_frame = tk.LabelFrame(left_frame, text="Acteurs commun")
actor_frame.pack(padx=10, pady=10)

# Champs texte pour actor1 et actor2
actor1_label = tk.Label(actor_frame, text="Actor 1")
actor1_label.pack()
actor1_entry_commun = tk.Entry(actor_frame)
actor1_entry_commun.pack()

actor2_label = tk.Label(actor_frame, text="Actor 2")
actor2_label.pack()
actor2_entry_commun = tk.Entry(actor_frame)
actor2_entry_commun.pack()

# Bouton "Exécuter"
execute_button = tk.Button(left_frame, text="Acteurs commun", command=executer_collaborateurs_communs)
execute_button.pack()

"""---------------------------------------------------------------"""




# Partie sur la frame de actor proche + bouton execution
"""---------------------------------------------------------------"""
# Titledpane pour les champs texte
actor_frame = tk.LabelFrame(left_frame, text="Acteurs proche")
actor_frame.pack(padx=10, pady=10)

# Champs texte pour actor1 et actor2
actor1_label = tk.Label(actor_frame, text="Actor")
actor1_label.pack()
actor1_entryproche = tk.Entry(actor_frame)
actor1_entryproche.pack()

distance_label = tk.Label(actor_frame, text="distance")
distance_label.pack()
distance_entryproche = tk.Entry(actor_frame)
distance_entryproche.pack()

# Bouton "Exécuter"
execute_button = tk.Button(left_frame, text="Acteurs proche", command=executer_collaborateurs_proche)
execute_button.pack()

"""---------------------------------------------------------------"""




# Partie sur la frame de est proche + bouton execution
"""---------------------------------------------------------------"""
# Titledpane pour les champs texte
actor_frame = tk.LabelFrame(left_frame, text="est_proche")
actor_frame.pack(padx=10, pady=10)

# Champs texte pour actor1 et actor2
actor1_label = tk.Label(actor_frame, text="Actor 1")
actor1_label.pack()
actor1_entry_estproche = tk.Entry(actor_frame)
actor1_entry_estproche.pack()

actor1_label = tk.Label(actor_frame, text="Actor 2")
actor1_label.pack()
actor2_entry_estproche = tk.Entry(actor_frame)
actor2_entry_estproche.pack()

distance_label = tk.Label(actor_frame, text="distance")
distance_label.pack()
distance_entry_estproche = tk.Entry(actor_frame)
distance_entry_estproche.pack()

# Bouton "Exécuter"
execute_button = tk.Button(left_frame, text="est proche", command=executer_collaborateurs_estproche)
execute_button.pack()

"""---------------------------------------------------------------"""



# Partie sur la frame de actor communs + bouton execution
"""---------------------------------------------------------------"""
# Titledpane pour les champs texte
actor_frame = tk.LabelFrame(left_frame, text="Distance entre Acteurs")
actor_frame.pack(padx=10, pady=10)

# Champs texte pour actor1 et actor2
actor1_label = tk.Label(actor_frame, text="Actor 1")
actor1_label.pack()
actor1_entry_distance = tk.Entry(actor_frame)
actor1_entry_distance.pack()

actor2_label = tk.Label(actor_frame, text="Actor 2")
actor2_label.pack()
actor2_entry_distance = tk.Entry(actor_frame)
actor2_entry_distance.pack()

# Bouton "Exécuter"
execute_button = tk.Button(left_frame, text="Distance ", command=executer_distance)
execute_button.pack()

"""---------------------------------------------------------------"""




# Partie sur la frame de centralité + bouton execution
"""---------------------------------------------------------------"""
# Titledpane pour les champs texte
actor_frame = tk.LabelFrame(left_frame, text="Centralite Actor")
actor_frame.pack(padx=10, pady=10)

# Champs texte pour actor1 et actor2
actor1_label = tk.Label(actor_frame, text="Actor 1")
actor1_label.pack()
actor1_entry_centralite = tk.Entry(actor_frame)
actor1_entry_centralite.pack()


# Bouton "Exécuter"
execute_button = tk.Button(left_frame, text="centralite ", command=executer_centralite)
execute_button.pack()

"""---------------------------------------------------------------"""




# Partie sur la frame de centralité hollywood + bouton execution
"""---------------------------------------------------------------"""
# Titledpane pour les champs texte
actor_frame = tk.LabelFrame(left_frame, text="Centralitalité hollywood")

# Bouton "Exécuter"
execute_button = tk.Button(left_frame, text="Centralitalité hollywood", command=executer_centra_hollywood)
execute_button.pack()

"""---------------------------------------------------------------"""




# Partie sur la frame de centralité + bouton execution
"""---------------------------------------------------------------"""
# Titledpane pour les champs texte
actor_frame = tk.LabelFrame(left_frame, text="Centralitalité hollywood")

# Bouton "Exécuter"
execute_button = tk.Button(left_frame, text="Eloignement Max ", command=executer_eloignement_max)
execute_button.pack()

"""---------------------------------------------------------------"""



# Sur La Partie Frame Gauche => bouton afficher graph
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Bouton "Afficher graph"
affiche_graph = tk.Button(left_frame, text="Afficher graph", command=afficher_image)
affiche_graph.pack(pady=(20, 0))
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Appel de la fonction pour afficher l'image dans le cadre
afficher_image()


# clique sur la croix de l'app
root.protocol("WM_DELETE_WINDOW", on_closing)


# Exécuter la boucle principale Tkinter
root.mainloop()

