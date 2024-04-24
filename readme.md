# Documentation du projet
## Installation django
Lorsque vous partez d'un projet à zéro procéder ainsi pour créer votre projet
- Assurez-vous que ``Python`` est installé sur votre machine\
pour vérifier si python est correctement installé sur votre machine taper la commande ``python --version``
- Assurez-vous d'avoir soit ``VSCode`` ou ``pycharm``
- Créez un nouveau projet dans l'environnement de développement integré de votre choix
____________________
- Installez django à partir du ``terminal`` de votre projet\
``pip install django``
- Créez votre projet \
 ``django-admin startproject opt_solution``
- Accèdez dans votre projet\
``cd opt_solution``
- Créez votre application\
``django-admin startapp params_basic``
- Ajoutez votre application dans le fichier ``settings.py`` plus précisement dans le bloc __``INSTALLED_APPS``__ dans notre cas notre application c'est ``params_basic``\
INSTALLED_APPS =[

&emsp;&emsp;&emsp;'``params_basic``'\
&emsp;&emsp;&emsp;]
- Créez un super utilisateur pour votre projet\
``python manage.py createsuperuser``
- Migration des données par défauts  et de nos futurs donnée\
``python manage.py makemigrations``\
``python manage.py migrate``
- Pour lancez le serveur taper la commande suivante\
``python manage.py runserver``
- Comme dans ce projet nous utilisons des API nous allons installer django rest framework]\
``pip install djangorestframework``
- Ensuite ajouter le package que vous venez d'installez dans le fichier ``settings.py`` se trouvant dans notre application ajoutez ``rest_framework``\
INSTALLED_APPS =[

&emsp;&emsp;&emsp;'``rest_framework``'\
&emsp;&emsp;&emsp;]


## Model
Qu'est-ce que sait un model ?
>Un modèle est la source unique et définitive d'informations sur vos données . Il contient les champs et comportements essentiels des données que vous stockez, comme le dit monsieur Hervé le modèle c'est la couche logique de nos donnée.

## Serializers Simple
Qu'est-ce que sait un serializer ?
>Les sérialiseurs sont utilisés pour convertir des types de données complexes, tels que les instances de modèle Django, en types de données Python
qui peuvent être facilement restitués en JSON, XML ou d'autres types de contenu . Les sérialiseurs assurent également la désérialisation, permettant aux données analysées d'être reconverties en types complexes après avoir d'abord validé les données entrantes.
* __*Importation*__
> from rest_framework import ``serializers``\
> from __.models__ import ``Option``
________
* __*Structure de la classe*__
> __class__ `OptionSerializer`(``serializers``.ModelSerializer):\
&emsp;&emsp;class `Meta`:\
> &emsp;&emsp;&emsp;&emsp;model = ``Option``\
> &emsp;&emsp;&emsp;&emsp;# Afficher tous les champs\
> &emsp;&emsp;&emsp;&emsp;fields = '``__all__``'\
> &emsp;&emsp;&emsp;&emsp; # Afficher des champs personalisés\
> &emsp;&emsp;&emsp;&emsp; fields = ['```libelleOption```','```Autrechamps```']\

___________

## View

## Api