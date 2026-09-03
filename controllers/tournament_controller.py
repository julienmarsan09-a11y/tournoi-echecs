from models.tournament import Tournament
from views.tournament_view import ask_tournament_info, show_tournament_created

def create_tournament(tournaments):
    name, location, start_date, end_date = ask_tournament_info()
    tournament = Tournament(name, location, start_date, end_date)
    tournaments.append(tournament)
    show_tournament_created(tournament)