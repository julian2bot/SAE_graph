
# import json
# import networkx as nx
# import itertools
# import re
# import matplotlib.pyplot as plt
# import time
# import cProfile


# def json_vers_nx(chemin_vers_le_fichier_json, affiche= False):
#     G=nx.Graph()
#     with open(chemin_vers_le_fichier_json,"r", encoding='utf-8') as f:
        
#         for dico in f:
            
#             data=json.loads(dico)#liste de dictionnaire
#             # print(len(ens_acteur_parcouru))
#             ens_acteur_parcouru=set()

#             liste_acteurs=data["cast"]
#             taille=len(liste_acteurs)
#             for i in range(taille):
#                 if liste_acteurs[i]not in ens_acteur_parcouru:
#                     ens_acteur_parcouru.add(liste_acteurs[i])
#                     for j in range(taille-i):
#                         G.add_edge(liste_acteurs[i],liste_acteurs[i+j])
#     # print("Il y a "+str(len(ens_acteur_parcouru))+" acteurs.")
#     # affichage_graph(G)
#     return G

# fichier = 'data.txt'

# print(json_vers_nx(fichier))






# # Cadre pour afficher l'image en haut à droite
# image_frame = tk.Frame(root, width=200, height=200, bg="white")
# image_frame.grid(row=0, column=1, padx=10, pady=10)

# # # image_path = r"""C:\Users\marqu\OneDrive\Bureau\SAE graph\src\data\G12.png"""

# # # Création du label pour afficher l'image
# image_label = tk.Label(image_frame)
# image_label.pack()
# def afficher_image():
#     # image_path = mainpy.save_graph(G) 
#     # image_path = fr"{image_path}" # Appel de la fonction save_graph pour obtenir le chemin absolu de l'image
#     global image_frame
#     image_path = r"""C:\Users\marqu\OneDrive\Bureau\SAE graph\src\data\G13.gif"""
#     image = Image.open(image_path)
#     photo = ImageTk.PhotoImage(image)

#     # Créer un widget Label pour afficher l'image
#     label_image = tk.Label(image_frame, image=photo)
#     label_image.pack()
    
    
#     # image_path = r"""C:\Users\marqu\OneDrive\Bureau\SAE graph\src\data\G13.gif""" # Appel de la fonction save_graph pour obtenir le chemin absolu de l'image
    
#     # global photo # Déclaration de la variable photo comme variable globale
#     # try:
#     #     print("image_path  :", image_path)

#     #     photo = PhotoImage(file=image_path)
#     #     print("ici")
#     #     image_label.config(image=photo)
#     #     print("la")
        
#     #     image_label.image = photo  # Nécessaire pour éviter la suppression par le garbage collector
#     # except Exception as e:
#     #     print("Erreur lors de la création de l'image :", e)

#     #     result_label.config(text=e)
#     # Créer un canvas
#     canvas = tk.Canvas(root, width=200, height=200)
#     canvas.grid(row=0, column=1, padx=10, pady=10)

#     # Charger l'image
#     # image_path = r"C:\Users\marqu\OneDrive\Bureau\SAE graph\src\data\G12.png"
#     photo = tk.PhotoImage(file=image_path)

#     # Afficher l'image dans le canvas
#     canvas.create_image(100, 100, image=photo)








# import tkinter as tk
# from PIL import ImageTk, Image

# def afficher_image(chemin_image):
#     # Créer une fenêtre Tkinter
#     fenetre = tk.Tk()
#     fenetre.title("Affichage d'une image")

#     # Charger l'image avec PIL
#     image = Image.open(chemin_image)
#     photo = ImageTk.PhotoImage(image)

#     # Créer un widget Label pour afficher l'image
#     label_image = tk.Label(fenetre, image=photo)
#     label_image.pack()

#     # Exécuter la boucle principale Tkinter
#     fenetre.mainloop()

# # Exemple d'utilisation de la fonction avec le chemin d'une image
# chemin_image = r"""C:\Users\marqu\OneDrive\Bureau\SAE graph\src\data\graph.png""" # Appel de la fonction save_graph pour obtenir le chemin absolu de l'image

# afficher_image(chemin_image)




# import tkinter as tk
# from PIL import ImageTk, Image

# def afficher_image_dans_cadre():
#     chemin_image = r"""C:\Users\marqu\OneDrive\Bureau\SAE graph\src\data\graph.png""" # Appel de la fonction save_graph pour obtenir le chemin absolu de l'image
#     # Charger l'image avec PIL
#     image = Image.open(chemin_image)
#     photo = ImageTk.PhotoImage(image)

#     # Mettre à jour le label avec la nouvelle image

#     image_frame.configure(image=photo)
#     image_frame.image = photo  # Cela permet de garder une référence à l'image et évite la suppression par le garbage collector

# # Créer une fenêtre Tkinter
# root = tk.Tk()
# root.title("Affichage d'une image dans un cadre")

# # Créer le cadre pour afficher l'image en haut à droite
# image_frame = tk.Frame(root, width=200, height=200, bg="white")
# image_frame.grid(row=0, column=1, padx=10, pady=10)

# # Créer le label pour afficher l'image dans le cadre
# image_label = tk.Label(image_frame)
# image_label.pack()

# # Chemin de l'image à afficher

# # Appel de la fonction pour afficher l'image dans le cadre
# afficher_image_dans_cadre()

# # Exécuter la boucle principale Tkinter
# root.mainloop()


import tkinter as tk
from PIL import ImageTk, Image

def afficher_image():
    chemin_image = r"""C:\Users\marqu\OneDrive\Bureau\SAE graph\src\data\G13.gif""" # Appel de la fonction save_graph pour obtenir le chemin absolu de l'image
    # chemin_image = r"""C:\Users\marqu\OneDrive\Images\2C8hCXfv2AAaO2S0CmsqmE.jpg""" # Appel de la fonction save_graph pour obtenir le chemin absolu de l'image

    # Charger l'image avec PIL
    image = Image.open(chemin_image)
    print(image)
    photo = ImageTk.PhotoImage(image)

    # Mettre à jour le label avec la nouvelle image
    image_label.configure(image=photo)
    image_label.image = photo  # Garder une référence à l'image pour éviter sa suppression par le garbage collector

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Affichage d'une image dans un cadre")
# Création de la barre de menu
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Ouvrir")
file_menu.add_separator()
file_menu.add_command(label="Quitter", command=root.quit)
menubar.add_cascade(label="Fichier", menu=file_menu)
root.config(menu=menubar)



# Créer le cadre pour afficher l'image en haut à droite
image_frame = tk.Frame(root, width=200, height=200, bg="white")
image_frame.grid(row=0, column=1, padx=10, pady=10)

# Créer le label pour afficher l'image dans le cadre
image_label = tk.Label(image_frame)
image_label.pack()

# Chemin de l'image à afficher

# Appel de la fonction pour afficher l'image dans le cadre
# afficher_image_dans_cadre()

# Partie gauche avec les champs texte et le bouton
left_frame = tk.Frame(root)
left_frame.grid(row=0, column=0, padx=10, pady=10)
# Bouton "affiché graph"
execute_button = tk.Button(left_frame, text="affiché graph", command=afficher_image)
execute_button.pack()

# afficher_image()

# Exécuter la boucle principale Tkinter
root.mainloop()
