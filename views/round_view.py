def show_matches(round):
    print(f"\n--- {round.name} ---")
    
    for match in round.matches:
        joueur1 = match[0][0]
        joueur2 = match[1][0]
        print(f"{joueur1} vs {joueur2}")