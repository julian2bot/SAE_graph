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
        print("     -Demander l'ensemble des acteurs ayant collaboré avec deux acteurs. Entrer A")
        print("     -Demander l'ensemble des acteurs se trouvant au plus à une certaine distance d'un acteur. Entrer B")
        print("     -Demander la distance séparant un acteur de l'acteur le plus éloigné de lui. Entrer C")
        print("     -Demander l'acteur étant le centre du graphe. Entrer D")
        print("     -Demander la distance entre deux acteurs. Entrer E")
        print("     -Demander l'acteur étant le centre d'un groupe d'acteur. Entrer F")
        print("Pour quitter, entrez Q.")
        demande=input("Quelle opétation voulez vous effectué ?\n")
        match demande:
            case "A":
                acteur1=input("Veuillez entrer le premier acteur.\n")
                acteur2=input("Veuillez entrer le deuxième acteur.\n")
                print("Voici l'ensemble des acteurs collaborant avec "+acteur1+" et "+acteur2)
                print(collaborateurs_communs(G,acteur1,acteur2))
            case "B":
                acteur=input("Veuillez entrer votre acteur.\n")
                ladistance=int(input("Veuillez entrer la distance maximale pour l'analyse.\n"))
                print(collaborateurs_proches(G,acteur,ladistance))
            case "C":
                acteur=input("Veuillez entrer votre acteur.\n")
                print(centralite(G,acteur))
            case "D":
                print(centre_hollywood(G))
            case "E":
                acteur1=input("Veuillez entrer le premier acteur.\n")
                acteur2=input("Veuillez entrer le deuxième acteur.\n")
                print(distance(G,acteur1,acteur2))
            case "F":
                ensemble_acteurs=set(input("Veuiller entrer votre groupe d'acteurs en les écrivants les uns à la suite des autres.\n").split(', '))
                print(ensemble_acteurs)
                print(centralite_groupe(G,ensemble_acteurs))
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
