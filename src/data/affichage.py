import tkinter as tk

from PIL import ImageTk, Image
from tkinter import filedialog
import graphdocpython as mainpy
import networkx as nx
G = nx.Graph()  # Initialisation de la variable globale G

def recuperer_cree_graph():
    filepath = filedialog.askopenfilename()
    global G
    try:
        G =  mainpy.json_vers_nx(filepath) 
        # result = collaborateurs_communs("grah", actor1_data, actor2_data)
        
        # le résultat dans le label
        result_label.config(text=G)
        return G
    except:
        return "Entrer un format valide" 
    

def ouvrir_fichier():
    global G
    G = recuperer_cree_graph()

def executer_collaborateurs_communs():
    # Récupérer les données des champs texte actor1 et actor2
    actor1_data = actor1_entry.get()
    actor2_data = actor2_entry.get()
    # Exécuter la fonction avec les données fournies
    result = mainpy.collaborateurs_communs(G,actor1_data, actor2_data)
    # Afficher le résultat
    print("colab: ", mainpy.collaborateurs_communs(G, "Paul Reubens", "Julian Marques"))  # Output: {'Carol Kane'}
    print("colab: ", mainpy.collaborateurs_communs(G, str(actor1_data),str(actor2_data)))  # Output: {'Carol Kane'}

    res= f"Acteurs communs entre {actor1_data} et {actor2_data} est {result}"


    result_label.config(text=res)

# Fonction fictive pour illustrer
def collaborateurs_communs(actor1, actor2):
    # global G
    print("colab: ", mainpy.collaborateurs_communs(G, "Paul Reubens", "Julian Marques"))  # Output: {'Carol Kane'}

    return f"Acteurs communs entre {actor1} et {actor2} est {mainpy.collaborateurs_communs(G, actor1, actor2)}"


# Création de la fenêtre
root = tk.Tk()
root.title("Interface graphique")

# barre de menu
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Ouvrir", command=recuperer_cree_graph)
file_menu.add_separator()
file_menu.add_command(label="Quitter", command=root.quit)
menubar.add_cascade(label="Fichier", menu=file_menu)
root.config(menu=menubar)




# arthur
# Créer le cadre pour afficher l'image en haut à droite
image_frame = tk.Frame(root, width=200, height=200, bg="green")
image_frame.grid(row=0, column=1, padx=10, pady=10)

# Créer le label pour afficher l'image dans le cadre
image_label = tk.Label(image_frame)
image_label.pack()

# canvas_image = tk.Canvas(root, width=200, height=200, bg="white")
# canvas_image.grid(row=0, column=1, padx=10, pady=10)
# canvas_image.pack()


# Zone pour afficher les résultats en dessous de l'image
result_label = tk.Label(image_frame, text="", bg="white")
result_label.pack()


# Partie gauche avec les textefields texte / bouton
frame_bouton = tk.Frame(root)
frame_bouton.grid(row=1, column=0, padx=10, pady=10)

# arthur
def afficher_image():
    global photo, canvas_image
    # chemin_image = r"G13.gif"
    # img = ImageTk.PhotoImage(Image.open(r"C:\Users\marqu\OneDrive\Bureau\SAE graph\src\data\G13.gif"))
    # panel = tk.Label(root, image = img)
    # panel.pack(side = "bottom", fill = "both", expand = "yes")
    
    # image = Image.open(chemin_image)

    # image_tk = ImageTk.PhotoImage(image)

    # # Créer un widget Label pour afficher l'image
    # image_label = tk.Label(left_frame, image=image_tk)
    # image_label.grid(row=1, column=1)

    # task draw img to tk canva
    
    # fichier = tk.PhotoImage(file=chemin_image)
    # canvas_image.create_image(0,0, image=fichier)

    # chemin_image = r"""C:/Users/marqu/OneDrive/Bureau/SAE graph/src/data/graph.png"""
    # if canvas_image is not None:  # Vérifier si canvas_image est initialisé
    #         chemin_image = r"""C:\Users\marqu\OneDrive\Bureau\SAE graph\src\data\G13.gif"""
            # Charger l'image avec PIL
            # print("la")
            # image = Image.open(chemin_image)
            # if image:
            #     print("Image chargée avec succès !")
            # else:
            #     print("Erreur lors du chargement de l'image.")

            # photo = ImageTk.PhotoImage(image)
            # print("laaa")

            # # Supprimer toute image existante dans le canvas
            # canvas_image.delete("all")
            # print("end?")

            # Afficher l'image dans le canvas
            # canvas_image.create_image(0, 0, anchor=tk.NW, image=photo)


    # # Afficher l'image dans le canvas
    # canvas_image.create_image(0, 0, anchor=tk.NW, image=photo)
# afficher_image()

# arthur
# Bouton "afficher graph"
affiche_button = tk.Button(frame_bouton, text="afficher graph", command=afficher_image)
affiche_button.pack()




# Partie gauche avec les champs texte / le bouton
left_frame = tk.Frame(root)
left_frame.grid(row=0, column=0, padx=10, pady=10)

# Titledpane pour les champs texte
actor_frame = tk.LabelFrame(left_frame, text="Acteurs commun")
actor_frame.pack(padx=10, pady=10)

# Champs texte pour actor1 et actor2
actor1_label = tk.Label(actor_frame, text="Actor 1")
actor1_label.pack()
actor1_entry = tk.Entry(actor_frame)
actor1_entry.pack()

actor2_label = tk.Label(actor_frame, text="Actor 2")
actor2_label.pack()
actor2_entry = tk.Entry(actor_frame)
actor2_entry.pack()

# Bouton "Exécuter"
execute_button = tk.Button(left_frame, text="Exécuter", command=executer_collaborateurs_communs)
execute_button.pack()

# def collaborateurs_proches(G,u,k):
# def est_proche(G,u,v,k=1):
# def distance_naive(G,u,v):
# def distance(G,u,v):

# Titledpane pour les champs texte
actor_frame_proche = tk.LabelFrame(left_frame, text="Acteurs proche")
actor_frame_proche.pack(padx=10, pady=10)

# Champs texte pour actor1 et actor2
actor1_label = tk.Label(actor_frame_proche, text="Actor 1")
actor1_label.pack()
actor1_entry = tk.Entry(actor_frame_proche)
actor1_entry.pack()

actor2_label = tk.Label(actor_frame_proche, text="Actor 2")
actor2_label.pack()
actor2_entry = tk.Entry(actor_frame_proche)
actor2_entry.pack()




# afficher_image()


# Lancement de la boucle principale
root.mainloop()
