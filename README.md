# Site web d'Orange County Lettings V2.0

## Table des matières

1. [Description du projet](#description-du-projet)
2. [Développement local](#développement-local)
3. [Déploiement](#déploiement)
4. [Documentation sur Read the Docs](#documentation-read-the-docs)

## Description du projet

L'objectif de ce projet est de mettre à l'échelle une application Django en utilisant une architecture modulaire. Plusieurs parties du site OC Lettings ont été améliorées depuis la première version du projet. Ce dépôt est un fork de cette version qui peut être trouvée à [Python-OC-Lettings-FR](https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR).

Les améliorations apportées sont :
  * Refonte de l'architecture modulaire dans le dépôt GitHub
  * Réduction de diverses dettes techniques sur le projet
  * Ajout d'un pipeline CI/CD ainsi que son déploiement
  * Surveillance de l’application et suivi des erreurs via Sentry
  * Création de la documentation technique de l’application avec Read The Docs et Sphinx


## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce dépôt
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd path/to/the/folder/OC-Project-13-Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd path/to/the/folder/OC-Project-13-Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python create_env_file.py`
- ouvrez le fichier `.env` avec un éditeur de texte et ajoutez les bonnes valeurs pour au moins les variables suivantes : `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd path/to/the/folder/OC-Project-13-Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd path/to/the/folder/OC-Project-13-Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Couverture de test

- `cd path/to/the/folder/OC-Project-13-Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `coverage report -m`

#### Base de données

- `cd path/to/the/folder/OC-Project-13-Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


###  Conteneurisation

1. Créez une image du site pour Docker et transférez-la vers le registre de conteneurs Docker Hub, avec deux balises d'abord avec le hachage de validation, ensuite avec la chaîne « latest » et lancez le site localement en utilisant l'image :

- `chmod +x path/to/build_push_run_docker_image.sh`
- `./build_push_run_docker_image.sh`
- Accédez le site dans un navigateur à http://0.0.0.0:8000/.

2. Récupérer l'image du registre sur votre machine locale et de lancer le site localement en utilisant la dernière image :

- `chmod +x path/to/run_latest_docker_image_locally.sh`
- `./run_latest_docker_image_locally.sh`
- Accédez le site dans un navigateur à http://0.0.0.0:8000/.

Si vous êtes sur Windows, il faut lancer ceci dans [le shell Bash pour Windows](https://learn.microsoft.com/fr-fr/windows/wsl/install).

**Notez que le fichier `.env` est nécessaire pour les valeurs `PORT`, `DOCKER_REPO`, `DOCKER_USER` et `DOCKER_PASSWORD` pour que ces scripts fonctionnent.**


## Déploiement

### Prérequis

Afin d'effectuer le déploiement et l'intégration continue de l'application, les comptes suivants sont nécessaires :

- compte [GitHub](https://github.com/)
- compte [CircleCI](https://circleci.com) (connecté au compte GitHub)
- compte [Docker](https://www.docker.com)
- compte [Heroku](https://www.heroku.com)
- compte [Sentry](https://sentry.io/welcome/)

### Description

Le déploiement de l'application est automatisé par un pipeline CircleCI. Lorsque l'on push des modifications sur le dépôt GitHub, le pipeline déclenche l'exécution des tests et du linting du code. Ces opérations sont effectuées sur **toutes les branches du projet**.

Si des modifications sont apportées à la branche **master**, et **si et seulement si** les tests et le linting sont réussis, les opérations suivantes sont déclenchées :

- Création d'une image Docker et dépôt sur DockerHub
- **Si et seulement si** l'étape précédente est réussie, déploiement de l'application sur Heroku

### Configuration

#### CircleCI

Après avoir récupéré le projet, mis en place l'environnement de développement local (voir [Développement local](#développement-local)) et créé les comptes requis, initialiser un projet sur CircleCI via *Create Project*. Voir [la documentation CircleCI](https://circleci.com/docs/getting-started/#) pour plus de détails. 

Le point crucial pour connecter CircleCI à notre projet est un `config.yml`, qui se trouve dans un répertoire `.circleci`. Une fois le projet prêt. Il faut ajouter les variables d'environnement suivantes dans les paramètres du projet CircleCI - *Project Settings* > *Environment Variables* (voir la partie [Définir les variables d'environnement](https://circleci.com/docs/set-environment-variable/#set-an-environment-variable-in-a-project) de la documentation CircleCI pour les détails) :


| Variable CircleCI | Description                                                                                                                                                                                                               |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SECRET_KEY | Clé secrète Django : générer une clé aléatoire avec [Djecrety](https://djecrety.ir) ou via la commande <br/> `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` |
| SENTRY_DSN        | URL du projet Sentry (voir [Sentry](#sentry))                                                                                                                                                                             |
| DOCKER_USER      | Nom d'utilisateur du compte Docker                                                                                                                                                                                        |
| DOCKER_PASSWORD   | Mot de passe du compte Docker                                                                                                                                                                                             |
| DOCKER_REPO       | Nom du repository sur DockerHub                                                                                                                                                                                           |
| HEROKU_APP_NAME   | Nom de l'application Heroku : l'application déployée sera accessible via `https://<HEROKU_APP_NAME>.<IDENTIFIER>.herokuapp.com/`                                                                                                       |
| HEROKU_API_KEY      | Token Heroku, disponible dans les paramètres du compte (*Heroku API Key*)                                                                                                                                                 |
| DEBUG      | Un booléen qui active/désactive le mode débogage pour Django 
| ALLOWED_HOSTS      | Une liste de chaînes représentant les noms d'hôte/domaine que ce site Django peut servir
| PORT      | Port à exposer pour exécuter des images Docker localement


#### Docker

Créer un dépôt sur DockerHub. Le nom du dépôt doit correspondre à la variable *DOCKER_REPO* définie pour CircleCI.

Le workflow de CircleCI va créer et déposer l'image de l'application dans le repository DockerHub défini.

Dans `.circleci/config.yml`, on tague les images avec deux noms d’image, `TAG` et `LATEST`, tous deux sont construits à partir de la variable d’environnement `DOCKER_REPO`, `TAG` ajoute le `CIRCLE_SHA1` au nom du dépôt Docker et le second ajoute le mot-clé « latest ». Notez que `CIRCLE_SHA1` est une variable d’environnement intégrée de CircleCI. Quel est le hachage SHA1 du dernier commit de la version actuelle.

#### Heroku

Tout d’abord, vous devrez créer l’application dans Heroku, en utilisant le site Web Heroku. Pour créer une application rendez-vous sur le Dashboard, cliquez sur *New* et *Create new app*. Le nom de l'application doit correspondre à la variable *HEROKU_APP_NAME* définie pour CircleCI.

Une fois l'application est prêt, le jeton Heroku, `HEROKU_API_KEY`, est disponible dans les paramètres du compte avec le nom *Heroku API Key*. Il ne faut pas oublier d’ajouter cette variable dans les variables d’environnement CircleCI.

#### Sentry

Pour utiliser Sentry et pouvoir utiliser le monitoring sur le projet accédé à votre compte.

  * Créer un nouveau projet
  * Choisissez une plateforme pour le projet, dans notre cas Django.
  * Choisissez une équipe pour votre projet ensuite cliquer sur : `Créer un projet`
  * Une fois le projet créé, vous pourrez récupérer la clé `SENTRY_DSN` dans `Project Settings > Client Keys (DSN)` à intégrer dans le fichier `.env`

Une fois toutes ces étapes exécutées et le serveur local lancer, vous pourrez visualiser sur Sentry l’activité de l’application.

La journalisation Sentry peut être testée en naviguant vers ``/sentry-debug/``, localement et sur l'application déployée via ``https://<HEROKU_APP_NAME>-<IDENTIFIER>.herokuapp.com/sentry-debug/``. Ce point de terminaison provoque une ``ZeroDivisionError``.

## Documentation Read the Docs

La documentation complète est disponible à l'adresse (https://oc-project-13-python-oc-lettings-fr.readthedocs.io/en/latest/).

Vous trouverez toutes les informations essentielles pour comprendre et travailler avec ce projet.

