import os
import glob

from logger import log_info, log_error

def write_section(dashboard, title, file_path):
    try:
        with open(file_path, "r") as f:
            dashboard.write(f"{title}\n")
            dashboard.write("-" * len(title) + "\n")
            dashboard.write(f.read())
            dashboard.write("\n")
    except FileNotFoundError:
        print(f"Le fichier {file_path} est introuvable.")


def generate_dashboard():
    print("\nCréation du tableau de bord de sécurité...")

    # Liste des fichiers de résultats
    result_files = [
        "results/nmap_results.txt",
        "results/metasploit_results.txt",
        "results/nvd_results.txt",
        "results/email_leak_results.txt",
        "results/dashboard.txt",
        "results/dns_results.txt",
        "results/vulnerabilities.txt",
    ]

    # Liste des fichiers de journaux
    log_files = [
        "logs/nmap_scan.log",
        "logs/metasploit_scan.log",
        "logs/scrape_nvd.log",
        "logs/check_email_leak.log",
        "logs/info.log",
    ]

    with open("results/dashboard.txt", "w") as dashboard:
        dashboard.write("Tableau de bord de sécurité\n")
        dashboard.write("============================\n\n")

        for result_file in result_files:
            write_section(dashboard, os.path.basename(result_file), result_file)

        dashboard.write("\nLogs\n")
        dashboard.write("====\n\n")

        for log_file in log_files:
            write_section(dashboard, os.path.basename(log_file), log_file)

    print("\nTableau de bord de sécurité créé avec succès dans results/dashboard.txt.")

def clear_logs_and_results():
    log_files = glob.glob("logs/*.log")
    result_files = glob.glob("results/*.txt") + glob.glob("results/*.csv")
    pycache_files = glob.glob("**/__pycache__/*.pyc", recursive=True)

    for file in log_files + result_files + pycache_files:
        try:
            os.remove(file)
            print(f"Suppression du fichier : {file}")
        except OSError as e:
            print(f"Erreur lors de la suppression du fichier : {file}, {e}")

    print("\nTous les fichiers de journaux et de résultats ont été supprimés.\n")
