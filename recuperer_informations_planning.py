# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 13:44:09 2023

@author: La famille tong
"""
import requests
from ics import Calendar
import pytz



def convert_to_local_time(utc_dt):
    """ Convert UTC datetime to local time """

    # Set the time zone for your events
    local_tz = pytz.timezone('Europe/Paris')  # Replace with your actual timezone
    return utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)


def telecharger_calendrier(url):
    """  Fonction pour télécharger un calendrier depuis une URL ical"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        cal = Calendar(response.text)
        return cal
        
    except requests.exceptions.RequestException as e:
        print(f"Error : {e}")
        return None
    
def recuperer_evenements(cal):
    evenements = []
    #evenements = list(cal.events)
    #return evenements
    for component in list(cal.events):
        # Extraire les dates et horaires de début et de fin d'évenement (cours) 
        date_debut = component.begin
        date_fin = component.end
        
        # Convertir en heure local (Europe/paris)
        date_debut = convert_to_local_time(date_debut)
        date_fin = convert_to_local_time(date_fin)
        
        # Ajouter l'evenement à la liste avec des clés spécifiques
        evenements.append({
            'titre': component.name,
            'date_debut': date_debut,
            'date_fin': date_fin,
            'heure_debut': date_debut.hour,
            'minutes_debut': date_debut.minute,
            'heure_fin': date_fin.hour,
            'minutes_fin': date_fin.minute
            
        })
    return evenements







   