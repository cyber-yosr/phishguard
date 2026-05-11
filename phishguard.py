import re
def analyser_url(url):
    score = 0
    alertes = []

    print(f"\n Analyse de : {url}")
    
    #Verification 1: HTTP/ HTTPS
    if "https" not in url:
        score += 2
        alertes.append("Pas de HTTPS -> connexion non securisée ")
    
    #Verification 2: Mots suspects
    mots_suspects= ["login", "verify", "secure", "account", "update", "password", "confirm"]
    for mot in mots_suspects:
        if mot in url.lower():
            score += 1
            alertes.append(f" Mot suspect détecté : '{mot}'")

    #Verification 3: URL trop longue
    if len(url) > 75:
        score += 1
        alertes.append(f" URL suspecte : trop longue ({len(url)} caracteres)")

    #Verification 4: adresse IP
    pattern_ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    if re.search(pattern_ip, url):
        print(f"DEBUG IP trouvée : {re.search(pattern_ip, url)}")
        score += 3
        alertes.append("Adresse IP détectée!")

    return score, alertes


with open("test_urls.txt", "r") as fichier:
    urls = fichier.readlines()

for url in urls:
    url = url.strip()
    if url:
        score, alertes = analyser_url(url)

        print(f"Score de risque : {score}")
        for alerte in alertes:
            print(alerte)
        print("-" * 40)
