#!/usr/bin/python3
#-*-coding:utf-8-*-

data_file_name = 'data/1_Poisy-ParcDesGlaisins.txt'
data_file_name = 'data/2_Piscine-Patinoire_Campus.txt'


try:
    with open(data_file_name, 'r') as f:
        content = f.read()
except OSError:
    # 'File not found' error message.
    print("File not found")

def dates2dic(dates):
    dic = {}
    splitted_dates = dates.split("\n")
    #print(splitted_dates)
    for stop_dates in splitted_dates:
        tmp = stop_dates.split(" ")
        dic[tmp[0]] = tmp[1:]
    return dic
"""
slited_content = content.split("\n\n")
regular_path = slited_content[0]
regular_date_go = dates2dic(slited_content[1])
regular_date_back = dates2dic(slited_content[2])
we_holidays_path = slited_content[3]
we_holidays_date_go = dates2dic(slited_content[4])
we_holidays_date_back = dates2dic(slited_content[5])

"""

#test git



#Test avec 5 arrets
"""   
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

"""