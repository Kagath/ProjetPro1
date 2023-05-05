#!/usr/bin/env python3

import os
import sys

from pymetasploit3.msfrpc import MsfRpcClient
from nmap_scan import run_nmap_scan
from scrape_nvd import scrape_nvd_vulnerabilities
from check_email_leak import run_check_email_leak
from dashboard import generate_dashboard
from dashboard import clear_logs_and_results
from dig import run_dns_enum

def clear_screen():
    if os.name == 'nt':  # Pour Windows
        os.system('cls')
    else:  # Pour Unix/Linux/Mac
        os.system('clear')
        
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Vérifiez et créez les dossiers 'logs' et 'results'
create_directory("logs")
create_directory("results")

def main():

    clear_screen()
    
    while True:
        print("________________________________________________________")
        print("Veuillez choisir une option: \n")
        print("1. Exécuter un scan Nmap")
        print("2. Exécuter une simulation d'attaque avec Metasploit")
        print("3. Récupérer les vulnérabilités critiques à jour")
        print("4. Vérifier les fuites d'email")
        print("5. Générer un tableau de bord de sécurité")
        print("6. Effacer tous les fichiers de résultats et de journaux")
        print("7. Enumération DNS avec dig\n")
        print("0. Quitter\n")

        print("________________________________________________________")
        choice = input("Entrez le numéro de votre choix: ")

        if choice == "1":
            run_nmap_scan()
        elif choice == "2":
            target = input("Entrez la cible pour la simulation d'attaque Metasploit (IP): ")
            run_metasploit_scan(target)
        elif choice == "3":
            scrape_nvd_vulnerabilities()
            print("\nRésultat disponible dans le dossier results, en format TXT et CSV(à ouvrir avec un logiciel tableur).\n")
        elif choice == "4":
            run_check_email_leak()
        elif choice == "5":
            generate_dashboard()
        elif choice == "6":
            clear_logs_and_results()
        elif choice == "7":
            run_dns_enum()
        elif choice == "0":
            print("\nAu revoir!\n")
            print("________________________________________________________")
            sys.exit(0)
        else:
            print("\nChoix invalide ! Veuillez réessayer.")

if __name__ == '__main__':
    main()
