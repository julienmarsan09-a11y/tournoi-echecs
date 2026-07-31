"""Script de test manuel des modèles (Player + Round).

Suit exactement l'exemple donné dans l'énoncé de l'étape 1 :
1. créer quelques joueurs ;
2. créer un tour, ajouter les joueurs ;
3. voir comment les joueurs sont associés (points) ;
4. gagner/perdre des matchs de manière aléatoire ;
5. vérifier que les données des modèles sont correctement mises à jour.
"""

import random

from models.player import Player
from models.round import Round

# 1. Créer quelques joueurs
joueurs = [
    Player("Dupont", "Marie", "12/05/1990", "AB12345"),
    Player("Martin", "Paul", "03/11/1985", "CD67890"),
    Player("Bernard", "Julie", "22/01/1998", "EF11223"),
    Player("Petit", "Lucas", "17/09/1992", "GH44556"),
]

print("Joueurs créés :")
for joueur in joueurs:
    print(f"  {joueur}")

# 2. Créer un tour, ajouter les joueurs (par paires : 1v2, 3v4)
round_1 = Round("Round 1")
match_a = round_1.add_match(joueurs[0], joueurs[1])
match_b = round_1.add_match(joueurs[2], joueurs[3])

# 3. Voir comment les joueurs sont associés
print(f"\n{round_1.name} - {len(round_1.matches)} match(s) créés :")
print(f"  Match 1 : {joueurs[0].first_name} vs {joueurs[1].first_name}")
print(f"  Match 2 : {joueurs[2].first_name} vs {joueurs[3].first_name}")

# 4. Gagner/perdre des matchs de manière aléatoire
resultats_possibles = [(1, 0), (0, 1), (0.5, 0.5)]  # victoire / défaite / nul
score_a1, score_a2 = random.choice(resultats_possibles)
score_b1, score_b2 = random.choice(resultats_possibles)

round_1.record_result(match_a, score_a1, score_a2)
round_1.record_result(match_b, score_b1, score_b2)
round_1.close()

# 5. Vérifier que les données sont correctement mises à jour
print(f"\nRésultats du {round_1.name} (clôturé à {round_1.end_datetime}) :")
for joueur in joueurs:
    print(f"  {joueur}")
