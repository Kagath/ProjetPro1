import os
from nmap_scan import run_nmap_scan
from metasploit_attack import run_metasploit_attack
from scrape_nvd import run_nvd_scrape
from check_email_leak import run_email_leak_scan
from dashboard import generate_dashboard

def main():
    if not os.path.exists("logs"):
        os.mkdir("logs")
    if not os.path.exists("results"):
        os.mkdir("results")

    while True:
        print("Sélectionnez une fonctionnalité à exécuter :")
        print("1. Scanner les vulnérabilités avec Nmap")
        print("2. Simuler une attaque avec Metasploit")
        print("3. Récupérer les vulnérabilités critiques (scrapping NVD)")
        print("4. Vérifier les fuites d'emails avec l'API Have I Been Pwned")
        print("5. Générer un tableau de bord de sécurité")
        print("6. Quitter")

        choice = input("Entrez le numéro de la fonctionnalité choisie : ")

        if choice == "1":
            run_nmap_scan()
        elif choice == "2":
            run_metasploit_attack()
        elif choice == "3":
            run_nvd_scrape()
        elif choice == "4":
            run_email_leak_scan()
        elif choice == "5":
            generate_dashboard()
        elif choice == "6":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
