import os
import sys
from pymetasploit3.msfrpc import MsfRpcClient
from nmap_scan import run_nmap_scan
from scrape_nvd import scrape_nvd_vulnerabilities
from check_email_leak import check_email_leak
from security_dashboard import generate_security_dashboard

def main():
    while True:
        print("Veuillez choisir une option:")
        print("1. Exécuter un scan Nmap")
        print("2. Exécuter une simulation d'attaque avec Metasploit")
        print("3. Récupérer les vulnérabilités critiques à jour (NVD)")
        print("4. Vérifier les fuites d'email")
        print("5. Générer un tableau de bord de sécurité")
        print("0. Quitter")

        choice = input("Entrez le numéro de votre choix: ")

        if choice == "1":
            targets = input("Entrez les cibles pour le scan Nmap (IPs ou plages d'IPs): ")
            run_nmap_scan(targets)
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
            generate_security_dashboard()
        elif choice == "0":
            print("Au revoir!")
            sys.exit(0)
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == '__main__':
    main()
