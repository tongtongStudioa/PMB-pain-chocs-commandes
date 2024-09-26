# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 13:42:23 2023

@author: axel
"""

# Fonction pour obtenir le nombre d'élèves pour une date et une heure précise
def obtenir_nombre_eleves_pour_heure_precise_par_classe(date : str, heure, minutes, liste_groupes):
    """ Permet d'obtenir le nombre d'élèves présent à une date et à une heure précise.
        La fonction retourne un nombre d'élèves présent à l'heure indiqué (int)
        et un nombre d'élèves qui n'ont pas cours après l'heure indiqué (int) """
        
    presence = {'nombre_eleves_present': 0, 'trou': 0}
    heure_debut_prochain_evenement = 0 
    minutes_debut_prochain_evenement = 0
    
    for groupe in liste_groupes :
        for i in range(len(groupe['evenements'])):  #for i in range(5):
            # Debugage 
            #print(groupe['evenements'][i].name)
            
            # Extraire la date et l'heure de début et de fin de l'événement
            date_debut = groupe['evenements'][i].begin 
            date_fin = groupe['evenements'][i].end 
            
            # Extraire l'heure de début et de fin d'évenement en rajoutant 1h car problème mauvaise heure de l'évenement
            heure_debut = date_debut.hour + 2 # + 2
            heure_fin = date_fin.hour + 2 # + 2
            minutes_debut = date_debut.minute
            minutes_fin = date_fin.minute
            
            
            #print(f"horaire cours : {heure_debut}h{minutes_debut} - {heure_fin}h{minutes_fin}")
            #print(f"date_debut_cours : {date_debut.strftime('%d-%m-%Y')} - date precise : {date}")
            #print("date event == date ? : ",date_debut.strftime('%d-%m-%Y') == date)
            
            pas_cours_apres = abs(heure_debut_prochain_evenement * 60 + minutes_debut_prochain_evenement - (heure_fin * 60 + minutes_fin)) > 110
            fin_cours_maintenant = abs(heure * 60 + minutes - (heure_debut*60 + minutes_debut)) <= 90 and (heure_fin *60 + minutes_fin) <= heure * 60 + minutes
            if date_debut.strftime('%d-%m-%Y') == date:
                #print(date_debut.strftime('%d-%m-%Y'))
                if pas_cours_apres and fin_cours_maintenant :
                     #horaire = f"{heure_fin_dernier_evenement}h{minutes_fin_dernier_evenement} - {heure_debut}h{minutes_debut}"
                     #presence['trous'][i] = {'heure':0}
                     presence['trou'] += groupe['effectif']
                     #print("trou :", presence['trou'], f" avant {heure}h{minutes}")

                # mémorisation de l'heure de fin du prochain evenement
                date_debut_prochain_evenement = groupe['evenements'][i+1].begin
                heure_debut_prochain_evenement = date_debut_prochain_evenement.hour
                minutes_debut_prochain_evenement = date_debut_prochain_evenement.minute
                
                if fin_cours_maintenant : 
                    # regarde si l'evenement débute moins de 2h avant la vente et 
                    # et se déroule après la fin de l'evenement, le tout comparer en secondes
                    presence['nombre_eleves_present'] += groupe['effectif']
                    #print("nb_eleves actualiser = ",presence['nombre_eleves_present'])
                    continue

    return presence