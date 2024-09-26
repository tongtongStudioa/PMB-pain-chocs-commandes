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
    events = []
    evenements = list(cal.events)
    return evenements
    """for component in cal.walk('vevent'):
        event = {
            'summary': str(component.get('summary')),
            'start': component.get('dtstart').dt,
            'end': component.get('dtend').dt
        }
        events.append(event)
    return events"""
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



   