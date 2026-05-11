from flask import Flask, render_template, request
from phishguard import analyser_url

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultat = None
    if request.method == "POST":
        url = request.form["url"]
        score, alertes = analyser_url(url)
        resultat = {
            "url" : url,
            "score" : score,
            "alertes" : alertes
        }
    return render_template("index.html", resultat=resultat)

if __name__ == "__main__":
    app.run(debug=True)

