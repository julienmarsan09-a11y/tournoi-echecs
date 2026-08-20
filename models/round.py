"""
Ce fichier contient la classe Round (un tour de tournoi).

Un tour contient une liste de matchs, un nom ("Round 1", "Round 2"...),
et deux dates : le debut et la fin du tour.
"""

from datetime import datetime


class Round:

    def __init__(self, name):
        self.name = name
        self.matches = []  # au debut, un tour ne contient encore aucun match

        # On note tout de suite l'heure de creation du tour, comme demande
        # dans le cahier des charges (date de debut remplie automatiquement).
        self.start_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # La date de fin sera remplie plus tard, quand on appellera close().
        # Pour l'instant elle vaut None, ce qui veut dire "pas de valeur".
        self.end_datetime = None

    def add_match(self, player1, player2):
        # D'apres le cahier des charges, un match doit etre stocke comme
        # un tuple de deux listes : chaque liste contient un joueur et son score.
        # Le score commence a 0 pour les deux joueurs.
        match = ([player1, 0], [player2, 0])
        self.matches.append(match)
        return match

    def record_result(self, match, score1, score2):
        # On recupere les deux joueurs du match.
        joueur1 = match[0][0]
        joueur2 = match[1][0]

        # On met a jour le score directement dans le match...
        match[0][1] = score1
        match[1][1] = score2

        # ...et on ajoute aussi les points au total de chaque joueur,
        # sinon le classement du tournoi ne serait jamais a jour.
        joueur1.add_points(score1)
        joueur2.add_points(score2)

    def close(self):
        # On appelle cette methode quand l'utilisateur decide que le tour
        # est termine. C'est a ce moment-la que la date de fin est remplie.
        self.end_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def to_dict(self):
        # Meme principe que pour Player : on transforme le tour en
        # dictionnaire pour pouvoir le sauvegarder en JSON plus tard.
        # On ne garde que l'identifiant du joueur (chess_id), pas toutes
        # ses infos : elles sont deja stockees a part, dans la base des joueurs.
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
