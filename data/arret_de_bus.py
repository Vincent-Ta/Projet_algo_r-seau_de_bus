from horaires import *

class Arret_de_bus:
    '''
    Arrets voisin = [[ligne, arret_suivant, arret_precedent], [ligne, arret_suivant, arret_precedent]]
    Horaires=[[ligne, horaire_suivant, horaire_precedent], [ligne,horaire_suivant, horaire_precedent]]
    Horairesjf=[[ligne, horairejf_suivant, horairejf_pecedent], [ligne, horairejf_suivant, horairejf_precedent]]
    '''

    def __init__(self, nom):
        self.nom = nom
        self.arrets_voisins=[]
        self.horaires=[]
        self.horaires_jf=[]

    def __str__(self):
        return self.nom
   
    def add_arret(self, new_arret):
        if new_arret not in self.arrets_voisins:
            self.arrets_voisins.append(new_arret)
            new_arret.arrets_voisins.append(self)

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

    def dijkstra(self, liste_arrets, destination):
       pass 

    def distance_entre_deux_arrets_adjacents_minutes(self, dest):
            dep=changer_string_en_heure(self.horaires[self.arrets_voisins.index(dest)][0])
            arr=changer_string_en_heure(dest.horaires[dest.arrets_voisins.index(self)][0])
            

if __name__=="__main__":
    #test avec 3 arrets        a1 -> a2 -> a3
    a1=Arret_de_bus("soleil levant")
    a2=Arret_de_bus("cimetierre")
    a3=Arret_de_bus("plessis piquet")
    a4=Arret_de_bus("marche")


    h_sc=["10:10", "11:11"]
    h_cp=["10:13", "11:14"]
    h_pm=["10:16", "11:17"]
    h_ms=["10:19", "11:20"]

    h_pc=["7:16", "13:17"]
    h_cs=["7:19", "13:20"]
    h_sm=["7:22", "13:23"]
    h_mp=["7:25", "13:26"]



    a1.add_arret(a2)
    a2.add_arret(a3)
    a3.add_arret(a4)
    a1.add_arret(a4)

    a1.add_horaire(h_sc)
    a1.add_horaire(h_sm)

    a2.add_horaire(h_cs)
    a2.add_horaire(h_cp)

    a3.add_horaire(h_pc)
    a3.add_horaire(h_pm)

    a4.add_horaire(h_ms)
    a4.add_horaire(h_mp)


    print(a1.distance_entre_deux_arrets_adjacents_minutes(a2))