Guide d'utilisation
===================

Accéder à l'application
-----------------------

En local, l'application est accessible à l'adresse suivante :

``http://127.0.0.1:8000/``

En production, elle est accessible à l'adresse suivante :

``https://oc-lettings-47nw.onrender.com/``

Consulter les locations
-----------------------

Depuis la page d'accueil, ouvrez la section des locations.

La page ``/lettings/`` affiche la liste des locations disponibles.

Sélectionnez une location pour consulter :

* son titre ;
* son adresse complète.

Consulter les profils
---------------------

Depuis la page d'accueil, ouvrez la section des profils.

La page ``/profiles/`` affiche la liste des profils utilisateurs.

Sélectionnez un profil pour consulter :

* le nom de l'utilisateur ;
* sa ville favorite.

Utiliser l'administration Django
--------------------------------

L'interface d'administration est disponible à l'adresse suivante :

``/admin/``

Elle nécessite un compte administrateur créé avec la commande :

.. code-block:: console

   python manage.py createsuperuser

Après authentification, l'administrateur peut gérer les données enregistrées
dans l'application.

Cas d'utilisation principaux
----------------------------

Visiteur
^^^^^^^^

Un visiteur peut :

* afficher la page d'accueil ;
* consulter la liste des locations ;
* consulter le détail d'une location ;
* consulter la liste des profils ;
* consulter le détail d'un profil.

Administrateur
^^^^^^^^^^^^^^

Un administrateur peut :

* se connecter à l'interface d'administration Django ;
* ajouter, modifier ou supprimer des adresses ;
* ajouter, modifier ou supprimer des locations ;
* ajouter, modifier ou supprimer des profils ;
* gérer les utilisateurs Django.

Arrêter l'application locale
----------------------------

Dans le terminal où le serveur de développement est lancé, utilisez :

.. code-block:: text

   Ctrl + C
