
from horaires import *
import operator
from math import inf


def fastest(reseau, dep, dest):
    """Algorithme qui calcule le chemin le plus court en prenant en compte le temps de trajet entre deux arrets"""
    """Meme principe que pour le shortest mais la distance entre les arrets n'est plus de 1"""
    noeud_courant=dep
    liste_tot=reseau.liste_totale_arrets
    arrets_connus={noeud_courant.nom:[0,[noeud_courant.nom], ["aucune ligne"]]}
    arrets_inconnus={k.nom:[inf,'',"aucune ligne"] for k in liste_tot if k!=noeud_courant}

    for id_voisin in range(len(dep.arrets_voisins)):
        if dep.arrets_voisins[id_voisin].nom != "terminus":
            #On a une distance entre deux arrets donnees par la fonction distance_entre_deux_arrets
            arrets_inconnus[dep.arrets_voisins[id_voisin].nom]=[distance_en_min_entre_deux_arrets(dep, dep.arrets_voisins[id_voisin]), dep.nom, dep.ligne[id_voisin]]

    while arrets_inconnus !=[] and any(arrets_inconnus[k][0]<inf for k in arrets_inconnus):
        noeud_courant=get_new_arret_fastest(arrets_inconnus, liste_tot)
        mise_a_jour_fastest(noeud_courant, arrets_connus, arrets_inconnus, liste_tot)

    print(arrets_connus)
    return arrets_connus[dest.nom]


def mise_a_jour_fastest(arret, arrets_connus, arrets_inconnus, liste_tot):

        for v in arret.arrets_voisins:
            if v.nom in arrets_inconnus :
                #la distance d est la discante de l'arret courant + la distance entre l'arret courant et l'arret initial
                d= arrets_inconnus[arret.nom][0] +  distance_en_min_entre_deux_arrets(arret, v)
               
                if d<arrets_inconnus[v.nom][0] :
                    indice_arret_v=arret.arrets_voisins.index(v)
                    arrets_inconnus[v.nom]=[d,arret.nom, arret.ligne[indice_arret_v]]


        old_arret_nom=arrets_inconnus[arret.nom][1]
        for i in liste_tot :
            if old_arret_nom==i.nom :
                old_arret=i
        indice_arret_v=old_arret.arrets_voisins.index(arret)
        

        arrets_connus[arret.nom]=[arrets_inconnus[arret.nom][0], arrets_connus[arrets_inconnus[arret.nom][1]][1] + [arret.nom], arrets_connus[arrets_inconnus[arret.nom][1]][2] + [old_arret.ligne[indice_arret_v]]]
        del arrets_inconnus[arret.nom]

def affichage_fastest(chemin):
    """Meme principe que l'affichage shortest"""
    for i in range(1, len(chemin[1])):
        print("aller à", chemin[1][i], "avec la", chemin[2][i])

def get_new_arret_fastest(arrets_inconnus, liste_tot):
    """Meme principe que le get_new_arret_shortest"""
    if arrets_inconnus != []:
        nom_arret=min(arrets_inconnus.items(), key=operator.itemgetter(1))[0]
        for i in liste_tot:
            if i.nom==nom_arret:
                return i  