import requests
import base64

API_KEY = "ac17e126654f7871b35d1c4d64817c0a1ad8a34e5ff1384ab4e3a1cc3f609037"

def verifier_url_virustotal(url):
    #Encoder l'URL en base 64
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")

    #Envoyer la requete a VirusTotal
    headers = {
        "x-apikey" : API_KEY
    }
    response = requests.get(
        f"https://www.virustotal.com/api/v3/urls/{url_id}",
        headers=headers
    )

    if response.status_code == 200:
        data = response.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]
        malveillants = stats["malicious"]
        suspects = stats["suspicious"]
        return malveillants, suspects
    else:
        return None, None
    