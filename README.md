# Projet_algo_reseau_de_bus

Le but de ce projet est la représentation d'un réseau de bus en python

Les arrets et le réseau sont représentés dans le fichier arret_de_bus.py

On cherche à connaître le plus court chemin entre 2 arrêts de trois manières différentes :
- the shortest way : on prend le plus court chemin en nombre d'arcs
- the fastest way : on prend le plus court chemin en prenant en compte le poids des arcs (la durée de trajet entre 2 arrêts)
- the foremost way : on choisit une heure de départ et on prend le chemin le plus court en partant à cette heure (en comptant les temps de trajet entre les arrêts et les temps d'attente des bus)


Pour parcourir le graphe composé d'arrêts et trouver le plus court chemin, on utilise l'algorithme de Djikstra.

INITIALISATION:
- On prend l'arrêt de départ comme arrêt courant
- On crée un dictionnaire des arrêts connus contenant l'arrêt de départ avec une distance initialisée à 0 (la distance entre le départ et lui-même).
- On crée un dictionnaire des arrêts inconnus contentant tout les autres arrêts avec leurs distances au départ initialisées à l'infini (on ne les connait pas).
- Pour chaque voisin de l'arrêt de départ, on actualise leur distance à celui-ci

ALGORITHME:
- On regarde les arrêts voisins de l'arrêt courant et on prend comme nouvel arrêt courant le voisin que l'on a pas visité (qui est dans le dictionnaire des arrêts inconnus) qui a la plus petite distance à l'arrêt de départ
- Pour chaque voisin de ce nouvel arrêt courant on regarde si la distance pour arriver à l'arrêt courant + la distance pour aller de l'arrêt courant à son voisin est inférieure à la distance connue entre l'arrêt de départ et ce voisin
- Si oui, on remplace la distance et le chemin par le nouveau chemin
- On recommence l'aalgorithme jusqu'à avoir visité tous les arrêts du réseau

On obtient un dictionnaire d'arrêts connus qui contient tous les arrêts du réseau avec leurs distances et leur chemin (le plus court) depuis l'arrêt de départ

MODE D'EMPLOI:
- Aller dans le fichier main.py
- Enlever les guillemets autour de l'algorithme que vous souhaitez exécuter 
- Une liste d'arrets s'affiche avec leurs numéros
- Rentrez les numéros des arrêts de départ et d'arrivée
- POUR LE FOREMOST : rentrez 'True' si vous souhaitez partir un jour férié, 'False' sinon. Rentrez l'heure de départ sous la forme 'HEURE:MINUTES' (exemple : '10:10')
- Félicitations : le programme vous affiche le trajet à prendre.