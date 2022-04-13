from operator import contains
#from horaires import *
from math import inf
import operator

from data2py import dates2dic

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
        if self not in liste and self.nom!='terminus':
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
        if dep.arrets_voisins[id_voisin].nom != "terminus":
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

def creation_arrets(data_file_name):
    try:
        with open(data_file_name, 'r') as f:
            content = f.read()
    except OSError:
    # 'File not found' error message.
        print("File not found")

    slited_content = content.split("\n\n")
    regular_path = slited_content[0]
    regular_date_go = dates2dic(slited_content[1])
    regular_date_back = dates2dic(slited_content[2])
    we_holidays_path = slited_content[3]
    we_holidays_date_go = dates2dic(slited_content[4])
    we_holidays_date_back = dates2dic(slited_content[5])
    
    l_arrets=[]
    terminus=Arret_de_bus("terminus")
 

    for i in range(len(regular_date_go)):
        l_arrets.append(Arret_de_bus(list(regular_date_go.keys())[i]))
    
    for j in range(len(l_arrets)):
        if j==0 :
            l_arrets[j].add_arret(terminus, "linge 1")
            l_arrets[j].add_arret(l_arrets[j+1], "ligne 1")
        elif j==len(l_arrets)-1:
            l_arrets[j].add_arret(terminus, "ligne 1")
        else :
            l_arrets[j].add_arret(l_arrets[j+1], "ligne 1")
        

    for valeur in regular_date_back.values() :
        l_arrets[j].add_horaire(regular_date_back.values())

    for valeur in we_holidays_date_go.values() :
        l_arrets[j].add_horaire_jf(we_holidays_date_go.values())

    return l_arrets

if __name__=="__main__":
    
    data_file_name = 'data/1_Poisy-ParcDesGlaisins.txt'
    data_file_name = 'data/2_Piscine-Patinoire_Campus.txt'
    l_arrets=creation_arrets(data_file_name)

   
    affichage_shortest(shortest(l_arrets[0], l_arrets[11]))
    

    