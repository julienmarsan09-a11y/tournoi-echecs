"""Point d'entrée du programme : menu principal en console.

Pour l'instant le menu ne fait qu'une chose : ajouter un joueur.
On teste petit à petit, une fonctionnalité à la fois, avant d'en ajouter
d'autres (créer un tournoi, lancer un tour, etc.).
"""

from models.player import Player

# Liste des joueurs en mémoire, pour l'instant (pas encore de sauvegarde JSON).
players = []


def show_menu():
    """Affiche les options du menu principal."""
    print("\n--- Menu principal ---")
    print("1. Ajouter un joueur")
    print("2. Quitter")


def add_player():
    """Demande les infos d'un joueur à l'utilisateur et l'ajoute à la liste."""
    print("\n--- Ajout d'un joueur ---")
    last_name = input("Nom de famille : ")
    first_name = input("Prénom : ")
    birth_date = input("Date de naissance (JJ/MM/AAAA) : ")
    chess_id = input("Identifiant national d'échecs (ex: AB12345) : ")

    player = Player(last_name, first_name, birth_date, chess_id)
    players.append(player)

    print(f"\nJoueur ajouté : {player}")


def main():
    """Boucle principale du programme."""
    while True:
        show_menu()
        choice = input("Votre choix : ")

        if choice == "1":
            add_player()
        elif choice == "2":
            print("\nAu revoir !")
            break
        else:
            print("\nChoix invalide, réessayez.")

    print(f"\nNombre de joueurs ajoutés pendant cette session : {len(players)}")
    for player in players:
        print(player)


if __name__ == "__main__":
    main()
