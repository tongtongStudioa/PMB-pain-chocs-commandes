# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 13:42:23 2023

@author: axel vaissade
"""


def nb_eleve_par_heure(date : str, heure_pause, minutes_pause, liste_groupes):
    """ Permet d'obtenir le nombre d'élèves présent à une date et à une heure précise.
        La fonction retourne un nombre d'élèves présent à l'heure indiqué (int)
        et un nombre d'élèves qui n'ont pas cours après l'heure indiqué (int) """
        
    presence = {'nombre_eleves_present': 0, 'grande_pause': 0}
    prochain_evenement =0
    
    for groupe in liste_groupes :
        if date not in groupe['evenements']:
            continue
        evenements_du_jour = groupe['evenements'][date]
        for i in range(len(evenements_du_jour)-1):

            # mémorisation du prochain evenement
            prochain_evenement = evenements_du_jour[i+1]
            
            # Convertir horaires de la pause et des cours en minutes totales depuis minuit
            debut_pause = heure_pause * 60 + minutes_pause
            debut_prochain_evenement = prochain_evenement['heure_debut'] * 60 + prochain_evenement['minutes_debut']
            debut_evenement = evenements_du_jour[i]['heure_debut'] * 60 + evenements_du_jour[i]['minutes_debut']
            fin_evenement = evenements_du_jour[i]['heure_fin'] * 60 + evenements_du_jour[i]['minutes_fin']
            
            pas_cours_apres = abs(debut_prochain_evenement - fin_evenement) > 110
            fin_cours_maintenant = abs(debut_pause - debut_evenement) <= 90 and (fin_evenement) <=  debut_pause
            
            if pas_cours_apres and fin_cours_maintenant :
                 presence['grande_pause'] += groupe['effectif']
            
            if fin_cours_maintenant : 
                # regarde si l'evenement débute moins de 90min avant la vente et 
                # et se déroule après la fin de l'evenement, le tout comparer en secondes
                presence['nombre_eleves_present'] += groupe['effectif']
                continue

    return presence