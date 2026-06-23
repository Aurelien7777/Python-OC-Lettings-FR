Déploiement
===========

Vue d'ensemble
--------------

Le déploiement de l'application repose sur les services suivants :

* GitHub Actions pour exécuter la CI/CD ;
* Docker pour construire l'image de l'application ;
* Docker Hub pour stocker l'image ;
* Render pour héberger l'application.

Le déploiement en production est déclenché uniquement depuis la branche
``master``.

Conteneurisation
----------------

Le fichier ``Dockerfile`` situé à la racine du projet décrit l'image Docker de
l'application.

L'image :

* installe les dépendances Python ;
* copie le code du projet ;
* collecte les fichiers statiques ;
* lance l'application avec Gunicorn ;
* expose le port utilisé par le service.

Construire l'image localement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Depuis la racine du projet :

.. code-block:: console

   docker build -t oc-lettings:local .

Lancer le conteneur localement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   docker run --rm -p 8000:8000       -e SECRET_KEY=django-insecure-local       -e DEBUG=False       -e ALLOWED_HOSTS=localhost,127.0.0.1       oc-lettings:local

Sous PowerShell, la commande peut être écrite sur une seule ligne :

.. code-block:: powershell

   docker run --rm -p 8000:8000 -e SECRET_KEY=django-insecure-local -e DEBUG=False -e ALLOWED_HOSTS=localhost,127.0.0.1 oc-lettings:local

L'application est alors accessible à l'adresse suivante :

``http://127.0.0.1:8000/``

Pipeline CI/CD
--------------

Le workflow GitHub Actions est stocké dans le dossier :

``.github/workflows``

Il comporte trois étapes principales.

Tests
^^^^^

À chaque ``push`` et à chaque ``pull_request``, la CI :

#. installe les dépendances ;
#. exécute les tests Django avec ``coverage`` ;
#. vérifie que la couverture est au moins égale à 80 % ;
#. exécute ``flake8``.

Les commandes principales sont :

.. code-block:: console

   coverage run manage.py test
   coverage report --fail-under=80
   flake8

Construction et publication de l'image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lorsque les tests réussissent sur la branche ``master``, le workflow :

#. construit l'image Docker ;
#. se connecte à Docker Hub ;
#. publie l'image avec le tag ``latest`` ;
#. publie également une image identifiée par le SHA du commit.

Image de production :

``docker.io/aurelienamorin/oc-lettings:latest``

Déploiement sur Render
^^^^^^^^^^^^^^^^^^^^^^

Après la publication de l'image Docker, GitHub Actions appelle le deploy hook
fourni par Render.

Render récupère alors la nouvelle image ``latest`` depuis Docker Hub et
redémarre le service avec cette version.

Variables d'environnement
-------------------------

Les variables suivantes doivent être configurées sur Render :

``SECRET_KEY``
   Clé secrète Django utilisée en production.

``DEBUG``
   Doit être définie à ``False``.

``ALLOWED_HOSTS``
   Doit contenir le nom d'hôte du service Render.

``SENTRY_DSN``
   DSN du projet Sentry.

``SENTRY_ENVIRONMENT``
   Environnement transmis à Sentry, par exemple ``production``.

``PORT``
   Port fourni au conteneur par Render.

Les secrets utilisés par GitHub Actions, notamment les identifiants Docker Hub
et l'URL du deploy hook Render, doivent être enregistrés dans les secrets du
dépôt GitHub.

Fichiers statiques
------------------

WhiteNoise sert les fichiers statiques en production.

La commande suivante collecte les fichiers statiques avant le lancement de
l'application :

.. code-block:: console

   python manage.py collectstatic --noinput

Application en production
-------------------------

L'application déployée est accessible à l'adresse suivante :

``https://oc-lettings-47nw.onrender.com/``

Vérifications après déploiement
-------------------------------

Après chaque déploiement, vérifiez :

* l'affichage de la page d'accueil ;
* la navigation vers les locations et les profils ;
* l'accès à l'interface d'administration ;
* le chargement des fichiers statiques ;
* l'absence d'erreurs dans les journaux Render ;
* la remontée des erreurs dans Sentry.
