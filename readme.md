# Documentation du projet

## Model


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