
class Arret_de_bus:

    def __init__(self, nom, horaires, arrets_voisins):
        self.nom = nom
        self.dict_horaire = horaires
        # d={"horaires_normales_ligne_1":liste_d'horaires, "horaires_normales_ligne_2":liste_d'horaires}
        self.arrets_voisins = arrets_voisins
        #p={"prochain_arret_ligne_1":arret, "arret_precedent_ligne_1":arret}

    def __str__(self):
        return self.nom

    



if __name__=="__main__":

    '''
    d={"horaires_normales_ligne_1":["10:15", "11:25"]}
    p={"arret_suivant_ligne_1" : "Ponchy"}

    a1=Arret_de_bus("campus", d, p)

    m={"arret_suivant_ligne_1" : a1}

    
    a2=Arret_de_bus("ponchy", d, m) 

    m={"arret_suivant_ligne_1":a1, "arret_precedent_ligne_1":a2}

    a3=Arret_de_bus("France_Barattes", p, m)

    print(a3.arrets_voisins["arret_suivant_ligne_1"].nom)
    '''