import nmap

def run_nmap_scan(targets, options='-sV'):
    nm = nmap.PortScanner()
    nm.scan(hosts=targets, arguments=options)

    for host in nm.all_hosts():
        print(f"Host : {host} ({nm[host].hostname()})")
        print("State : {}".format(nm[host].state()))
        for protocol in nm[host].all_protocols():
            print("Protocol : {}".format(protocol))
            ports = nm[host][protocol].keys()
            for port in ports:
                print("port : {}\tstate : {}".format(port, nm[host][protocol][port]["state"]))

    return nm

# Exemple d'utilisation de la fonction
if __name__ == '__main__':
    targets = '192.168.1.1-255'  # Exemple de cibles: une plage d'adresses IP
    scan_results = run_nmap_scan(targets)
