import requests
import json

from logger import log_info, log_error, save_result

api_key = "59918da982474e6d99b3ac573ec6a02d"

def run_check_email_leak():
    print("\n________________________________________________________")
    email = input("Entrez l'adresse e-mail à vérifier : \n")
    print("\n")    
    print("Buvez un café, ça risque de prendre du temps..")
    print("Démarrage du scan de fuite de données sur cette adresse email.")

    base_url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "hibp-api-key": api_key,
        "User-Agent": "MyApp"
    }

    try:
        response = requests.get(base_url, headers=headers)
        if response.status_code == 200:
            breaches = json.loads(response.content)
            log_info(f"Vérification des fuites de données pour l'adresse e-mail : {email}")
            save_result(f"Nombre de fuites trouvées pour {email} : {len(breaches)}", result_file="results/email_leak_results.txt")
            print(f"\n{len(breaches)} fuites de données trouvées pour {email}: \n")
            for breach in breaches:
                print(f"{breach['Name']} - {breach['Domain']}")
        elif response.status_code == 404:
            log_info(f"Aucune fuite de données trouvée pour l'adresse e-mail : {email} \n")
            print(f"Aucune fuite de données trouvée pour l'adresse e-mail : {email} \n")
        else:
            log_error(f"Erreur lors de la récupération des données de fuites pour l'adresse e-mail : {email} (code {response.status_code})")
    except Exception as e:
        log_error(f"Erreur lors de la vérification des fuites de données pour l'adresse e-mail : {email} : {e}")
