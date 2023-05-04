import requests

from logger import log_info, log_error, save_result

def run_email_leak_scan():
    email = input("Entrez l'adresse e-mail à vérifier : ")
    log_info(f"Vérification des fuites d'email pour : {email}")

    # Remplacez [your_key] par votre clé d'API personnelle pour Have I Been Pwned
    api_key = "[your_key]"
    headers = {
        "hibp-api-key": api_key,
        "user-agent": "MySecurityTool"
    }
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        breaches = response.json()
        log_info(f"{email} a été trouvé dans {len(breaches)} fuites de données")
        save_result(f"{email} a été trouvé dans {len(breaches)} fuites de données", result_file="results/email_leak_results.txt")
    elif response.status_code == 404:
        log_info(f"Aucune fuite de données trouvée pour {email}")
        save_result(f"Aucune fuite de données trouvée pour {email}", result_file="results/email_leak_results.txt")
    else:
        log_error(f"Erreur lors de la vérification des fuites d'email pour {email} (code {response.status_code})")
