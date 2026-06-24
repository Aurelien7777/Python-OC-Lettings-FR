Présentation du projet
======================

Contexte
--------

OC Lettings est une application web développée avec Django pour une entreprise
spécialisée dans la location de biens immobiliers.

OPENCLASSROOMS APRES WEBOOK

L'application permet de consulter :

* la liste des locations disponibles ;
* les informations détaillées de chaque location ;
* la liste des profils utilisateurs ;
* les informations associées à chaque profil ;
* l'interface d'administration Django.

Objectifs du projet
-------------------

Le projet consiste à améliorer une application Django existante sans modifier
son apparence ni ses fonctionnalités principales.

Les objectifs techniques sont les suivants :

* remplacer l'architecture monolithique par une architecture modulaire ;
* séparer les fonctionnalités dans les applications ``lettings`` et ``profiles`` ;
* migrer les données existantes avec les migrations Django ;
* améliorer la qualité du code avec le linting, les tests et les docstrings ;
* atteindre une couverture de tests supérieure à 80 % ;
* intégrer Sentry pour la surveillance des erreurs et des logs ;
* conteneuriser l'application avec Docker ;
* mettre en place un pipeline CI/CD avec GitHub Actions ;
* publier l'image de production sur Docker Hub ;
* déployer l'application sur Render ;
* publier la documentation technique avec Sphinx et Read the Docs.

Architecture fonctionnelle
---------------------------

L'application est organisée autour de trois composants principaux :

``oc_lettings_site``
   Contient la configuration générale du projet, la page d'accueil et les pages
   d'erreur personnalisées.

``lettings``
   Gère les adresses et les locations immobilières.

``profiles``
   Gère les profils associés aux utilisateurs Django.

Application en production
-------------------------

L'application est accessible à l'adresse suivante :

https://oc-lettings-47nw.onrender.com
