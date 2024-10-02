# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:10:52 2023

@author: axel vaissade
"""
from fpdf import FPDF
from recuperer_informations_planning import telecharger_calendrier
from recuperer_informations_planning import recuperer_evenements
from recuperer_nb_eleves_par_heures import nb_eleve_par_heure
import os


def grouper_evenements_par_jour(liste_evenements):
    """Groupe les évenements d'un même calendrier par jour pour améliorer la rapidité de l'analyse"""
    evenements_par_jour = {}
    
    for evenement in liste_evenements:
        date = evenement['date_debut'].strftime('%d-%m-%Y') # Converti la date dans un format lisible
        if date not in evenements_par_jour:
            evenements_par_jour[date] = []
        evenements_par_jour[date].append(evenement)
        
    return evenements_par_jour

def recolter_trier_evenements(url_edt):
    """ Utilise d'autres fonctions pour récolter et trier les évenements par jour pour chaque classe/groupes"""
        
    ical_calendrier = telecharger_calendrier(url_edt)
    tous_les_evenements = recuperer_evenements(ical_calendrier)
    
    # Trie les evenements par date croissant
    tous_les_evenements.sort(key=lambda event: event['date_debut'])
    
    return grouper_evenements_par_jour(tous_les_evenements)
         


def generer_rapport(horaires, liste_classes,nom_rapport):
    """ 
    Affiche les infos pour les disponibilités des étuidants sur
    différentes pauses spécifié pour tous les jours dans les calendriers.
        
    @param horaires dictionnaire avec heures et minutes à laquelles on veut les présences
    @param liste_classes dictionnaire pour savoir le nombre d'étudiants et avoir leurs edt 
    """
        
    # Préparer l'affichage des informations
    infos = "Calcules des présences pour les promos suivantes : \n"
    
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
    
    report_data = {}
    for date in max_nb_dates :
        data_pause = presence_etu_pauses(date, horaires, liste_classes)
        report_data[f'{date}'] = data_pause
        
        #infos += presence_etudiants_date(date,horaires, liste_classes)
    
    # Génération du rapport PDF 
    generate_pdf_report(report_data, nom_rapport)
    

def presence_etu_pauses(date,horaires, liste_classes):
    
    listes_presence_pauses = []
    
    # Heures critiques pour notifier des départs
    heures_critiques = [13, 16]
    
    infos = f"Présence pour la date {date} :\n"

    for i in range(len(horaires)):
        heure = horaires[i]['heure']
        minute = horaires[i]['minutes']
        #print(f"heure precise : {horaires['heures'][i]}h{horaires['minutes'][i]}")
        
        infos_presences = nb_eleve_par_heure(date, heure, minute, liste_classes)
        nombre_eleves = infos_presences['nombre_eleves_present']
        
        data_pause = {'horaire': f"{heure}h{minute:02d}",
                'nb_etu': infos_presences['nombre_eleves_present'],
                'nb_etu_grd_pause': infos_presences['grande_pause']}
    
        
        listes_presence_pauses.append(data_pause)
        
        infos += f"Pour {heure}h{minute:02d}, il y aura approximativement {nombre_eleves} élèves présents.\n"
        
        # Alerte pour les heures où les étudiants peuvent quitter
        if heure in heures_critiques:
            data_pause['note'] = "N.B : Attention ce sont des heures où les étudiants quittent généralement l'établissement."
    infos += "\n"
    print(infos)
    return listes_presence_pauses

def generate_pdf_report(report_data,nom):
    
    # Récupérer le chemin du dossier de téléchargement
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    
    # Créer le chemin entier vers le fichier avec le nom du dossier
    pdf_file_path = os.path.join(downloads_path, f"{nom}.pdf")
   
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Student Presence Report Polytech Chambéry", ln=True, align='C')
    pdf.ln(10)
    
    # Boucler pour formater les données dans le PDF
    for jour, liste_pauses in report_data.items():
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, txt=f"Présence pour la date {jour}:", ln=True)
        pdf.ln(5)
        
        pdf.set_font("Arial", size=12)
        for pause in liste_pauses:
            pdf.cell(200, 10, txt=f"Pour {pause['horaire']}, il y aura approximativement {pause['nb_etu']} élèves présents.", ln=True)
            if 'note' in pause:
                pdf.cell(200, 10, txt=pause['note'], ln=True)
        
        # Add a line break between days
        pdf.ln(10)

    
    pdf.output(pdf_file_path)
    print(f"PDF report generated, saved at : {pdf_file_path}")


