from math import inf
import operator

def shortest(reseau, dep, dest):
    """Algorithme qui trouve le chemin le plus court en nombre d'arcs"""
    #On prend l'arret de départ comme noeud courant et on crée la liste totale d'arrets
    noeud_courant=dep
    liste_tot=reseau.liste_totale_arrets

    #On initialise les listes des arrets que l'on a visité et ceux que l'ont a pas visité (arrets connus et inconnus)
    #On met la distance de l'arret de départ à l'arret de départ à 0
    arrets_connus={noeud_courant.nom:[0,[noeud_courant.nom], ["aucune ligne"]]}
    #On initialise les distances à l'infini
    arrets_inconnus={k.nom:[inf,'',"aucune ligne"] for k in liste_tot if k!=noeud_courant}

    #Pour chaque arret voisin de l'arret de départ, on met la distance de l'arret de départ à 1 et le chemin pour y accéder (arret de depart -> voisin de l'arret de départ)
    for id_voisin in range(len(dep.arrets_voisins)):
        #On ne prend pas en compte la présence de l'arret terminus, qui n'est pas vraiment un voisin
        if dep.arrets_voisins[id_voisin].nom != "terminus":
            arrets_inconnus[dep.arrets_voisins[id_voisin].nom]=[1, dep.nom, dep.ligne[id_voisin]]

    #Tant que l'on a pas visite tous les arrets ou qu'il reste des distances a des arrets infinies (que l'on ne connait pas)
    while arrets_inconnus !=[] and any(arrets_inconnus[k][0]<inf for k in arrets_inconnus):
        noeud_courant=get_new_arret_shortest(arrets_inconnus, liste_tot)#On prend le nouveau noeud courant (celui avec la + petite distance dans les arrets inconnus)
        mise_a_jour_shortest(noeud_courant, arrets_connus, arrets_inconnus, liste_tot)#mise a jour des distances 

    
    return arrets_connus[dest.nom]

def get_new_arret_shortest(arrets_inconnus, liste_tot):
    """Fonction qui permet de choisir le nouveau noeud courant"""
    if arrets_inconnus != []:
        nom_arret=min(arrets_inconnus.items(), key=operator.itemgetter(1))[0] #Permet d'avoir le nom de l'arret qui a la plus petite distance connue
        #On retrouve ensuite l'arret avec son nom
        for i in liste_tot:
            if i.nom==nom_arret:
                return i        
            
def affichage_shortest(chemin):
    """Affichage du chemin le plus court"""
    for i in range(1, len(chemin[1])):
        print("aller à", chemin[1][i], "avec la", chemin[2][i])



#arrets inconnus avec la longueur et l arret precedent
#arret est inconnu
def mise_a_jour_shortest(arret, arrets_connus, arrets_inconnus, liste_tot):
    """Fonction qui permet de mettre à jour les distances des arrets dans les arrets inconnus"""
    #arret est le noeud courant dans la liste des arrets inconnus

    #Si l'arret voisin n'a pas encore été visité, on regarde si sa distance connue avec le départ est inférieur à la distance entre le départ et le noeud courant +1 (car c'est son voisin il n'y a qu'un arc)
    for v in arret.arrets_voisins:
        if v.nom in arrets_inconnus :
           d= arrets_inconnus[arret.nom][0] + 1
           if d<arrets_inconnus[v.nom][0] :
               #Si oui on change sa distance et son chemin
                indice_arret_v=arret.arrets_voisins.index(v)
                arrets_inconnus[v.nom]=[d,arret.nom, arret.ligne[indice_arret_v]]

    #On trouve l'indice du nouveau noeud courant 
    old_arret_nom=arrets_inconnus[arret.nom][1]
    for i in liste_tot :
        if old_arret_nom==i.nom :
            old_arret=i
    indice_arret_v=old_arret.arrets_voisins.index(arret)

    #On ajoute l'arret courant au dictionnaires des arrets connus et on le supprime des arrets inconnus
    arrets_connus[arret.nom]=[arrets_inconnus[arret.nom][0], arrets_connus[arrets_inconnus[arret.nom][1]][1] + [arret.nom], arrets_connus[arrets_inconnus[arret.nom][1]][2] + [old_arret.ligne[indice_arret_v]]]
    del arrets_inconnus[arret.nom]