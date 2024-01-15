Description du projet
=====================

Orange County Lettings site web 2.0 a été créé pour répondre aux besoins de la start-up Orange County Lettings.

L'entreprise étant en pleine phase d’expansion, a décidé d'améliorer le site. Pour cela, les modifications suivantes ont été apportées :

    * Refonte de l'architecture modulaire dans le repository GitHub ;
        * Reorganiser le code en 3 applications lettings, profiles et home pour séparer les fonctionnalités de l'application.
    * Réduction de diverses dettes techniques sur le projet ;
        * Corriger les erreurs de linting ;
        * Corriger la pluralisation des noms de modèles dans le site d'administration ;
        * Des pages personnalisées en cas d’erreur 404 ou 500 ;
        * Une docstring sur chaque module, classe et fonction ;
        * Une couverture de test supérieure à 80 %.
    * Ajout d'un pipeline CI/CD avec `CircleCI`_ et déploiement sur `Heroku`_ ;
        * Compilation et tests : exécuter le linting et la suite de tests (sur toutes les branches);
        * Conteneurisation : construire une image du site avec `Docker`_ et push vers `Docker Hub`_ (si étape i. réussie, branche master uniquement) ;
        * Déploiement : mettre en service le site avec Heroku (si étape ii. réussie, branche master uniquement).
    * Surveillance de l’application et suivi des erreurs via `Sentry`_ ; 
    * Création de la documentation technique de l’application avec `Read the Docs`_ et `Sphinx`_.


.. _CircleCI: https://circleci.com/
.. _Heroku: https://www.heroku.com/
.. _Sentry: https://sentry.io/welcome/
.. _Docker: https://www.docker.com/
.. _Docker Hub: https://hub.docker.com/
.. _Read the Docs: https://about.readthedocs.com/
.. _Sphinx: https://www.sphinx-doc.org/fr/master/