"""
Créer un fichier .env avec une clé secrète générée aléatoirement et
des variables d'environnement préconfigurées. Voir le fichier
.env.dist pour l'exemple.

Les noms de variables d'environnement préconfigurés sont :

    - SECRET_KEY
    - DEBUG
    - ALLOWED_HOSTS
    - SENTRY_DSN
    - DOCKER_USER
    - DOCKER_PASSWORD
    - DOCKER_REPO
    - HEROKU_APP_NAME
    - PORT

Le fichier .env généré doit être configuré avec des valeurs appropriées
pour chaque variable d'environnement avant utilisation.

Exemple d'utilisation :

    1. Exécutez ce script pour générer un fichier .env.
    2. Configurez les valeurs des variables d'environnement
       dans le fichier .env généré.
    3. Utilisez le fichier .env pour configurer
       l'environnement de votre application oc_lettings_site.

.. note::
    Remarque :
    Le fichier .env généré ne doit pas être partagé publiquement
    car il contient des informations sensibles.

"""

from django.core.management.utils import get_random_secret_key

# Liste des noms de variables d'environnement
env_variable_names = [
    "SECRET_KEY",
    "DEBUG",
    "ALLOWED_HOSTS",
    "PORT",
    "SENTRY_DSN",
    "DOCKER_USER",
    "DOCKER_PASSWORD",
    "DOCKER_REPO",
    "HEROKU_APP_NAME",
]

# Générer la clé secrète aléatoire
secret_key = get_random_secret_key()
debug = True
port = 8000
allowed_hosts = "*"

# Ouvrir le fichier .env en mode écriture
try:
    with open(".env", "w") as f:
        # Écrire les noms des variables d'environnement avec leurs valeurs
        f.write(f"DEBUG={debug}\n")
        f.write(f"SECRET_KEY={secret_key}\n")
        f.write(f"PORT={port}\n")
        f.write(f"ALLOWED_HOSTS={allowed_hosts}\n")
        for env_var in env_variable_names[4:]:
            f.write(f"{env_var}=\n")
except IOError as e:
    print(f"Couldn't write to file ({e})")
else:
    # Afficher un message indiquant que le modèle de fichier .env a été créé
    print(f".env file has created successfully!")
