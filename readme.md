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


## Model simple
Qu'est-ce que sait un model ?
>Un modèle est la source unique et définitive d'informations sur vos données . Il contient les champs et comportements essentiels des données que vous stockez, comme le dit monsieur Hervé le modèle c'est la couche logique de nos donnée.

* __*Importation*__
>from __django.db__ import __models__

* __*Structure de la classe*__
> __class__ `TimeStampModel`(models.Model):\
&emsp;&emsp;created_at = models.DateTimeField(auto_now_add=True)\
&emsp;&emsp;updated_at = models.DateTimeField(auto_now=True)
>
> &emsp;&emsp;class Meta:\
> &emsp;&emsp;&emsp;&emsp;abstract = True

> __class__ `Option`(TimeStampModel):\
&emsp;&emsp;libelleOption = models.CharField(max_length=100, null=True, blank=True)\
\
&emsp;&emsp;``def __str__(self):``\
&emsp;&emsp;&emsp;&emsp; return self.libelleOption

_________________
## Serializers Simple
Qu'est-ce que sait un serializer ?
>Les sérialiseurs sont utilisés pour convertir des types de données complexes, tels que les instances de modèle Django, en types de données Python
qui peuvent être facilement restitués en JSON, XML ou d'autres types de contenu . Les sérialiseurs assurent également la désérialisation, permettant aux données analysées d'être reconverties en types complexes après avoir d'abord validé les données entrantes.

* Créez un fichier __serializers.py__ dans votre application

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
> &emsp;&emsp;&emsp;&emsp; fields = ['```libelleOption```','```Autrechamps```']

___________
## Enregistrez vos models dans le fichier admin.py de votre application

``admin.site.register(Option)``\
``...``

## View simple
* __*Importation*__
> from .serializer import ``OptionSerializer``\
> from __.models__ import ``Option``


> class OptionViewSet(viewsets.ModelViewSet):\
    &emsp;&emsp;&emsp;queryset = Option.objects.all()\
    &emsp;&emsp;&emsp;serializer_class = OptionSerializer

## Créez un fichier url dans votre application
* __*url.py*__ dans ce fichier nous définirons un router pour permettre le routage de nos differentes viewset\
* Structure du code
>from rest_framework import routers\
from .views import OptionViewSet\
> 
> router = routers.DefaultRouter()\
router.register(r'option', OptionViewSet)\
urlpatterns = router.urls

### Inclure votre fichier url.py contenant le routage des differents vues dans votre fichier urls.py se trouvant la repertoire principal du projet
* Structure du code
> from django.contrib import admin\
> from django.urls import path, include
>
> urlpatterns = [\
    path('admin/', admin.site.urls),\
    path('api/', include('params_basic.url'))\
]

* Lancez votre serveur depuis le terminal avec
* notre mini simple api se trouve dans la route *``/api``*
>``python manage.py runserver``
## Api (Application programming interface)
* Quelques méthodes\
POST\
GET\
PUT\
DELETE\


## ViewSet Action
Les routeurs par défaut inclus dans le framework REST fourniront des routes pour un ensemble standard d'actions

Ameliorant notre ViewSet avec ces méthodes inclut par défaut dans notre ViewSet

> create\
> list\
> update\
> destroy\
> retrieve

* __*Importation*__
> from rest_framework import viewsets, permissions, status\
> from rest_framework.response import Response\
> from .serializer import ``OptionSerializer``\
> from __.models__ import ``Option``

> class OptionViewSet(viewsets.ModelViewSet):\
    &emsp;&emsp;&emsp;queryset = Option.objects.all()\
    &emsp;&emsp;&emsp;serializer_class = OptionSerializer\
    &emsp;&emsp;&emsp;# Protection de la route avec l'authentification\
    &emsp;&emsp;&emsp;permission_classes = [permissions.IsAuthenticated]\
\
    &emsp;&emsp;&emsp;def __``create``__(self, request, *args, **kwargs):\
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;serializer = OptionSerializer(data=request.data)\
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if serializer.is_valid():\
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;return Response(status=status.HTTP_201_CREATED, data={"message": "Enregistrement réussi avec succès",'option': serializer.data})\
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)\
\
    &emsp;&emsp;&emsp;def __``list``__(self, request, *args, **kwargs):\
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;option = Option.objects.all()\
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;serializer = OptionSerializer(option, many=True)\
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;return Response(data={'options': serializer.data})\
\
    &emsp;&emsp;&emsp;def __``update``__(self, request, *args, **kwargs):\
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;option = self.get_object()\
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;serializer = SectionSerializer(option, data=request.data)\
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if serializer.is_valid():\
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;serializer.save()\
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;return Response(data={"message": "Modification réussie avec succès", 'option': serializer.data}, status=status.HTTP_200_OK)\
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)\
\
    &emsp;&emsp;&emsp;def __``destroy``__(self, request, *args, **kwargs):\
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;option = self.get_object()\
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;option.delete()\
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "Suppression réussie avec succès"})

