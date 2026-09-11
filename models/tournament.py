import random

from models.round import Round
from models.player import trouver_joueur_par_id
from models.round import creer_round_depuis_dict


class Tournament:

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
        self.players.append(player)

    def is_finished(self):
        return self.current_round >= self.number_of_rounds

    def deja_joue_ensemble(self, joueur1, joueur2):
        for round_deja_joue in self.rounds:
            for match in round_deja_joue.matches:
                adversaire1 = match[0][0]
                adversaire2 = match[1][0]
                meme_ordre = adversaire1 == joueur1 and adversaire2 == joueur2
                ordre_inverse = adversaire1 == joueur2 and adversaire2 == joueur1
                if meme_ordre or ordre_inverse:
                    return True
        return False

    def creer_les_paires(self, joueurs_dans_l_ordre):
        joueurs_restants = list(joueurs_dans_l_ordre)
        paires = []

        while len(joueurs_restants) > 0:
            joueur1 = joueurs_restants.pop(0)

            index_adversaire = 0

            for index in range(len(joueurs_restants)):
                adversaire_possible = joueurs_restants[index]
                if not self.deja_joue_ensemble(joueur1, adversaire_possible):
                    index_adversaire = index
                    break

            joueur2 = joueurs_restants.pop(index_adversaire)
            paires.append((joueur1, joueur2))

        return paires

    def get_points(self, player):
        return player.points

    def start_next_round(self):
        if self.is_finished():
            raise ValueError("Le tournoi est deja termine.")

        if len(self.rounds) == 0:
            joueurs_dans_l_ordre = list(self.players)
            random.shuffle(joueurs_dans_l_ordre)
        else:
            joueurs_dans_l_ordre = sorted(self.players, key=self.get_points, reverse=True)

        paires = self.creer_les_paires(joueurs_dans_l_ordre)

        nouveau_round = Round(f"Round {self.current_round + 1}")
        for joueur1, joueur2 in paires:
            nouveau_round.add_match(joueur1, joueur2)

        self.rounds.append(nouveau_round)
        self.current_round = self.current_round + 1
        return nouveau_round

    def to_dict(self):
        liste_id_joueurs = []
        for player in self.players:
            liste_id_joueurs.append(player.chess_id)

        liste_rounds = []
        for round_ in self.rounds:
            liste_rounds.append(round_.to_dict())

        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "description": self.description,
            "players": liste_id_joueurs,
            "rounds": liste_rounds,
        }

    def __repr__(self):
        return f"{self.name} - tour {self.current_round}/{self.number_of_rounds}"


def creer_tournoi_depuis_dict(dictionnaire, players):
    tournament = Tournament(
        dictionnaire["name"],
        dictionnaire["location"],
        dictionnaire["start_date"],
        dictionnaire["end_date"],
        dictionnaire["number_of_rounds"],
        dictionnaire["description"],
    )
    tournament.current_round = dictionnaire["current_round"]
    for chess_id in dictionnaire["players"]:
        player = trouver_joueur_par_id(players, chess_id)
        tournament.add_player(player)
    for round_dict in dictionnaire["rounds"]:
        tournament.rounds.append(creer_round_depuis_dict(round_dict, players))

    return tournament


def trouver_tournoi_par_nom(tournaments, name):
    for tournament in tournaments:
        if tournament.name == name:
            return tournament
    return None
