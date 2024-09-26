# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 13:42:23 2023

@author: axel
"""


def nb_eleve_par_heure(date : str, heure_pause, minutes_pause, liste_groupes):
    """ Permet d'obtenir le nombre d'élèves présent à une date et à une heure précise.
        La fonction retourne un nombre d'élèves présent à l'heure indiqué (int)
        et un nombre d'élèves qui n'ont pas cours après l'heure indiqué (int) """
        
    presence = {'nombre_eleves_present': 0, 'trou': 0}
    heure_debut_prochain_evenement = 0 
    minutes_debut_prochain_evenement = 0
    
    for groupe in liste_groupes :
        if date not in groupe['evenements']:
            continue
        evenements_du_jour = groupe['evenements'][date]
        for i in range(len(evenements_du_jour)-1):  #for i in range(5):
                # Extraire la date et l'heure de début et de fin de l'événement
                date_debut = evenements_du_jour[i].begin 
                date_fin = evenements_du_jour[i].end 
                
                # Extraire l'heure de début et de fin d'évenement en rajoutant 2h car problème mauvaise heure de l'évenement
                heure_debut = date_debut.hour + 1 # + 2
                heure_fin = date_fin.hour + 1 # + 2
                minutes_debut = date_debut.minute
                minutes_fin = date_fin.minute
                
                # Convertir heures et minutes en minutes totales 
                debut_pause = heure_pause * 60 + minutes_pause
                debut_prochain_evenement = heure_debut_prochain_evenement * 60 + minutes_debut_prochain_evenement
                debut_evenement = heure_debut*60 + minutes_debut
                fin_evenement = heure_fin * 60 + minutes_fin
                
                pas_cours_apres = abs(debut_prochain_evenement - fin_evenement) > 110
                fin_cours_maintenant = abs(debut_pause - debut_evenement) <= 90 and (fin_evenement) <=  debut_pause
                if pas_cours_apres and fin_cours_maintenant :
                     presence['trou'] += groupe['effectif']
    
                # mémorisation de l'heure de fin du prochain evenement
                date_debut_prochain_evenement = evenements_du_jour[i+1].begin
                heure_debut_prochain_evenement = date_debut_prochain_evenement.hour
                minutes_debut_prochain_evenement = date_debut_prochain_evenement.minute
                
                if fin_cours_maintenant : 
                    # regarde si l'evenement débute moins de 90min avant la vente et 
                    # et se déroule après la fin de l'evenement, le tout comparer en secondes
                    presence['nombre_eleves_present'] += groupe['effectif']
                    continue

    return presence