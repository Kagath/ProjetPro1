# README ProjetPro1

Ce projet est une boîte à outils de cybersécurité qui comprend plusieurs fonctionnalités pour tester et surveiller la sécurité de votre réseau. Les fonctionnalités incluent :

1. Scanner les vulnérabilités avec Nmap
2. Simuler une attaque avec Metasploit
3. Récupérer les vulnérabilités critiques (scrapping NVD)
4. Vérifier les fuites d'emails avec l'API Have I Been Pwned
5. Générer un tableau de bord de sécurité

## Installation

Clonez ce dépôt GitHub sur votre machine locale :

git clone [https://github.com/Kagath/ProjetPro1.git]

pip install -r requirements.txt

## Utilisation

Exécutez le fichier `main.py` pour lancer le programme :

python main.py

Sélectionnez la fonctionnalité souhaitée à partir du menu affiché et suivez les instructions à l'écran.

Les résultats des différentes fonctionnalités seront enregistrés dans le sous-dossier `results`, et les logs d'exécution seront enregistrés dans le sous-dossier `logs`.

## Licence

Ce projet est publié sous licence MIT. Voir le fichier `LICENSE` pour plus d'informations.
