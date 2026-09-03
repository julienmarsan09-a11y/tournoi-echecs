# Ce fichier centralise l'affichage des messages d'erreur.
# Au lieu d'ecrire print("Erreur : ...") a plusieurs endroits differents
# du projet, tous les fichiers appellent cette seule fonction.
# Avantage : si on veut changer la facon d'afficher une erreur plus tard
# (par exemple ajouter un symbole, ou l'ecrire aussi dans un fichier log),
# on ne modifie qu'un seul endroit, pas dix fichiers differents.


def show_error(message):
    print(f"Erreur : {message}")
