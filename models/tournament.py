"""Modèle représentant un tournoi d'échecs."""

import random

from models.round import Round


class Tournament:
    """Un tournoi : des joueurs inscrits, qui s'affrontent sur plusieurs tours.

    Attributes:
        name: Nom du tournoi.
        location: Lieu du tournoi.
        start_date: Date de début.
        end_date: Date de fin.
        number_of_rounds: Nombre de tours prévus (4 par défaut).
        current_round: Numéro du tour en cours (0 = pas encore commencé).
        rounds: Liste des tours déjà joués.
        players: Liste des joueurs inscrits.
        description: Remarques générales du directeur du tournoi.
    """

    def __init__(self, name, location, start_date, end_date, number_of_rounds=4, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.current_round = 0
        self.rounds = []
        self.players = []
        self.description = description

    def add_player(self, player):
        """Inscrit un joueur au tournoi."""
        self.players.append(player)

    def is_finished(self):
        """Renvoie True si tous les tours prévus ont été joués."""
        return self.current_round >= self.number_of_rounds

    def _already_played_pairs(self):
        """Reconstruit l'ensemble des paires de joueurs qui se sont déjà
        affrontés, en relisant l'historique des tours déjà joués."""
        played = set()
        for round_ in self.rounds:
            for match in round_.matches:
                player1, player2 = match[0][0], match[1][0]
                played.add(frozenset({player1.chess_id, player2.chess_id}))
        return played

    def _make_pairs(self, players_order):
        """Associe les joueurs deux par deux, en évitant les matchs déjà joués
        quand c'est possible (voir les specs : 'faites au mieux')."""
        already_played = self._already_played_pairs()
        unpaired = list(players_order)
        pairs = []

        while unpaired:
            player1 = unpaired.pop(0)
            opponent_index = 0
            for index, candidate in enumerate(unpaired):
                pair_key = frozenset({player1.chess_id, candidate.chess_id})
                if pair_key not in already_played:
                    opponent_index = index
                    break
            player2 = unpaired.pop(opponent_index)
            pairs.append((player1, player2))

        return pairs

    def start_next_round(self):
        """Démarre le tour suivant : mélange ou trie les joueurs, les associe,
        crée les matchs, et renvoie le nouveau Round."""
        if self.is_finished():
            raise ValueError("Le tournoi est déjà terminé.")

        if not self.rounds:
            # Premier tour : ordre aléatoire, comme demandé dans les specs.
            players_order = list(self.players)
            random.shuffle(players_order)
        else:
            # Tours suivants : tri par points décroissants.
            players_order = sorted(self.players, key=lambda player: player.points, reverse=True)

        pairs = self._make_pairs(players_order)

        new_round = Round(f"Round {self.current_round + 1}")
        for player1, player2 in pairs:
            new_round.add_match(player1, player2)

        self.rounds.append(new_round)
        self.current_round += 1
        return new_round

    def to_dict(self):
        """Convertit le tournoi en dictionnaire, pour la sauvegarde JSON.

        Les joueurs ne sont référencés que par leur identifiant échecs :
        leurs infos complètes vivent dans la base des joueurs, pas ici.
        """
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "description": self.description,
            "players": [player.chess_id for player in self.players],
            "rounds": [round_.to_dict() for round_ in self.rounds],
        }

    def __repr__(self):
        return f"{self.name} - tour {self.current_round}/{self.number_of_rounds} - {len(self.players)} joueur(s)"
