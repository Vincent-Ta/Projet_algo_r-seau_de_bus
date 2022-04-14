def changer_string_en_min(heure_en_string):
    #change une heure en string par un int du nb de min
    if heure_en_string=='-':
        return 0
    elif heure_en_string[1]==':':
        return int(heure_en_string[0])*60+int(heure_en_string[2])*10+int(heure_en_string[3])
    elif heure_en_string[2]==':':
        return int(heure_en_string[0])*60*10+int(heure_en_string[1])*60+int(heure_en_string[3])*10+int(heure_en_string[4])
    else : return -1



def horaire_d_arrivee(dep, dest):
    ligne=dep.ligne[dep.arrets_voisins.index(dest)]
    indice_h=0

    for i in range(len(dest.ligne)):
        if dest.ligne[i]==ligne and dest.arrets_voisins[i]!=dep:
            indice_h=i
    return indice_h

def horaire_depart(dep, dest):
    for i in range(len(dep.arrets_voisins)):
        if dep.arrets_voisins[i]==dest:
            indice_h=i
    return indice_h


def distance_en_min_entre_deux_arrets(dep,dest):
    #Pour avoir le temps en minute entre deux arrets
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



