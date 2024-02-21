## 🌐 Présentation du Projet

### 🎯 Objectif du Projet "Seahawks Monitoring"

La société "NFL IT" souhaite améliorer son efficacité opérationnelle en concevant une solution de maintenance à distance. Le projet vise à collecter des informations techniques et à assurer la maintenance à distance des réseaux locaux des franchises de la NFL.

### Seahawks Harvester

Permet d'afficher sur une interface WEB, la liste de tout les Seahawks Harvester et pouvoir voir le résultat du dernier scan réseau. 

(Voir https://github.com/NxRitsu/SeahawksHarvesterMSPR-E6.1)
 
## 🚀 Comment utiliser l’Application web Seahawks Nester ?

⚠️ Uniquemnent sous distribution Debian ⚠️

1. Télécharger les fichiers :

```
git clone https://github.com/NxRitsu/SeahawksNesterMSPR-E6.1
```

2. Exécuter la commande suivante (dans le dossier dossier téléchargé) :
```
make
```
Cela va alors télécharger tout les paquets nécessaire au bon fonctionnement

3. Exécutez cette commande pour lancer l'application graphique Python :

```
python3 ./app.py
```

Cela exécutera l'application Seahawks Nester dont l'interface web est accessible à l'adresse suivante : http://127.0.0.1:5000 
