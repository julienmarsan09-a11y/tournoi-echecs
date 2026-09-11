from views.round_view import show_matches

def get_last_name(player):
    return player.last_name

def show_players_report(players):
    print("\n--- Liste des joueurs ---")
    joueurs_tries = sorted(players, key=get_last_name)
    for player in joueurs_tries:
        print(player)

def show_tournaments_report(tournaments):
    print("\n--- Liste des tournois ---")
    for tournament in tournaments:
        print(tournament)

def ask_tournament_name():
    name = input("Nom du tournoi : ")
    return name

def show_tournament_details(tournament):
    print(f"\n--- {tournament.name} ---")
    print(f"Lieu : {tournament.location}")
    print(f"Date de debut : {tournament.start_date}")
    print(f"Date de fin : {tournament.end_date}")

def show_tournament_players_report(tournament):
    print(f"\n--- Joueurs de {tournament.name} ---")
    joueurs_tries = sorted(tournament.players, key=get_last_name)
    for player in joueurs_tries:
        print(player)

def show_tournament_rounds_report(tournament):
    print(f"\n--- Tours et matchs de {tournament.name} ---")
    for round_ in tournament.rounds:
        show_matches(round_)

def show_reports_menu():
    print("\n--- Rapports ---")
    print("1. Liste des joueurs")
    print("2. Liste des tournois")
    print("3. Details d'un tournoi")
    print("4. Liste des joueurs d'un tournoi")
    print("5. Liste des tours et matchs d'un tournoi")
    print("6. Retour au menu principal")
