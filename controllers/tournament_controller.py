from models.tournament import Tournament
from models.player import trouver_joueur_par_id
from views.tournament_view import (
    ask_tournament_info,
    show_tournament_created,
    ask_chess_id_to_add,
    show_player_added_to_tournament,
)
from views.error_view import show_error


def create_tournament(tournaments):
    name, location, start_date, end_date = ask_tournament_info()
    tournament = Tournament(name, location, start_date, end_date)
    tournaments.append(tournament)
    show_tournament_created(tournament)


def add_players_to_tournament(tournament, players):
    while True:
        chess_id = ask_chess_id_to_add()
        if chess_id == "fin":
            break

        player = trouver_joueur_par_id(players, chess_id)

        if player is None:
            show_error("Aucun joueur trouve avec cet identifiant.")
        else:
            tournament.add_player(player)
            show_player_added_to_tournament(player)