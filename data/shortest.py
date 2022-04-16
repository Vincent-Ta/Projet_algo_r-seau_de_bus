



def shortest(dep, dest):
    noeud_courant=dep
    liste_tot=dep.liste_arrets([])
    arrets_connus={noeud_courant.nom:[0,[noeud_courant.nom], ["aucune ligne"]]}
    arrets_inconnus={k.nom:[inf,'',"aucune ligne"] for k in liste_tot if k!=noeud_courant}

    for id_voisin in range(len(dep.arrets_voisins)):
        if dep.arrets_voisins[id_voisin].nom != "terminus":
            arrets_inconnus[dep.arrets_voisins[id_voisin].nom]=[1, dep.nom, dep.ligne[id_voisin]]
    while arrets_inconnus !=[] and any(arrets_inconnus[k][0]<inf for k in arrets_inconnus):
        noeud_courant=get_new_arret_2(arrets_inconnus, liste_tot)
    
        mise_a_jour_2(noeud_courant, arrets_connus, arrets_inconnus, liste_tot)
    return arrets_connus[dest.nom]

def meme_nom_dans_la_liste(a, liste):
    b=False
    for i in liste :
        if a.nom==i.nom:
            b=True
    return b

def get_new_arret_2(arrets_inconnus, liste_tot):
    if arrets_inconnus != []:
        nom_arret=min(arrets_inconnus.items(), key=operator.itemgetter(1))[0]


        for i in liste_tot:
            if i.nom==nom_arret:
                return i        
            
def affichage_shortest(chemin):
    for i in range(1, len(chemin[1])):
        print("aller à", chemin[1][i], "avec la", chemin[2][i])

def find_object_and_remove(a, liste):
    
    for i in liste :
        if a.nom==i.nom:
            result=i
            liste.remove(i)
            return result