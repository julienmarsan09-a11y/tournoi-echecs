from models.storage import save_players, load_players
from views.player_view import show_menu
from views.error_view import show_error
from controllers.player_controller import add_player
from controllers.tournament_controller import create_tournament, add_players_to_tournament

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

    print(f"\nNombre de joueurs enregistrés : {len(players)}")
    for player in players:
        print(player)

if __name__ == "__main__":
    main()