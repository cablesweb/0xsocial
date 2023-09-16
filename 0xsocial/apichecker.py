import requests
from pystyle import *
import os

os.system('cls' if os.name == 'nt' else 'clear')

listapi = input("Nom du fichier texte : ")

def check_api(api_key):
    url = f"https://zefame.com/api/v2?key={api_key}&action=balance"
    headers = {'Authorization': 'Bearer ' + api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(Colorate.Diagonal(Colors.green_to_blue, f'[Succes] API Key {api_key} FONCTIONNE ! :) '))
        return True
    else:
        print(Colorate.Diagonal(Colors.red_to_purple, f'[Error] API Key {api_key} ban par le fdp :( '))
        return False

# Lecture des clés API à partir du fichier "api_list.txt"
with open(listapi, 'r') as file:
    api_keys = file.read().splitlines()

# Vérification de chaque clé API
valid_api_keys = []
invalid_api_keys = []
for api_key in api_keys:
    if check_api(api_key):
        valid_api_keys.append(api_key)
    else:
        invalid_api_keys.append(api_key)

# Demande à l'utilisateur s'il souhaite supprimer les clés API non fonctionnelles
choice = input("Voulez-vous supprimer les clés API non fonctionnelles du fichier ? (oui/non): ")
if choice.lower() == "oui":
    with open(listapi, 'w') as file:
        file.write('\n'.join(valid_api_keys))
        print("Les clés API non fonctionnelles ont été supprimées du fichier.")
else:
    print("Les clés API non fonctionnelles n'ont pas été supprimées du fichier.")
