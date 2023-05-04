import requests
from bs4 import BeautifulSoup
from logger import log_info, log_error, save_result

def run_nvd_scrape():
    base_url = "https://nvd.nist.gov/vuln/full-listing"
    log_info(f"Début du scrapping des vulnérabilités critiques du NVD")

    response = requests.get(base_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        critical_vulns = soup.find_all("span", class_="red bold")

        log_info(f"Scrapping des vulnérabilités critiques du NVD terminé")
        save_result(f"Vulnérabilités critiques trouvées : {len(critical_vulns)}", result_file="results/nvd_results.txt")
    else:
        log_error(f"Erreur lors de la récupération des données du NVD (code {response.status_code})")

# Pour tester la fonction run_nvd_scrape() directement
if __name__ == "__main__":
    run_nvd_scrape()
