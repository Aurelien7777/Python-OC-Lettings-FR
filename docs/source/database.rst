Base de données et modèles
===========================

Base de données
---------------

Le projet utilise SQLite comme base de données.

Le fichier principal est situé à la racine du projet :

``oc-lettings-site.sqlite3``

Django accède aux données par l'intermédiaire de son ORM. Les requêtes SQL
directes ne sont donc pas nécessaires dans le fonctionnement normal de
l'application.

Modèle Address
--------------

Le modèle ``Address`` appartient à l'application ``lettings``.

Il représente l'adresse d'un bien immobilier et contient les informations
suivantes :

* numéro ;
* rue ;
* ville ;
* État ou région ;
* code postal ;
* code du pays.

La table correspondante est :

``lettings_address``

Modèle Letting
--------------

Le modèle ``Letting`` appartient à l'application ``lettings``.

Il représente une location et contient :

* un titre ;
* une relation vers une adresse.

Chaque location est associée à une seule adresse au moyen d'une relation
``OneToOneField``.

La table correspondante est :

``lettings_letting``

Modèle Profile
--------------

Le modèle ``Profile`` appartient à l'application ``profiles``.

Il complète le modèle utilisateur fourni par Django et contient :

* une relation vers un utilisateur Django ;
* une ville favorite.

Chaque profil est associé à un seul utilisateur au moyen d'une relation
``OneToOneField``.

La table correspondante est :

``profiles_profile``

Relations principales
---------------------

Les principales relations de données sont les suivantes :

* un ``Letting`` est lié à un ``Address`` ;
* un ``Profile`` est lié à un utilisateur Django ;
* la suppression d'un objet lié entraîne la suppression de l'objet dépendant
  lorsque l'option ``on_delete=models.CASCADE`` est utilisée.

Migrations
----------

Les migrations Django décrivent les évolutions successives de la base de
données.

Elles sont stockées dans les dossiers suivants :

* ``lettings/migrations`` ;
* ``profiles/migrations`` ;
* ``oc_lettings_site/migrations``.

Lors de la séparation de l'application monolithique, des migrations de données
ont copié les anciens enregistrements vers les nouvelles tables.

Ces migrations ont conservé :

* les identifiants existants ;
* les relations entre les locations et les adresses ;
* les relations entre les profils et les utilisateurs.

Commandes utiles
----------------

Afficher l'état des migrations :

.. code-block:: console

   python manage.py showmigrations

Créer une migration après une modification de modèle :

.. code-block:: console

   python manage.py makemigrations

Appliquer les migrations :

.. code-block:: console

   python manage.py migrate

Ouvrir le shell Django pour consulter les données avec l'ORM :

.. code-block:: console

   python manage.py shell
