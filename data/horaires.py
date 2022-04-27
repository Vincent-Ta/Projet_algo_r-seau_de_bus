def changer_string_en_min(heure_en_string):
    #change une heure en string par un int du nb de min
    if heure_en_string=='-':
        return 0
    elif heure_en_string[1]==':':
        return int(heure_en_string[0])*60+int(heure_en_string[2])*10+int(heure_en_string[3])
    elif heure_en_string[2]==':':
        return int(heure_en_string[0])*60*10+int(heure_en_string[1])*60+int(heure_en_string[3])*10+int(heure_en_string[4])
    else : return 0



def horaire_d_arrivee(dep, dest):
    """Donne l'indice de l'horaire à utiliser entre deux arrets"""
    ligne=dep.ligne[dep.arrets_voisins.index(dest)]
    indice_h=0

    for i in range(len(dest.ligne)):
        if dest.ligne[i]==ligne and dest.arrets_voisins[i]!=dep:
            indice_h=i
    return indice_h

def horaire_depart(dep, dest):
    """Donne l'indice de l'horaire à utiliser entre deux arrets"""
    for i in range(len(dep.arrets_voisins)):
        if dep.arrets_voisins[i]==dest:
            indice_h=i
    return indice_h


def heure_d_arrivee(arret, arret_suivant, h_depart):
    """calcule l'heure d'arrivee au prochain arret"""
    for i in range(len(arret_suivant.arrets_voisins)):
        if arret_suivant.arrets_voisins[i]!=arret and arret_suivant.ligne[i]==arret.ligne[arret.arrets_voisins.index(arret_suivant)]:
            for j in arret_suivant.horaires[i]:
                if changer_string_en_min(j)>h_depart:
                    return j
 


def temps_d_attente(heure, arret, arret_suivant, jf):    
    """calcule le temps d'attente en min pour que le prochain bus arrive"""
    if arret_suivant.nom=='terminus':
        return 0
    else :
        for i in range(len(arret.horaires[arret.arrets_voisins.index(arret_suivant)])):
            if changer_string_en_min(arret.horaires[arret.arrets_voisins.index(arret_suivant)][i])>=heure:
                """ print('arret.nom', arret.nom)
                print(arret.horaires)
                print(arret.horaires[arret.arrets_voisins.index(arret_suivant)][i])
                print('resultat  :', changer_string_en_min(arret.horaires[arret.arrets_voisins.index(arret_suivant)][i])-heure)"""
                return changer_string_en_min(arret.horaires[arret.arrets_voisins.index(arret_suivant)][i])-heure
        for i in range(len(arret.horaires[arret.arrets_voisins.index(arret_suivant)])):
            if changer_string_en_min(arret.horaires[arret.arrets_voisins.index(arret_suivant)][i])!=0:
                return 24*60-heure+changer_string_en_min(arret.horaires[arret.arrets_voisins.index(arret_suivant)][i])
    




def distance_en_min_entre_deux_arrets(dep,dest):
    #Pour avoir le temps en minute entre deux arrets
    #On prend la premiere horaire valable de la liste pour le depart et la destination et on les soustrait
    iddep=horaire_depart(dep, dest)
    iddest=horaire_d_arrivee(dep,dest)
    h1=changer_string_en_min(dep.horaires[iddep][0])
    h2=changer_string_en_min(dest.horaires[iddest][0])
    cpth1=0 
    
    while h1==0:
        cpth1=cpth1+1
        h1=changer_string_en_min(dep.horaires[iddep][cpth1])
    
    cpth2=0
    while h2==0 :
        cpth2=cpth2+1
        h2=changer_string_en_min(dest.horaires[iddest][cpth2])


    #Cette partie permet de réguler pour le bus à lycee de Poisy qui ne va pas jusquau bout tout le temps
    
    booleen=True
    while booleen:
        if h1<h2:
            if changer_string_en_min(dep.horaires[iddep][cpth1+1])==0:
                while changer_string_en_min(dep.horaires[iddep][cpth1+1])==0:
                    cpth1=cpth1+1
            elif changer_string_en_min(dep.horaires[iddep][cpth1+1])>h2:
                booleen=False
            else : 
                cpth1=cpth1+1
                h1=changer_string_en_min(dep.horaires[iddep][cpth1])
        elif h2<h1 :
            if changer_string_en_min(dest.horaires[iddest][cpth2+1])==0:
                while changer_string_en_min(dest.horaires[iddest][cpth2+1])==0:
                    cpth2=cpth2+1
            elif changer_string_en_min(dest.horaires[iddest][cpth2+1])>h1:
                booleen=False
            else : 
                cpth2=cpth2+1

                h2=changer_string_en_min(dest.horaires[iddest][cpth2])



    if h1>= h2:
        return h1-h2
    else : return h2-h1



