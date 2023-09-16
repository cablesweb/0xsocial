import requests
import json
import time
from pystyle import *
from pygments import highlight, lexers, formatters
import os
import random

os.system('cls')

def is_api_key_valid(api_key):
    url = f"https://zefame.com/api/v2?key={api_key}&action=balance"
    headers = {'Authorization': 'Bearer ' + api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return True
    else:
        return False

banner = """
        ╦══╩══════════════0══════════════════╩══╦

     ▄▄ ·  ▄▄▄· ▄▄· ▐▄• ▄  ▄▄·  ▄▄▄· ▄▄▄▄· ▄▄▌  ▄▄▄ .
    ▐█ ▀. ▐█ ▄█▐█ ▌▪ █▌█▌▪▐█ ▌▪▐█ ▀█ ▐█ ▀█▪██•  ▀▄.▀·
    ▄▀▀▀█▄ ██▀·██ ▄▄ ·██· ██ ▄▄▄█▀▀█ ▐█▀▀█▄██▪  ▐▀▀▪▄
     █▄▪▐█▐█▪·•▐███▌▪▐█·█▌▐███▌▐█ ▪▐▌██▄▪▐█▐█▌▐▌▐█▄▄▌
     ▀▀▀▀ .▀   ·▀▀▀ •▀▀ ▀▀·▀▀▀  ▀  ▀ ·▀▀▀▀ .▀▀▀  ▀▀▀ 
        ╩══╦══════════════0══════════════════╦══╩
 ╔═════════╩═════════════════════════════════╩═════════╗
"""

print(Colorate.Diagonal(Colors.red_to_yellow, banner))

menu_choice = input(Colorate.Diagonal(Colors.red_to_yellow, """
                        [1] View Menu
                        [2] Likes Menu\n\n\n        
[?] Choose an option: """))

if menu_choice == '1':
    link1 = input(Colorate.Diagonal(Colors.red_to_green, "\n[?] Entrez le lien du tiktok: "))
    quantity = 1000
    service_id = 367
    key1 = input(Colorate.Diagonal(Colors.red_to_green, "\n[?] Entrez Votre clé personnel :  "))

    # Vérification de la clé API
    if not is_api_key_valid(key1):
        print("Clé invalide, veuillez contacter l'administrateur.")
        exit()

    url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={key1}"
    
    success_count = 0
    error_count = 0
    view_add = 0
    delay = random.randint(50, 105)  # Délai aléatoire entre 2 et 5 minutes

    while True:
        print(Colorate.Diagonal(Colors.white_to_blue, f"\nStatistique de votre compte:\n\nValidation de commande : {success_count}\nErreur/Changement : {error_count}\nVues totals : {view_add}"))
        response = requests.get(url1)
        data = response.json()
        if data == {'error': 'error.incorrect_service_id'}:
            error_count += 1
            print(Colorate.Diagonal(Colors.blue_to_black, '\nChangement du service id...'))
            params = {
                "key": key1,
                "action": "services"
            }
            response_services = requests.get(url1, params=params)
            services = response_services.json()
            for service in services:
                category = service.get("category")
                if category == 'Services gratuits':
                    service_id = service.get("service")
                    break
            url1 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link1}&quantity={quantity}&key={key1}"
        elif data == {'error': 'neworder.error.link_duplicate'}:
            print(Colorate.Diagonal(Colors.yellow_to_green, '\nEn attente de validation de la commande...'))
        elif data == {'error': 'Invalid API key'}:
            print(Colorate.Diagonal(Colors.red_to_black, '\n Votres Clés Personnel est plus valide'))
        else:
            success_count += 1; view_add += 1000*2
            print(Colorate.Diagonal(Colors.green_to_cyan, f"\nValidation, Les {quantity} vues ont bien été envoyés\nNouvelle commande en preparation merci de patientez {delay} second..."))
            time.sleep(delay)
                

if menu_choice == '2':
    link2 = input(Colorate.Diagonal(Colors.red_to_green, "\n[?] Entrez le lien du tiktok: "))
    quantity2 = 50
    service_id = 429
    key2 = input(Colorate.Diagonal(Colors.red_to_green, "\n[?] Entrez Votre clé personnel :  "))

    # Vérification de la clé API
    if not is_api_key_valid(key2):
        print("Clé invalide, veuillez contacter l'administrateur.")
        exit()

    url2 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link2}&quantity={quantity2}&key={key2}"
    
    success_count = 0
    error_count = 0
    likes_add = 0
    view_add = 0
    delay = random.randint(180, 300)  # Délai aléatoire entre 2 et 5 minutes

    while True:
        delay = random.randint(180,300)  # Délai aléatoire entre 2 et 10 minutes
        print(f"Délai d'attente avant la prochaine vérification : {delay} secondes")
        print(Colorate.Diagonal(Colors.white_to_blue, f"\nStatistique de votre compte:\n\nValidation de commande : {success_count}\nErreur/Changement : {error_count}\nVues totals : {view_add}"))
        response = requests.get(url2)
        data = response.json()
        if data == {'error': 'error.incorrect_service_id'}:
            error_count += 1
            print(Colorate.Diagonal(Colors.blue_to_black, '\nChangement du service id...'))
            params2 = {
                "key": key2,
                "action": "services"
            }
            response_services = requests.get(url2, params=params2)
            services = response_services.json()
            for service in services:
                category = service.get("category")
                if category == 'Services gratuits':
                    service_id = service.get("service")
                    break
            url2 = f"https://zefame.com/api/v2?action=add&service={service_id}&link={link2}&quantity={quantity2}&key={key2}"
        elif data == {'error': 'neworder.error.link_duplicate'}:
            print(Colorate.Diagonal(Colors.yellow_to_green, '\nEn attente de validation de la commande...'))
            print(Colorate.Diagonal(Colors.yellow_to_green, '\nAttendez 10 second , API réssaie...'))
            time.sleep(10)
        elif data == {'error': 'Invalid API key'}:
            print(Colorate.Diagonal(Colors.red_to_black, '\n Votres Clés Personnel est plus valide'))
            break
        else:
            success_count += 1; likes_add += 10
            print(Colorate.Diagonal(Colors.green_to_cyan, f"\nValidation, Les {quantity2} Likes ont bien été envoyés\nNouvelle commande en preparation merci de patientez {delay} second..."))