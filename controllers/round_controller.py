from views.round_view import show_matches, ask_match_result, show_round_closed

def lancer_round(tournament):
    round = tournament.start_next_round()
    show_matches(round)
    
def saisir_resultats(round):
    for match in round.matches:
        joueur1 = match[0][0]
        joueur2 = match[1][0]
        score1, score2 = ask_match_result(joueur1, joueur2)
        round.record_result(match, score1, score2)
        
def cloturer_round(round):
    round.close()
    show_round_closed(round)
