"""Script de test manuel pour la classe Tournament.

Même logique que test_models.py, mais à l'échelle d'un tournoi complet :
1. créer un tournoi et inscrire des joueurs ;
2. lancer le round 1 (ordre aléatoire) ;
3. simuler des résultats et lancer le round 2 (tri par points, pas de revanche) ;
4. vérifier que tout est cohérent.
"""

import random

from models.player import Player
from models.tournament import Tournament

# 1. Créer un tournoi et inscrire 4 joueurs
tournoi = Tournament(
    name="Tournoi de printemps",
    location="Centre échecs",
    start_date="01/09/2026",
    end_date="01/09/2026",
    number_of_rounds=2,
    description="Tournoi de test",
)

joueurs = [
    Player("Dupont", "Marie", "12/05/1990", "AB12345"),
    Player("Martin", "Paul", "03/11/1985", "CD67890"),
    Player("Bernard", "Julie", "22/01/1998", "EF11223"),
    Player("Petit", "Lucas", "17/09/1992", "GH44556"),
]
for joueur in joueurs:
    tournoi.add_player(joueur)

print(f"Tournoi créé : {tournoi}")

# 2. Lancer le round 1
round_1 = tournoi.start_next_round()
print(f"\n{round_1.name} - appariement aléatoire :")
for match in round_1.matches:
    print(f"  {match[0][0].first_name} vs {match[1][0].first_name}")

# Simuler des résultats aléatoires et clôturer le round
resultats_possibles = [(1, 0), (0, 1), (0.5, 0.5)]
for match in round_1.matches:
    score1, score2 = random.choice(resultats_possibles)
    round_1.record_result(match, score1, score2)
round_1.close()

print("\nClassement après le round 1 :")
for joueur in sorted(joueurs, key=lambda j: j.points, reverse=True):
    print(f"  {joueur}")

# 3. Lancer le round 2 : les joueurs sont triés par points, sans revanche
round_2 = tournoi.start_next_round()
print(f"\n{round_2.name} - appariement par points (sans revanche) :")
for match in round_2.matches:
    print(f"  {match[0][0].first_name} vs {match[1][0].first_name}")

for match in round_2.matches:
    score1, score2 = random.choice(resultats_possibles)
    round_2.record_result(match, score1, score2)
round_2.close()

# 4. Vérifier l'état final
print(f"\nTournoi terminé ? {tournoi.is_finished()}")
print("Classement final :")
for joueur in sorted(joueurs, key=lambda j: j.points, reverse=True):
    print(f"  {joueur}")
