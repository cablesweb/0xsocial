import random
import string

def generate_api_key(length):
    letters_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_digits) for _ in range(length))

# Génération des clés API aléatoires
api_keys = [generate_api_key(32) for _ in range(500000)]

# Écriture des clés API dans le fichier "api_list.txt"
with open('random_api.txt', 'w') as file:
    file.write('\n'.join(api_keys))

print("Les clés API ont été générées et stockées dans le fichier 'api_list.txt'.")
