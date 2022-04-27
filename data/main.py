from arret_de_bus import *
from shortest import *
from arret_de_bus import *
from fastest import *
from foremost import *

#On renseigne les noms des fichiers
data_file_name1 = 'data/1_Poisy-ParcDesGlaisins.txt'
data_file_name2 = 'data/2_Piscine-Patinoire_Campus.txt'

#On créé le réseau de bus et on ajoute les arrets
r=Reseau_de_bus("Sibra")
creation_arrets(data_file_name1, 'ligne 1', r)
creation_arrets(data_file_name2, 'ligne 2', r)    

#Affichage des arrets
for i in range(len(r.liste_totale_arrets)) :
    print(i, " : ", r.liste_totale_arrets[i].nom)

#On choisit notre arret de départ et notre destination

id_dep=input("Entrez l'id de l'arrêt de départ : ")
id_dest=input("Entrez l'id de l'arrêt d'arrivée : ")
jf=input("Est ce un jour férié ? True si oui, False sinon : ")

dep=r.liste_totale_arrets[int(id_dep)]
dest=r.liste_totale_arrets[int(id_dest)]
heure=input("Entrez l'heure de départ (exemple 10:44) : ")

    
#On exécute l'algorithme qui nous plaît 

#Shortest
"""print("Chemin pour aller de", dep.nom,"à",dest.nom)
affichage_shortest(shortest(r, dep, dest))"""

#Fastest
"""print("Chemin pour aller de", dep.nom,"à",dest.nom)
affichage_fastest(fastest(r, dep, dest))"""

#Foremost
"""print("chemin pour aller de", dep.nom,"à",dest.nom)
affichage_foremost(foremost(r, dep, dest, heure, jf))"""
