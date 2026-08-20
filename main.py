# Ce fichier est le point de depart du programme : c'est lui qu'on lance
# avec "python main.py". Pour l'instant il affiche un menu tout simple
# avec une seule action possible : ajouter un joueur.

from models.player import Player
from datetime import datetime

# Cette liste contient tous les joueurs ajoutes pendant qu'on utilise
# le programme. Attention : pour l'instant rien n'est sauvegarde sur
# le disque, donc si on ferme le programme, la liste est perdue.
# Ce sera regle plus tard, avec la sauvegarde en JSON.
players = []


def show_menu():
    # Cette fonction n'a qu'un role : afficher les choix a l'ecran.
    print("\n--- Menu principal ---")
    print("1. Ajouter un joueur")
    print("2. Quitter")


def add_player():
    # input() met le programme en pause et attend que l'utilisateur
    # tape quelque chose au clavier, puis appuie sur Entree.
    print("\n--- Ajout d'un joueur ---")
    last_name = input("Nom de famille : ")
    first_name = input("Prénom : ")
    while True:
        birth_date = input("Date de naissance (JJ/MM/AAAA) : ")
        try:
            datetime.strptime(birth_date, "%d/%m/%Y")
            break
        except ValueError:
            print("Date invalide, veuillez reessayer.")
    chess_id = input("Identifiant national d'échecs (ex: AB12345) : ")

    # On cree un nouvel objet Player avec les infos saisies...
    player = Player(last_name, first_name, birth_date, chess_id)
    # ...et on l'ajoute a la liste des joueurs de cette session.
    players.append(player)

    print(f"\nJoueur ajouté : {player}")


def main():
    # Une boucle "while True" tourne indefiniment, jusqu'a ce qu'on
    # rencontre un "break" quelque part a l'interieur.
    while True:
        show_menu()
        choice = input("Votre choix : ")

        if choice == "1":
            add_player()
        elif choice == "2":
            print("\nAu revoir !")
            # "break" arrete la boucle while : le programme sort du menu.
            break
        else:
            print("\nChoix invalide, réessayez.")

    # Ce code ne s'execute qu'apres le "break", donc juste avant que
    # le programme se termine : c'est le petit recapitulatif de fin.
    print(f"\nNombre de joueurs ajoutés pendant cette session : {len(players)}")
    for player in players:
        print(player)


# Cette condition est une convention Python : le code a l'interieur
# ne s'execute que si on lance CE fichier directement (python main.py),
# pas si on l'importe depuis un autre fichier.
if __name__ == "__main__":
    main()
