Installation
============

Prérequis
---------

L'installation locale nécessite les outils suivants :

* Git ;
* Python 3.7 ;
* ``pip`` ;
* le module Python ``venv`` ;
* SQLite 3, uniquement pour consulter directement la base de données.

Le projet doit être exécuté avec Python 3.7 afin de conserver sa compatibilité
avec Django 3.0.

Cloner le dépôt
---------------

Placez-vous dans le dossier où le projet doit être installé, puis clonez le
dépôt GitHub :

.. code-block:: console

   git clone https://github.com/Aurelien7777/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR

Remplacez l'URL par celle du dépôt GitHub public du projet.

Créer l'environnement virtuel
-----------------------------

Windows
^^^^^^^

Créez l'environnement virtuel avec Python 3.7 :

.. code-block:: powershell

   py -3.7 -m venv venv

Activez-le :

.. code-block:: powershell

   .\venv\Scripts\Activate.ps1

Vérifiez la version et l'interpréteur utilisés :

.. code-block:: powershell

   python --version
   (Get-Command python).Path

macOS et Linux
^^^^^^^^^^^^^^

Créez l'environnement virtuel :

.. code-block:: console

   python3.7 -m venv venv

Activez-le :

.. code-block:: console

   source venv/bin/activate

Vérifiez la version et l'interpréteur utilisés :

.. code-block:: console

   python --version
   which python

Installer les dépendances
-------------------------

Depuis la racine du projet :

.. code-block:: console

   python -m pip install --upgrade pip
   pip install -r requirements.txt

Configurer les variables d'environnement
-----------------------------------------

Créez un fichier ``.env`` à la racine du projet :

.. code-block:: text

   SECRET_KEY=replace-with-a-local-secret-key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   SENTRY_ENVIRONMENT=development

Pour activer Sentry localement, ajoutez également :

.. code-block:: text

   SENTRY_DSN=replace-with-your-sentry-dsn

Le fichier ``.env`` contient des données sensibles et ne doit jamais être
ajouté au dépôt Git.

Appliquer les migrations
------------------------

Exécutez les migrations Django :

.. code-block:: console

   python manage.py migrate

Cette commande crée ou met à jour les tables de la base de données selon
l'historique des migrations.

Lancer l'application
--------------------

Démarrez le serveur de développement :

.. code-block:: console

   python manage.py runserver

L'application est ensuite accessible à l'adresse suivante :

http://127.0.0.1:8000/

Créer un compte administrateur
------------------------------

Créez un compte administrateur local :

.. code-block:: console

   python manage.py createsuperuser

L'interface d'administration est disponible à l'adresse suivante :

http://127.0.0.1:8000/admin/

Vérifier l'installation
-----------------------

Vérifiez la configuration Django :

.. code-block:: console

   python manage.py check

Lancez les tests avec la mesure de couverture :

.. code-block:: console

   coverage run manage.py test

Vérifiez le linting :

.. code-block:: console

   flake8

Affichez le rapport de couverture et vérifiez que le seuil minimum de 80 % est
respecté :

.. code-block:: console

   coverage report --fail-under=80