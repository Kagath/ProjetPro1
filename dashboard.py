import os

from logger import log_info, log_error

def generate_dashboard():
    print("\nCréation du tableau de bord de sécurité...")

    # Liste des fichiers de résultats
    result_files = [
        "results/nmap_results.txt",
        "results/metasploit_results.txt",
        "results/nvd_results.txt",
        "results/email_leak_results.txt",
    ]

    # Liste des fichiers de journaux
    log_files = [
        "logs/nmap_scan.log",
        "logs/metasploit_scan.log",
        "logs/scrape_nvd.log",
        "logs/check_email_leak.log",
    ]

    with open("results/dashboard.txt", "w") as dashboard:
        dashboard.write("Tableau de bord de sécurité\n")
        dashboard.write("============================\n\n")

        for result_file in result_files:
            try:
                with open(result_file, "r") as f:
                    dashboard.write(f"{os.path.basename(result_file)}\n")
                    dashboard.write("--------------------\n")
                    dashboard.write(f.read())
                    dashboard.write("\n")
            except FileNotFoundError:
                print(f"Le fichier {result_file} est introuvable.")

        dashboard.write("\nLogs\n")
        dashboard.write("====\n\n")

        for log_file in log_files:
            try:
                with open(log_file, "r") as f:
                    dashboard.write(f"{os.path.basename(log_file)}\n")
                    dashboard.write("----------------\n")
                    dashboard.write(f.read())
                    dashboard.write("\n")
            except FileNotFoundError:
                print(f"Le fichier {log_file} est introuvable.")

    print("\nTableau de bord de sécurité créé avec succès dans results/dashboard.txt.")

def clear_logs_and_results():
    log_files = [
        "logs/nmap_scan.log",
        "logs/metasploit_scan.log",
        "logs/scrape_nvd.log",
        "logs/error.log",
        "logs/info.log",
        "logs/check_email_leak.log",
    ]

    result_files = [
        "results/nmap_results.txt",
        "results/metasploit_results.txt",
        "results/nvd_results.txt",
        "results/email_leak_results.txt",
        "results/dashboard.txt",
    ]

    files_to_remove = log_files + result_files

    for file_path in files_to_remove:
        try:
            os.remove(file_path)
            print(f"Fichier supprimé : {file_path}")
        except FileNotFoundError:
            print(f"Le fichier {file_path} est introuvable.")

    print("\nTous les fichiers de résultats et de journaux ont été supprimés.")
