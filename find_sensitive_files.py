import requests
import time
import os

from bs4 import BeautifulSoup
from urllib.parse import urlsplit, urljoin

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
