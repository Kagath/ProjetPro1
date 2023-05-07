import requests
import time
import os
import random
import string

from bs4 import BeautifulSoup
from urllib.parse import urlsplit, urljoin
from logger import log_info, log_error
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

SENSITIVE_FILES = [
    "robots.txt",
    "sitemap.xml",
    ".git",
    ".htaccess",
    "config.php",
    "wp-config.php",
    "database.sql",
    "backup.sql",
]

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
                
def is_https():
    print("________________________________________________________")
    url = input("Entrez l'URL du site web que vous souhaitez scanner : \n")
    try:
        response = requests.get(url, verify=False)
        is_https = response.url.startswith("https://")

        with open("results/https_results.txt", "a") as f:
            f.write(f"{url}: {'HTTPS' if is_https else 'Non-HTTPS'}\n")

        print(f"Le site {url} est {'sécurisé (HTTPS)' if is_https else 'non sécurisé (non-HTTPS)'}.")
        print("Le résultat a été ajouté au fichier results/https_results.txt.")
    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la vérification de l'URL {url}: {e}")
        
def generate_secure_password():
    try:
        print("________________________________________________________")
        length = int(input("Entrez la longueur souhaitée pour le mot de passe : \n"))
        if length < 4:
            print("Veuillez choisir une longueur de mot de passe d'au moins 4 caractères.")
            return
            
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        with open("results/passwords.txt", "a") as f:
            f.write(f"{password}\n")

        print(f"\nMot de passe généré : {password}")
        
        print("\nLe mot de passe a été ajouté au fichier results/passwords.txt.")
        log_info(f"Un mot de passe sécurisé de longueur {length} a été généré et enregistré dans results/passwords.txt.")

    except ValueError:
        print("Veuillez entrer un nombre entier valide pour la longueur du mot de passe.")
        log_error("Erreur lors de la saisie de la longueur du mot de passe.")
        
def find_sensitive_files():
    print("________________________________________________________")
    url = input("Entrez l'URL du site web que vous souhaitez scanner : \n")
    parsed_url = urlsplit(url)

    create_directory("logs")
    create_directory("results")

    log_file = open("logs/find_sensitive_files.log", "w")
    result_file = open(f"results/find_sensitive_files_{parsed_url.netloc}.txt", "w")

    for file in SENSITIVE_FILES:
        check_url = urljoin(url, file)
        response = requests.get(check_url)

        if response.status_code == 200:
            print(f"Fichier sensible trouvé : {check_url}")
            log_file.write(f"Fichier sensible trouvé : {check_url}\n")
            result_file.write(f"Fichier sensible trouvé : {check_url}\n")
        else:
            print(f"Fichier non trouvé : {check_url}")
            log_file.write(f"Fichier non trouvé : {check_url}\n")

    log_file.close()
    result_file.close()

if __name__ == "__main__":
    find_sensitive_files()
