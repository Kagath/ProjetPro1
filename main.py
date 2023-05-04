import os
import sys

from pymetasploit3.msfrpc import MsfRpcClient
from nmap_scan import run_nmap_scan
from scrape_nvd import run_nvd_scrape
from check_email_leak import run_email_leak_scan
from dashboard import generate_dashboard
from dashboard import clear_logs_and_results

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Vérifiez et créez les dossiers 'logs' et 'results'
create_directory("logs")
create_directory("results")

def main():
    while True:
        print("Veuillez choisir une option:")
        print("1. Exécuter un scan Nmap")
        print("2. Exécuter une simulation d'attaque avec Metasploit")
        print("3. Récupérer les vulnérabilités critiques à jour")
        print("4. Vérifier les fuites d'email")
        print("5. Générer un tableau de bord de sécurité")
        print("6. Effacer tous les fichiers de résultats et de journaux")
        print("0. Quitter")

        choice = input("Entrez le numéro de votre choix: ")

        if choice == "1":
            run_nmap_scan()
        elif choice == "2":
            target = input("Entrez la cible pour la simulation d'attaque Metasploit (IP): ")
            run_metasploit_scan(target)
        elif choice == "3":
            year = input("Entrez l'année pour récupérer les vulnérabilités NVD (par exemple, 2022): ")
            scrape_nvd_vulnerabilities(year)
        elif choice == "4":
            email = input("Entrez l'adresse e-mail à vérifier pour les fuites de données: ")
            check_email_leak(email)
        elif choice == "5":
            generate_dashboard()
        elif choice == "6":
            clear_logs_and_results()
            
        elif choice == "0":
            print("Au revoir!")
            sys.exit(0)
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == '__main__':
    main()
