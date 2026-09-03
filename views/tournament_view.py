def ask_tournament_info():
    print("\n--- Création d'un tournoi ---")
    name = input("Nom du tournoi : ")
    location = input("Lieu : ")
    start_date = input("Date de début (JJ/MM/AAAA) : ")
    end_date = input("Date de fin (JJ/MM/AAAA) : ")

    return name, location, start_date, end_date

def show_tournament_created(tournament):
    print(f"\nTournoi créé : {tournament}")
    
def ask_chess_id_to_add():
    chess_id = input("Identifiant du joueur a ajouter (ou 'fin' pour arreter) :")
    return chess_id

def show_player_added_to_tournament(player):
    print(f"\n{player} a ete ajoute au tournoi")