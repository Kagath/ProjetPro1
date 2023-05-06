import subprocess

from logger import log_info, log_error, save_result

def run_dns_query(record_type, target_domain):
    dig_command = f"dig {target_domain} {record_type} +noall +answer"
    try:
        output = subprocess.check_output(dig_command, shell=True, text=True)
        log_info(f"Récupération des enregistrements {record_type} pour {target_domain}")
        return output
    except subprocess.CalledProcessError as e:
        log_error(f"Erreur lors de la récupération des enregistrements {record_type} pour {target_domain}: {e}")
        return ""

def run_dns_enum():
    target_domain = input("\nEntrez le domaine cible pour l'énumération DNS: \n")

    log_info(f"Début de l'énumération DNS pour {target_domain}")
    print("\nDébut de l'énumération DNS \n")

    dns_records = {
        "A": run_dns_query("A", target_domain),
        "NS": run_dns_query("NS", target_domain),
        "MX": run_dns_query("MX", target_domain),
    }

    with open("results/dns_results.txt", "w") as dns_results_file:
        for record_type, records in dns_records.items():
            dns_results_file.write(f"Enregistrements {record_type}:\n")
            dns_results_file.write("------------------\n")
            dns_results_file.write(records)
            dns_results_file.write("\n")

    log_info(f"Énumération DNS terminée pour {target_domain}")
    print("\nÉnumération DNS terminée \n")
