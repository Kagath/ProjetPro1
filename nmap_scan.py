import nmap

from logger import log_info, log_error, save_result

def run_nmap_scan():

    print("\n________________________________________________________")
    targets = input("Veuillez entrer l'adresse IP, la plage d'adresses IP ou le CIDR à scanner (exemple : 192.168.1.0/24 ou 192.168.1.1-192.168.1.254) : \n")
    ports = "22,21,23,443,80,53,135,8080,8888" # Ports à scanner
    options = "-A -O -sV -T4" # Options pour le scan Nmap
    print("\nBuvez un café, ça risque de prendre du temps..")
    print("Démarrage du scan Nmap sur les cibles.\n")
    
    log_info(f"Démarrage du scan Nmap sur les cibles : {targets}, ports : {ports}\n")
    scanner = nmap.PortScanner()

    try:
        scanner.scan(hosts=targets, ports=ports, arguments=options)

        result_str = f"Résultats du scan Nmap pour les cibles : {targets}, ports : {ports}\n"
        for host in scanner.all_hosts():
            result_str += f"{host}:\n"
            for proto in scanner[host].all_protocols():
                for port in scanner[host][proto].keys():
                    port_state = scanner[host][proto][port]['state']
                    if port_state not in ['closed', 'filtered']:
                        result_str += f"  {port}: {port_state} {scanner[host][proto][port]['name']} {scanner[host][proto][port]['product']} {scanner[host][proto][port]['version']}\n"
        save_result(result_str, result_file="results/nmap_results.txt")
        log_info(f"Scan Nmap terminé pour les cibles : {targets}, ports : {ports}")
        print("________________________________________________________")
        print("\nScan Nmap terminé : results/nmap_results.txt\n")
        

    except Exception as e:
        log_error(f"Erreur lors de l'exécution du scan Nmap : {e}")
