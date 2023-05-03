from logger import log_info, log_error

def generate_dashboard():
    log_info("Génération du tableau de bord de sécurité")

    try:
        with open("results/nmap_results.txt", "r") as nmap_results:
            nmap_data = nmap_results.read()

        with open("results/metasploit_results.txt", "r") as metasploit_results:
            metasploit_data = metasploit_results.read()

        with open("results/nvd_results.txt", "r") as nvd_results:
            nvd_data = nvd_results.read()

        with open("results/email_leak_results.txt", "r") as email_leak_results:
            email_leak_data = email_leak_results.read()

        dashboard_data = f"""Tableau de bord de sécurité :
        \n=== Résultats Nmap ===
        \n{nmap_data}
        \n=== Résultats Metasploit ===
        \n{metasploit_data}
        \n=== Résultats NVD ===
        \n{nvd_data}
        \n=== Résultats des fuites d'email ===
        \n{email_leak_data}
        """

        print(dashboard_data)
        log_info("Tableau de bord de sécurité généré avec succès")

    except FileNotFoundError as e:
        log_error(f"Erreur lors de la génération du tableau de bord de sécurité : {e}")
