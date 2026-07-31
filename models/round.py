"""Modèle représentant un tour (round) d'un tournoi d'échecs."""

from datetime import datetime


class Round:
    """Un tour de tournoi : une liste de matchs, avec une date de début et de fin.

    Attributes:
        name: Nom du tour (ex: "Round 1").
        matches: Liste des matchs du tour.
        start_datetime: Date/heure de début, remplie automatiquement à la création.
        end_datetime: Date/heure de fin, remplie automatiquement à la clôture.
    """

    def __init__(self, name):
        self.name = name
        self.matches = []
        self.start_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.end_datetime = None

    def add_match(self, player1, player2):
        """Crée un match et l'ajoute au tour.

        Conforme aux specs : un match est un tuple de deux listes,
        chacune contenant un joueur et un score (0 au départ).
        """
        match = ([player1, 0], [player2, 0])
        self.matches.append(match)
        return match

    def record_result(self, match, score1, score2):
        """Enregistre le résultat d'un match et met à jour les points des joueurs.

        score1 et score2 valent 1 (victoire), 0.5 (nul) ou 0 (défaite).
        """
        player1, player2 = match[0][0], match[1][0]
        match[0][1] = score1
        match[1][1] = score2
        player1.add_points(score1)
        player2.add_points(score2)

    def close(self):
        """Marque le tour comme terminé et horodate la fin."""
        self.end_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def to_dict(self):
        """Convertit le tour en dictionnaire, pour la sauvegarde JSON.

        On ne sauvegarde que l'identifiant échecs du joueur dans chaque match,
        pas toutes ses infos : elles vivent déjà dans la base des joueurs.
        """
        return {
            "name": self.name,
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime,
            "matches": [
                [[match[0][0].chess_id, match[0][1]], [match[1][0].chess_id, match[1][1]]]
                for match in self.matches
            ],
        }

    def __repr__(self):
        return f"{self.name} - {len(self.matches)} match(s) - terminé : {self.end_datetime is not None}"
