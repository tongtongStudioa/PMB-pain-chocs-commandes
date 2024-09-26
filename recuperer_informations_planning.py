# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 13:44:09 2023

@author: La famille tong
"""
import requests
from ics import Calendar


def telecharger_calendrier_et_extraire_evenements(url):
    """  Fonction pour télécharger un calendrier depuis une URL et extraire les événements """
    try:
        response = requests.get(url)
        response.raise_for_status()
        cal = Calendar(response.text)
        evenements = list(cal.events)
        return evenements
    except requests.exceptions.RequestException as e:
        return []
    
def lire_fichier_ical(url_edt,heure, minutes):
    calendar_evenements = telecharger_calendrier_et_extraire_evenements(url_edt)
    evenements = []
    for event in calendar_evenements:
        evenement = {
            'summary': event.name,
            'start': event.begin,
            'end': event.end
        }
        evenements.append(evenement)
    #evenements.sort(key=lambda event: event.begin)
    evenements.sort(key=lambda event: event["start"])
    for i in range(5):
        print(f"Résumé : {evenements[i]['summary']}")
        print(f"Début : {evenements[i]['start']}")
        print(f"Fin : {evenements[i]['end']}")
        print(f"abs({heure * 60 + minutes} - ({(evenements[i]['start'].hour + 1) * 60} + {evenements[i]['start'].minute} + 2 * 60)) = {abs(heure *60 + minutes - ((evenements[i]['start'].hour +1)* 60 + evenements[i]['start'].minute + 2 * 60))}")
        print(f"{(evenements[i]['end'].hour *60 + evenements[i]['end'].minute + 2*60) - (heure *60 + minutes)}")
        print(abs(heure * 60 + minutes- ((evenements[i]['start'].hour+1)*60+ evenements[i]['start'].minute + 2*60)) <= 2 *60 and ((evenements[i]['end'].hour+1) *60 + evenements[i]['end'].minute + 2*60) <= heure *60 + minutes)
        if (abs(heure * 60 + minutes - ((evenements[i]['start'].hour+1)*60+ evenements[i]['start'].minute + 2*60)) <= 2 * 60 and ((evenements[i]['end'].hour +1)*60 + evenements[i]['end'].minute + 2*60) <= heure *60 + minutes):
            print("ajouter effectif")
        print()



   