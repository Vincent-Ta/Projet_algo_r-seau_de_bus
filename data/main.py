from arret_de_bus import *


#On renseigne les noms des fichiers
data_file_name1 = 'data/1_Poisy-ParcDesGlaisins.txt'
data_file_name2 = 'data/2_Piscine-Patinoire_Campus.txt'

#On créé le réseau de bus et on ajoute les arrets
r=Reseau_de_bus("Sibra")
creation_arrets(data_file_name1, 'ligne 1', r)
creation_arrets(data_file_name2, 'ligne 2', r)    

#On choisit notre arret de départ et notre destination
dep=r.liste_totale_arrets[2]
dest=r.liste_totale_arrets[3]
    
#On exécute l'algorithme qui nous plaît 


"""print("chemin pour aller de", dep.nom,"à",dest.nom)
affichage_shortest(shortest(r, dep, dest))"""



"""print("chemin pour aller de", dep.nom,"à",dest.nom)
affichage_fastest(fastest(r, dep, dest))"""


print("chemin pour aller de", dep.nom,"à",dest.nom)
affichage_foremost(foremost(r, dep, dest, '10:44'))