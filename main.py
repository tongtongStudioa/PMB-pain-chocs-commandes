# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:19:25 2023

@author: axel vaissade
@GitHub: tongtongStudioa

**
J'ai créé ce programme pour rendre compte d'une nombre d'étudiants disponible à une pause dans mon école susceptible d'achter
des viennoiseries pour une association.
**

"""
from affiche_infos_utiles import generer_rapport

# Fichier principal avec tous les infos, les effectifs sont estimès ici, ces informations peuvent être modifiés.
# Les url des des emplois du temps peuvent être pris de l'intranet sur la vue emploi du temps pour chaque filière.

listes_classes = [
        {'nom':"FISE_BAT3_1",
         'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=4795&projectId=2&calType=ical&lastDate=2042-08-14',
         'effectif':25
         },
         {'nom':"FISE_BAT3_2",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=5726&projectId=2&calType=ical&lastDate=2042-08-14',
          'effectif':25
          },
         {'nom':"FISA_BAT3",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=5728&projectId=2&calType=ical&lastDate=2042-08-14',
          'effectif':35
          },
         {'nom':"EIT3",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=5727&projectId=2&calType=ical&lastDate=2042-08-14',
          'effectif':35
          },
         {'nom':"FISA_BAT4",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=2640&projectId=2&calType=ical&lastDate=2042-08-14',
          'effectif':32,
          },
         {'nom':"FISE_BAT4_1",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=2308&projectId=2&calType=ical&lastDate=2042-08-14',
          'effectif':20,
          },
         {'nom':"FISE_BAT4_2",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=2314&projectId=2&calType=ical&lastDate=2042-08-14',
          'effectif':23,
          },
         {'nom':"EIT4",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=2761&projectId=2&calType=ical&lastDate=2042-08-14',
          'effectif':30
          },
]

# Remplir avec les horaires de pauses qui nous intéressent
horaires_pauses = [{"heure": 9, "minutes": 30},
                   {"heure": 11, "minutes": 15},
                   {"heure": 16, "minutes": 30},
                   ]


#Génère un rapport pdf et sur la console
generer_rapport(horaires_pauses,listes_classes,"Presence 1 semestre PMB(1)")

