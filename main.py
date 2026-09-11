from models.storage import save_players, load_players, save_tournaments, load_tournaments
from views.player_view import show_menu
from views.error_view import show_error
from controllers.player_controller import add_player
from controllers.tournament_controller import create_tournament, add_players_to_tournament
from controllers.round_controller import lancer_round, saisir_resultats, cloturer_round
from controllers.report_controller import afficher_rapports

players = load_players()
tournaments = load_tournaments(players)


def main():
    while True:
        show_menu()
        choice = input("Votre choix : ")

        if choice == "1":
            add_player(players)
        elif choice == "2":
            create_tournament(tournaments)
        elif choice == "3":
            if len(tournaments) == 0:
                show_error("Aucun tournoi n'a ete cree.")
            else:
                add_players_to_tournament(tournaments[-1], players)
        elif choice == "4":
            if len(tournaments) == 0:
                show_error("Aucun tournoi n'a ete cree.")
            else:
                lancer_round(tournaments[-1])
        elif choice == "5":
            if len(tournaments) == 0 or len(tournaments[-1].rounds) == 0:
                show_error("Aucun round en cours.")
            else:
                saisir_resultats(tournaments[-1].rounds[-1])
        elif choice == "6":
            if len(tournaments) == 0 or len(tournaments[-1].rounds) == 0:
                show_error("Aucun round en cours.")
            else:
                cloturer_round(tournaments[-1].rounds[-1])
        elif choice == "7":
            afficher_rapports(players, tournaments)
        elif choice == "8":
            print("\nAu revoir !")
            save_players(players)
            save_tournaments(tournaments)
            break
        else:
            show_error("Choix invalide, réessayez.")

    print(f"\nNombre de joueurs enregistrés : {len(players)}")
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
