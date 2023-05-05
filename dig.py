import subprocess
from logger import log_info, log_error, save_result

def run_dns_enum():
    target_domain = input("\nEntrez le domaine cible pour l'énumération DNS: \n")

    log_info(f"Début de l'énumération DNS pour {target_domain}")
    print("\nDébut de l'énumération DNS \n")

    try:
        # Récupération des enregistrements A
        dig_a_command = f"dig {target_domain} A +noall +answer"
        a_records_output = subprocess.check_output(dig_a_command, shell=True, text=True)
        save_result(a_records_output, result_file="results/dns_results.txt")

        # Récupération des enregistrements NS
        dig_ns_command = f"dig {target_domain} NS +noall +answer"
        ns_records_output = subprocess.check_output(dig_ns_command, shell=True, text=True)
        save_result(ns_records_output, result_file="results/dns_results.txt")

        # Récupération des enregistrements MX
        dig_mx_command = f"dig {target_domain} MX +noall +answer"
        mx_records_output = subprocess.check_output(dig_mx_command, shell=True, text=True)
        save_result(mx_records_output, result_file="results/dns_results.txt")

        log_info(f"Énumération DNS terminée pour {target_domain}")
        print("\nÉnumération DNS terminée \n")

    except subprocess.CalledProcessError as e:
        log_error(f"Erreur lors de l'énumération DNS pour {target_domain}: {e}")
