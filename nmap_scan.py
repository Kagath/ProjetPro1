import os
import subprocess
from logger import log_info, log_error, save_result

def run_nmap_scan():
    target = input("Entrez l'adresse IP cible : ")
    log_info(f"Scan Nmap lancé pour la cible : {target}")

    try:
        scan_result = subprocess.check_output(["nmap", "-sV", "-T4", target])
        scan_result = scan_result.decode("utf-8")
        print(scan_result)
        
        log_info(f"Scan Nmap terminé pour la cible : {target}")
        save_result(scan_result, result_file="results/nmap_results.txt")
