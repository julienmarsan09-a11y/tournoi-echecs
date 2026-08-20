"""
Ce fichier contient la classe Player (un joueur d'echecs).

Un objet Player represente une seule personne inscrite au club.
On utilise une classe plutot qu'un simple dictionnaire parce que
le cahier des charges du projet le demande explicitement.
"""


class Player:

    # Le constructeur : il s'execute automatiquement quand on ecrit Player(...)
    # "self" represente l'objet qu'on est en train de creer.
    def __init__(self, last_name, first_name, birth_date, chess_id):
        self.last_name = last_name      # nom de famille
        self.first_name = first_name    # prenom
        self.birth_date = birth_date    # date de naissance, ex: "12/05/1990"
        self.chess_id = chess_id        # identifiant national d'echecs, ex: "AB12345"

        # Un joueur qui vient d'etre cree n'a encore joue aucun match,
        # donc il commence toujours a 0 point.
        self.points = 0

    def add_points(self, points):
        # Cette methode sert a ajouter des points apres un match.
        # points vaut 1 (victoire), 0.5 (match nul) ou 0 (defaite).
        self.points = self.points + points

    def to_dict(self):
        # JSON ne sait pas ecrire un objet Python directement, seulement
        # des dictionnaires, des listes, des nombres et du texte.
        # Cette methode transforme donc le joueur en dictionnaire.
        joueur_en_dict = {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "points": self.points,
        }
        return joueur_en_dict

    def __repr__(self):
        # Cette methode dit a Python quoi afficher quand on fait
        # print(un_joueur). Sans elle, print afficherait un truc
        # illisible comme <Player object at 0x1234>.
        return f"{self.first_name} {self.last_name} ({self.chess_id}) - {self.points} pts"


def creer_joueur_depuis_dict(dictionnaire):
    # Fonction "inverse" de to_dict : elle prend un dictionnaire
    # (par exemple lu depuis un fichier JSON) et recree un vrai
    # objet Player a partir de ses informations.
    joueur = Player(
        dictionnaire["last_name"],
        dictionnaire["first_name"],
        dictionnaire["birth_date"],
        dictionnaire["chess_id"],
    )
    # .get() renvoie 0 si la cle "points" n'existe pas dans le dictionnaire,
    # au lieu de faire planter le programme.
    joueur.points = dictionnaire.get("points", 0)
    return joueur
