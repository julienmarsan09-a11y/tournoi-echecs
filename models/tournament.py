"""
Ce fichier contient la classe Tournament (un tournoi).

Un tournoi regroupe des joueurs et plusieurs tours (rounds).
C'est cette classe qui decide comment les joueurs sont associes
a chaque tour, en suivant les regles du cahier des charges.
"""

import random

from models.round import Round


class Tournament:

    def __init__(self, name, location, start_date, end_date, number_of_rounds=4, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds  # 4 tours par defaut, comme demande
        self.current_round = 0  # aucun tour joue pour l'instant
        self.rounds = []
        self.players = []
        self.description = description

    def add_player(self, player):
        self.players.append(player)

    def is_finished(self):
        # Le tournoi est termine quand on a joue tous les tours prevus.
        return self.current_round >= self.number_of_rounds

    def deja_joue_ensemble(self, joueur1, joueur2):
        # Cette methode verifie si deux joueurs se sont deja affrontes,
        # en regardant l'historique de tous les tours deja joues.
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
        # On associe les joueurs deux par deux, dans l'ordre donne,
        # en evitant si possible de refaire un match deja joue.
        joueurs_restants = list(joueurs_dans_l_ordre)
        paires = []

        while len(joueurs_restants) > 0:
            joueur1 = joueurs_restants.pop(0)

            # Par defaut, on prend le premier joueur restant comme adversaire...
            index_adversaire = 0

            # ...mais si un autre joueur n'a pas encore ete affronte, on le prefere.
            for index in range(len(joueurs_restants)):
                adversaire_possible = joueurs_restants[index]
                if not self.deja_joue_ensemble(joueur1, adversaire_possible):
                    index_adversaire = index
                    break

            joueur2 = joueurs_restants.pop(index_adversaire)
            paires.append((joueur1, joueur2))

        return paires

    def get_points(self, player):
        # Petite fonction utilitaire pour trier les joueurs par points.
        # sorted() a besoin qu'on lui dise quelle valeur comparer.
        return player.points

    def start_next_round(self):
        if self.is_finished():
            raise ValueError("Le tournoi est deja termine.")

        if len(self.rounds) == 0:
            # Premier tour : on melange les joueurs au hasard,
            # comme demande dans le cahier des charges.
            joueurs_dans_l_ordre = list(self.players)
            random.shuffle(joueurs_dans_l_ordre)
        else:
            # Tours suivants : on trie les joueurs du plus grand
            # nombre de points au plus petit.
            joueurs_dans_l_ordre = sorted(self.players, key=self.get_points, reverse=True)

        paires = self.creer_les_paires(joueurs_dans_l_ordre)

        nouveau_round = Round(f"Round {self.current_round + 1}")
        for joueur1, joueur2 in paires:
            nouveau_round.add_match(joueur1, joueur2)

        self.rounds.append(nouveau_round)
        self.current_round = self.current_round + 1
        return nouveau_round

    def to_dict(self):
        # On ne garde que l'identifiant des joueurs (chess_id) : leurs infos
        # completes sont deja stockees a part, dans la base des joueurs.
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
