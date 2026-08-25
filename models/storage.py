import json
from models.player import creer_joueur_depuis_dict

def save_players(players):
    liste_de_dicos = []
    for player in players:
        liste_de_dicos.append(player.to_dict())
        
    with open("joueurs.json", "w") as fichier:
        json.dump(liste_de_dicos, fichier)
        
def load_players():
    with open("joueurs.json", "r") as fichier:
        liste_de_dicos = json.load(fichier)
        
    players = []
    for dico in liste_de_dicos:
        players.append(creer_joueur_depuis_dict(dico))
        
    return players