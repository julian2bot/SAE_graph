from requetes import *
import platform

def main():
    quitter=False
    bon_chemin=False
    while not bon_chemin:
        chemin_vers_le_fichier_data=input("Veuillez entrez le chemin vers votre fichier à analyser.\n")
        le_bon_chemin=input("Êtes vous sur qu'il s'agit du bon chemin ? Répondez O si oui et N si non.\n")
        if le_bon_chemin=="O":
            bon_chemin=True
    G=json_vers_nx(chemin_vers_le_fichier_data)
    arret=False
    while not arret:
        print("Voici les différentes opération proposée :")
        print("     -Afficher le graphe. Entrez A")
        print("     -Demander le nombre de sommets et d'arrètes du graphe. Entrez B")
        print("     -Demander l'ensemble des acteurs ayant collaboré avec deux acteurs. Entrer C")
        print("     -Demander l'ensemble des acteurs se trouvant au plus à une certaine distance d'un acteur. Entrer D")
        print("     -Demander la distance séparant un acteur de l'acteur le plus éloigné de lui. Entrer E")
        print("     -Demander l'acteur étant le centre du graphe. Entrez F")
        print("     -Demander la distance entre deux acteurs. Entrez G")
        print("     -Demander l'acteur étant le centre d'un groupe d'acteur. Entrez H")
        print("     -Enregister le graphe en tant qu'image. Entrez S")
        print("     -Nettoyer le terminal. Entrez clear")
        print("Pour quitter, entrez Q.")
        demande=input("Quelle opération voulez vous effectué ?\n")
        match demande:
            case "A":
                affichage_graph(G)
            case "B":
                print("Ce graphe contient "+G.number_of_nodes()+" et "+G.number_of_edges()+".")
            case "C":
                acteur1=input("Veuillez entrer le premier acteur.\n")
                acteur2=input("Veuillez entrer le deuxième acteur.\n")
                print("Voici l'ensemble des acteurs collaborant avec "+acteur1+" et "+acteur2)
                print(collaborateurs_communs(G,acteur1,acteur2))
            case "D":
                acteur=input("Veuillez entrer votre acteur.\n")
                ladistance=int(input("Veuillez entrer la distance maximale pour l'analyse.\n"))
                print(collaborateurs_proches(G,acteur,ladistance))
            case "E":
                acteur=input("Veuillez entrer votre acteur.\n")
                print(centralite(G,acteur))
            case "F":
                print(centre_hollywood(G))
            case "G":
                acteur1=input("Veuillez entrer le premier acteur.\n")
                acteur2=input("Veuillez entrer le deuxième acteur.\n")
                print(distance(G,acteur1,acteur2))
            case "H":
                ensemble_acteurs=set(input("Veuiller entrer votre groupe d'acteurs en les écrivants les uns à la suite des autres.\n").split(', '))
                print(ensemble_acteurs)
                print(centralite_groupe(G,ensemble_acteurs))
            case "S":
                nom_image=input("Veuillez entrez le nom de votre image.\n")
                save_graph(G,nom_image)
            case "clear":
                print("Console clear !")
                if platform.system() == "Windows":
                    os.system("cls")
                else:
                    os.system("clear")
            case "Q":
                print("Exit ! Fin du programme, Au revoir")
                arret=True

main()
