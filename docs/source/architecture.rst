Architecture du projet
=======================

Organisation générale
---------------------

Le projet suit une architecture Django modulaire.

La configuration globale reste dans ``oc_lettings_site`` tandis que les
fonctionnalités métier sont réparties dans des applications dédiées.

Structure principale
--------------------

``oc_lettings_site``
   Contient la configuration générale du projet Django, les URL principales,
   la page d'accueil et les pages d'erreur personnalisées.

``lettings``
   Gère les adresses et les locations immobilières.

``profiles``
   Gère les profils associés aux utilisateurs Django.

Répartition des responsabilités
-------------------------------

Chaque application contient ses propres éléments Django :

* modèles dans ``models.py`` ;
* vues dans ``views.py`` ;
* routes dans ``urls.py`` ;
* tests dans ``tests.py`` ou dans un dossier ``tests`` ;
* migrations dans le dossier ``migrations`` ;
* modèles HTML dans le dossier ``templates``.

Routage des URL
---------------

Le fichier ``oc_lettings_site/urls.py`` centralise les routes principales et
inclut les routes propres aux applications ``lettings`` et ``profiles``.

Chaque application possède ainsi son propre fichier ``urls.py`` afin de limiter
le couplage entre les fonctionnalités.

Flux d'une requête
------------------

Lorsqu'un utilisateur accède à une page :

#. Django analyse l'URL demandée ;
#. la route correspondante appelle une vue ;
#. la vue récupère les données nécessaires depuis les modèles ;
#. la vue transmet ces données à un template ;
#. Django génère puis retourne la réponse HTML.

Architecture modulaire
----------------------

La séparation en applications permet :

* d'isoler les responsabilités ;
* de faciliter la maintenance ;
* de limiter les dépendances entre fonctionnalités ;
* de simplifier les tests ;
* de faire évoluer une application sans modifier les autres.

Migration depuis l'ancienne architecture
----------------------------------------

Les modèles autrefois regroupés dans ``oc_lettings_site`` ont été déplacés
dans les applications ``lettings`` et ``profiles``.

Des migrations de données ont été utilisées pour copier les enregistrements
existants vers les nouvelles tables tout en conservant leurs identifiants et
leurs relations.
