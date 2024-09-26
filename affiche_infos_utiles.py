# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:10:52 2023

@author: axel
"""
from recuperer_informations_planning import telecharger_calendrier_et_extraire_evenements
from recuperer_nb_eleves_par_heures import nb_eleve_par_heure


def grouper_evenements_par_jour(liste_evenements):
    evenements_par_jour = {}
    for evenement in liste_evenements:
        date = evenement.begin.strftime('%d-%m-%Y')
        if date not in evenements_par_jour:
            evenements_par_jour[date] = []
        evenements_par_jour[date].append(evenement)
    return evenements_par_jour

def récolter_trier_evenements(data_classes):
    # Collecter et trier les événements par classe
    for classe in data_classes['classes']:
        
        classe['evenements'] = telecharger_calendrier_et_extraire_evenements(
            classe['url_edt'])
        
        # Trie les evenements par date croissant
        classe['evenements'].sort(key=lambda event: event.begin)
    return grouper_evenements_par_jour(classe['evenements'])


def generer_rapport(horaires, data_classes):
    """ 
    Affiche les infos d'une semaine 
        
    @param liste_dates liste de dates de la semaine
    @param horaires dictionnaire avec heures et minutes à laquelles on veut les présences
    @data_classes dictionnaire pour savoir le nombre d'étudiants et avoir leurs edt 
    """
        
    # Affichage de la semaine
    infos = "Rapport de présences pour la vente \n\n"
    infos += "Calcules des présences pour les promos suivantes : \n"
    
    nb_total_etu = 0
    for classe in data_classes['classes']:
        nb_total_etu += classe['effectif']
        
        infos += f"{classe['name']} : {classe['effectif']} étudiants\n"
        
    infos += f"Nombre d'étudiants total dans les classes : {nb_total_etu}"
    infos += "\n"
    print(infos) # Imprimer les informations d'introduction
    infos = ""
    
    #Récupére les données depuis les url des calendriers de chaque classes
    evenements_par_jour = récolter_trier_evenements(data_classes)
    for date, evenements_du_jour in evenements_par_jour.items():
        #for j, date in enumerate(liste_dates):  # 5 jours dans la semaine
        infos += presence_etudiants_date(date,horaires, evenements_du_jour, data_classes['classes'])
        if date == "03-10-2024":
            break
    
    
    # Affichage des informations finales
    print(infos)
    #return infos

def presence_etudiants_date(date,horaires,evenements_du_jour, liste_classes):
    # Heures critiques pour notifier des départs
    heures_critiques = [13, 16]
    
    infos = f"Présence pour la date {date} :\n"

    for i in range(len(horaires)):
        heure = horaires[i]['heure']
        minute = horaires[i]['minutes']
        #print(f"heure precise : {horaires['heures'][i]}h{horaires['minutes'][i]}")
        
        infos_presences = nb_eleve_par_heure(date, heure, minute,evenements_du_jour, liste_classes)
        nombre_eleves = infos_presences['nombre_eleves_present']

        infos += f"Pour {heure}h{minute:02d}, il y aura approximativement {nombre_eleves} élèves présents.\n"
        
        # Alerte pour les heures où les étudiants peuvent quitter
        if heure in heures_critiques:
            infos += " N.B : Attention ce sont des heures où les étudiants quittent généralement l'établissement.\n"
    infos += "\n"
    
    return infos








