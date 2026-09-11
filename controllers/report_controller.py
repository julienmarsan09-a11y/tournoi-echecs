from views.report_view import (
    show_reports_menu,
    show_players_report,
    show_tournaments_report,
    ask_tournament_name,
    show_tournament_details,
    show_tournament_players_report,
    show_tournament_rounds_report,
)
from views.error_view import show_error
from models.tournament import trouver_tournoi_par_nom


def afficher_rapports(players, tournaments):
    while True:
        show_reports_menu()
        choice = input("Votre choix : ")

        if choice == "1":
            show_players_report(players)
        elif choice == "2":
            show_tournaments_report(tournaments)
        elif choice == "3":
            name = ask_tournament_name()
            tournament = trouver_tournoi_par_nom(tournaments, name)
            if tournament is None:
                show_error("Aucun tournoi trouve avec ce nom.")
            else:
                show_tournament_details(tournament)
        elif choice == "4":
            name = ask_tournament_name()
            tournament = trouver_tournoi_par_nom(tournaments, name)
            if tournament is None:
                show_error("Aucun tournoi trouve avec ce nom.")
            else:
                show_tournament_players_report(tournament)
        elif choice == "5":
            name = ask_tournament_name()
            tournament = trouver_tournoi_par_nom(tournaments, name)
            if tournament is None:
                show_error("Aucun tournoi trouve avec ce nom.")
            else:
                show_tournament_rounds_report(tournament)
        elif choice == "6":
            break
        else:
            show_error("Choix invalide, réessayez.")
