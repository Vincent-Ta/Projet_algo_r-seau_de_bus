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
id_dep = input("Entrer le numéro de l'arret de depart : ")
id_dest = input("Entrer le numéro de l'arret d'arrivee : ")
jf = input("Est ce un jour férié (True ou False) ? ")
heure= input("Votre heure de départ ? (exemple : 10h44) ")
dep=r.liste_totale_arrets[int(id_dep)]
dest=r.liste_totale_arrets[int(id_dest)]


    
#On exécute l'algorithme qui nous plaît 
"""print("Chemin pour aller de", dep.nom,"à",dest.nom)
affichage_shortest(shortest(r, dep, dest))"""


"""print("Chemin pour aller de", dep.nom,"à",dest.nom)
affichage_fastest(fastest(r, dep, dest))"""


print("Chemin pour aller de", dep.nom,"à",dest.nom)
affichage_foremost(foremost(r, dep, dest, heure, jf))
