def ask_tournament_info():
    print("\n--- Création d'un tournoi ---")
    name = input("Nom du tournoi : ")
    location = input("Lieu : ")
    start_date = input("Date de début (JJ/MM/AAAA) : ")
    end_date = input("Date de fin (JJ/MM/AAAA) : ")

    return name, location, start_date, end_date

def show_tournament_created(tournament):
    print(f"\nTournoi créé : {tournament}")