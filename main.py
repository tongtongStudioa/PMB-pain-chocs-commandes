# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:19:25 2023

@author: axel
"""
from affiche_infos_utiles import afficher_infos_presence_semaine
from recuperer_informations_planning import lire_fichier_ical

# main file

data_classes = {
    'classes':[
        {'name':"FISE_BAT3_1",
         'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=9789&projectId=1&calType=ical&lastDate=2042-08-14',
         'effectif':25
         },
         {'name':"FISE_BAT3_2",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=9794&projectId=1&calType=ical&lastDate=2042-08-14',
          'effectif':25
          },
         {'name':"FISA_BAT3",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=9822&projectId=1&calType=ical&lastDate=2042-08-14',
          'effectif':27
          },
         {'name':"EIT_A",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=5738&projectId=1&calType=ical&lastDate=2042-08-14',
          'effectif':20
          },
         {'name':"EIT_B",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=85&projectId=1&calType=ical&lastDate=2042-08-14',
          'effectif':20,
          },
         {'name':"FISA_BAT4_1",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=9784&projectId=1&calType=ical&lastDate=2042-08-14',
          'effectif':15,
          },
         {'name':"FISA_BAT4_2",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=9795&projectId=1&calType=ical&lastDate=2042-08-14',
          'effectif':15,
          },
         {'name':"FISE_BAT4_1",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=9551&projectId=1&calType=ical&lastDate=2042-08-14',
          'effectif':25,
          },
         {'name':"FISE_BAT4_2",
          'url_edt':'https://ade-usmb-ro.grenet.fr/jsp/custom/modules/plannings/direct_cal.jsp?data=b5cfb898a9c27be94975c12c6eb30e9233bdfae22c1b52e2cd88eb944acf5364c69e3e5921f4a6ebe36e93ea9658a08f,1&resources=9552&projectId=1&calType=ical&lastDate=2042-08-14',
          'effectif':23,
          }
    ]
}

# Date précise pour laquelle vous voulez connaître le nombre d'élèves
date_semaine = {'liste_dates':["09-04-2024","10-04-2024","11-04-2024","12-04-2024","13-04-2024"],
                'liste_horaires':{
                    "heures":[9,11,13,14,16],
                    "minutes":[30,15,00,45,30]}
                }

# Jour précis pour lequel on veut connaitre le nombre d'èlèves
#nombre_eleves = obtenir_nombre_eleves_pour_heure_precise(date,heure, data_classes)

#print(f"Pour {date['heures']}h{date['minutes']}, il y a approximativement {nombre_eleves} élèves présents.")

afficher_infos_presence_semaine(date_semaine['liste_dates'], date_semaine['liste_horaires'],data_classes)
#print(data_classes['classes'][0]['name'])
#Ylire_fichier_ical(data_classes['classes'][0]['url_edt'],9,30)

