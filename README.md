# OC Lettings

OC Lettings est une application web Django permettant de consulter des locations immobilières et des profils utilisateurs.

Le projet a été refactorisé afin de passer d'une architecture monolithique à une architecture modulaire, puis conteneurisé, testé et déployé avec une chaîne CI/CD.

## Liens

- Application en production : https://oc-lettings-47nw.onrender.com/
- Documentation : https://python-oc-lettings-fr-aurelien7777.readthedocs.io/fr/latest/
- Dépôt GitHub : https://github.com/Aurelien7777/Python-OC-Lettings-FR

## Fonctionnalités

- consultation de la liste des locations ;
- consultation du détail d'une location ;
- consultation de la liste des profils ;
- consultation du détail d'un profil ;
- administration des données avec l'interface Django ;
- pages d'erreur personnalisées ;
- surveillance des erreurs avec Sentry.

## Technologies

- Python 3.7 ;
- Django 3.0 ;
- SQLite ;
- Gunicorn ;
- WhiteNoise ;
- Docker ;
- GitHub Actions ;
- Docker Hub ;
- Render ;
- Sentry ;
- Sphinx ;
- Read the Docs.

## Architecture

Le projet est organisé en trois composants principaux :

- `oc_lettings_site` : configuration générale, page d'accueil et pages d'erreur ;
- `lettings` : gestion des adresses et des locations ;
- `profiles` : gestion des profils utilisateurs.

## Installation locale

### Prérequis

- Git ;
- Python 3.7 ;
- `pip` ;
- le module `venv`.

### Cloner le dépôt

```bash
git clone https://github.com/Aurelien7777/Python-OC-Lettings-FR.git
cd Python-OC-Lettings-FR
```

### Créer l'environnement virtuel

Sous Windows :

```powershell
py -3.7 -m venv venv
.\venv\Scripts\Activate.ps1
```

Sous macOS ou Linux :

```bash
python3.7 -m venv venv
source venv/bin/activate
```

### Installer les dépendances

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Configurer les variables d'environnement

Créer un fichier `.env` à la racine du projet :

```env
SECRET_KEY=replace-with-a-local-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
SENTRY_ENVIRONMENT=development
```

Pour activer Sentry localement :

```env
SENTRY_DSN=replace-with-your-sentry-dsn
```

Le fichier `.env` ne doit pas être ajouté au dépôt Git.

### Appliquer les migrations

```bash
python manage.py migrate
```

### Lancer l'application

```bash
python manage.py runserver
```

L'application est accessible à l'adresse suivante :

http://127.0.0.1:8000/

## Administration

Créer un compte administrateur :

```bash
python manage.py createsuperuser
```

Puis ouvrir :

http://127.0.0.1:8000/admin/

## Tests et qualité du code

### Tests avec couverture

```bash
coverage run manage.py test
coverage report --fail-under=80
```

La CI exige une couverture minimale de 80 %.

### Linting

```bash
flake8
```

## Docker

### Construire l'image

```bash
docker build -t oc-lettings:local .
```

### Lancer le conteneur sous PowerShell

```powershell
docker run --rm -p 8000:8000 -e SECRET_KEY=django-insecure-local -e DEBUG=False -e ALLOWED_HOSTS=localhost,127.0.0.1 oc-lettings:local
```

L'application est alors accessible à l'adresse suivante :

http://127.0.0.1:8000/

## CI/CD

Le workflow GitHub Actions :

1. exécute les tests Django avec `coverage` ;
2. vérifie que la couverture atteint au moins 80 % ;
3. exécute `flake8` ;
4. construit l'image Docker sur la branche `master` ;
5. publie l'image sur Docker Hub avec les tags `latest` et le SHA du commit ;
6. déclenche le déploiement sur Render.

Image Docker de production :

```text
docker.io/aurelienamorin/oc-lettings:latest
```

## Surveillance avec Sentry

Sentry centralise les erreurs rencontrées par l'application.

La configuration repose principalement sur les variables suivantes :

- `SENTRY_DSN` ;
- `SENTRY_ENVIRONMENT`.

L'option `send_default_pii` est désactivée afin de ne pas transmettre automatiquement les données personnelles des utilisateurs.

## Documentation

La documentation technique est générée avec Sphinx et publiée sur Read the Docs :

https://python-oc-lettings-fr-aurelien7777.readthedocs.io/fr/latest/

Pour construire la documentation localement :

```powershell
cd docs
.\make.bat clean
.\make.bat html
```

Les fichiers HTML sont générés dans :

```text
docs/build/html/
```
