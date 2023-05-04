# README ProjetPro1

Ce projet est une boîte à outils de cybersécurité qui comprend plusieurs fonctionnalités pour surveiller et tester la sécurité de votre SI. 

Les fonctionnalités incluent :

1. Scanner les vulnérabilités avec Nmap
2. Simuler une attaque avec Metasploit
3. Récupérer les vulnérabilités critiques
4. Vérifier les fuites d'emails avec l'API Have I Been Pwned
5. Générer un tableau de bord de sécurité
6. Effacer tous les fichiers de résultats et de journaux

## Prérequis

## Installation de Metasploit Framework

1. Mettez à jour votre système:
sudo apt update && sudo apt upgrade

2. Installez les dépendances requises:
sudo apt install -y curl git gnupg2 postgresql pip

3. Ajoutez le référentiel Metasploit Framework:
curl -fsSL https://apt.metasploit.com/metasploit-framework.gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/metasploit-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/metasploit-archive-keyring.gpg] https://apt.metasploit.com/ $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/metasploit-framework.list

4. Installez Metasploit Framework:
sudo apt update
sudo apt install metasploit-framework

## Configuration de msfrpcd (Metasploit RPC Daemon)

1. Configurez la base de données PostgreSQL pour Metasploit:
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo msfdb init

2. Démarrez msfrpcd avec le mot de passe de votre choix (remplacez `my_password` par un mot de passe de votre choix):
msfrpcd -P password -S -f

Maintenant, msfrpcd est en cours d'exécution et vous pouvez interagir avec lui à l'aide de la bibliothèque python-metasploit. Assurez-vous de modifier le mot de passe dans le script `metasploit_scan.py` pour correspondre au mot de passe que vous avez défini pour msfrpcd.

## Installation

Clonez ce dépôt GitHub sur votre machine locale :

git clone https://github.com/Kagath/ProjetPro1.git

pip install -r requirements.txt

./msfrpcd -P password -n -f -a 127.0.0.1

## Utilisation

Exécutez le fichier `main.py` pour lancer le programme :

python main.py

Sélectionnez la fonctionnalité souhaitée à partir du menu affiché et suivez les instructions à l'écran.

Les résultats des différentes fonctionnalités seront enregistrés dans le sous-dossier `results`, et les logs d'exécution seront enregistrés dans le sous-dossier `logs`.

## Licence

Ce projet est publié sous licence MIT. 
Voir le fichier `LICENSE` pour plus d'informations.
