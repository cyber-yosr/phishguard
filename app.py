from flask import Flask, render_template, request
from phishguard import analyser_url
from vt_checker import verifier_url_virustotal

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultat = None
    url = ""
    score = 0
    alertes = []
    malveillants = None
    suspects = None
    pourcentage = 0
    if request.method == "POST":
        url = request.form["url"]
        score, alertes = analyser_url(url)
        #Verification VirusTotal
        malveillants, suspects = verifier_url_virustotal(url)
        if malveillants is not None:
            if malveillants > 0 :
                score += malveillants
                alertes.append(f"VirusTotal : {malveillants} antivirus ont détecté cette URL comme malveillante !")
            if suspects > 0:
                alertes.append(f"VirusTotal : {suspects} antivirus trouvent que cette adresse est suspecte!")
            pourcentage = min(round((score / 20) * 100), 100)

        resultat = {
            "url" : url,
            "score" : score,
            "alertes" : alertes,
            "vt_malveillants" : malveillants,
            "vt_suspects" : suspects,
            "pourcentage" : pourcentage
        }
    return render_template("index.html", resultat=resultat)

if __name__ == "__main__":
    app.run(debug=True)

