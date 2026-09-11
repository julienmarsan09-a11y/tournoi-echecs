# Tournoi d'échecs

Petit programme en Python, à lancer dans le terminal, pour gérer un tournoi d'échecs : les joueurs, les tournois, les rounds et les matchs, avec sauvegarde automatique.

Ce projet fait partie de ma formation OpenClassrooms "Développeur d'application Python".

## Ce que le programme sait faire

- Ajouter un joueur (nom, prénom, date de naissance, identifiant national d'échecs)
- Créer un tournoi (nom, lieu, dates, nombre de rounds, description)
- Ajouter des joueurs à un tournoi
- Lancer un round (les joueurs sont mélangés au round 1, puis appariés par nombre de points ensuite, sans qu'ils se rejouent deux fois)
- Saisir les résultats des matchs d'un round
- Clôturer un round
- Consulter des rapports : liste des joueurs, liste des tournois, détails d'un tournoi, joueurs d'un tournoi, tours et matchs d'un tournoi
- Sauvegarder et recharger automatiquement les joueurs et les tournois (fichiers `joueurs.json` et `tournois.json`)

## Comment le lancer

Il faut avoir Python installé (version 3).

Depuis le dossier `tournoi_echecs`, lancer :

```
python main.py
```

Un menu s'affiche dans le terminal, avec un numéro à taper pour chaque action.

## Organisation du code

Le projet suit une architecture MVC (Modèle - Vue - Contrôleur) :

- `models/` : les classes qui représentent les données (`Player`, `Tournament`, `Round`) et la sauvegarde JSON (`storage.py`)
- `views/` : tout ce qui affiche des choses à l'écran ou demande une saisie à l'utilisateur
- `controllers/` : le lien entre les modèles et les vues, la logique de chaque action du menu
- `main.py` : le point d'entrée du programme, avec le menu principal

## Outils utilisés

- Python 3
- Le module `json` pour la sauvegarde des données
- `flake8` pour vérifier que le code respecte les conventions de style Python (PEP8)

## Rapport flake8

Le rapport de vérification flake8 (aucune erreur détectée) est disponible dans le dossier `flake8_rapport/`, à ouvrir avec le fichier `index.html`.
