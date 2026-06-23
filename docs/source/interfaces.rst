Interfaces et URL
=================

Type d'interface
----------------

OC Lettings ne fournit pas d'API REST.

L'application expose des pages web générées par Django. Les données sont
récupérées par les vues, puis transmises aux templates HTML.

Routes principales
------------------

Page d'accueil
^^^^^^^^^^^^^^

URL :

``/``

Cette page permet d'accéder aux sections principales de l'application.

Liste des locations
^^^^^^^^^^^^^^^^^^^

URL :

``/lettings/``

Cette page affiche l'ensemble des locations disponibles.

Détail d'une location
^^^^^^^^^^^^^^^^^^^^^

URL :

``/lettings/<letting_id>/``

Le paramètre ``letting_id`` correspond à l'identifiant numérique d'une
location.

La vue récupère la location correspondante et affiche son titre ainsi que son
adresse.

Liste des profils
^^^^^^^^^^^^^^^^^

URL :

``/profiles/``

Cette page affiche la liste des profils utilisateurs.

Détail d'un profil
^^^^^^^^^^^^^^^^^^

URL :

``/profiles/<username>/``

Le paramètre ``username`` correspond au nom d'utilisateur associé au profil.

La vue affiche les informations du profil sélectionné, notamment sa ville
favorite.

Interface d'administration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

URL :

``/admin/``

Cette interface est fournie par Django et nécessite un compte administrateur.

Organisation des routes
-----------------------

Les routes principales sont déclarées dans :

``oc_lettings_site/urls.py``

Les routes propres à chaque application sont déclarées dans :

* ``lettings/urls.py`` ;
* ``profiles/urls.py``.

Le fichier principal utilise la fonction ``include()`` afin de déléguer la
gestion des URL à chaque application.

Gestion des erreurs
-------------------

L'application prévoit des pages personnalisées pour les erreurs HTTP
suivantes :

* erreur 404 : ressource introuvable ;
* erreur 500 : erreur interne du serveur.

Les vues d'erreur sont gérées dans le projet ``oc_lettings_site``.
