Démarrage rapide
================

Cette section suppose que l'installation et la configuration du projet ont
déjà été effectuées.

Activer l'environnement virtuel
-------------------------------

Sous Windows :

.. code-block:: powershell

   .\venv\Scripts\Activate.ps1

Sous macOS ou Linux :

.. code-block:: console

   source venv/bin/activate

Préparer la base de données
---------------------------

Depuis la racine du projet, appliquez les migrations Django :

.. code-block:: console

   python manage.py migrate

Lancer le serveur
-----------------

Démarrez le serveur de développement :

.. code-block:: console

   python manage.py runserver

Le serveur est alors accessible à l'adresse suivante :

http://127.0.0.1:8000/

Pages principales
-----------------

Les principales pages de l'application sont :

* accueil : http://127.0.0.1:8000/ ;
* locations : http://127.0.0.1:8000/lettings/ ;
* profils : http://127.0.0.1:8000/profiles/ ;
* administration : http://127.0.0.1:8000/admin/.

Arrêter le serveur
------------------

Dans le terminal où le serveur est lancé, utilisez la combinaison suivante :

.. code-block:: text

   Ctrl + C
