"""Modèle représentant un joueur d'échecs."""


class Player:
    """Un joueur du club, avec son identifiant national d'échecs.

    Attributes:
        last_name: Nom de famille du joueur.
        first_name: Prénom du joueur.
        birth_date: Date de naissance, au format "JJ/MM/AAAA".
        chess_id: Identifiant national d'échecs (ex: "AB12345").
        points: Nombre de points du joueur dans le tournoi en cours.
    """

    def __init__(self, last_name, first_name, birth_date, chess_id):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        # Au départ d'un tournoi, un joueur n'a aucun point.
        self.points = 0

    def add_points(self, points):
        """Ajoute des points au joueur (1 pour une victoire, 0.5 pour un nul)."""
        self.points += points

    def to_dict(self):
        """Convertit le joueur en dictionnaire, pour la sauvegarde JSON."""
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "points": self.points,
        }

    @classmethod
    def from_dict(cls, data):
        """Recrée un Player à partir d'un dictionnaire (chargement JSON)."""
        player = cls(
            data["last_name"],
            data["first_name"],
            data["birth_date"],
            data["chess_id"],
        )
        player.points = data.get("points", 0)
        return player

    def __repr__(self):
        """Affichage lisible du joueur, pratique pour le débogage (print(player))."""
        return f"{self.first_name} {self.last_name} ({self.chess_id}) - {self.points} pts"
