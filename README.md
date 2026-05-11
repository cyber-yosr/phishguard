# Phishguard
Outil Python de détection et sensibilisation au phishing

## Description
Phishguard analyse des URLs suspectes et détecte les indicateurs classique de phishing : absence HTTPS, mots suspects, adresses IP cachées, URLs anormalement longues.

Ceci est un projet realisé dans le cadre d'apprentissage autonome de la cybersecurité.

## Fonctionnalités
- Détection HTTP non sécurisé
- Détection de mots suspects (login, verify, secure...)
- Détection d'adresses IP dans l'URL
- Analyse d'URLs trop longues
- Scoring de risque avec verdict
- **Interface web** via Flask

## Utilisation
```bash
python phishguard.py
```
Puis ouvre ton navigateur sur **http://127.0.0.1:5000**

## Technologies
- Python 3
- Flask
- Bibliothèque  're'
- HTML / CSS

## Auteure
Yosr - Etudiante en Prépa, passionnée de cybersecurité.
