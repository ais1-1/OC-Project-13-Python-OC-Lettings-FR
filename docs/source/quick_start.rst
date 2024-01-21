Guide de démarrage rapide
=========================

Créer et activer l'environnement virtuel
----------------------------------------
1. Pointer votre terminal vers le dossier du projet :

    .. code-block:: bash

        cd path/to/the/folder/OC-Project-13-Python-OC-Lettings-FR

2. Créer un environnement virtuel avec le nom venv (vous pouvez également le nommer env; si vous utilisez d'autres noms, veuillez ajouter le nom aux fichiers gitignore et dockerignore) :
    
    .. code-block:: bash

        python -m venv venv

3. Activer l'environnement virtuel

    Pour Linux et MacOS :

    .. code-block:: bash

        source venv/bin/activate

    Pour Windows :

    .. code-block:: bash

        venv\Scripts\activate.bat

.. note::

    Vous pouvez désactiver l'environnement virtuel en utilisant la commande ``deactivate``

Installer les packages nécessaires
----------------------------------

Une fois l'environnement virtuel activé exécuter la commande suivante pour installer les packages :

.. code-block:: bash

    pip install -r requirements.txt

.. _create-venv:

Configurer les variables d'environnement : fichier `.env`
---------------------------------------------------------

Les variables d'environnements sont utilisées pour le stockage les valeurs sensibles. Ils doivent stocker dans le fichier `.env`. Pour l'execution de l'application en local au moin les variables suivantes doivent configuer :

.. code-block:: python
    
    SECRET_KEY
    DEBUG
    ALLOWED_HOSTS

Il y a deux options pour la création du fichier `.env` :

1. En utilisant le fichier `.env.dist`

    Renommer le fichier `.env.dist` de la racine du projet en `.env`.

2. En utilisant le script `create_env_file.py`

    Exécuter le script avec la commande suivante pour créer le fichier `.env` avec certaines valeurs par défaut :

    .. code-block:: bash

        python create_env_file.py

**Une fois le fichier `.env` créé, ouvrez-le avec un éditeur de texte et ajoutez les bonnes valeurs pour chaque variable.**

.. _run-website-runserver:

Exécuter l’Application
----------------------

Utilisez ces étapes pour exécuter l’application après avoir activer l'environnement virtuel (voir `Créer et activer l'environnement virtuel`_) :

1. Lancez le serveur :

    .. code-block:: bash

        cd path/to/the/folder/OC-Project-13-Python-OC-Lettings-FR
        python manage.py runserver

2. Accédez à l’application dans le navigateur de votre choix :

    Aller à l’adresse http://127.0.0.1:8000/ dans le navigateur.
