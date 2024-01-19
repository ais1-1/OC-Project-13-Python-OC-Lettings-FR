Guide d’utilisation
===================

Linting
-------
Le projet utilise le module flake8 pour linting. Flake8 a été configuré pour permettre une longueur maximale de ligne de code jusqu'à 99 caractères. Et il ne lintera pas dans les dossiers de migrations et d’environnement virtuel. Ces comportements sont obtenus grâce à des lignes suivantes du fichier ``setup.cfg`` :

.. code-block:: cfg

    [flake8]
    max-line-length = 99
    exclude = **/migrations/*,venv, env

Exécutez le linting à l'aide des commandes suivantes :

.. code-block:: bash

    # Déplacer à la racine du dossier
    cd path/to/the/folder/OC-Project-13-Python-OC-Lettings-FR
    # Activer l'environnement virtuel
    source venv/bin/activate
    # Faire le linting
    flake8

Tests unitaires
----------------
Le projet utilise le module pytest pour les tests. Les tests correspondant à chaque application (home, lettings et profiles) sont regroupés dans des dossiers de mêmes noms sous le dossier ``tests/unit_tests``. Les tests unitaires sont écrits avec des classes.

La configuration pytest peut être vue dans le fichier ``setup.cfg`` sous la ligne ``[tool:pytest]``.

Lancez des tests à l'aide des commandes suivantes :

.. code-block:: bash

    # Déplacer à la racine du dossier
    cd path/to/the/folder/OC-Project-13-Python-OC-Lettings-FR
    # Activer l'environnement virtuel
    source venv/bin/activate
    # Lancer le test
    pytest


Couverture de test
------------------
Le projet utilise Coverage.py et pytest-cov (plugin Coverage.py pour pytest) pour une meilleur lecture du couverture.

La configuration de la couverture, comme les fichiers à exclure, se trouve dans le fichier ``.coveragerc``.

Pour voir le rapport de couverture sur le terminal :

.. code-block:: bash

    # Déplacer à la racine du dossier
    cd path/to/the/folder/OC-Project-13-Python-OC-Lettings-FR
    coverage report -m

Pour voir le rapport avec une rapport de test :

.. code-block:: bash

    # Déplacer à la racine du dossier
    cd path/to/the/folder/OC-Project-13-Python-OC-Lettings-FR
    pytest --cov=.


Utilisation de Sentry 
---------------------
* Configuration

Pour utiliser Sentry et pouvoir utiliser le monitoring sur le projet accédé à votre compte ( si vous n'en avez pas encore une, `créer un compte Sentry <https://sentry.io/signup/>`_).

    * Créer un nouveau projet

    * Choisissez une plateforme pour le projet, dans notre cas Django.

    * Choisissez une équipe pour votre projet ensuite cliquer sur : Créer un projet

    * Une fois le projet créé, vous pourrez récupérer la clé ``SENTRY_DSN`` dans ``Project Settings > Client Keys (DSN)`` à intégrer dans le fichier ``.env``

Une fois toutes ces étapes exécutées et le serveur local lancer, vous pourrez visualiser sur Sentry l’activité de l’application.

La journalisation Sentry peut être testée en naviguant vers ``/sentry-debug/``, localement et sur l'application déployée via ``https://<HEROKU_APP_NAME>-<IDENTIFIER>.herokuapp.com/sentry-debug/``. Ce point de terminaison provoque une ``ZeroDivisionError``. Voici un exemple :

.. image:: _static/sentry_zero_division_error.png
  :width: 600
  :alt: ZeroDivisionError in Sentry

.. note:: Pour collaborer sur un projet, vous devez créer des équipes et accorder des autorisations dans la configuration Sentry. Consultez `la documentation officielle de Sentry <https://docs.sentry.io/product/accounts/membership/>`_ pour plus de détails.

* Logging

Pour compléter la gestion des erreurs en insérant des logs appropriés dans le code, ce projet utilise le module de logging de Python. Le logging Python est prise en charge par Sentry avec le module ``sentry-sdk`` installé. Ces logs doivent être placés aux endroits stratégiques du code, tels que les fonctions critiques, les blocs try/except et les points de validation des données.

Voici un extrait de code depuis le projet (``lettings/views.py``). Notez la partie ``except`` pour l'exemple de l'utilisation de ``logging`` :

.. code-block:: python

    def letting(request, letting_id):
    """Detailed view of a letting.
    Parameters:
    letting_id (int): id of a letting"""
        try:
            letting = get_object_or_404(Letting, id=letting_id)
            context = {
                "title": letting.title,
                "address": letting.address,
            }
            return render(request, "lettings/letting.html", context)
        except Exception as e:
            logging.error(str(e))
            return render(request, "error.html", {"message": str(e)}, status=404)


Voyez lire `la documentation officielle <https://docs.sentry.io/platforms/python/integrations/logging/>`_ pour plus d'exemple.

Utilisation de Docker
----------------------
* Construire et taguer une image du site
    1. `Téléchargez et installez Docker <https://docs.docker.com/get-docker/>`_ 

    2. Accédez au répertoire du projet :
    
    .. code-block:: bash

        cd path/to/the/folder/OC-Project-13-Python-OC-Lettings-FR

    3. Assurez-vous que le ``Dockerfile`` et le ``.dockerignore`` (ce fichier est utilisé pour exclure les dossiers inutiles comme venv lors de la création de l'image) sont présents dans le répertoire.

    4. Assurez-vous que le fichier ``.env`` a été préalablement créé (voir :ref:`create-venv`)

    5. Construisez l'image  avec le nom de l'image souhaitée :

    .. code-block:: bash

        docker build -t <image-name> .

* Pousser l'image vers le DockerHub

    1. Créer un compte sur DockerHub (`la page de connexion <https://hub.docker.com/signup>`_).

    2. Connectez-vous avec la commande suivante :

    .. code-block:: bash 

        docker login --username <username> --password-stdin
    
        Vous pouvez taper le mot de passe ensuite dans le terminal.

    3. Pousser l'image :

    .. code-block:: bash 

        docker push <image-name>

* Lancer le site localement avec un image Docker

Il y a trois façon pour lancer le site avec un image Docker.

    * Avec l'image que vous avez construit :

        1. Lancer un conteneur docker avec l'image que vous avez construit :

        .. code-block:: bash 

            docker run --env-file .env --name <container_name> -p 8000:8000 -it -d <image_name>
        
        Le fichier ``.env`` est nécessaire pour la valeur ``PORT`` dans le ``Dockerfile``
        
        2. Accédez le site dans un navigateur à http://0.0.0.0:8000/.

    * Avec la dernière image disponible du registre DockerHub

        1. Connectez-vous avec la commande suivante :

        .. code-block:: bash 

            docker login --username <username> --password-stdin
        
        2. Extraire la dernière image :

        .. code-block:: bash 

            docker pull <image_name>
        
        3. Lancer un conteneur docker :

        .. code-block:: bash 

            docker run --env-file .env --name <container_name> -p 8000:8000 -it -d <image_name>
                
        4. Accédez le site dans un navigateur à http://0.0.0.0:8000/.

    * Utiliser le script Bash ``run_latest_docker_image_locally.sh`` comme ceci :

        1. Donner la permission au script de s'exécuter :

        .. code-block:: bash 
            
            chmod +x path/to/run_latest_docker_image_locally.sh

        2. Executer le script :

        .. code-block:: bash

            ./run_latest_docker_image_locally.sh
        
        .. note:: Si vous êtes sur Windows, il faut lancer ceci dans `le shell Bash pour Windows <https://learn.microsoft.com/fr-fr/windows/wsl/install>`_.


Utilisation de CircleCI
-----------------------
* Configuration

Utilisation de Heroku 
----------------------
* Configuration