Surveillance et journalisation
==============================

Objectif
--------

L'application utilise Sentry pour surveiller les erreurs rencontrées en
production et centraliser les informations utiles au diagnostic.

Configuration de Sentry
-----------------------

L'initialisation de Sentry est regroupée dans le module ``monitoring.py``.

La configuration utilise principalement les variables d'environnement
suivantes :

``SENTRY_DSN``
   Identifie le projet Sentry auquel les événements sont envoyés.

``SENTRY_ENVIRONMENT``
   Indique l'environnement d'exécution, par exemple ``development`` ou
   ``production``.

Si ``SENTRY_DSN`` n'est pas défini, l'application peut fonctionner sans envoyer
d'événement à Sentry.

Protection des données
----------------------

L'option ``send_default_pii`` est désactivée afin de ne pas transmettre
automatiquement les données personnelles des utilisateurs.

Les mots de passe, clés secrètes, jetons et autres données sensibles ne doivent
jamais être écrits dans les journaux.

Erreurs surveillées
-------------------

Sentry enregistre les exceptions non gérées qui surviennent pendant
l'exécution de l'application.

Un événement contient notamment :

* le type de l'exception ;
* le message d'erreur ;
* la trace d'exécution ;
* l'environnement concerné ;
* la version ou le contexte disponible au moment de l'erreur.

Journalisation
--------------

L'application utilise également le module ``logging`` de Python pour produire
des messages de journalisation.

Les niveaux principaux sont :

``DEBUG``
   Informations détaillées utiles pendant le développement.

``INFO``
   Informations décrivant le fonctionnement normal de l'application.

``WARNING``
   Situation inhabituelle qui ne bloque pas nécessairement l'application.

``ERROR``
   Erreur empêchant l'exécution normale d'une opération.

``CRITICAL``
   Erreur grave pouvant empêcher l'application de fonctionner.

Consulter les événements
------------------------

Les erreurs envoyées à Sentry sont consultables depuis le tableau de bord du
projet Sentry.

Les journaux du conteneur et du service sont également disponibles dans
l'interface Render.

Lors de l'analyse d'un incident, vérifiez :

#. le message d'erreur ;
#. la trace d'exécution ;
#. l'environnement concerné ;
#. l'heure de l'événement ;
#. les journaux Render associés.

Tester la surveillance
----------------------

Un test de surveillance peut être effectué dans un environnement contrôlé en
provoquant volontairement une exception.

Après le test, vérifiez que :

* l'événement apparaît dans Sentry ;
* l'environnement indiqué est correct ;
* aucune donnée sensible n'est transmise ;
* l'application continue de fonctionner normalement après correction.

Maintenance
-----------

Lors d'une évolution de l'application :

* conservez le DSN dans les variables d'environnement ;
* ne placez jamais le DSN ou la clé secrète directement dans le code ;
* utilisez des messages de logs précis et utiles ;
* évitez les messages redondants ;
* vérifiez régulièrement les événements non résolus dans Sentry.
