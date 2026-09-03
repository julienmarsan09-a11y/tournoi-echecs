from views.error_view import show_error


def show_menu():
    # Cette fonction n'a qu'un role : afficher les choix a l'ecran.
    print("\n--- Menu principal ---")
    print("1. Ajouter un joueur")
    print("2. Quitter")
    print("3. Créer un tournoi")
    print("4. Ajouter des joueurs au tournoi")


def ask_player_info():
    print("\n--- Ajout d'un joueur ---")
    last_name = input("Nom de famille : ")
    first_name = input("Prénom : ")
    while True:
        birth_date = input("Date de naissance (JJ/MM/AAAA) : ")
        if len(birth_date) == 10 and birth_date[2] == "/" and birth_date[5] == "/":
            break
        else:
            show_error("Format invalide, veuillez reessayer.")
    chess_id = input("Identifiant national d'échecs (ex: AB12345) : ")

    return last_name, first_name, birth_date, chess_id


def show_player_added(player):
    print(f"\nJoueur ajouté : {player}")
