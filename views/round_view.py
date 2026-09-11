def show_matches(round):
    print(f"\n--- {round.name} ---")

    for match in round.matches:
        joueur1 = match[0][0]
        joueur2 = match[1][0]
        print(f"{joueur1} vs {joueur2}")


def ask_match_result(joueur1, joueur2):
    score1 = float(input(f"Score de {joueur1.first_name} {joueur1.last_name} (1 / 0.5 / 0) :"))
    score2 = float(input(f"Score de {joueur2.first_name} {joueur2.last_name} (1 / 0.5 / 0) :"))
    return score1, score2


def show_round_closed(round):
    print(f"\n{round.name} est termine.")
