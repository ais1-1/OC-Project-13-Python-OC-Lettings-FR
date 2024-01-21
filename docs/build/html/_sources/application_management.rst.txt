Gestion de l'application - Django Admin
=======================================

Se connecter sur le sit de gestion
----------------------------------

L’interface d’administration de Django est accessible en naviguant vers ``/admin/``, localement (avec :ref:`runserver <run-website-runserver>` ou :ref:`une image Docker <run-website-docker>`) et sur l'application déployée via ``https://<HEROKU_APP_NAME>-<IDENTIFIER>.herokuapp.com/admin/``.

.. note:: 

    * nom d’utilisateur : admin
    * mots de passe : Abc1234!

.. image:: _static/django_admin_login.png
  :width: 800
  :alt: Django admin - login page

Créer et gérer des éléments
---------------------------

Pour créer et gérer des utilisateurs (*Users*), *Lettings*, *Profiles* et *Addresses*, rendez-vous sur le site de gestion. Une fois connecté, vous aurez accès à toutes les ressources via les titres correspondants depuis la page d'accueil d'administration :

.. image:: _static/django_admin_home.png
  :width: 800
  :alt: Django admin - home page