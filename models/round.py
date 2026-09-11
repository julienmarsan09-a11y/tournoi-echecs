from datetime import datetime
from models.player import trouver_joueur_par_id


class Round:

    def __init__(self, name):
        self.name = name
        self.matches = []

        self.start_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        self.end_datetime = None

    def add_match(self, player1, player2):
        match = ([player1, 0], [player2, 0])
        self.matches.append(match)
        return match

    def record_result(self, match, score1, score2):
        joueur1 = match[0][0]
        joueur2 = match[1][0]

        match[0][1] = score1
        match[1][1] = score2

        joueur1.add_points(score1)
        joueur2.add_points(score2)

    def close(self):
        self.end_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def to_dict(self):
        liste_matchs = []
        for match in self.matches:
            joueur1_id = match[0][0].chess_id
            score1 = match[0][1]
            joueur2_id = match[1][0].chess_id
            score2 = match[1][1]
            liste_matchs.append([[joueur1_id, score1], [joueur2_id, score2]])

        return {
            "name": self.name,
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime,
            "matches": liste_matchs,
        }

    def __repr__(self):
        return f"{self.name} - {len(self.matches)} match(s)"


def creer_round_depuis_dict(dictionnaire, players):
    round = Round(dictionnaire["name"])
    round.start_datetime = dictionnaire["start_datetime"]
    round.end_datetime = dictionnaire["end_datetime"]
    for match_dict in dictionnaire["matches"]:
        joueur1 = trouver_joueur_par_id(players, match_dict[0][0])
        score1 = match_dict[0][1]
        joueur2 = trouver_joueur_par_id(players, match_dict[1][0])
        score2 = match_dict[1][1]
        round.matches.append(([joueur1, score1], [joueur2, score2]))

    return round
