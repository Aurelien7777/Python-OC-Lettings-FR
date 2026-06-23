Technologies utilisées
=======================

Langage et framework
--------------------

Le projet utilise les technologies principales suivantes :

* Python 3.7 ;
* Django 3.0 ;
* HTML et CSS pour les modèles de pages ;
* SQLite comme base de données.

Qualité du code et tests
------------------------

Les outils suivants sont utilisés pour vérifier la qualité du projet :

* ``flake8`` pour le contrôle du style du code ;
* le test runner intégré à Django pour exécuter les tests ;
* ``coverage`` pour mesurer la couverture des tests ;
* un seuil minimal de couverture fixé à 80 % dans la CI.

Configuration et surveillance
-----------------------------

Le projet utilise également :

* ``python-dotenv`` pour charger les variables d'environnement ;
* Sentry pour la surveillance des erreurs et la journalisation ;
* ``gunicorn`` comme serveur WSGI en production ;
* WhiteNoise pour servir les fichiers statiques.

Conteneurisation et déploiement
-------------------------------

Le déploiement repose sur :

* Docker pour construire l'image de l'application ;
* Docker Hub pour stocker l'image ;
* GitHub Actions pour exécuter la CI/CD ;
* Render pour héberger l'application.

Documentation
-------------

La documentation est construite avec :

* Sphinx ;
* le thème ``sphinx_rtd_theme`` ;
* Read the Docs pour la publication en ligne.
