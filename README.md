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

## Utilisation
```bash
python phishguard.py
```

## Technologies
- Python 3
- Bibliothèque  're'

## Auteure
Yosr - Etudiante en Prépa, passionnée de cybersecurité.
