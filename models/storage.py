import json
from models.player import creer_joueur_depuis_dict
from models.tournament import creer_tournoi_depuis_dict
from views.error_view import show_error


def save_players(players):
    liste_de_dicos = []
    for player in players:
        liste_de_dicos.append(player.to_dict())

    with open("joueurs.json", "w") as fichier:
        json.dump(liste_de_dicos, fichier)


def load_players():
    try:
        with open("joueurs.json", "r") as fichier:
            liste_de_dicos = json.load(fichier)
        players = []
        for dico in liste_de_dicos:
            players.append(creer_joueur_depuis_dict(dico))

        return players
    except FileNotFoundError:
        show_error("La liste des joueurs n'existe pas")
        return []


def save_tournaments(tournaments):
    liste_de_dicos = []
    for tournament in tournaments:
        liste_de_dicos.append(tournament.to_dict())

    with open("tournois.json", "w") as fichier:
        json.dump(liste_de_dicos, fichier)


def load_tournaments(players):
    try:
        with open("tournois.json", "r") as fichier:
            liste_de_dicos = json.load(fichier)
        tournaments = []
        for dico in liste_de_dicos:
            tournaments.append(creer_tournoi_depuis_dict(dico, players))
        return tournaments
    except FileNotFoundError:
        show_error("La liste des tournois n'existe pas encore")
        return []
