from selenium import webdriver
import random
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
import string
from pystyle import *
from selenium.common.exceptions import NoSuchElementException
import random
import string





chromedriver_path = 'c:\chromedriver.exe'
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(executable_path=chromedriver_path)
browser.get("https://zefame.com/signup")



banner = """
        ╦══╩══════════════0══════════════════╩══

         ██████╗ ██╗  ██╗████████╗ ██████╗ ██╗  ██╗
        ██╔═████╗╚██╗██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝
        ██║██╔██║ ╚███╔╝    ██║   ██║   ██║█████╔╝ 
        ████╔╝██║ ██╔██╗    ██║   ██║   ██║██╔═██╗ 
        ╚██████╔╝██╔╝ ██╗   ██║   ╚██████╔╝██║  ██╗
        ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
        ╩══╦══════════════0══════════════════╦══╩
 ╔═════════╩═════════════════════════════════╩═════════╗
"""

print(Colorate.Diagonal(Colors.red_to_yellow, banner))

menu_choice = input(Colorate.Diagonal(Colors.red_to_yellow, """
                        [1] api creator 
                        [2] api checker \n\n\n        
[?] Choose an option:  """))




if menu_choice == '1':

    api_count = 0
    api_name = 'api a bien etait créer'
    captcha_text = input("complete captcha and press enter :  ")
    while True:
       
     



      # Générer un pseudo aléatoire de 8 à 10 caractères
       pseudo_length = random.randint(5, 15)
       pseudo_aleatoire = ''.join(random.choice(string.ascii_letters) for _ in range(pseudo_length))

       # Générer une adresse e-mail aléatoire se terminant par "@0xcable.com"
       email_aleatoire = f'{"".join(random.choice(string.ascii_lowercase) for _ in range(10))}@0xcable.com'




       captcha_text = input("complete captcha and press enter :  ")
       #nom dutilisateur
       username = browser.find_element_by_xpath('//*[@id="login"]')
       username.click()
       username.send_keys('cable'+ pseudo_aleatoire)

       #email
       email = browser.find_element_by_xpath('//*[@id="email"]')
       email.click()
       email.send_keys(email_aleatoire)

       #prenom
       time.sleep(0.4)
       prenom = browser.find_element_by_xpath('//*[@id="first_name"]')
       prenom.click()
       prenom.send_keys('cable')

       #nom
       time.sleep(0.4)
       nom = browser.find_element_by_xpath('//*[@id="last_name"]')
       nom.click()
       nom.send_keys('0xcable')

       #pays
       pays = browser.find_element_by_xpath('//*[@id="website"]')
       pays.click()
       pays.send_keys('arabeee')


       #rue
       rue = browser.find_element_by_xpath('//*[@id="whatsapp"]')
       rue.click()
       rue.send_keys('rue des gros lgbt comme toi')

       #ville
       ville = browser.find_element_by_xpath('//*[@id="telegram"]')
       ville.click()
       ville.send_keys('de base c telegram tdrc')

       #postal
       postal = browser.find_element_by_xpath('//*[@id="skype"]')
       postal.click()
       postal.send_keys('code postal c pas skype fdp')

       #mdp
       mdp = browser.find_element_by_xpath('//*[@id="password"]')
       mdp.click()
       mdp.send_keys('0xcablebest1')

       #confirmmdp
       confirmmdp = browser.find_element_by_xpath('//*[@id="password_again"]')
       confirmmdp.click()
       confirmmdp.send_keys('0xcablebest1')

       #case
       case = browser.find_element_by_xpath('//*[@id="block_30"]/div/div[4]/div/div/div/div/form/div[1]/div[12]/div/div/div/div/label[1]/span')
       case.click()

       #create
       time.sleep(0.1)
       create = browser.find_element_by_xpath('//*[@id="block_30"]/div/div[4]/div/div/div/div/form/div[2]/div/div/button')
       create.click()

       #parametre
       time.sleep(0.2)
       parametre = browser.find_element_by_xpath('//*[@id="navbar-collapse-11"]/div[2]/ul[3]/li[1]/a')
       parametre.click()

       #api_create
       time.sleep(0.1)
       api_create = browser.find_element_by_xpath('//*[@id="block_2"]/div/div[4]/div/div/div[6]/div/form/div/div/div/div/div/div/button')
       api_create.click()

       #api_clef
       time.sleep(0.1)
       api_clef = browser.find_element_by_xpath('//*[@id="block_2"]/div/div[4]/div/div/div[1]')
       api_key_text = api_clef.text.strip()
       index = api_key_text.index(":")
       api_key = api_key_text[index + 1:].strip()

       with open("api_create.txt", "a") as api_file:  # Utilisation de 'a' pour ajouter à la fin du fichier
           api_file.write(f"{api_key}\n")

       #deco
       deco = browser.find_element_by_xpath('//*[@id="navbar-collapse-11"]/div[2]/ul[3]/li[2]/a')
       deco.click()

       inscription = browser.find_element_by_xpath('//*[@id="navbar-collapse-14"]/div[2]/ul/li[3]/a')
       inscription.click()

       api_count += 1
       print(Colorate.Diagonal(Colors.red_to_yellow ,f'{api_name} + {api_count}'))
       
       #retourner a while true
       time.sleep(1)
       continue


       




