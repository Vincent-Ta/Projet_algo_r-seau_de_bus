def changer_string_en_heure(heure_en_string):
    #change une heure en string par un int du nb de min
    if heure_en_string[1]==':':
        return int(heure_en_string[0])*60+int(heure_en_string[2])*10+int(heure_en_string[3])
    elif heure_en_string[2]==':':
        return int(heure_en_string[0])*60*10+int(heure_en_string[1])*60+int(heure_en_string[3])*10+int(heure_en_string[4])
    else : return -1


def comparer_deux_horaires_int(h1,h2):
    #Pour avoir le temps en minute entre deux arrets
    return h1-h2


if __name__=="main":
    s1='6:54'
    s2='23:15'
    s3='000114'

    print(changer_string_en_heure(s1))
    print(changer_string_en_heure(s2))
    print(changer_string_en_heure(s3))