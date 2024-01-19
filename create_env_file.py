"""
Create an .env file with a randomly generated secret key and
preconfigured environment variables. View file
.env.dist for the example.

The preconfigured environment variable names are:

    - SECRET_KEY
    - DEBUG
    - ALLOWED_HOSTS
    - SENTRY_DSN
    - DOCKER_USER
    - DOCKER_PASSWORD
    - DOCKER_REPO
    - HEROKU_APP_NAME
    - PORT

The generated .env file must be configured with appropriate values
for each environment variable before use.

Example of use :

    1. Run this script to generate an .env file.
    2. Configure environment variable values
       in the generated .env file.
    3. Use the .env file to configure
       the environment of your oc_lettings_site application.

.. note::
    The generated .env file should not be shared publicly
    because it contains sensitive information.

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
