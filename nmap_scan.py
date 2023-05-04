import nmap
from logger import log_info, log_error, save_result

def run_nmap_scan():
    targets = input("Veuillez entrer l'adresse IP, la plage d'adresses IP ou le CIDR à scanner (exemple : 192.168.1.0/24 ou 192.168.1.1-192.168.1.254) : ")
    ports = "22,21,23,443,80,53,135,8080,8888" # Ports à scanner
    options = "-A -O -sV -T4" # Options pour le scan Nmap
    print("Buvez un café, ça risque de prendre du temps..")
    print("Démarrage du scan Nmap sur les cibles.")
    
    log_info(f"Démarrage du scan Nmap sur les cibles : {targets}, ports : {ports}")
    scanner = nmap.PortScanner()

    try:
        scan_result = scanner.scan(hosts=targets, ports=ports, arguments=options)
        log_info(f"Scan Nmap terminé pour les cibles : {targets}, ports : {ports}")

        result_str = f"Résultats du scan Nmap pour les cibles : {targets}, ports : {ports}\n"
        for host, host_info in scan_result["scan"].items():
            result_str += f"{host}:\n"
            for proto in host_info["tcp"]:
                port_state = host_info['tcp'][proto]['state']
                if port_state not in ['closed', 'filtered']:
                    result_str += f"  {proto}: {port_state} {host_info['tcp'][proto]['name']} {host_info['tcp'][proto]['product']} {host_info['tcp'][proto]['version']}\n"
        save_result(result_str, result_file="results/nmap_results.txt")

    except Exception as e:
        log_error(f"Erreur lors de l'exécution du scan Nmap : {e}")
