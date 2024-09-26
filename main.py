# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:19:25 2023

@author: axel
"""
from affiche_infos_utiles import generer_rapport
from fpdf import FPDF

# main file

data_classes = {
    'classes':[
        {'name':"FISE_BAT3_1",
         'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=4795&projectId=2&calType=ical&lastDate=2042-08-14',
         'effectif':25
         },
         {'name':"FISE_BAT3_2",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=5726&projectId=2&calType=ical&lastDate=2042-08-14',
          'effectif':25
          },
         {'name':"FISA_BAT3",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=5728&projectId=2&calType=ical&lastDate=2042-08-14',
          'effectif':35
          },
         {'name':"EIT3",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=5727&projectId=2&calType=ical&lastDate=2042-08-14',
          'effectif':35
          },
         {'name':"FISA_BAT4",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=2640&projectId=2&calType=ical&lastDate=2042-08-14',
          'effectif':32,
          },
         {'name':"FISE_BAT4_1",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=2308&projectId=2&calType=ical&lastDate=2042-08-14',
          'effectif':20,
          },
         {'name':"FISE_BAT4_2",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=2314&projectId=2&calType=ical&lastDate=2042-08-14',
          'effectif':23,
          },
         {'name':"EIT4",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=2761&projectId=2&calType=ical&lastDate=2042-08-14',
          'effectif':30
          },
    ]
}

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


horaires_pauses = [{"heure": 9, "minutes": 30},
                   {"heure": 11, "minutes": 15},
                   {"heure": 16, "minutes": 30},
                   ]

# Jour précis pour lequel on veut connaitre le nombre d'èlèves
#nombre_eleves = obtenir_nombre_eleves_pour_heure_precise(date,heure, data_classes)

#print(f"Pour {date['heures']}h{date['minutes']}, il y a approximativement {nombre_eleves} élèves présents.")

generer_rapport(horaires_pauses,data_classes)
#print(data_classes['classes'][0]['name'])
#Ylire_fichier_ical(data_classes['classes'][0]['url_edt'],9,30)

