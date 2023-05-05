import requests
import csv
from datetime import datetime, timedelta

def scrape_nvd_vulnerabilities():
    print("\nBuvez un café, ça risque de prendre du temps..")
    print("Récupération des CVEs depuis la NVD des USA.")
    base_url = "https://services.nvd.nist.gov/rest/json/cves/1.0"

    today = datetime.now()
    yesterday = today - timedelta(days=1)
    
    today_str = today.strftime('%Y-%m-%dT00:00:00:000 UTC-05:00')
    yesterday_str = yesterday.strftime('%Y-%m-%dT00:00:00:000 UTC-05:00')

    params = {
        "modStartDate": yesterday_str,
        "modEndDate": today_str,
        "resultsPerPage": 2000
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        json_data = response.json()
        vulnerabilities = json_data["result"]["CVE_Items"]

        with open('results/vulnerabilities.csv', 'w', newline='', encoding='utf-8') as csv_file, open('results/vulnerabilities.txt', 'w', encoding='utf-8') as txt_file:
            fieldnames = ['CVE ID', 'Published Date', 'Last Modified Date', 'Description']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for vulnerability in vulnerabilities:
                cve_id = vulnerability["cve"]["CVE_data_meta"]["ID"]
                published_date = vulnerability["publishedDate"]
                last_modified_date = vulnerability["lastModifiedDate"]
                description = vulnerability["cve"]["description"]["description_data"][0]["value"]

                writer.writerow({
                    'CVE ID': cve_id,
                    'Published Date': published_date,
                    'Last Modified Date': last_modified_date,
                    'Description': description
                })

                txt_file.write(f"CVE ID: {cve_id}\n")
                txt_file.write(f"Published Date: {published_date}\n")
                txt_file.write(f"Last Modified Date: {last_modified_date}\n")
                txt_file.write(f"Description: {description}\n")
                txt_file.write("\n")

    else:
        print(f"Error: Unable to fetch data (HTTP {response.status_code})")
