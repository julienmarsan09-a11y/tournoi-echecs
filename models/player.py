class Player:

    def __init__(self, last_name, first_name, birth_date, chess_id):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.chess_id = chess_id

        self.points = 0

    def add_points(self, points):
        self.points = self.points + points

    def to_dict(self):
        joueur_en_dict = {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "points": self.points,
        }
        return joueur_en_dict

    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.chess_id}) - {self.points} pts"


def creer_joueur_depuis_dict(dictionnaire):
    joueur = Player(
        dictionnaire["last_name"],
        dictionnaire["first_name"],
        dictionnaire["birth_date"],
        dictionnaire["chess_id"],
    )
    joueur.points = dictionnaire.get("points", 0)
    return joueur

def trouver_joueur_par_id(players, chess_id):
    for player in players:
        if player.chess_id == chess_id:
            return player
    return None
