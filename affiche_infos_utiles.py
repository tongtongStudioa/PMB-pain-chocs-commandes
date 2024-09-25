# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:10:52 2023

@author: axel
"""
from recuperer_informations_planning import telecharger_calendrier_et_extraire_evenements
from recuperer_nb_eleves_par_heures import obtenir_nombre_eleves_pour_heure_precise_par_classe


def afficher_infos_presence_semaine(liste_dates, horaires, data_classes):
    """ Affiche les infos d'une semaine 
        @param liste_dates liste de dates de la semaine
        @param horaires dictionnaire avec heures et minutes à laquelles on veut les présences
        @data_classes dictionnaire pour savoir le nombre d'étudiants et avoir leurs edt """
        
    infos = f"Semaine du {liste_dates[0]}\n\n"
    infos += "Calcules des présences pour les promos suivantes : \n"
    nb_total_etu = 0
    for classe in data_classes['classes']:
        nb_total_etu += classe['effectif']
        classe['evenements'] = telecharger_calendrier_et_extraire_evenements(
            classe['url_edt'])
        # Trie les evenements par date croissant
        classe['evenements'].sort(key=lambda event: event.begin)
        infos += f"{classe['name']} : {classe['effectif']} étudiants\n"
    infos += f"Nombre d'étudiants total dans les classes : {nb_total_etu}"
    infos += "\n"
    print(infos)
    infos = ""

    for j in range(5):  # 5 jours dans la semaine
        infos += f"{liste_dates[j]}\n"
        # print(liste_dates[j])
        for i in range(len(horaires['heures'])):
            #print(f"heure precise : {horaires['heures'][i]}h{horaires['minutes'][i]}")
            infos_presences = obtenir_nombre_eleves_pour_heure_precise_par_classe(
                liste_dates[j], horaires['heures'][i], horaires['minutes'][i], data_classes['classes'])
            # print()

            infos += f"Pour {horaires['heures'][i]}h{horaires['minutes'][i]}, il y aura approximativement {infos_presences['nombre_eleves_present']} élèves présents.\n"
            if horaires['heures'][i] == "13" or horaires['heures'][i] == "16":
                infos += " N.B : Attention ce sont des heures où les étudiants quittent généralement l'établissement.\n"
        infos += "\n"
    print(infos)
