from operator import contains
from horaires import *
from math import inf
import operator

class Arret_de_bus:
    '''
    Arrets voisin = [[ligne, arret_suivant, arret_precedent], [ligne, arret_suivant, arret_precedent]]
    Horaires=[[ligne, horaire_suivant, horaire_precedent], [ligne,horaire_suivant, horaire_precedent]]
    Horairesjf=[[ligne, horairejf_suivant, horairejf_pecedent], [ligne, horairejf_suivant, horairejf_precedent]]
    '''

    def __init__(self, nom):
        self.nom = nom
        self.arrets_voisins=[]
        self.ligne=[]
        self.horaires=[]
        self.horaires_jf=[]

    def __str__(self):
        return  "arret : " + self.nom
   
    def add_arret(self, new_arret, new_ligne):
        if new_arret not in self.arrets_voisins:
            self.arrets_voisins.append(new_arret)
            new_arret.arrets_voisins.append(self)
            self.ligne.append(new_ligne)
            new_arret.ligne.append(new_ligne)

    def liste_arrets(self, liste=[]):
        if self not in liste:
            liste.append(self)
        for i in self.arrets_voisins:
            if i not in liste:
                i.liste_arrets(liste)
        return liste    

    def add_horaire(self, horaire):
        self.horaires.append(horaire)    

    def add_horaire_jf(self, horaire_jf):
        self.horaires_jf.append(horaire_jf) 
'''
    def distance_entre_deux_arrets_adjacents_minutes(self, dep,  dest):
            dep=changer_string_en_heure(self.horaires[self.arrets_voisins.index(dest)][0])
            dest=changer_string_en_heure(dest.horaires[dest.arrets_voisins.index(self)][0])
'''
#arrets inconnus avec la longueur et l arret precedent
#arret est inconnu
def mise_a_jour_2(arret, arrets_connus, arrets_inconnus, liste_tot):
        #arret est le noeud courant dans la liste des arrets inconnus
        """
        if len(arrets_connus)==1:
            dep=arret
        else : dep=0
        """

        for v in arret.arrets_voisins:
            if v.nom in arrets_inconnus :
               d= arrets_inconnus[arret.nom][0] + 1
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


def shortest(dep, dest):
    noeud_courant=dep
    liste_tot=dep.liste_arrets([])
    arrets_connus={noeud_courant.nom:[0,[noeud_courant.nom], ["aucune ligne"]]}
    arrets_inconnus={k.nom:[inf,'',"aucune ligne"] for k in liste_tot if k!=noeud_courant}
    for id_voisin in range(len(dep.arrets_voisins)):
        arrets_inconnus[dep.arrets_voisins[id_voisin].nom]=[1, dep.nom, dep.ligne[id_voisin]]
    while arrets_inconnus !=[] and any(arrets_inconnus[k][0]<inf for k in arrets_inconnus):
        noeud_courant=get_new_arret_2(arrets_inconnus, liste_tot)
        mise_a_jour_2(noeud_courant, arrets_connus, arrets_inconnus, liste_tot)
    return arrets_connus[dest.nom]


def get_new_arret_2(arrets_inconnus, liste_tot):
    if arrets_inconnus != []:
        nom_arret=min(arrets_inconnus.items(), key=operator.itemgetter(1))[0]
        for i in liste_tot:
            if i.nom==nom_arret:
                return i        

def affichage_shortest(chemin):
    for i in range(1, len(chemin[1])):
        print("aller à", chemin[1][i], "avec la", chemin[2][i])

if __name__=="__main__":
    #test avec 3 arrets        a1 -> a5 -> a2 -> a3 -> a4 -> a1
    a1=Arret_de_bus("soleil levant")
    a2=Arret_de_bus("cimetiere")
    a3=Arret_de_bus("plessis piquet")
    a4=Arret_de_bus("marche")
    a5=Arret_de_bus("theatre")

    h_sc=["10:10", "11:11"]
    h_cp=["10:13", "11:14"]
    h_pm=["10:16", "11:17"]
    h_ms=["10:19", "11:20"]

    h_pc=["7:16", "13:17"]
    h_cs=["7:19", "13:20"]
    h_sm=["7:22", "13:23"]
    h_mp=["7:25", "13:26"]



    a1.add_arret(a5, "ligne 189")
    a5.add_arret(a2, "ligne 189")
    a2.add_arret(a3, "ligne 189")
    a3.add_arret(a4, "ligne 189")
    a1.add_arret(a4, "ligne 189")

    a1.add_horaire(h_sc)
    a1.add_horaire(h_sm)

    a2.add_horaire(h_cs)
    a2.add_horaire(h_cp)

    a3.add_horaire(h_pc)
    a3.add_horaire(h_pm)

    a4.add_horaire(h_ms)
    a4.add_horaire(h_mp)

    a5.add_horaire(h_ms)
    a5.add_horaire(h_mp)


    affichage_shortest(shortest(a1, a3))
