import requests
from pystyle import *
import os

os.system('cls')

def send_likes(api_key1, link, quantity):
    api_key1 = "9320bd30991779e6723437125e2adbad"
    service_id = 1224
    url = f"https://addsmm.com/api/v2?action=add&service={service_id}&link={link}&quantity={quantity}&key={api_key1}"

    response = requests.get(url)

    if response.status_code == 200:
        print(Colorate.Diagonal(Colors.red_to_green, "Les likes ont bien été envoyés."))
    else:
        print(Colorate.Diagonal(Colors.red_to_black, "Une erreur s'est produite lors de l'envoi des likes."))

banner = """
        ╦══╩══════════════0══════════════════╩══╦
     ▄▄ ·  ▄▄▄· ▄▄· ▐▄• ▄  ▄▄·  ▄▄▄· ▄▄▄▄· ▄▄▌  ▄▄▄ .
    ▐█ ▀. ▐█ ▄█▐█ ▌▪ █▌█▌▪▐█ ▌▪▐█ ▀█ ▐█ ▀█▪██•  ▀▄.▀·
    ▄▀▀▀█▄ ██▀·██ ▄▄ ·██· ██ ▄▄▄█▀▀█ ▐█▀▀█▄██▪  ▐▀▀▪▄
     █▄▪▐█▐█▪·•▐███▌▪▐█·█▌▐███▌▐█ ▪▐▌██▄▪▐█▐█▌▐▌▐█▄▄▌
     ▀▀▀▀ .▀   ·▀▀▀ •▀▀ ▀▀·▀▀▀  ▀  ▀ ·▀▀▀▀ .▀▀▀  ▀▀▀ 
                    admin account
        ╩══╦══════════════0══════════════════╦══╩
 ╔═════════╩═════════════════════════════════╩═════════╗
"""

print(Colorate.Diagonal(Colors.red_to_yellow, banner))

menu_choice = input(Colorate.Diagonal(Colors.red_to_yellow, 
"""
        ╦══╩══════════════0══════════════════╩══╦
        ╩═          admin choice                ╩
                 [1] View Tiktok              
                 [2] Likes Tiktok [Not work]                                  
                 [3] Telegram Post View
                 [4] Twitter Tweet Views
                 [5] like instagram 
                 [6] member canal instagram [soon] 
                 [7] follow instagram [not work]
        ╦═                                     ═╦
        ╩══╦══════════════0══════════════════╦══╩
                        
[?] Choose an option: """))




if menu_choice == '5':
    link = input(Colorate.Diagonal(Colors.red_to_green, "\n[?] Entrez le lien de la publication Instagram : "))
    quantity = 100
    api_key1 = "9320bd30991779e6723437125e2adbad"

    send_likes(api_key1, link, quantity)

