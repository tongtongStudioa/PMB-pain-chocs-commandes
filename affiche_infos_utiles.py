# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:10:52 2023

@author: axel
"""
from fpdf import FPDF
from recuperer_informations_planning import telecharger_calendrier
from recuperer_informations_planning import recuperer_evenements
from recuperer_nb_eleves_par_heures import nb_eleve_par_heure


def grouper_evenements_par_jour(liste_evenements):
    """Groupe les évenements d'un même calendrier par jour pour améliorer la rapidité de l'analyse"""
    evenements_par_jour = {}
    
    for evenement in liste_evenements:
        date = evenement.begin.strftime('%d-%m-%Y') # Converti la date dans un format lisible
        if date not in evenements_par_jour:
            evenements_par_jour[date] = []
        evenements_par_jour[date].append(evenement)
        
    return evenements_par_jour

def recolter_trier_evenements(url_edt):
    """ Utilise d'autres fonctions pour récolter et trier les évenements par jour pour chaque classe/groupes"""
        
    ical_calendrier = telecharger_calendrier(url_edt)
    tous_les_evenements = recuperer_evenements(ical_calendrier)
    
    # Trie les evenements par date croissant
    tous_les_evenements.sort(key=lambda event: event.begin)
    
    return grouper_evenements_par_jour(tous_les_evenements)
         


def generer_rapport(horaires, liste_classes):
    """ 
    Affiche les infos d'une semaine 
        
    @param liste_dates liste de dates de la semaine
    @param horaires dictionnaire avec heures et minutes à laquelles on veut les présences
    @liste_classes dictionnaire pour savoir le nombre d'étudiants et avoir leurs edt 
    """
        
    # Affichage de la semaine
    infos = "Rapport de présences pour la vente \n\n"
    infos += "Calcules des présences pour les promos suivantes : \n"
    
    nb_total_etu = 0
    maxlen = 0
    max_nb_dates = 0
    for classe in liste_classes:
        
        nb_total_etu += classe['effectif']
        
        # Collecter et trier les événements par classe
        classe['evenements'] = recolter_trier_evenements(classe['url_edt'])
        if len(classe['evenements']) > maxlen:
            max_nb_dates = classe['evenements']
        infos += f"{classe['nom']} : {classe['effectif']} étudiants\n"
        
    infos += f"Nombre d'étudiants total dans les classes : {nb_total_etu}"
    infos += "\n"
    print(infos) # Imprimer les informations d'introduction
    infos = ""
    
    for date in max_nb_dates :
        infos += presence_etudiants_date(date,horaires, liste_classes)
    
    
    # Affichage des informations finales
    print(infos)
    #return infos

def presence_etudiants_date(date,horaires, liste_classes):
    # Heures critiques pour notifier des départs
    heures_critiques = [13, 16]
    
    infos = f"Présence pour la date {date} :\n"

    for i in range(len(horaires)):
        heure = horaires[i]['heure']
        minute = horaires[i]['minutes']
        #print(f"heure precise : {horaires['heures'][i]}h{horaires['minutes'][i]}")
        
        infos_presences = nb_eleve_par_heure(date, heure, minute, liste_classes)
        nombre_eleves = infos_presences['nombre_eleves_present']

        infos += f"Pour {heure}h{minute:02d}, il y aura approximativement {nombre_eleves} élèves présents.\n"
        
        # Alerte pour les heures où les étudiants peuvent quitter
        if heure in heures_critiques:
            infos += " N.B : Attention ce sont des heures où les étudiants quittent généralement l'établissement.\n"
    infos += "\n"
    
    return infos

def generate_pdf_report(day_student_counts, pdf_file_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Student Presence Report", ln=True, align='C')
    pdf.ln(10)

    # Loop over each day and display the results
    for date, times in day_student_counts.items():
        pdf.cell(200, 10, txt=f"Présence pour la date {date.strftime('%d-%m-%Y')} :", ln=True)
        for time_info in times:
            time = time_info["time"]
            student_count = time_info["count"]
            pdf.cell(200, 10, txt=f"Pour {time['hour']}h{time['minute']:02d}, il y aura approximativement {student_count} élèves présents.", ln=True)
            if time['hour'] == 13 or time['hour'] == 16:
                pdf.cell(200, 10, txt=" N.B : Attention ce sont des heures où les étudiants quittent généralement l'établissement.", ln=True)
        pdf.ln(10)

    
    pdf.output(pdf_file_path)
    print(f"PDF report generated: {pdf_file_path}")


