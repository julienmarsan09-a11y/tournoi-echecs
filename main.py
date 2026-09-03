# Ce fichier est le point de depart du programme : c'est lui qu'on lance
# avec "python main.py". Pour l'instant il affiche un menu tout simple
# avec une seule action possible : ajouter un joueur.

from models.storage import save_players, load_players
from views.player_view import show_menu
from views.error_view import show_error
from controllers.player_controller import add_player
from controllers.tournament_controller import create_tournament

# Cette liste contient tous les joueurs. Au demarrage, on la recupere
# directement depuis le fichier joueurs.json grace a load_players().
players = load_players()
tournaments = []


def main():
    while True:
        show_menu()
        choice = input("Votre choix : ")

        if choice == "1":
            add_player(players)
        elif choice == "2":
            print("\nAu revoir !")
            save_players(players)
            break
        elif choice == "3":
            create_tournament(tournaments)
        elif choice == "4":
            if len(tournaments) == 0:
                show_error("Aucun tournoi n'a ete cree.")
            else:
                add_players_to_tournament(tournaments[-1], players)
        else:
            show_error("Choix invalide, réessayez.")

    # Ce code ne s'execute qu'apres le "break", donc juste avant que
    # le programme se termine : c'est le petit recapitulatif de fin.
    print(f"\nNombre de joueurs enregistrés : {len(players)}")
    for player in players:
        print(player)


# Cette condition est une convention Python : le code a l'interieur
# ne s'execute que si on lance CE fichier directement (python main.py),
# pas si on l'importe depuis un autre fichier.
if __name__ == "__main__":
    main()